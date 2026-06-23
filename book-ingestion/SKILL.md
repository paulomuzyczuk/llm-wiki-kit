---
name: book-ingestion
description: >
  Ingests a single approved batch of chapters from a book into a Karpathy-style
  LLM Wiki vault, producing synthesized topic pages, entity updates, index entries,
  log entries, and negative-space records. Use this skill whenever the user says
  "ingest", "process", "synthesize", or "start batch N" for a book — even if they
  just say "next batch" or "continue the book." Also triggers when the user names
  a chapter number or page range to process. Always requires an approved ingestion
  plan (ingestion-plan.md) to exist before running — if it does not exist, invoke
  book-planner first and halt. Never ingests more than one approved batch per
  invocation. Never runs headlessly or chains into the next batch automatically.
  Always chains into book-review once per chapter in the batch — review is per chapter, not per batch.
---

# Book Ingestion

Synthesizes one approved batch of source chapters into the wiki. One invocation =
one batch = one fresh session. The skill reads the vault schema from CLAUDE.md,
the approved plan from the book's ingestion-plan.md, and progress from meta.md —
then ingests exactly the next un-ingested batch and stops.

Vault-specific configuration (frontmatter schema, citation format, negative-space categories) is read from the vault's CLAUDE.md at runtime.

---

## Prerequisites — check before doing anything

1. **Ingestion plan exists.** Read `raw-input/books/<slug>/ingestion-plan.md`. If
   it does not exist, stop: invoke `book-planner` first. Do not derive the batch
   strategy on the fly — the plan is authoritative.

2. **Identify the next batch.** Read `meta.md` to see which chapters are ticked
   complete. Cross-reference the plan's batch table to find the first batch whose
   chapters are not all ticked. That is the batch to ingest. State it in one line:
   *"Plan recovered. Batches 1–N complete. Next: Batch N+1 (chapters X–Y,
   strategy Z)."*

3. **Confirm with the human.** Do not begin ingesting until the human confirms.
   A human request authorizes exactly one batch. Never self-authorize.

---

## Phase 1 — Load context

Read in this order:
1. `wiki/log.md` — last 5 ingest entries for this book, to understand what has
   already been synthesized and what cross-references exist.
2. `wiki/index.md` — to know which pages already exist (avoid duplicates, find
   enrichment candidates).
3. `wiki/entities/books/<slug>-book.md` — the book entity, to see chapter completion
   status and any per-chapter notes.
4. The specific topic pages most likely to be enriched by this batch (identified
   from the plan's convergence-watch section, if present).

Do NOT load the full wiki. Load only what is relevant to this batch.

---

## Phase 2 — Read the source

### Format check — convert non-PDF formats first

If the source file is not a `.pdf` (e.g. `.epub`, `.mobi`, `.azw`, `.azw3`),
convert it to PDF using Calibre before proceeding. Do not attempt to extract
text from non-PDF formats directly.

```bash
ebook-convert "raw-input/books/<slug>/<source-file>" \
  "raw-input/books/<slug>/<slug>.pdf"
```

Verify the output PDF was created before continuing. If `ebook-convert` is not
available, stop and ask the human to install Calibre (`brew install --cask calibre`)
before re-running the skill. Do not attempt workarounds — Calibre is the required
tool and there is no acceptable substitute here.

Once a PDF exists (whether converted or original), proceed with extraction:

```bash
pdftotext -f <start_page> -l <end_page> \
  "raw-input/books/<slug>/<slug>.pdf" - 2>/dev/null
```

Read the extracted text fully before synthesizing anything. Do not synthesize
while reading — complete the read pass first.

---

## Phase 3 — Synthesize

Apply the synthesis strategy declared in the plan for each chapter in this batch.

Chapters vary in synthesis weight (foundational principles vs. reference catalog). When
a chapter is clearly reference material rather than conceptual development, synthesise
structural principles and decision criteria only; do not capture mechanics or recipes.
Declare the synthesis strategy per chapter in the ingest report (e.g. 'full synthesis'
/ 'principles + decision criteria' / 'enrichment only').

> **Note:** Vaults may extend the above paragraph in their CLAUDE.md as inline
> behavioral extensions read at runtime alongside the skill.

**Before writing any page for a chapter,** internally outline the key concepts and
decide where emphasis should land — organize first, write second. This is not a
human-confirmation gate; chapters in an authorized batch are ingested autonomously
within the batch.

### Full synthesis
For foundational and conceptual chapters: create one topic page per distinct
concept that warrants its own page. Apply all discipline rules from CLAUDE.md:

- **Frontmatter:** every new page must include all frontmatter fields declared in
  the vault's CLAUDE.md schema. Use the exact topic-tag field name the vault
  declares (e.g. `topics:`, not `tags:`), include the vault's domain tag if it
  declares one, and apply any per-type field rules. If CLAUDE.md doesn't declare
  the schema, stop and flag it — don't invent fields. Omitting any declared field
  is a Check 6 FAIL.
- **Controlled vocabulary (resolve before minting):** if the vault has a
  `wiki/topics-authority.md`, resolve every `topics:` value and every new
  `aliases:` entry against it *before* writing the page. When the candidate
  already resolves to a preferred term, reuse that term — never introduce a
  scattered variant of an existing subject or an alias already claimed by
  another page. Register a genuinely new subject or alias in
  `topics-authority.md` in the same change. vault-lint's vocabulary check is the
  catch-net; this is where scatter is prevented.
- **Concept graining:** anchor pages for load-bearing concepts; stub-with-intent
  only if the source explicitly forward-references; dead wikilinks for concepts
  named but not yet paged.
- **Citation density:** every H2 and H3 with original claims gets its own inline
  citation at PDF-page granularity. Format per CLAUDE.md citation convention.
  A deferred citation is a present gap — never defer.
- **Citation accuracy:** a citation has two page parts and both must be derived
  from the source, never computed by a fixed offset. `#page=N` is the PDF page on
  which the cited sentence actually appears. The printed-page tail (`, p. N`) is
  the printed page **containing** that sentence: read it from the PDF's own printed
  numbers when present, or — for an EPUB-derived PDF that strips them — from the
  EPUB `page0NNN` page-div containing the sentence (one div = one printed page). Do
  not infer the tail from a PDF→printed offset: the offset drifts within a chapter
  and a printed page overflows onto the next PDF page, so `#page` and the tail
  legitimately differ. For any book whose PDF strips printed numbers, build and
  maintain `raw-input/books/<book>/printed-page-map.md` (EPUB-div → printed → PDF)
  and derive every tail from it. If the source affords no printed-page ground
  truth, record the tail as unverifiable rather than guessing.
- **Negative space:** every page gets a `## Negative Space` section listing what
  was deliberately omitted and why, using the rejection categories from CLAUDE.md.
  Every chapter's log entry must note what was rejected. Silent omissions are
  the primary failure mode — the reviewer will catch them; prevent them here.
- **Figures:** never reproduce as ASCII. Capture the underlying insight as prose
  or a structured list, then cite the figure by name.
- **Enrichment-not-replacement:** for pages that already exist, add new content
  as new H2 sections preserving all prior content and citations.
- **Pair-and-split (canonical definition):** when a chapter presents two paired or contrasting concepts (e.g. *precision* vs. *recall*; *encapsulation* vs. *inheritance*), give each its own page and bridge them with reciprocal wikilinks — never conflate the pair onto a single page. Each concept stays independently retrievable while the relationship is preserved by the cross-links. This bullet is the canonical definition; book-review (Check 2) enforces it and vault-lint points back here.
- **Source-entity backlink:** every topic page created or enriched from the book
  must link the book entity page (`wiki/entities/books/<slug>-book.md`), so the entity
  is not left orphaned. The orphan check excludes `index.md`, so the catalogue
  entry does not count as an inbound link — ticking the entity in Phase 4 only
  links *outward*, and this backlink is the inbound link that makes it reachable.
  Add it in the page's `## Sources` section as a dedicated
  `**Source entities:** [[<slug>-book]]` line (list every book entity the page draws
  on, comma-separated). The entity slug carries the `-book` type suffix (see
  book-planner Phase 0.3); link `[[<slug>-book]]`, not `[[<slug>]]` — the latter
  dangles or collides with a same-named concept page and fails the
  `book-entity-backlink` lint check. Use the per-page form — every citing page carries the
  line, not a single representative link — so the requirement clears the orphan
  check and populates the cross-reference graph uniformly. The enforcement target
  is the *edge* (an entity wikilink exists for each cited book), so a vault that
  already links the entity idiomatically elsewhere in `## Sources` also satisfies
  it; the labeled line is the canonical form the skill emits.

### Principles + decision criteria
For reference-catalog chapters: do not create per-item mechanics pages. Capture:
- The governing principle (what this category of things is for)
- The decision criteria (when to use which option and why)
- The named options with one-line descriptions
- Negative space: reject per-item mechanics as too-granular

### Theory-heavy chapters

Theory-heavy chapters (math, proofs, formal methods, formal logic, statistical models, type-theoretic notation, algorithm pseudocode, multi-step derivations): preserve notation precisely and have the human verify the summary captures the result correctly before moving on.

When ingesting any multi-line printed formula, solution to a differential or recurrence equation, or derivation chain that purports to satisfy a parent equation, apply an algebraic self-check before committing the page. The check is two-step:

(a) **Boundary or base condition.** Verify the formula satisfies its stated initial condition (e.g. A(0)=0, B(0)=0, the recurrence holds at n=1, the posterior integrates to 1, the probability sums to unity) by direct substitution.

(b) **Parent equation or constraint.** Verify the formula satisfies its parent equation or constraint — an ODE, a recurrence relation, a fixed-point identity, a probability normalisation, a conservation law, an algebraic identity asserted in the source — by direct differentiation, substitution, or analogous algebraic manipulation.

Halt on failure. If either check fails, do not commit the page. Insert a top-of-page flag in the form:

> **Transcription uncertain — awaiting human verification.** Formula `<id>` failed self-check step `<(a) or (b)>`: `<one-line description of the inconsistency>`.

Surface the failure in your batch progress report. Do not silently re-OCR the formula or paraphrase it to make the check pass; the source must be re-read, ideally via a fresh rendering of the page (image-based reading rather than re-running text extraction on the same PDF, when the source's OCR quality is suspect).

(d) Set the chapter state in meta.md to `- [!] Ch.<n> — <Title> (self-check halted: <one-line description of the failed check>)`. This is the ONLY meta.md write Phase 3 performs on halt — Phase 4's tick and reviewer chain do not run for this chapter. The halt state persists in meta.md until the human resolves the blocker. Write the halt log entry to `wiki/log.md` using the HALTED schema defined in Phase 4 step 4.

Scope: this discipline applies only to formulas with a derivable parent — equations claimed to satisfy something else. Bare definitions ("let X be the discount factor at maturity N"), notational introductions, and stated assumptions are not algebraically checkable and need only notation fidelity, not self-check.

This is the operational counterpart to the vault CLAUDE.md's algebraic self-check rule. CLAUDE.md declares the requirement; this subsection declares the procedure. Apply it during synthesis (Phase 3), NOT during review — the reviewer is a fidelity auditor, not a re-derivation agent.

> **Note:** Notation-heavy vaults may extend this guidance in their CLAUDE.md
> (e.g. "Theory-heavy chapters are the norm here, not the exception") as
> vault-specific behavioral extensions.

---

## Chapter state machine

Each chapter in `raw-input/books/<slug>/meta.md` carries one of five states:

| State | Syntax | Meaning |
|---|---|---|
| Not yet ingested | `- [ ] Ch.N — Title` or absent | No synthesis work started |
| Halted on self-check | `- [!] Ch.N — Title (self-check halted: <one-line description>)` | Synthesis attempted; the algebraic self-check (Phase 3, Theory-heavy chapters) failed and the page was NOT committed; human action required to unblock — **intermediate, must not persist at book completion** |
| Ingested, not reviewed | `- [x] Ch.N — Title` (no suffix) | Synthesised into wiki; review not yet run or not yet clean — **intermediate, must not persist at book completion** |
| Reviewed-clean | `- [x] Ch.N — Title ✓ reviewed-clean` | Synthesised AND passed `/book-review`; all FAILs resolved, all WARNs fixed or deferred with a logged note — **terminal** |
| Note-only | `- [x] Ch.N — Title (note only)` | Deliberately not synthesised; dispositioned as negative space — **terminal**. Must carry a logged rejection rationale in the chapter's log entry or book-entity note; never a silent skip. |

The orchestrator (this skill) sets these states — the reviewer is report-only and never
writes to `meta.md`. The intermediate `[x]` tick is set during Phase 4 step 2; the
transition to `✓ reviewed-clean` happens in the mark-reviewed-clean step (Phase 4
step 6) on a clean review. `[ ]` and `(note only)` represent the not-started and
deliberately-skipped states respectively.

The Halted-on-self-check state is set by Phase 3 (Theory-heavy chapters, self-check failure path) and persists until the human resolves the blocker (typically by re-OCR with image-based reading and re-running the ingest). The reviewer is never invoked on a Halted chapter — Phase 4 (which invokes the reviewer) does not run when synthesis halts in Phase 3.

---

## Phase 3.5 — Pre-commit self-check (per chapter)

**Halted-chapter guard.** Skip this phase if Phase 3 halted on a self-check for
this chapter (`[!]` state). Phase 4 is also skipped in that case.

After Phase 3 has written this chapter's pages to disk and before proceeding to
Phase 4, run two mechanical checks. Both WARN classes have recurred across multiple
books (anchor drift: OoI, IFIO, and CAT; source_count: OoI and IFIO); catching
them here eliminates fix-and-re-review cycles.

> **Retain-reviewer rule.** These checks supplement — never replace — the
> reviewer's equivalent checks (Check 1 citation anchor accuracy, Check 6
> source_count). The reviewer runs independently on the committed pages in Phase 4.
> Do not interpret a passing pre-commit check as a substitute for the reviewer.

### Check A — source_count

For each page written by Phase 3 (new pages and enriched pages alike), where
`<page>` is the actual file path on disk (e.g. `wiki/topics/<slug>.md`):

1. Count distinct `raw-input/books/` slug directories cited in the file:
   ```bash
   grep -oE 'raw-input/books/[^/]+/' <page> | sort -u | wc -l
   ```
2. Compare the count to `source_count:` in the file's frontmatter.
3. If mismatch: correct the frontmatter value in the file before Phase 4 runs.

### Check B — #page anchors

**Guard — PDF required.** This check calls `pdftotext` on
`raw-input/books/<slug>/<slug>.pdf`. Phase 2 guarantees this file exists (EPUB
and other non-PDF inputs are converted there before synthesis begins). If the PDF
is absent at this point despite Phase 2 completing, skip Check B and note it in
the pre-commit report.

For each `#page=N` anchor in the citations of this chapter's written pages:

1. **Pick 2–3 distinctive words** from the cited sentence — prefer proper nouns,
   technical terms, numbers, or uncommon domain vocabulary. Avoid common words
   (the, and, is, that, this, of, in). The goal: words unlikely to appear on
   pages N−1 and N+1 so a match on the wrong page is improbable. Record the
   words chosen (they appear in the pre-commit report line).

2. Extract and normalize page N, then grep each distinctive word as a separate
   `grep -q` call — all words must match for the anchor to be confirmed:
   ```bash
   pdftotext -f N -l N "raw-input/books/<slug>/<slug>.pdf" - 2>/dev/null \
     | tr '[:upper:]' '[:lower:]' \
     | tr -cs 'a-z0-9' ' '
   ```
   This collapses ligatures, em-dashes, smart quotes, and other encoding
   artifacts to spaces before matching.

3. If all words match: anchor confirmed. Proceed.

4. If any word fails: try N−1 and N+1 with the same normalized grep. Correct
   the anchor in the file to the first page where all words match.

5. If no match on any of N−1, N, N+1: leave the original N unchanged in the
   file and flag the anchor as "unresolved — manual check" in the pre-commit
   report. The reviewer's Check 1 will make the judgment call on the committed
   anchor. Do not block synthesis.

> **Scope limit.** This check covers `#page=N` anchors only. The printed-page
> tail (`, p. N`) requires the EPUB page-div map or PDF-embedded printed numbers
> — a Phase 3 synthesis discipline. The reviewer's Check 1 remains the gate for
> tail correctness.

### Pre-commit report line

State in one line before proceeding to Phase 4:

*"Pre-commit check: [N] pages × source_count verified ([M] corrected); [P]
anchors verified ([Q] corrected, [R] unresolved)."*

List any unresolved anchors by file path and citation location.

---

## Phase 4 — Update operational files and review (per chapter)

**Halted-chapter guard.** If Phase 3 halted on a self-check for this chapter (chapter state is `[!]` in meta.md after Phase 3), skip Phase 4 entirely for this chapter. The reviewer is not invoked; meta.md is not re-ticked (Phase 3 already wrote the halt state); no further log entry is written by Phase 4. Resume the chapter via a fresh `/book-ingest` invocation after the human has resolved the blocker.

After each chapter is synthesized, complete the following steps for that chapter
before moving to the next. Repeat Phases 3 and 4 for every chapter in the batch.

1. **Book entity** (`wiki/entities/books/<slug>-book.md`): tick the ingested chapter
   in the chapter index. Do not tick chapters not yet done.

2. **meta.md** (`raw-input/books/<slug>/meta.md`): tick the ingested chapter.
   meta.md is the source of truth for progress — it must always agree with the
   entity page.

3. **index.md** (`wiki/index.md`): add a one-line entry per new topic page under
   the appropriate book section. Enrich existing entries if a page was enriched.

4. **log.md** (`wiki/log.md`): append one entry for this chapter using the schema
   format:
   ```
   ## [YYYY-MM-DD] book-ingest | <slug> ch.<n> | <Chapter Title> — created
   <page1>, <page2>; enriched <page3>; negative-space: <item> (<category>),
   <item> (<category>)
   ```
   For chapters that were halted in Phase 3 (state `[!]`), the log entry is written
   by Phase 3 itself (not by Phase 4 step 4) using this schema:
   `## [YYYY-MM-DD] book-ingest | <slug> ch.<n> | <Chapter Title> — HALTED: <halt description>`

5. **Review:** invoke `/book-review <slug> <chapter-number>`. Address any FAILs
   before proceeding to the next chapter in this batch. WARNs may be addressed
   immediately or carried to the batch summary report — never silently ignored.

6. **Mark reviewed-clean (orchestrator only — reviewer stays report-only).** If
   `/book-review` returned clean — all FAILs resolved AND all WARNs either fixed or
   deferred with a logged deferral note in `log.md` or `meta.md` — append
   ` ✓ reviewed-clean` to that chapter's line in `meta.md`. **Idempotent:** if the
   suffix is already present (e.g. after a human-requested re-review passes), do not
   append again. If any FAIL is unresolved or any WARN has no logged deferral, leave
   the bare `[x]` — the chapter stays intermediate.

---

## Phase 5 — Batch summary report

After all chapters in the batch are ingested and reviewed (Phases 3 and 4 complete
for every chapter), deliver the batch summary:
- Pages created (with names)
- Pages enriched (with names)
- Negative-space items logged (count and categories)
- Cross-book convergences found (if any)
- Review outcomes per chapter: PASS / WARN / FAIL / HALTED summary and any deferred WARNs; list any `[!]` halted chapters separately with the self-check failure description
- Which batch this was and what batch comes next (per the plan)

Do NOT begin the next batch. The next batch requires a new explicit human request.

---

## Phase 6 — On book completion (automatic)

After any chapter reaches a terminal state (`✓ reviewed-clean` via the
mark-reviewed-clean step, or `(note only)`), inspect the full ingest-status checklist
and fire this phase IF AND ONLY IF all hold:
  - every chapter is terminal: marked `✓ reviewed-clean` OR carrying `(note only)`,
  - no bare `[x]` (ingested-not-reviewed) chapter remains,
  - no `[!]` (halted-on-self-check) chapter remains,
  - no `wiki/digests/ingest-report-<slug>-*.md` already exists for this book.
If any condition fails, do nothing here and proceed to the batch-outcome report.

When all conditions hold:
  1. Generate the ingest report by synthesising ONLY from existing vault
     artifacts — `meta.md`, `log.md`, `index.md`, `wiki/entities/books/<slug>-book.md`,
     and the review digests for this book (`review-<slug>-*.md`). Do NOT re-read the
     source PDF; this is a rollup, not a fresh extraction. Write to
     `wiki/digests/ingest-report-<slug>-<YYYY-MM-DD>.md` using the schema below.
  2. Stamp `wiki/entities/books/<slug>-book.md`: set frontmatter
     `ingest_status: complete (<YYYY-MM-DD>)` and add a link to the report under
     the chapter index. Link it; never inline the report (keep the entity bounded).
  3. File any newly surfaced cross-book gaps into `gaps.md` §1.
  4. Append to `log.md`:
     `## [YYYY-MM-DD] digest | <slug> ingest complete | <N> ch reviewed-clean, <X> new pages, <Y> enrichments, <Z> convergences; report at <path>`
  5. Write the lint-pending marker to `log.md` — but only if one is not already
     present. Idempotency check: scan `log.md` for any
     `lint | pending | <vault-slug>` entry that appears after the most recent
     `lint | <vault-slug> |` entry (the last resolved lint). If such a pending
     entry already exists, skip this step. If none exists, append:
     `## [YYYY-MM-DD] lint | pending | <vault-slug>`
     where `<vault-slug>` is the vault's slug (e.g. `software-craft`), NOT the
     book's slug. Read the vault slug from the `vault_slug:` field in the
     VAULT-LINT-EXTENSIONS block of CLAUDE.md.
  6. Deliver the BOOK COMPLETE report: state the book is fully ingested — every
     chapter terminal (`✓ reviewed-clean` or `(note only)`), no `[!]`
     halted chapters remaining — list the ingest report path, and note that a
     vault-wide lint is now due and must be run in a fresh session. Do NOT run
     lint inline. Then stop.

### Ingest report schema

Path: `wiki/digests/ingest-report-<slug>-<YYYY-MM-DD>.md`

Frontmatter: standard fields per Conventions, plus `type: digest`;
  `topics: [<domain>, ingest-report, <slug>]`; `source_count: 1`; `status: active`.

§1 Scope — chapters reviewed-clean / total (state reviewed-clean, not merely
  ingested); PDF page span; batches & sessions; synthesis strategies used.

§2 Output — new pages (wikilinked list, one line each) and enriched pages
  (table: page | chapter(s) | substance added). These wikilinked lists ARE the
  navigational index; do not add a separate index section.

§3 Cross-book convergence — table: concept | prior source(s) | this book's
  contribution. THEN a convergence-misses note: convergences the ingestion plan
  expected that did NOT materialise, and why. This section is the primary
  payoff — keep it prominent.

§4 Negative-space summary — recurring rejection categories across the book, with
  examples and rough frequency.

§5 Review rollup — verdict table, one row per review unit (batch or chapter):
  unit | PASS/WARN/FAIL | issues | resolution | link to its review digest.
  Enumerate any WARN accepted rather than fixed, with rationale. State total
  unresolved explicitly (must be 0 for this report to exist). Do NOT compress
  to a single line.

§6 Gaps surfaced — list new field-level gaps and confirm each was filed to
  `gaps.md` §1. If none, state "no new gaps surfaced." Never leave this silent.

§7 Final state — self-audit table confirming every write landed: `meta.md` ticks;
  entity page (including the `ingest_status: complete` stamp and report link);
  `index.md`; `log.md`; all reviews.

Principle: the report AGGREGATES across the book; it must NOT restate the
per-chapter log lines.

---

## Hard rules (non-negotiable)

**Batch scope:** one human request = one batch. Never ingest more than the
approved batch, even if context permits.

**No chaining to next batch:** when the batch is complete, do not begin the next
batch. The context reset between batches is a human-held gate. Chaining into
`/book-review` is the sole exception — it runs once per chapter automatically as
part of the Phase 4 per-chapter loop.

**No headless execution:** this skill is never run by the scheduler or
autonomously. Always triggered by an explicit human request.

**Plan is authoritative:** never re-derive batch sizes or synthesis strategy
on the fly. If the plan seems wrong, surface the concern to the human and
wait for an updated plan — do not improvise.

**Reviewer is mandatory and authoritative:** book-review must run after every
successfully synthesised chapter in the batch (i.e., those NOT in `[!]` halted
state), as the final step of Phase 4 before moving to the next chapter. This
skill's job ends at ingest; it does not review its own output. If book-review fails to
execute for any reason, see CLAUDE.md's `### Book-review` section for the full
reviewer-failure procedure — the short version: STOP, surface the failure to the
human, never self-review.

---

## Vault-specific configuration

Frontmatter schema, citation format and depth table, and negative-space categories
are read from the vault's CLAUDE.md — not hard-coded here. If any of these are
missing from CLAUDE.md, stop and flag it before ingesting.
