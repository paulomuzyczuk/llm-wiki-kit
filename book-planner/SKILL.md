---
name: book-planner
description: >
  Produces and persists an ingestion plan BEFORE any book is ingested into a wiki
  vault, and recovers that plan when resuming a partially-ingested book. On first add,
  also handles book onboarding (creating meta.md and the book entity page). Use this
  whenever the user is about to ingest a new book, says they want to start/plan/scope
  a book, asks how to batch a book, or resumes a book mid-way — even if they don't say
  the word "plan." Always run this before the first batch of a book and at the start of
  any session resuming a book, so the batching and per-chapter synthesis strategy
  survive context resets between batches. Surveys chapter structure, proposes batching
  and synthesis strategy, flags compaction risk, writes the approved plan to a file, and
  HALTS for human approval. This skill plans only — it never ingests and never reviews.
---

# Book Planner

The planning step that runs before book ingestion. Its job: turn a raw book into an
agreed, persisted ingestion plan, then stop. It does not ingest (that is `book-ingestion-skill.md`) and it does not review (that is the `book-review`
skill). Three separate jobs, three separate steps.

## Why this skill exists

A book is ingested in batches, one batch per fresh session. The batching and
per-chapter synthesis strategy are decided once, up front — but if they live only in
conversation context, a context reset between batches loses them, and the next session
either re-derives the strategy (wasting effort) or silently re-decides it differently
(inconsistency). This skill prevents that by writing the approved plan to a file that
the resuming session reads back.

## When this runs

- **First add:** when a book is added to the vault for the first time (`meta.md` does
  not yet exist). Phase 0 runs book onboarding before Phase 1 surveys the content.
- **New book, post-onboarding:** at the START of ingesting a new book, before the first
  batch. Phase 1 onwards.
- **Resume:** at the start of any session RESUMING a partially-ingested book.

If an approved plan file already exists for the book, this skill READS and reports it
rather than regenerating it. The approved plan is authoritative; never silently re-plan
a book that already has a plan.

## Phase 0 — Book onboarding

**Runs first-time only.** Detect: does `raw-input/books/<slug>/meta.md` already exist?
If yes, skip Phase 0 entirely and proceed to Phase 1 (survey) or the resume path if a
plan file also exists.

### 0.1 — Confirm and convert source file

Confirm the PDF is present at `raw-input/books/<slug>/`. If the source is a non-PDF
format (`.epub`, `.mobi`, `.azw`, `.azw3`), convert it with Calibre before proceeding:

```bash
ebook-convert "raw-input/books/<slug>/<source-file>" \
  "raw-input/books/<slug>/<slug>.pdf"
```

If `ebook-convert` is not available, stop and ask the human to install Calibre
(`brew install --cask calibre`) before re-running. Do not attempt workarounds.

### 0.2 — Write meta.md

Read the table of contents. Write `raw-input/books/<slug>/meta.md` with:
- Title and author
- Edition/printing, and ISBN (or DOI) when available — the specific manifestation being ingested, so citations resolve against a known edition
- Chapter → PDF-page-range map (using PDF page indices, not printed page numbers)
- Ingest-status checklist: one line per chapter, all unticked

```
- [ ] Ch.1 — <Title>
- [ ] Ch.2 — <Title>
```

**If the PDF strips printed page numbers** (common in EPUB-derived PDFs), also build
`raw-input/books/<slug>/printed-page-map.md` — a mapping of EPUB `page0NNN` div →
printed page → PDF page — so every citation tail can be derived from it rather than
guessed from an offset.

### 0.3 — Create book entity stub

Create `wiki/entities/books/<slug>-book.md` as a stub. The entity filename carries
a **`-book` type suffix** (the book *folder* under `raw-input/books/` stays
`<slug>`; only the entity page gets the suffix). This makes the wikilink
self-describing and collision-proof against a same-named concept page in
`wiki/topics/` — e.g. a "periodization" book becomes `periodization-book.md` so it
never collides with the `periodization` concept page — and gives the
`book-entity-backlink` lint check a deterministic source→entity mapping. The suffix
encodes source *type* only; it is independent of `source_tier` (do not infer tier
from it). Stub contents:
- One-line overview of what the book covers
- "Why it matters" placeholder for the vault
- Chapter index with empty wikilinks (filled as ingestion progresses)

Set the entity's source-identity frontmatter — `edition` and `isbn`/`doi` for the
manifestation (copied from `meta.md`; `null` when unavailable) — so this page is the
edition-stable anchor every `#page=N` citation resolves through. If the vault has a
`wiki/topics-authority.md`, resolve any alias you give the entity (title variants,
acronyms) against it first and register new ones there — the same
resolve-before-minting rule the ingest skill applies to topic pages.

This page is the living hub for the book's synthesis. It is updated after each ingested
chapter; Phase 4 of the ingestion skill ticks the chapter index and `meta.md` together.

### 0.3b — Seed the topics-authority skeleton (first content into a fresh vault)

If `wiki/topics-authority.md` is still an unpopulated skeleton (`status: stub` with a
`SEED-ME` comment), this book is the vault's first content — seed the file now, per the
CLAUDE.md Conventions *First-ingest seed* rule: populate **up to 10 subject categories**
(the `topics:` vocabulary) and **up to 30 aliases**, drawn from this book's structure and
the domain; set `status: active` and remove the `SEED-ME` comment. The 10/30 caps apply
to this initial seed only — later ingests grow the vocabulary under resolve-before-minting.
If the file is already populated, skip this step.

### 0.4 — Halt for human review

Surface `meta.md` and the entity stub to the human for confirmation before proceeding
to Phase 1. Do not begin the survey until the human confirms both look correct.

---

## Phase 1 — Survey

Read the book's `raw-input/books/<slug>/meta.md` and the chapter structure from the source PDF at `raw-input/books/<slug>/`. For every
chapter and appendix, record:

- PDF page range and page count
- Estimated tokens (start from ~525 tokens/page, then apply the calibration below)
- Type: foundational / methodology / reference-catalog / mixed / applied-domain
- A one-line density read: how much genuine synthesis weight the chapter carries

Present this as a chapter-assessment table.

## Phase 2 — Propose batching

### Sizing computation

Before presenting the batch table, measure the book and the current wiki:

- Extract full text: `pdftotext <pdf-path> - | wc -c` → divide by 4 for total estimated tokens. Prorate per chapter by that chapter's share of total PDF pages to get per-chapter estimates.
- Compute current wiki size: `find <vault>/wiki -name "*.md" | xargs wc -c 2>/dev/null | tail -1` → divide by 4 for approximate token load already in context.

Present a table: Chapter | PDF pp | Est. tokens | Proposed batch.

**Sizing discipline:** token estimates from `pdftotext` are **raw source text only**; real context consumption runs roughly **2× raw** — synthesized output, cross-reference loading, and the reverse-omission-sweep review all add to it. Size batches against the doubled figure, not the raw estimate. Default ceiling: **≤30 raw PDF pages per batch** (≈30k effective tokens after doubling). Any chapter ≥25 raw pages is a solo batch regardless of adjacency. When the ingestion plan flags a chapter as Large, solo, or compaction-risk, that flag is authoritative and overrides this heuristic — if the heuristic and the plan disagree, the plan wins. Default to smaller batches when in doubt: context compaction mid-batch degrades extraction quality (citation ranges drift, omissions increase), and the cost of an extra session is lower than the cost of a degraded batch.

Group chapters into batches (one batch = one fresh session). For each batch give:
chapters, page range, page count, estimated tokens, and a **synthesis strategy per
chapter**:

- **Full synthesis** — for foundational and conceptual chapters.
- **Principles + decision criteria** — for reference-catalog chapters: capture the
  governing principles and the when-to-use logic, NOT the per-item mechanics. (Same
  non-uniform approach that fits a catalog chapter where mechanics are reference detail.)

Declare the strategy explicitly per chapter — the reviewer checks for this (synthesis
strategy declaration), so a chapter with no declared strategy is a gap.

**Calibration — raw estimates undercount, roughly 2×.** The ~525 tokens/page rate
measures only raw source text. Real consumption is about double, because ingestion also
spends context on synthesized output, cross-reference loading, and the reverse-sweep
review. Size batches against the doubled figure. When a batch looks borderline, split
it — a wasted fresh session is cheap; a mid-chapter compaction on dense material is not.

**Solo chapters.** Give its own batch to any chapter that is the conceptual spine
other chapters reference. Flag these.

**Compaction-risk flag.** Mark any batch likely to fill the context window mid-run.

**Oversized reference catalogs / appendices.** If a section is too large to ingest as a
normal chapter (e.g. a 100+ page reference catalog), do NOT propose synthesizing it.
Present a scope decision to the human: (A) note existence only; (B) extract the
structural pattern + taxonomy into one page; (C) selective deep-dive on a few items as
worked examples. Recommend A or B unless the items will be used actively as templates.

## Phase 3 — Persist and halt

Present the full plan (chapter assessment + batching + any scope decisions) and STOP.
Do NOT begin ingesting.

**The approval decision is always the human's.** The agent cannot reliably judge its own
remaining context, so it proposes and halts; it never self-authorizes a batch or a batch
size. Wait for explicit approval or adjustments.

**On approval**, write the plan to the plan file (below). Only the approved version gets
written — not the draft.

## The plan file

Path: `raw-input/books/<slug>/ingestion-plan.md`

The plan file holds the agreed **strategy only** — batching, per-chapter synthesis
strategy, and scope decisions — and is immutable once approved. It does NOT track ingest
progress. Chapter completion lives in `meta.md`, which stays the single source of truth
for progress. Keeping strategy and progress in separate files prevents the two from
drifting on the same fact.

Format:

```
---
title: Ingestion Plan — <Book Title>
book: <slug>
date: <approval date>
status: approved
---

# Ingestion Plan — <Book Title>

## Scope decisions
- <e.g. Appendix B: taxonomy extraction only (Option B); individual trees rejected as
  too-granular negative space>

## Batches
| Batch | Chapters | PDF pp | Synthesis strategy |
|---|---|---|---|
| 1 | Intro + Ch.1 | 23–64 | Full synthesis |
| ... | ... | ... | ... |

## Convergence watch (for the reviewer)
- <existing pages this book is expected to enrich>
```

## Resuming a partially-ingested book

1. Read `raw-input/books/<slug>/ingestion-plan.md` to recover batching + synthesis strategy + scope decisions.
2. Read `raw-input/books/<slug>/meta.md` to see which chapters are already ticked complete.
3. Determine the next un-ingested batch from the plan.
4. Report in one line: "Plan recovered. Batches 1–N complete (per meta.md). Next:
   Batch N+1 (chapters X–Y), strategy Z."
5. Hand off to `book-ingestion-skill.md` (invoke `/book-ingest`) for that batch — this skill's job
   ends at recovery; it does not ingest.

Never re-plan a book that already has an approved plan file unless the human explicitly
asks to revise it. If the human asks to revise, update the file and re-present for
approval — same propose-and-halt gate.
