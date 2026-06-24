---
title: Review — Producing Open Source Software Ch.8 (batch 15 [8b])
aliases: []
source_tier: 1
topics: [software-craft, book-review, producing-open-source-software]
date: 2026-06-24
last_updated: 2026-06-24
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software, Ch.8 "Managing Participants" (batch 15 [8b])

Review of the batch-15 ingest (Ch.8 second half: §Transitions, §Committers incl. §Credit,
§Forks — PDF pp. 162–170 / printed 149–157), which completes Chapter 8. Run #1 found 2
citation-anchor FAILs (Check 1); both were fixed and confirmed clean on run #2. Final verdict
below reflects the corrected pages.

## Aggregate score

**9/9 applicable checks PASS** (Check 8 diagnostic + compression-ratio excluded from score;
Check 9 N/A — no ingest-report yet, book in progress). **0 WARN, 0 unresolved FAIL** (2 Check-1
anchor FAILs found on run #1, fixed, re-verified on run #2).

## Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density & anchor accuracy | PASS (after fix) | Density/format/depth clean throughout. 2 cross-boundary anchors corrected (see below); all anchors re-verified vs PDF footers 149–157 (printed = PDF − 13). |
| 2 — Wikilink integrity | PASS | All wikilinks resolve; source-entity backlinks on all 8 pages; pair-and-split forkability↔forks reciprocal verified (resolves prior dead [[forks]]); transitions resolves prior dead [[transitions]]. |
| 3 — Negative-space discipline | PASS | Log + per-page Negative Space use only CLAUDE.md categories (illustrative-scaffolding, case-study-specifics, tool-specific/perishable, subsumed-by, too-granular). |
| 4 — Stance preservation | PASS | Foils framed as foils: "exclusive club" committership, auto-expiring dormant access, the "add a helper" transition dodge, fork-as-debating-threat, the three-party-email mistake. |
| 5 — Enrichment-not-replacement | PASS | forkability, praise-and-criticism, open-source-participation, code-review enriched additively; prior citations intact; new content in new H2s; open-source-participation source_count 1→2 with Fogel entity added. |
| 6 — Frontmatter completeness | PASS | All schema fields present on 4 new + 4 enriched pages; topics resolve to preferred subjects; last_updated = 2026-06-24. |
| 7 — Index & log consistency | PASS | 4 new pages in index.md; Ch.8 ticked in meta.md + book entity (✓ batch 14, 15); exactly one ch.8 batch-15 book-ingest log entry. |
| 8 — Extraction quality | *diagnostic: good* | 3/3 forward spot-checks Match; reverse omission sweep clean. |
| 9 — Synthesis-strategy declaration | N/A — SKIP | No ingest-report yet (book in progress; only Ch.9 remains). |
| 10 — Notation hygiene | PASS | Vault opts in, but no page contains notation → all sub-checks N/A. |

## Fixes applied between run #1 and run #2 (both Check 1)

1. **`credit-and-attribution.md`** — the quote "keeps accurate records of who did what, when"
   was anchored `#page=167, p. 154` but appears on PDF p. 166 (printed 153). Split into two
   citations: the "who did what, when" quote → `#page=166, p. 153`; "be specific / J. Random /
   reproduction recipe" → `#page=167, p. 154`. Re-verified: `did what`→p.166, `reproduction`→p.167.
2. **`forks.md`** — the GCC/EGCS quotes ("adopted the EGCS codebase", "a single GCC, but greatly
   improved", "you cannot always regard a fork as an unadulteratedly bad thing") were anchored
   `#page=170, p. 157` but appear on PDF p. 169 (printed 156). Split: GCC/EGCS + "cannot always
   regard" → `#page=169, p. 156`; "keep an eye on it / who joins / avoid the fork by becoming it"
   → `#page=170, p. 157`. Re-verified: `unadulteratedly`/`codebase`→p.169, `mindshare`→p.170.

## Extraction quality (Check 8)

**Forward spot-checks (3/3 Match):**
1. `committers.md` — "If you have 100 committers, 12 of whom make large changes… that's still
   better than having only the 12." Source PDF 165 (p.152): verbatim. **Match.**
2. `credit-and-attribution.md` — "slightly over two-thirds of people who later became committers
   themselves were credited in this way… before becoming a committer." Source PDF 167 (p.154):
   faithful. **Match.**
3. `forks.md` — "a fork is, in essence, a vote of confidence." Source PDF 169 (p.156): verbatim.
   **Match.**

**Reverse omission sweep:**

| Source heading / caveat | Disposition | Detail |
|---|---|---|
| §Transitions | In wiki | [[transitions]] |
| §Committers — Defining "Committer" / Commit Access | In wiki | [[committers]] (intro: authoritative repo as social concept) |
| §Committers vs Maintainers | In wiki | [[committers]] (formally-distinct-class section) |
| §Choosing Committers | In wiki | [[committers]] (Hippocratic Principle) |
| §Revoking Commit Access | In wiki | [[committers]] |
| §Partial Commit Access | In wiki | [[committers]] |
| §Dormant Committers | In wiki | [[committers]] |
| §Avoid Mystery | In wiki | [[committers]] (publish rules + roster) |
| §Credit | In wiki | [[credit-and-attribution]] |
| §Forks — Development vs Hard Forks | In wiki | [[forks]] |
| §Figuring Out Whether You're the Fork | In wiki | [[forks]] |
| §Handling a Fork (incl. GCC/EGCS) | In wiki | [[forks]] |
| §Initiating a Fork | In wiki | [[forks]] |
| Caveat: "review would spot those quickly anyway" | In wiki | [[committers]] + [[code-review]] enrichment |
| Caveat: "committers before should remain committers afterward" | In wiki | [[forks]] handling section |
| Caveat: "the perceptions are the objective truth" | In wiki | [[forks]] which-side section |
| §Documentation Manager, §Issue Manager (PDF 160–161) | Negative-space (batch 14) | `too-granular` on [[sharing-project-management]] ("further documentation/issue/FAQ managers… past this batch's page range"); §Sharing Management Tasks tail, not batch-15 scope |
| I18N vs L10N (PDF 160) | In wiki (batch 6) | [[translation-infrastructure]] |

Nothing substantive silently omitted from the batch-15 scope. Overall rating: **good**.

## Pages reviewed

- `wiki/topics/committers.md` (new)
- `wiki/topics/transitions.md` (new)
- `wiki/topics/forks.md` (new)
- `wiki/topics/credit-and-attribution.md` (new)
- `wiki/topics/forkability.md` (enriched)
- `wiki/topics/praise-and-criticism.md` (enriched)
- `wiki/topics/open-source-participation.md` (enriched)
- `wiki/topics/code-review.md` (enriched)
- `wiki/entities/books/producing-open-source-software-book.md`
- `wiki/index.md`, `wiki/log.md`, `raw-input/books/producing-open-source-software/meta.md`
