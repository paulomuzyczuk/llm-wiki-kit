---
title: Review — Producing Open Source Software Ch.8 (batch 14 [8a])
aliases: []
source_tier: 1
topics: [software-craft, book-review, producing-open-source-software]
date: 2026-06-24
last_updated: 2026-06-24
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software, Ch.8 "Managing Participants" (batch 14 [8a])

**Aggregate: 8/8 applicable checks PASS, 0 WARN, 0 FAIL.** Check 9 N/A (no ingest report yet —
book in progress). Check 10 PASS (no notation present on any reviewed page). Check 8 diagnostic
rating: **good**. Ch.8 is partially ingested (8a); meta.md and the book entity correctly show
⏳ partial — the full tick + `✓ reviewed-clean` are deferred to batch 15 [8b].

## Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density | PASS | Every claim section/subsection cited at PDF-page granularity; all paths `../../raw-input/...` (correct topics depth); all 22 `#page` anchors + printed-page tails verified against PDF footers (printed = PDF−13, confirmed 136–146). |
| 2 — Wikilink integrity | PASS | All 7 new pages carry `## See also` + `**Source entities:** [[producing-open-source-software-book]]`. Only deliberate dead links: `[[forks]]` (forkability, batch 15) and `[[transitions]]` (praise-and-criticism, batch 15). Pair handling noted below. |
| 3 — Negative-space discipline | PASS | Every new page has `## Negative Space`; log entry enumerates rejections with valid CLAUDE.md labels (supporting-argument, subsumed-by, illustrative-scaffolding, too-granular, case-study-specifics, tool-specific/perishable, foreshadowing). |
| 4 — Stance preservation | PASS | Foils framed as foils: territoriality, cookie licking, author tags, "That was sloppy", verbose-posting status norm, the angry/curt bug-report reply, the "fountain of bile" rude user — all negative-framed, none as peer alternatives. |
| 5 — Enrichment-not-replacement | PASS | governance, forkability, continuous-integration, open-source-participation enriched via new H2/See-also only; prior citations intact (CI retains all 6 Guo & Leitner refs; governance/forkability retain Ch.4 refs). |
| 6 — Frontmatter completeness | PASS | All 11 modified topic pages carry the full schema; `last_updated: 2026-06-24`; `type: topic`. CI `source_count` correctly raised 1→2 (now cites Fogel + the paper). |
| 7 — Index & log consistency | PASS | 7 new pages in index.md; exactly one `book-ingest | … ch.8 |` log entry; meta.md + entity show Ch.8 ⏳ partial (intentional — split chapter, completion at batch 15). |
| 8 — Extraction quality | good | 3/3 forward spot-checks Match; reverse omission sweep clean (one negative-space disposition: Meeting In Person). Diagnostic only — not scored. |
| 9 — Synthesis-strategy declaration | N/A — SKIP | No `ingest-report-*` yet; book in progress. |
| 10 — Notation hygiene | PASS | Vault opts into notation hygiene, but no reviewed page contains notation (no math/formal markers); all sub-checks N/A. |

## Notes on Check 2 — pair handling

The chapter contains several conceptual pairs; each was grained deliberately, not conflated:

- **Praise vs. criticism** → one page `[[praise-and-criticism]]`. This is *faithful to stance*,
  not a conflation: Fogel's explicit thesis is that "praise and criticism are not opposites; in
  many ways, they are very similar" (both are forms of attention). Splitting them would
  misrepresent the author's framing. PASS, not WARN.
- **Regression vs. unit testing** → captured as an explicit contrast (retrospective vs.
  prospective) within `[[the-automation-ratio]]` §"Regression vs. unit testing". The source
  treats them in a brief sidebar — below the anchor-page threshold (a section + ≥2 connections)
  — so two standalone pages would be over-granular. The contrast is preserved, not lost.
- **Inquiry vs. assignment** → a sub-distinction of delegation, captured as a section within
  `[[delegation-in-open-source]]`, with the contrast explicit. Not two standalone concepts.

## Check 8 — extraction quality

### Part A — forward spot-checks

1. **"Attention is the true currency"** — wiki `[[contributor-motivation]]` and
   `[[sharing-project-management]]` render: *"The true currency of open source projects is
   attention… people who can see that they are getting attention will keep participating."*
   Source (PDF p.159 / printed 146): "The true currency of open source projects is attention:
   people who can see that they are getting attention will keep participating, even if not every
   patch they submit lands." **Match.** Anchor `#page=159`, tail p.146 — both correct.
2. **Automation ratio = 10×** — wiki `[[the-automation-ratio]]`: *"automating a common task is
   worth at least ten times the effort a developer would spend doing that task manually one
   time."* Source (PDF p.154 / printed 141): identical wording. **Match.** Anchor `#page=154`,
   tail p.141 — both correct.
3. **Cookie licking attribution** — wiki `[[preventing-territoriality]]` credits Sumana
   Harihareswara: *"Nobody in their right mind would pick up and eat the licked cookie."*
   Source (PDF p.152 / printed 139): "The wonderful term cookie licking, which I first heard
   from Sumana Harihareswara… 'Nobody in their right mind would pick up and eat the licked
   cookie or finish the [task].'" **Match.** Attribution correct; anchor `#page=152`, tail
   p.139 — both correct.

No ASCII figure reproductions (the chapter has no figures).

### Part B — reverse omission sweep

| Source heading / caveat (PDF pp.149–159) | Disposition | Detail |
|---|---|---|
| Chapter intro — politics is inevitable | In wiki | `[[open-source-governance]]` §"Politics is inevitable" |
| Community and Motivation | In wiki | `[[contributor-motivation]]` |
| Delegation | In wiki | `[[delegation-in-open-source]]` |
| Distinguish Clearly Between Inquiry and Assignment | In wiki | `[[delegation-in-open-source]]` § |
| Follow Up After You Delegate | In wiki | `[[delegation-in-open-source]]` § |
| Notice What People Are Interested In | In wiki | `[[delegation-in-open-source]]` § |
| Praise and Criticism | In wiki | `[[praise-and-criticism]]` |
| Prevent Territoriality | In wiki | `[[preventing-territoriality]]` |
| Cookie Licking | In wiki | `[[preventing-territoriality]]` § |
| Banning author tags (Sander Striker) | In wiki | `[[preventing-territoriality]]` § |
| The Automation Ratio | In wiki | `[[the-automation-ratio]]` |
| Automated testing | In wiki | `[[the-automation-ratio]]` § + `[[continuous-integration]]` enrichment |
| Regression Testing and Unit Testing | In wiki | `[[the-automation-ratio]]` § |
| Treat Every User as a Potential Participant | In wiki | `[[treating-users-as-participants]]` |
| Meeting In Person (Conferences, Hackfests…) | Negative-space | `subsumed-by [[funding-non-programming-activities]]`; nuance "primary output is social connections" captured on `[[contributor-motivation]]` |
| Share Management Tasks as Well as Technical Tasks | In wiki | `[[sharing-project-management]]` |
| "Manager" Does Not Mean "Owner" | In wiki | `[[sharing-project-management]]` § |
| Patch Manager (or Pull Request Manager) | In wiki | `[[sharing-project-management]]` § |
| Translation Manager | In wiki | `[[sharing-project-management]]` § (continues p.160+ → batch 15 range) |

Nothing substantive omitted.

### Part C — overall rating

**good** — no mismatches, no unsourced derivations, no silent omissions.

## Pages reviewed

- Created: `[[contributor-motivation]]`, `[[delegation-in-open-source]]`, `[[praise-and-criticism]]`,
  `[[preventing-territoriality]]`, `[[the-automation-ratio]]`, `[[treating-users-as-participants]]`,
  `[[sharing-project-management]]`
- Enriched: `[[open-source-governance]]`, `[[forkability]]`, `[[continuous-integration]]`,
  `[[open-source-participation]]`
- `wiki/entities/books/producing-open-source-software-book.md`, `wiki/index.md`, `wiki/log.md`,
  `raw-input/books/producing-open-source-software/meta.md`, `wiki/topics-authority.md`
