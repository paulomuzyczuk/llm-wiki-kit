# Pipeline — how content enters a vault

This document describes the *workflow* that turns source material into wiki pages: the
stages, the skills that run them, and — most importantly — the human-in-the-loop gates
that keep the LLM from being the sole judge of its own work. For the structure of what
gets produced see [architecture.md](architecture.md); for why the pipeline is shaped
this way (especially the mandatory review) see [theory.md](theory.md).

## The shape of it

```
        ┌─────────────┐
books → │ book-planner │ → ingestion-plan.md ──(human approves)──┐
        └─────────────┘                                          │
                                                                 ▼
                                                   ┌────────────────────────┐
                                  (one batch) ───→ │     book-ingestion     │
                                                   └────────────────────────┘
                                                                 │
                                              (per chapter, mandatory)
                                                                 ▼
                                                   ┌────────────────────────┐
                                                   │      book-review       │ → digest
                                                   └────────────────────────┘

articles → article-ingestion (fetch → ingest)
vault    → vault-lint (health sweep)   ·   vault-evaluator (does it actually help?)
```

The throughline is **the LLM proposes, a reviewer and the human dispose.** Each stage
below is deliberately bounded so that no single automated step gets to both produce
and bless content.

## Planning — `book-planner`

Before any book is ingested, `book-planner` surveys its chapter structure and produces
a persisted **ingestion plan** (`ingestion-plan.md`): how the book is batched, the
per-chapter synthesis strategy, and where compaction risk lies. It also handles
first-time book onboarding (creating `meta.md` and the book's entity page) and, on the
very first ingest into a vault, seeds the controlled vocabulary.

Two properties are load-bearing:

- **It plans only — it never ingests and never reviews.**
- **It HALTS for human approval.** The plan is written to a file precisely so it
  survives context resets between batches and so a human signs off on the batching
  strategy before any synthesis happens. Resuming a half-ingested book starts here, by
  recovering the plan.

## Ingestion — `book-ingestion`

`book-ingestion` consumes **one approved batch** of chapters and produces the
synthesized output: topic pages, entity-page updates, index and log entries, and the
negative-space records. Its discipline:

- **One batch per invocation.** It never ingests more than a single approved batch, and
  never runs headlessly or chains into the next batch automatically.
- **It requires an approved plan.** With no `ingestion-plan.md`, it defers to
  `book-planner` and halts.
- **It chains into review** — once per chapter in the batch. Review is per chapter, not
  per batch.

## Review — `book-review` (mandatory, independent)

After each chapter is ingested, `book-review` runs as an **independent** check — the
single most important gate in the system, because it is what stops the writer from also
being the judge of its own work. It is **report-only**: it never modifies wiki files,
it writes a verdict digest to `wiki/digests/`.

It runs ten checks: citation density, wikilink integrity, negative-space discipline,
stance preservation, enrichment-not-replacement, frontmatter completeness, index/log
consistency, extraction quality (diagnostic only — no fail), synthesis-strategy
declaration, and notation-hygiene application (conditional, only when the vault opts
into it). The reasoning for making review mandatory and separate — that judging what a
text is *about* ("subject analysis") is exactly where a confident computational
describer fails — is in
[theory.md](theory.md#a-human-reviews-what-the-machine-describes).

## The article path — `article-ingestion`

Articles have their own two-step path in a single skill: **fetch** a URL into a
provenance-stamped Markdown note, then **ingest** that pending note into the wiki
(topic/entity synthesis, vocabulary resolution, index/log entries, lint trigger). It
can run interactively or headlessly. Note that fetched web content is *untrusted input*
and a prompt-injection vector — see [`SECURITY.md`](../SECURITY.md).

## Health and value — `vault-lint` and `vault-evaluator`

Two skills watch the vault as a whole rather than a single ingest:

- **`vault-lint`** is a health-check sweep: citation-resolution failures, orphan pages,
  dangling wikilinks, missing cross-references, duplicate concepts, stale claims, data
  gaps, vocabulary scatter, and role-count drift between the index and page frontmatter,
  plus any per-vault extension checks. It is **report-only** (it emits a dated digest
  and a ready-to-apply patch for role-count drift) and is the gate CI runs against the
  example vault.
- **`vault-evaluator`** answers "does the vault actually help?" by running question sets
  across three conditions — no context, raw-source context, and vault context — across
  multiple model classes, then reporting comparative performance. It measures
  contribution rather than assuming it.

## The human-in-the-loop gates

Pulling the discipline together, the pipeline forces a human decision at each point
where an automated step could otherwise run away with itself:

1. **Plan approval** — no ingestion without a human-approved `ingestion-plan.md`.
2. **One batch per invocation** — no unbounded headless ingestion.
3. **Mandatory independent review** — every chapter is checked by a separate pass.
4. **Human as curator** — the human keeps final say over what the vault asserts.

## Scheduled operations (optional)

The repo ships launchd templates (`scheduled-job.plist.template`,
`freshness-job.plist.template`) that invoke Claude Code against a vault on a cadence —
macOS-only, and entirely optional. Because a scheduled job runs the agent
unattended, understand what it is allowed to do before enabling it (see
[`SECURITY.md`](../SECURITY.md)).
