---
name: vault-evaluator
description: >
  Evaluates the quality contribution of a Karpathy-style LLM Wiki vault by running
  structured question sets across three conditions (no context, raw source context,
  vault context) and across multiple model classes, then produces a comparative
  performance report. Every model answer is produced by an isolated headless
  subprocess, never by the evaluating session itself. Use this skill whenever the
  user wants to measure, benchmark, test, or evaluate how much a vault is helping,
  whether the vault adds value over raw sources, how different models benefit from
  vault context, or whether a vault is ready to serve as a reference implementation.
  Also triggers on phrases like "does the vault help", "test the vault", "benchmark
  vault quality", "compare models on the vault", or "evaluate knowledge quality".
  This skill is the right tool any time vault effectiveness needs to be measured
  rather than assumed.
---

# Vault Evaluator

Measures how much a Karpathy-style LLM Wiki vault improves answer quality over
baseline (no context) and over raw sources — across multiple model classes. Produces
a structured comparative report. The evaluation is always comparative: the vault earns
its value by beating both baselines, not just one.

The session running this skill is the **orchestrator** — it builds the question set,
assembles contexts, launches answer and judge subprocesses, and compiles the report.
It never answers a question itself and never scores an answer itself.

---

## Execution model — isolation rules

These rules are what make the numbers mean anything. Do not relax them.

1. **Every question × condition × model cell is one fresh headless subprocess:**

   ```sh
   cd "$EVAL_RUN_DIR" && claude -p --model <model> --output-format json < cell-prompt.md > cell-result.json
   ```

   Pass the prompt on **stdin** as above, never as a shell argument — golden-set
   questions and pasted context contain quotes. Parse the answer text from the
   JSON `result` field, and record the cell's `usage` token counts,
   `total_cost_usd`, and `duration_ms` — the efficiency analysis in Phase 5
   needs them for every cell.

2. **`EVAL_RUN_DIR` is a temp directory (`mktemp -d`) outside the vault.** Running
   `claude -p` from inside the vault auto-loads the vault's `CLAUDE.md` into the
   subprocess and silently poisons Condition A. Never launch a cell from the vault
   directory or any directory carrying a `CLAUDE.md`.

3. **The orchestrator never answers a golden-set question.** By Phase 1 it has read
   `index.md` and vault pages; any answer it produced would contaminate Condition A
   and bias the B-vs-C comparison. All context a subprocess needs is pasted inline
   into its prompt; the subprocess gets no file paths and no directory context.

4. **Preflight.** `command -v claude` must succeed. If it doesn't, halt and tell the
   user this skill requires the Claude Code CLI on PATH — do not fall back to
   answering in-session.

5. **Cost gate.** Before launching any subprocess, state the exact call count for the
   requested run (answer cells + judge calls — e.g. the minimal version is 30 calls;
   a full single-model run is 98 answer cells + 64 judge calls; the 3-model matrix
   is 294 answer cells + 192 judge calls) and get explicit confirmation. Each call
   is a full headless session billed to the user's account.

6. **Failure handling.** A cell whose subprocess exits non-zero or returns empty
   output is retried once; on a second failure, record the cell as `FAILED` in the
   answers file and continue. Never fabricate, paraphrase, or self-author an answer
   for a failed cell. A run with FAILED cells reports them explicitly.

---

## Why three conditions, not two

The vault's claim is that compiled, cross-referenced wiki pages outperform both no
context AND raw source pages. If the vault only beats "no context," it might just be
reproducing the sources without adding synthesis value. If it doesn't beat raw sources
on synthesis questions, the wiki compression isn't earning its cost. Both comparisons
are needed to understand what the vault is actually doing.

| Condition | What it measures |
|---|---|
| A — No context | Model's baseline knowledge |
| B — Raw source context | Value of source material alone |
| C — Vault context | Value of compiled synthesis |

Target: C > B > A on synthesis questions. C ≈ B on factual questions (acceptable —
synthesis pages shouldn't lose factual fidelity). C > B on applied judgment questions
(the vault's highest-value claim).

---

## Question taxonomy

Every golden set must contain all three scored question types in roughly this
ratio — 20% factual, 40% cross-source synthesis, 40% applied judgment — plus a
small set of separately-tracked abstention controls (Type 4).

### Type 1 — Single-source factual (20%)
Tests basic information retrieval and fidelity. Should be easy for conditions B and C;
used as a sanity check that the vault isn't losing information during synthesis.

Example: *"What are the four ACID properties and what does each guarantee?"*

Evaluation: correctness only. Pass/fail. Both B and C should score near-perfect.
If C fails these, the vault has a compression quality problem.

### Type 2 — Cross-source synthesis (40%)
Tests the vault's core value proposition: connections across books that no single
source contains. These questions are HARD for condition A (model knowledge), HARD
for condition B (requires reading multiple sources simultaneously), and should be
EASY for condition C (the wiki has already done the synthesis work).

Example: *"Three sources in this vault discuss the relationship between module
boundaries and cognitive load. What's the unified view, and where do the authors
disagree?"*

Evaluation: depth, accuracy of cross-references, identification of tensions.
This is where C should most clearly beat B.

### Type 3 — Applied judgment (40%)
Tests whether the vault produces actionable guidance for novel situations not
explicitly covered in any single source.

Example: *"I'm designing a service that needs to store user session state accessible
from multiple geographic regions with sub-100ms read latency. Using what this vault
covers, what are the key trade-offs and which consistency model should I target?"*

Evaluation: whether the answer draws on the right concepts, applies them correctly
to the novel scenario, and surfaces the relevant trade-offs without hallucinating
constraints the sources don't mention.

### Type 4 — Abstention controls (unscored; tracked separately)
Tests the property this vault system uniquely claims: negative-space honesty.
Questions on topics *adjacent to* the corpus that the vault deliberately does not
cover — drawn from `wiki/gaps.md` §2 and the pages' Negative Space records. A good
Condition C answer says the vault doesn't cover this (ideally citing the exclusion
record) instead of producing a fluent hallucination.

Example (for a software-craft vault that excludes people management):
*"According to this vault, what's the recommended approach to compensation
bands for open source maintainers?"*

Evaluation: classification, not scoring — ABSTAINED / HEDGED / ANSWERED (see
Phase 3). These questions never enter the win-rate or average computations.

---

## Phase 1 — Build the golden set

Read `wiki/index.md` to survey the vault's full topic coverage. Build a golden set
of 30 scored questions (6 factual, 12 cross-source synthesis, 12 applied judgment)
plus 4 abstention controls (Type 4, sourced from `wiki/gaps.md` §2 and
Negative Space records — their rubric states the expected coverage boundary and,
where one exists, the exclusion record a good answer should cite). The 30 scored
questions must:

1. Span the full corpus — don't cluster around one book
2. Include at least 5 cross-book synthesis questions that explicitly require
   connecting concepts from ≥2 books
3. Include at least 3 role-specific questions testing role-MoC navigation
   (e.g., "as a system-designer evaluating storage options..."). **If the vault has
   no role MoCs** (no `wiki/role-*.md` pages), skip this requirement, note
   "no role MoCs — role navigation untested" in the golden-set header, and use the
   index-based Condition C loading described in Phase 2.
4. Are answerable from vault content — don't include questions whose answers
   require knowledge the vault doesn't have

For each question, also specify:
- Which vault pages are the authoritative sources
- Which raw source sections are the ground truth
- A brief rubric: what a good answer must include, and what a bad answer would miss

Write the golden set to `wiki/digests/eval-golden-set-<YYYY-MM-DD>.md` (frontmatter
per the Vault conventions section below). This file is immutable once created —
never modify questions after running any condition against them, or comparisons
become invalid.

**Stop and show the golden set to the human before proceeding.**
The human must approve or adjust before any model runs.

---

## Phase 2 — Run the three conditions

For each question, collect three answers — one subprocess per condition, per the
Execution model rules. Run all conditions for one question before moving to the
next, so context assembly stays consistent.

**One cell-prompt template for every condition** — identical preamble, only the
context block differs (omitted entirely in Condition A):

```
Answer the question below directly and completely. If context is provided,
treat it as your primary source. Do not mention whether context was provided.

[BEGIN CONTEXT]
<pasted pages>
[END CONTEXT]

Question: <question text>
```

### Condition A — No context
The bare template: no context block, no vault pages, no domain priming. Record the
subprocess output verbatim.

### Condition B — Raw source context
Paste only the raw source sections identified as ground truth in the golden-set
rubric. Do not paste wiki pages. For cross-source synthesis questions this means
pasting sections from multiple books — which is what makes condition B harder than
condition C for these questions.

### Condition C — Vault context
Paste the role MoC for the most relevant role plus the specific topic pages
identified in the rubric. Do not paste raw source pages. If the vault has no role
MoCs, paste `wiki/index.md` plus the rubric's topic pages instead.

**Abstention controls** run conditions A and C only — B has no meaningful
raw-source context for a question the corpus deliberately doesn't cover.

**Context loading discipline:** Conditions B and C must load the same *volume* of
context (approximately equal token counts — estimate as characters ÷ 4, the same
method book-planner uses) so the comparison is fair. If condition B would load
8,000 tokens of raw source and condition C would load 2,000 tokens of wiki pages,
pad condition C with additional related wiki pages, or trim condition B, until the
token counts are comparable. Log the actual estimates for both.

Write all answers to `wiki/digests/eval-answers-<YYYY-MM-DD>.md` in this structure
(a failed cell records `FAILED — <reason>` in place of the answer):

```
## Q{N}: {question text}
**Type:** factual | cross-source | applied | abstention-control
**Condition A:** {answer}
**Condition B:** {answer}
**Condition C:** {answer}
**Context tokens — B:** {count} · **C:** {count}
**Cell usage:** per condition — in/out tokens, USD, ms (from the cell JSON)
```

---

## Phase 3 — Blind scoring

Scoring is done by a **judge subprocess**, never by the orchestrator — the
orchestrator assembled the contexts and knows which answer is the vault's, so its
scores would be self-graded.

**Judge model is fixed for the entire evaluation:** always the frontier tier,
regardless of which model produced the answers. A per-row judge would confound
answerer capability with judge capability in the cross-model matrix.

**Position-swapped pairwise judging, per scored question — two judge calls:**

LLM judges are more reliable at comparison than at absolute scoring, and they
carry position bias (favoring the answer shown first). Both calls use an
identical prompt except the answers are presented in **reverse order** in the
second call; blind shuffling alone does not cancel position bias — the swap does.

1. Shuffle the three answers into an arbitrary order (vary the permutation across
   questions; record each permutation — it is unblinded in step 5).
2. Build the judge prompt: the question, its golden-set rubric, and the three
   answers labeled only **Answer 1 / Answer 2 / Answer 3**. No condition names, no
   words like "vault", "wiki", or "source" in the labels or framing. Instruct the
   judge to produce, in a fixed mechanically-parseable block: (a) a 1–5 score per
   rubric dimension per answer, and (b) a strict best-to-worst **ranking** with a
   one-line justification.
3. Run the judge twice (fresh subprocess each time, same stdin/temp-dir rules as
   Phase 2): once with the shuffled order, once with that order reversed.
4. If a judge output is unparseable, re-run that call once; on a second failure
   mark the question `JUDGE-FAILED` and exclude it from win rates and averages
   (report it).
5. Unblind and derive, per question:
   - **Pairwise verdicts** (C vs B, C vs A, B vs A): a pair's verdict is the
     relation the two orderings agree on; if the orderings disagree, the pair is
     a **tie** — that disagreement is position bias, not signal.
   - **Diagnostic scores**: the mean of the two calls' rubric scores, with the
     N/A and weighting rules below applied mechanically by the orchestrator —
     the judge scores dimensions; the orchestrator applies policy.

The rubric dimensions the judge scores:

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| **Accuracy** | Factually wrong or missing key claims | Partially correct; misses important nuances | Fully correct; all key claims present |
| **Synthesis depth** | Single-source or generic answer | Some cross-referencing; limited connection-making | Explicit cross-source connections; tensions named |
| **Actionability** | Abstract or generic guidance | Applicable in principle but vague | Specific, directly applicable to the scenario |

Factual questions: score only accuracy (synthesis depth and actionability N/A).
Synthesis questions: score all three dimensions.
Applied judgment questions: score all three dimensions, weight actionability 2×.

**Headline metric — win rates with a significance gate.** For each pair (C vs B
is the one that matters most), report wins–losses–ties across questions, overall
and per question type. Excluding ties, a win count is **significant (two-sided
p < 0.05, sign test)** only at or above these thresholds:

| n (non-tied questions) | 10 | 12 | 15 | 20 | 25 | 30 |
|---|---|---|---|---|---|---|
| wins needed | 9 | 10 | 12 | 15 | 18 | 21 |

(For other n, compute the exact binomial or use the nearest larger threshold.)
Below the threshold, report the direction but call it what it is: not
statistically distinguishable from noise at this sample size. Never present a
sub-threshold average delta as a finding.

**Abstention controls — one judge call per control:** present the question, the
expected coverage boundary from its rubric, and the A and C answers (shuffled,
labeled Answer 1 / Answer 2). The judge classifies each answer as **ABSTAINED**
(declines and names the coverage boundary), **HEDGED** (partially answers with
caveats), or **ANSWERED** (confident specifics). Unblind: C passes only on
ABSTAINED — ideally citing the vault's gap or negative-space record; ANSWERED is
a hallucination failure. Comparing A's and C's classifications shows whether
vault context makes the model *more* honest than its bare baseline.

The per-question **vault advantage** flag is the C-vs-B pairwise verdict:
win = `C > B`, tie = `C ≈ B`, loss = `C < B` (losses get diagnosed in Phase 5).

Write scores to `wiki/digests/eval-scores-<YYYY-MM-DD>.md`, including each
question's blinding permutation, both orderings' rankings, and the derived
pairwise verdicts, so the run is auditable end to end.

---

## Phase 4 — Cross-model comparison

Repeat Phases 2 and 3 for each model class specified by the human, varying only the
`--model` argument of the answer cells (the judge stays fixed — see Phase 3).
Typical comparison:

| Tier | `--model` value | Why include |
|---|---|---|
| Frontier | `opus` (e.g. claude-opus-4-8) | Ceiling — what's possible |
| Mid-tier | `sonnet` (e.g. claude-sonnet-4-6) | Cost-effective production target |
| Fast | `haiku` (e.g. claude-haiku-4-5) | Latency-sensitive use cases |

Pass whatever your `claude --model` accepts (aliases or full model IDs, current
equivalents if these have moved on) and record the exact value used plus the run
date in the report — model performance changes across versions.

For each model, run all three conditions on the full golden set. This generates a
3×3 matrix per question (3 models × 3 conditions) which reveals:

1. **Does the vault help more for smaller models?** (Expected: yes — weaker models
   benefit more from compiled context because their own synthesis capacity is lower)
2. **Does vault context close the gap between model tiers?** (The key claim: a
   mid-tier model with vault context should approach frontier model without context)
3. **Where does vault context fail regardless of model?** (Questions where all
   models score poorly in condition C reveal synthesis gaps in the vault itself)

Use identical prompts, identical context loading, and identical scoring rubrics
across all models.

---

## Phase 5 — Report

Write `wiki/digests/eval-report-<YYYY-MM-DD>.md` containing:

### Headline: win rates
Lead with the pairwise results, not averages — per model, per pair (C vs B
foremost), wins–losses–ties overall and by question type, each marked
**significant** or **below threshold** per the Phase 3 sign-test table. A
sub-threshold direction is reported as exactly that.

### Summary table (diagnostic averages)
```
| Model | Condition | Factual avg | Synthesis avg | Judgment avg | Overall |
|---|---|---|---|---|---|
| Opus | No context | ... | ... | ... | ... |
| Opus | Raw source | ... | ... | ... | ... |
| Opus | Vault | ... | ... | ... | ... |
| Sonnet | No context | ... | ... | ... | ... |
...
```

### Efficiency
From the per-cell usage data (Execution model rule 1):
- **Vault lift per 1k context tokens** — score/win-rate lift of C over A, divided
  by the context volume C paid for it, per model.
- **Quality per dollar** — for each model × condition, average score against
  measured `total_cost_usd`.
- **Cost substitution** — the cheapest configuration that matches or beats the
  frontier-model no-context row. "Mid-tier + vault ≥ frontier bare" stated as a
  measured cost saving, or explicitly not achieved.

### Abstention honesty
Per condition (A and C), the ABSTAINED / HEDGED / ANSWERED counts on the Type 4
controls. Any C hallucination (ANSWERED) is listed verbatim with the gap or
negative-space record it should have cited. State whether vault context made the
model more or less honest than its bare baseline.

### Vault advantage analysis
- Questions where C clearly beat B (vault adds value): list them
- Questions where C ≈ B (vault neutral): list them
- Questions where C < B (vault hurt): list and diagnose each

### Cross-model vault lift
For each model: how much did vault context improve over no-context baseline?
Express as score delta. The "vault lift" metric.

### Vault gaps identified
Questions where ALL models scored poorly in condition C reveal synthesis gaps.
These are candidates for vault improvement — either missing topic pages, thin
synthesis, or absent cross-book connections.

### Interpretation
State directly:
1. Is the vault adding value over raw sources? (Significant C-over-B win rate on
   synthesis questions?)
2. Does vault context close the gap between model tiers, and at what measured cost?
3. Which question types benefit most from the vault?
4. Is the vault honest at its coverage boundary?
5. What are the top 3 vault improvements that would most raise scores?

The report must also carry a **contamination caveat**: Condition A reflects what
the model already knows, and publicly published sources are typically in training
data — so lift measured on a public-book vault understates what the same
discipline yields on private or recent material. Name the sources this applies to.

After writing the report, append one log entry (see Vault conventions).

---

## Vault conventions

- All eval files live in `wiki/digests/`, named with the run date
  (`eval-golden-set-`, `eval-answers-`, `eval-scores-`, `eval-report-` +
  `<YYYY-MM-DD>.md`), and carry the digest frontmatter the vault's `CLAUDE.md`
  schema requires (`type: digest`, plus the vault's other required fields).
- One `log.md` entry per completed run, written after the report:
  `## [YYYY-MM-DD] eval | <vault-slug> | <models> × <conditions> on <N>-question set — <headline verdict>`
  A run abandoned after the Phase 2 confirmation gate logs
  `eval | <vault-slug> | aborted — <reason>` instead; a run abandoned before that
  gate logs nothing.

---

## Calibration notes

**On "vault context should win synthesis questions":** A well-built vault should
clearly beat raw source context on cross-source synthesis because the wiki has
already done the connection-making work. If condition B wins synthesis questions,
it usually means the vault's synthesis pages are under-linking — they describe
concepts in isolation rather than in relation to each other.

**On factual questions:** Expect C ≈ B here. If C loses factual questions to B,
the vault has a compression-fidelity problem — facts are being dropped or distorted
during synthesis. This is more serious than losing synthesis questions.

**On applied judgment questions:** These are the hardest to score consistently.
The blind judge must use the rubric strictly: does the answer name the specific
trade-offs relevant to the scenario? Does it cite the right principles without
hallucinating constraints? A good answer for an applied judgment question cites
vault concepts by name.

**On model tier gaps:** A mid-tier model with vault context scoring above a
frontier model without context is the strongest possible validation of the method.
If this doesn't happen on synthesis and judgment questions, the vault's synthesis
quality needs work.

---

## Minimal version (10-question quick signal) — mandatory first

Never launch the full evaluation cold. Run this minimal version first to get
directional signal (30 subprocess calls; state the count at the cost gate):

1. Pick 2 factual, 4 cross-source synthesis, 4 applied judgment questions
2. Run conditions A and C only (skip B for speed) — 20 answer cells, same
   isolation rules as Phase 2
3. Score with one blind judge call per question: the pair of answers in shuffled
   order, "which answer is better and why?" — no rubric and no position swap at
   this stage (directional signal only; the full run's verdicts are
   position-swapped)
4. If C clearly beats A on synthesis and judgment: proceed to the full evaluation
5. If C ≈ A: investigate whether context is being assembled correctly before
   spending the full matrix

The minimal version answers "does the vault help at all?" The full version answers
"how much, on what question types, and for which models?"
