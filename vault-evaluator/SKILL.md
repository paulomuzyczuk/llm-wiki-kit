---
name: vault-evaluator
description: >
  Evaluates the quality contribution of a Karpathy-style LLM Wiki vault by running
  structured question sets across three conditions (no context, raw source context,
  vault context) and across multiple model classes, then produces a comparative
  performance report. Use this skill whenever the user wants to measure, benchmark,
  test, or evaluate how much a vault is helping, whether the vault adds value over
  raw sources, how different models benefit from vault context, or whether a vault
  is ready to serve as a reference implementation. Also triggers on phrases like
  "does the vault help", "test the vault", "benchmark vault quality", "compare models
  on the vault", or "evaluate knowledge quality". This skill is the right tool any
  time vault effectiveness needs to be measured rather than assumed.
---

# Vault Evaluator

Measures how much a Karpathy-style LLM Wiki vault improves answer quality over
baseline (no context) and over raw sources — across multiple model classes. Produces
a structured comparative report. The evaluation is always comparative: the vault earns
its value by beating both baselines, not just one.

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

Every golden set must contain all three question types in roughly this ratio:
20% factual, 40% cross-source synthesis, 40% applied judgment.

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

---

## Phase 1 — Build the golden set

Read `wiki/index.md` to survey the vault's full topic coverage. Build a golden set
of 30 questions (6 factual, 12 cross-source synthesis, 12 applied judgment) that:

1. Span the full corpus — don't cluster around one book
2. Include at least 5 cross-book synthesis questions that explicitly require
   connecting concepts from ≥2 books
3. Include at least 3 role-specific questions testing the role-MOC navigation
   (e.g., "as a system-designer evaluating storage options...")
4. Are answerable from vault content — don't include questions whose answers
   require knowledge the vault doesn't have

For each question, also specify:
- Which vault pages are the authoritative sources
- Which raw source sections are the ground truth
- A brief rubric: what a good answer must include, and what a bad answer would miss

Write the golden set to `wiki/digests/eval-golden-set-<date>.md`. This file is
immutable once created — never modify questions after running any condition against
them, or comparisons become invalid.

**Stop and show the golden set to the human before proceeding.**
The human must approve or adjust before any model runs.

---

## Phase 2 — Run the three conditions

For each question in the golden set, collect three answers. Run all conditions for
one question before moving to the next, so context loading is consistent.

### Condition A — No context
Ask the model the question with no vault pages, no raw source pages, and no domain
priming. Record the answer verbatim.

### Condition B — Raw source context
Load only the raw source pages that contain the relevant content (identified in
the golden set rubric). Do not load wiki pages. Ask the question. Record verbatim.

For cross-source synthesis questions, this means loading pages from multiple books
simultaneously — which is what makes condition B harder than condition C for these
questions.

### Condition C — Vault context
Use the startup protocol: load the role-MOC for the most relevant role, then load
the specific topic pages identified in the rubric. Do not load raw source pages.
Ask the question. Record verbatim.

**Context loading discipline:** Conditions B and C must load the same *volume* of
context (approximately equal token counts) so the comparison is fair. If condition
B would load 8,000 tokens of raw source and condition C would load 2,000 tokens of
wiki pages, pad condition C with additional related wiki pages, or trim condition B,
until the token counts are comparable. Log the actual token counts for both.

Write all answers to `wiki/digests/eval-answers-<date>.md` in this structure:
```
## Q{N}: {question text}
**Type:** factual | cross-source | applied
**Condition A:** {answer}
**Condition B:** {answer}  
**Condition C:** {answer}
**Context tokens — B:** {count} · **C:** {count}
```

---

## Phase 3 — Score each answer

For each question, score all three conditions on three dimensions. Use a 1–5 scale.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| **Accuracy** | Factually wrong or missing key claims | Partially correct; misses important nuances | Fully correct; all key claims present |
| **Synthesis depth** | Single-source or generic answer | Some cross-referencing; limited connection-making | Explicit cross-source connections; tensions named |
| **Actionability** | Abstract or generic guidance | Applicable in principle but vague | Specific, directly applicable to the scenario |

Factual questions: score only accuracy (synthesis depth and actionability N/A).
Synthesis questions: score all three dimensions.
Applied judgment questions: score all three dimensions, weight actionability 2×.

For each question, also record a binary **vault advantage** flag:
- `C > B`: vault condition meaningfully outperformed raw source condition
- `C ≈ B`: roughly equivalent
- `C < B`: raw source outperformed vault (flag for investigation)

Write scores to `wiki/digests/eval-scores-<date>.md`.

---

## Phase 4 — Cross-model comparison

Repeat Phases 2 and 3 for each model class specified by the human. Typical comparison:

| Tier | Representative model | Why include |
|---|---|---|
| Frontier | claude-opus-4 or equivalent | Ceiling — what's possible |
| Mid-tier | claude-sonnet-4 or equivalent | Cost-effective production target |
| Fast | claude-haiku-4 or equivalent | Latency-sensitive use cases |

For each model, run all three conditions on the full golden set. This generates a
3×3 matrix per question (3 models × 3 conditions) which reveals:

1. **Does the vault help more for smaller models?** (Expected: yes — weaker models
   benefit more from compiled context because their own synthesis capacity is lower)
2. **Does vault context close the gap between model tiers?** (The key claim: a
   mid-tier model with vault context should approach frontier model without context)
3. **Where does vault context fail regardless of model?** (Questions where all
   models score poorly in condition C reveal synthesis gaps in the vault itself)

Use identical prompts, identical context loading, and identical scoring rubrics
across all models. Record model names and versions explicitly — model performance
changes across versions.

---

## Phase 5 — Report

Write `wiki/digests/eval-report-<date>.md` containing:

### Summary table
```
| Model | Condition | Factual avg | Synthesis avg | Judgment avg | Overall |
|---|---|---|---|---|---|
| Opus | No context | ... | ... | ... | ... |
| Opus | Raw source | ... | ... | ... | ... |
| Opus | Vault | ... | ... | ... | ... |
| Sonnet | No context | ... | ... | ... | ... |
...
```

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
1. Is the vault adding value over raw sources? (C > B on synthesis questions?)
2. Does vault context close the gap between model tiers?
3. Which question types benefit most from the vault?
4. What are the top 3 vault improvements that would most raise scores?

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
Use the rubric strictly: does the answer name the specific trade-offs relevant to
the scenario? Does it cite the right principles without hallucinating constraints?
A good answer for an applied judgment question cites vault concepts by name.

**On model tier gaps:** A mid-tier model with vault context scoring above a
frontier model without context is the strongest possible validation of the method.
If this doesn't happen on synthesis and judgment questions, the vault's synthesis
quality needs work.

---

## Minimal version (10-question quick signal)

Before running the full 30-question evaluation, run this minimal version to get
directional signal in under two hours:

1. Pick 2 factual, 4 cross-source synthesis, 4 applied judgment questions
2. Run conditions A and C only (skip B for speed)
3. Score manually without a rubric — just: "which answer is better and why?"
4. If C clearly beats A on synthesis and judgment: proceed to full evaluation
5. If C ≈ A: investigate whether context is loading correctly before proceeding

The minimal version answers "does the vault help at all?" The full version answers
"how much, on what question types, and for which models?"
