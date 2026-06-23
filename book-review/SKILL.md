---
name: book-review
---

# Book Chapter Reviewer

Verify a freshly ingested book chapter against the vault's nine discipline rules. **Reports only — never modifies any wiki file, never auto-fixes.**

## Invocation

```
/book-review <book-slug> <chapter-number>
```

Example: `/book-review my-book 3`

---

## Setup

**Arguments:** `$ARGUMENTS` → parse as `<book>` (slug, first token) and `<chapter>` (second token). `<chapter>` is either:

- an **integer N** (numbered chapter, e.g. `3`, `10`); or
- a **named key K** (front/back-matter unit, e.g. `afterword`, `preface`, `appendix-a`) — a lowercased single token that resolves to a `meta.md` row label by case-insensitive match with `-` normalized to space (so `afterword` → `Afterword`; `appendix-a` → `Appendix A`).

If either argument is missing, ask the user before proceeding.

**Locate vault root** — the vault root is the current working directory. Do not search parent directories. Derive all paths relative to `$(pwd)`:

- Meta: `raw-input/books/<book>/meta.md`
- Book entity: `wiki/entities/books/<book>-book.md` (entity filename carries a `-book` type suffix; older un-migrated vaults may still have `wiki/entities/books/<book>.md` — accept whichever exists)
- Log: `wiki/log.md`
- Index: `wiki/index.md`
- PDF (spot-check only): `raw-input/books/<book>/<book>.pdf`

---

## Phase 1 — Load context

1. Read `CLAUDE.md` from the vault root. Extract and hold for use in Phase 2:
   - (a) Frontmatter schema: all declared field names, the exact field name used for domain/topic tags (e.g. `topics:` vs. `tags:`), and per-type requirement rules (e.g. which fields are required only on certain `type` values).
   - (b) Citation convention: the declared format string, encoding rule (`%20` vs. literal spaces), and the depth table that maps each citing-file location (e.g. `wiki/topics/*.md`, `wiki/entities/books/*.md`) to its correct relative-path prefix.
   - (c) Negative-space category table: the exact labels listed in CLAUDE.md — not memorized categories from prior runs or other vaults.
   If CLAUDE.md is absent or any of (a), (b), (c) is not cleanly declared, note which facts are missing; the affected checks (6 for missing (a), 1 for missing (b), 3 for missing (c)) will flag a vault-configuration error rather than running.
2. Read `meta.md`. Find the row matching `<chapter>` → note its PDF page range:
   - **integer N**: match the row whose label is `Ch. N`.
   - **named key K**: match the row whose label matches K case-insensitively with hyphen→space (e.g. `afterword` matches `Afterword`; `appendix-a` matches `Appendix A`).

   Record the matched row's label verbatim as `<row-label>` — used by step 4 below and Phase 3. FAIL early if no row matches.
3. **Halted-chapter guard.** If the located meta.md row's checkbox is `[!]` (Halted-on-self-check state — see book-ingestion-skill.md state machine table for the full five-state set), do NOT proceed with the review. Return immediately with:

   > `chapter <slug>/<chapter> is HALTED (self-check halted: <description from meta.md row>) — resolve the synthesis-time blocker before review. The reviewer is not designed to run on halted chapters; no review digest will be written and no log entry will be appended.`

   Do not write a review digest, do not append to log.md, do not run Phase 2 (any check) or Phase 3. Just emit the message and exit cleanly.
4. Read the last 50 lines of `log.md`. Find the most recent `book-ingest` entry for this unit:
   - **integer N**: `book-ingest | <book> ch.N |`
   - **named key K**: `book-ingest | <book> <row-label> |` (e.g. `book-ingest | <book> Afterword |`)

   Parse its description to identify all pages created or updated — e.g. "created topic-name" → `wiki/topics/topic-name.md`; "enriched other-topic" → `wiki/topics/other-topic.md`; "created book entity page" → `wiki/entities/books/<book>-book.md`. Collect every such path.
5. Read every identified page in full, plus the book entity page, `wiki/index.md`, and `wiki/log.md`.

---

## Phase 2 — Nine checks

Run all nine in order. For each: state `PASS`, `WARN`, or `FAIL`; for WARN or FAIL add a one-line explanation and a suggested fix prompt.

### Check 1 — Citation density

- Every section **and subsection** containing original claims has ≥1 citation — this applies at all heading levels (H2, H3, H4), not only top-level H2s.
- Attributive claims have inline citation anchors.
- Near-verbatim quotes have per-item citations.
- All citations use the format and path encoding declared in the vault's CLAUDE.md citation convention (loaded in Phase 1 step 1). **Guard:** if the CLAUDE.md citation convention or depth table was not cleanly declared, score this check as `CONFIG-ERROR: vault CLAUDE.md does not declare a citation depth table — cannot validate citation paths; fix CLAUDE.md` and skip path-depth verification. Otherwise verify each cited path on every modified page:
  - Format matches the declared pattern (parenthetical anchor style, `%20` URL-encoding for spaces, page-anchor fragment such as `#page=N` if CLAUDE.md declares it).
  - Relative-path depth matches the entry in the CLAUDE.md depth table for the citing file's location: a citation in `wiki/topics/*.md` must use the topics-row prefix; a citation in `wiki/entities/books/*.md` must use the entities/books-row prefix. **Do not apply one fixed prefix to all files.** The depths are distinct (e.g. `../../` ≠ `../../../`) and only one is correct per location. (The `../` in the previous hard-coded example was wrong for every file location in this vault and is the likely source of broken citation paths.)
  - The constructed path must resolve to a real file — a path with wrong depth is a broken link regardless of whether it superficially matches any single pattern.

- **Citation anchor accuracy** — verify across *every* citation on every modified page (script it; this is not a 2–3 sample like Check 8), and run it **regardless of the depth-table Guard** (anchor/tail correctness doesn't depend on the depth table — this closes the same skip-hole the path check had). Check both halves of each page reference against the source:
  - `#page=N`: the grounded sentence actually appears on PDF page N of the cited file. Resolving to the file but pointing at the wrong page is a broken citation.
  - `, p. N` tail: N is the printed page **containing** the sentence, checked against the source's printed-page ground truth — the PDF's own printed numbers if present; otherwise, for an EPUB-derived PDF that strips them, the EPUB `page0NNN` page-div that contains the sentence (one div = one printed page; `raw-input/books/<book>/printed-page-map.md` records the div → printed → PDF mapping). The tail is the printed page of the *block holding the sentence* — **not** the printed page that merely begins on PDF page N, because a printed page overflows onto the next PDF page, so `#page` and the tail legitimately differ. No printed-page ground truth at all (no PDF numbers, no EPUB) → report the tail unverifiable, don't assume it.
  - A wrong `#page` anchor or a wrong printed-page tail is a broken citation → **FAIL**.
  - *Elided-anchor sub-case (not yet validated): where one EPUB div spans two printed pages, the tail is whichever of the two contains the sentence — flag for manual disambiguation until the handling is validated and encoded here.*

**FAIL vs. WARN threshold**: FAIL if any section or subsection containing original claims has no citation. WARN only if the gap is a pure summary, transition, or cross-reference block with no independent claims — a chapter-level citation at the top of the page is sufficient coverage for those. A citation described as deferred or to be added later is a present gap and scores as FAIL.

### Check 2 — Wikilink integrity

- Every `[[wikilink]]` in modified pages either (a) resolves to an existing vault file, or (b) is a deliberate dead link (acceptable — flag it but don't fail).
- Concepts named more than once in a page are linked on first mention.
- Every modified page has ≥1 `## See also` section with at least one wikilink.
- **Source-entity backlink** — for each book a modified page cites (every distinct `raw-input/books/<slug>` PDF reference on the page), the page must contain a wikilink to that book's entity page, canonically `[[<slug>-book]]` in a `**Source entities:**` line in `## Sources` (see book-ingestion Full-synthesis rule). The entity filename carries a `-book` type suffix, so the cited folder `<slug>` maps to entity `<slug>-book` (older un-migrated entities may still be `<slug>` — resolve to whichever entity file exists). A page that cites a book PDF but never wikilinks its entity is a **FAIL** — it orphans the entity (the orphan check excludes `index.md`). The check is on the edge: any wikilink resolving to the book's entity satisfies it, regardless of form.
- **Pair-and-split** — if the chapter introduced two paired or contrasting concepts (see the canonical pair-and-split definition in book-ingestion), verify they were split into separate pages bridged by reciprocal wikilinks, not conflated onto one page. A single page covering both halves of a genuine concept pair is a **WARN**: suggest splitting into one page per concept with reciprocal `[[wikilinks]]`.

### Check 3 — Negative-space discipline

- The log entry description or the book entity's chapter index note includes concepts noticed but not promoted to topic pages, each labeled with a category from the vault's declared negative-space category table (loaded in Phase 1 step 1 from CLAUDE.md). **Guard:** if the CLAUDE.md negative-space category table was not cleanly declared, score this check as `CONFIG-ERROR: vault CLAUDE.md does not declare a negative-space category table — cannot validate rejection labels; fix CLAUDE.md` and skip label validation. Otherwise accept only labels that appear verbatim in the declared table — do not accept labels not listed there, including any memorized from prior runs or other vaults (e.g. a label like `needs-more-evidence` that appears in another vault's table must be flagged as an invalid label if it is absent from this vault's declared table).
- If no such note exists anywhere for this chapter, FAIL with a fix prompt to add a negative-space section.

### Check 4 — Stance preservation

- Foil concepts (anti-patterns, counterexamples, things the author argues against) must be framed as foils, not peer alternatives.
- For each modified page, identify any concept named in the book's anti-pattern or red-flag lists. Verify surrounding prose uses negative framing ("anti-pattern", "leads to", "the author warns", "symptom of"). Flag any that reads as a neutral peer alternative.

### Check 5 — Enrichment-not-replacement

- For pages that pre-existed this chapter (enriched, not created): prior citations must still be present. New content must appear as new H2 sections, not interleaved into or replacing existing prose.
- Flag any prior citation that appears removed or overwritten.

### Check 6 — Frontmatter completeness

For every created or modified page, verify:
- **Guard:** if the CLAUDE.md frontmatter schema was not cleanly declared in Phase 1, score this check as `CONFIG-ERROR: vault CLAUDE.md does not declare a frontmatter schema — cannot validate fields or tags; fix CLAUDE.md` and skip field/tag validation. Otherwise: all frontmatter fields declared in the vault's CLAUDE.md schema are present. Apply per-type requirement rules: if CLAUDE.md marks a field as required only on certain `type` values (e.g. `roles:` required on topic pages but optional on digest artifacts), enforce accordingly. Use the exact field name declared in CLAUDE.md for the domain/topic-tag field — if the vault declares `topics:`, check `topics:`, not `tags:`. Verify the domain tag declared as the fixed first entry in that field is present on every page.
- `last_updated` matches today's date.
- `type` is one of: `topic`, `entity`, `digest`.

### Check 7 — Index and log consistency

- Every new page has an entry in `wiki/index.md` with a one-line summary.
- The chapter is marked as complete in the book entity's chapter index.
- The chapter is ticked in `raw-input/books/<book>/meta.md` ingest-status checklist.
- Exactly one `book-ingest` log entry was appended, in schema format:
  - **integer N**: `## [YYYY-MM-DD] book-ingest | <book> ch.N | <chapter-title>`
  - **named key K**: `## [YYYY-MM-DD] book-ingest | <book> <row-label> | <unit-title>` (e.g. `## [YYYY-MM-DD] book-ingest | <book> Afterword | Synthesizing Coda`)

### Check 8 — Extraction quality (diagnostic only — no FAIL)

**Target error classes:** misattribution (a claim attributed to the wrong source or person), unsourced derivation/calculation (a specific figure, year, or calculation not present in the source text), and silent omission (a source section or framework-qualifying caveat absent from the wiki with no negative-space rejection entry).

**Scope:** Check 8 is a textual and structural fidelity check — does the wiki page accurately reproduce what the cited PDF page says? It deliberately does NOT verify algebraic correctness of formulas (boundary conditions, parent-equation satisfaction, derivation correctness). Algebraic self-checks are a synthesis-time discipline in book-ingestion-skill.md Phase 3 (Theory-heavy chapters). Do not re-derive formulas independently during review — the reviewer is a fidelity auditor, not a re-derivation agent.

This check runs in three required parts. A Check 8 report that omits the Reverse omission sweep subsection is itself a rubric violation.

#### Part A — Forward spot-checks (minimum 2–3 per chapter)

- Note any self-reported extraction quality issues in the log entry.
- Select 2–3 specific claims from the wiki pages. Prefer claims involving statistics, attributions, named examples, specific dates, and framework-qualifying caveats — the categories most vulnerable to misattribution and unsourced derivation.
- For each claim: read the PDF at the cited page range; quote the relevant source sentence (under 15 words); state how the wiki renders it; give a **Match** or **Mismatch** verdict. A bare "claim substantiated" with no source quote is not acceptable.
- For each spot-checked claim, also confirm its citation's `#page` anchor and printed-page tail by Check 1's Citation-anchor-accuracy method (you're already in the source at that page); report any wrong anchor or tail under Check 1 as a FAIL, not merely as a Check 8 note.
- Flag any Mismatch as WARN with a suggested fix prompt.
- Flag any ASCII reproduction of a source figure (arrows, box diagrams, spatial layouts rendered in text characters). The correct approach is prose or structured lists citing the figure by name — e.g. "See Figure N-N for the visual." Flag as WARN with a fix prompt to convert to prose/list + figure citation.

#### Part B — Reverse omission sweep (MANDATORY)

- Read the source PDF for this chapter. Walk every H2 and H3 section heading, plus any named framework-qualifying caveats — statements that qualify, limit, or add nuance to the chapter's central argument, and are therefore most at risk of silent omission.
- For each heading or caveat, determine its disposition and record it in a table:
  - **In wiki** — substance is captured in a wiki page (name the page)
  - **Negative-space entry** — explicitly rejected in the log entry or book entity note with a valid rejection category from the vault's CLAUDE.md (the same set Check 3 validates against)
  - **WARN: silent omission** — present in the source, absent from the wiki, and missing from the negative-space log
- Produce the table with columns: Source heading/caveat | Disposition | Detail.
- Note: compressed reference chapters (40–60 source pages) are at highest risk of silent omission. Treat framework-qualifying caveats with extra scrutiny in those chapters.
- "Nothing substantive omitted" may appear as a conclusion ONLY immediately after this table is shown — never as a standalone assertion without a preceding sweep.

#### Part C — Overall rating

Rate overall: `good`, `minor-issues`, or `degraded`.
- `good` — no mismatches, no unsourced derivations, no silent omissions
- `minor-issues` — 1–2 WARNs across all three error classes, none framework-altering
- `degraded` — ≥3 WARNs, or any single WARN that misframes or omits a load-bearing claim

Note: these thresholds are stricter than pre-edit digests (which rated this field informally). Do not compare a post-edit rating against a pre-edit one as if they used the same scale.

### Check 9 — Synthesis-strategy declaration *(pass/fail)*

- Locate the book's protocol report: `<vault>/wiki/digests/ingest-report-<book-slug>-*.md`.
- If no protocol report exists yet (book still in progress), mark this check **N/A — SKIP**.
- If the protocol report exists: for every chapter row in the Scope table, verify a synthesis strategy is declared (e.g. 'full synthesis', 'principles + decision criteria', 'enrichment only').
- **FAIL** if any chapter row has no declared strategy.
- The reviewer checks declaration only — never whether the strategy was the correct one.

### Check 10 — Notation hygiene application *(conditional)*

**Guard:** if the vault's CLAUDE.md does not declare the notation hygiene rules (i.e., the algebraic self-check bullet is absent from the Conventions section — verified by searching CLAUDE.md for "self-consistency check" or "algebraic self-check"), score this check as `N/A — vault does not opt into notation hygiene` and skip. Otherwise proceed.

**Scope of "page contains notation":** the page has at least one of: display-math markers (`$$...$$`), inline math markers (`$...$`), formal-logic operators outside of prose, statistical notation with formal symbols, multi-step pseudocode with formal semantics. A passing mention of an equation number in prose without rendering the equation does NOT count.

For pages containing notation, verify that the notation hygiene rules from the vault's CLAUDE.md Conventions section were applied at synthesis time. **Evidence-based check** — verify the artifacts are present; do NOT re-verify the underlying math.

For each in-scope page, run three sub-checks:

(a) **Silent-correction footnotes.** Spot-check 1–2 formulas per page against the cited source. Where the wiki rendering differs from the source rendering on notation (any silent typo fix, normalisation, or convention swap), verify a visible footnote or parenthetical names the discrepancy in the pattern declared by CLAUDE.md ("Source prints X; this page uses Y..."). A wiki–source divergence without a corresponding footnote is **WARN**: silent correction without disclosure.

(b) **Self-consistency artifacts on multi-line formulas.** For any multi-line printed formula on the page (nested fractions, ODE solutions, derivation chains spanning multiple lines):

  - **FAIL** if a "transcription uncertain — awaiting human verification" flag is present at the top of the page. Per book-ingestion-skill.md Phase 3 Theory-heavy chapters, that flag means the page should not have been committed at all; its presence on a page that reached review is a hard violation of the synthesis-time halt rule.
  - **WARN** if no such flag is present AND no self-consistency footnote is present near the formula. Synthesis discipline not visibly applied — the algebraic check may or may not have been done, but no evidence remains.
  - **PASS** if a self-consistency footnote is present recording the algebraic check done at ingestion time.

(c) **Form-variant cross-reference disambiguation.** For each `[[wikilink]]` or inline cross-reference that points to a specific equation in another section or page, verify the reference notes which presentational variant it points to when the cited source uses multiple forms of the same fundamental relation (e.g. "the expectation form of equation (X.N)" rather than a bare "(X.N)"). Bare-number cross-references when multiple forms exist in the source → **WARN**: form-variant ambiguity. If the source uses only one form throughout, this sub-check is N/A.

**Verdict thresholds:**
- **FAIL** only if (b)'s "transcription uncertain" flag condition triggers — that's a hard violation of the synthesis-time halt rule.
- **WARN** for any unresolved (a), (b)-mid, or (c) finding.
- **PASS** if all applicable sub-checks pass or are inapplicable (e.g. no multi-line formulas on the page → (b) is N/A).

**Scope reminder.** This check verifies the discipline was applied — i.e., artifacts are present. It does NOT verify the underlying algebra. Algebraic correctness is a synthesis-time discipline (see book-ingestion-skill.md Phase 3 Theory-heavy chapters); the reviewer is a fidelity auditor, not a re-derivation agent (see Check 8 scope note).

### Compression-ratio diagnostic *(informational — not scored)*

- If no protocol report exists yet, skip.
- If the protocol report exists, produce a per-chapter table:

| Ch. | Source PDF pages | Wiki pages produced | Ratio (PDF pp / wiki pp) |
|---|---|---|---|
| … | … | … | … |

Calculate the book's median ratio. Surface the data; do not flag any chapter as a failure. This table is for the human's judgment.

---

## Phase 3 — Write report

Write the digest to:

- **integer N**: `<vault>/wiki/digests/review-<book>-chN-<YYYY-MM-DD>.md` (e.g. `…-ch10-2026-06-10.md`)
- **named key K**: `<vault>/wiki/digests/review-<book>-<K>-<YYYY-MM-DD>.md` (e.g. `…-afterword-2026-06-10.md`)

Frontmatter:

```yaml
---
title: Review — <Book Title> <unit-label>
aliases: []
source_tier: 1
<topic-field>: [<domain-tag>, book-review, <book-slug>]
date: <today>
last_updated: <today>
type: digest
source_count: 0
status: active
---
```

> `<topic-field>` — the field name for domain/topic tags declared in the vault's CLAUDE.md schema (loaded in Phase 1 step 1; e.g. `topics:` for the software-craft vault). `<domain-tag>` — the fixed domain tag declared as the first entry in that field (e.g. `software-craft`). Apply any other per-type field requirements from CLAUDE.md for `type: digest` pages. If the CLAUDE.md frontmatter schema was not cleanly declared, write the digest with best-effort frontmatter and open the body with `> CONFIG-ERROR: vault CLAUDE.md frontmatter schema not declared — frontmatter written with defaults; fix CLAUDE.md.`

> `<unit-label>` in the title — when `<chapter>` is integer `N`, `<unit-label>` is `Ch.N` (e.g. `Ch.10`), preserving the existing form. When `<chapter>` is a named key K, `<unit-label>` is the meta row label verbatim (e.g. `Afterword`).

Body sections:

1. **Aggregate score** — X/9 checks PASS when Check 10 fires (Check 8 and compression-ratio diagnostic excluded from score; if Check 10 guard says N/A, aggregate is X/8 — listed in results table with N/A reason), N warns, N fails.
2. **Results table** — one row per check: check name | PASS / WARN / FAIL | one-line note.
3. **Warns and fails detail** — for each WARN or FAIL: expanded explanation + suggested fix prompt.
4. **Extraction quality** — Check 8 verdict and any spot-check mismatches.
5. **Compression-ratio diagnostic** — per-chapter table (PDF source pages vs. wiki pages produced; book median ratio). Omit if no protocol report exists yet.
6. **Pages reviewed** — list of all pages read during this review.

Then append one line to `wiki/log.md` — for **integer N**:

```
## [YYYY-MM-DD] digest | <book> ch.N review | <aggregate score>
```

or for **named key K**:

```
## [YYYY-MM-DD] digest | <book> <row-label> review | <aggregate score>
```

---

## Constraints

- Do not modify any wiki page, topic page, entity page, or meta file.
- Do not auto-fix any issue found.
- Do not run headless.
- Do not merge with extraction-skill behavior.
