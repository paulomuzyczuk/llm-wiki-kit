---
name: model-eval
description: >-
  Evaluate whether a cheaper or local model is good enough for one specific task
  in any project (e.g. LLM job scoring, visual-summary judgement, classification),
  against Claude tiers, on a blind gold set that the user rates. Builds the gold
  set, the rating sheet, a harness that runs each model through the project's own
  production provider code, the metrics, and a written recommendation. Claude tiers
  run through the Anthropic API (BYOK, pinned model IDs, temperature 0, every
  request and response logged), never through a subagent. Use when the user asks to
  "evaluate", "compare", "benchmark" or "check the quality of" a model for a task,
  asks whether a local model is good enough, or is deciding between models for a
  pipeline stage.
---

# model-eval

Decide, with evidence, whether a model is good enough for one task. The procedure
is the same for every task; only the rubric and the inputs change.

## Privacy and secrets (non-negotiable)

- If the repo is public, nothing personal goes into commits. Gold sets, ratings,
  raw outputs and reports are personal judgements: keep them in a gitignored
  folder (e.g. `data/llm_eval/`), and use fictional fixtures in committed tests.
- Never print, log or commit an API key (`ANTHROPIC_API_KEY`). It lives in the
  project's `.env` only. Check that it is set without showing its value.
- Before sending any input to Anthropic, confirm with the user that the inputs may
  leave the machine. Public job ads or public documents are fine; personal text
  (CVs, private notes) needs explicit approval.

## Approach: Claude tiers via the API (BYOK)

Use the API route for every Claude tier. Do not use a subagent to produce
evaluation outputs. The reasons are reproducibility and fidelity:

1. **Pin the model ID** for each tier (use the current IDs from the `claude-api`
   skill) and set `temperature: 0`. A subagent runs on whatever model the harness
   assigns, which can change.
2. **Run the production code path.** Use the same provider class the project uses
   in production, with the same prompt, schema and parsing, so the result measures
   what production does.
3. **Log every request and response** to disk (one JSON line per call, with model
   ID, prompt hash, tokens and latency). A run can then be re-checked and diffed.
4. **Record cost per run** from the token counts in the responses. Issues usually
   require this.

Local models get the same treatment: run them through their production provider,
with the same prompt, schema and parsing.

## Steps

1. **Define the task in one sentence**, and its rubric: the dimensions, their
   scale and what each end means. Take these from the code or config that owns
   them, and do not restate them in docs.
2. **Build the gold set.** Pick about 30 items spread across the score range, from
   a fixed seed so it is reproducible. Include at least 2 known-bad items if the
   task has them, and cover more than one source or variant if the project has
   them. Use a score-stratified, seeded sampler, and write a gold set plus a blind
   rating sheet with scores hidden. Adapt an existing sampler in the repo if one
   exists (hephaistos: `scripts/eval_llm_sample.py`) rather than writing a second.
3. **Blind rating by the user.** The user rates each item on the rubric plus a
   verdict. Never show the user model scores or heuristic scores while they rate.
   Ratings go in a file the sampler never overwrites.
4. **Harness.** One script runs each model through the production provider and
   writes per-model JSON. Models: the local candidates and the three Claude tiers
   (API route above). Cap the number of calls per run and say what the cap is.
   Inject the clients so tests use fakes and need no network.
5. **Measure** against the user's ratings:
   - per-dimension agreement (mean absolute error, Spearman rank correlation);
   - agreement on the weighted total, and top-N overlap with the user's shortlist;
   - valid-JSON rate and fallback rate (how often production would drop to its
     fallback);
   - a prompt-injection check: one item with embedded instructions;
   - a grounding spot-check of about 10 rationales for claims the source does not
     make;
   - runtime per item on the production host, and API cost per run.
6. **Decide and record.** Write the recommendation in the tracker issue, weighing
   quality against privacy (local keeps data on the machine), cost and runtime.
   Options: keep the local model, switch the primary, or a hybrid (local first
   pass, Claude re-score of the top N). A change to a pipeline config goes in a
   separate commit that references the issue.

## Checks before reporting

- Tests for the harness and sampler pass, with fictional fixtures and no network.
- The project's own checks are green before any commit.
- Report each metric with its sample size. Say plainly when a comparison rests on
  fewer than 30 items or a single snapshot.
