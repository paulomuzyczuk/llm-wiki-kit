---
title: Review — Producing Open Source Software Ch.5
aliases: []
source_tier: 1
topics: [software-craft, book-review, producing-open-source-software]
date: 2026-06-23
last_updated: 2026-06-23
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software, Ch.5 (batch 7 [5a])

Scope: batch 7 of a multi-batch chapter — Ch.5 "Organizations and Money," PDF pp. 80–91
(printed pp. 67–78). Full-synthesis strategy. Ch.5 continues in batches 8–9; this review
covers only the pages produced/enriched by batch 7.

## 1. Aggregate score

**8/8 applicable checks PASS — 0 WARN, 0 FAIL.** Check 9 N/A (no ingest report yet — book in
progress). Check 10 fires (vault opts into notation hygiene) and PASSes (no notation on any
reviewed page). Check 8 is diagnostic: **good**.

## 2. Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density | PASS | Every H2/H3 with original claims cited at PDF-page granularity; all 12 distinct `#page` anchors (80–91) resolve; every tail = printed = PDF−13, confirmed against the PDF's own printed footers. |
| 2 — Wikilink integrity | PASS | All `[[wikilinks]]` resolve; each new page has a `## See also` and a `**Source entities:** [[producing-open-source-software-book]]` backlink. No conflated concept pair. |
| 3 — Negative-space discipline | PASS | All 4 new pages carry `## Negative Space`; log entry lists 13 rejections, every label from the CLAUDE.md table. |
| 4 — Stance preservation | PASS | Proprietary relicensing, "vendors don't want open source," and the CVS-protocol case all framed as cautionary/foil, not neutral peers. |
| 5 — Enrichment-not-replacement | PASS | `open-source-governance` gained one new H2 (funding strains the BD model); all prior Ch.4 citations (p72–79) intact, no prose overwritten. |
| 6 — Frontmatter completeness | PASS | All 11 schema fields present on each new page; `last_updated: 2026-06-23`; `type: topic`; `roles:` present. |
| 7 — Index/log consistency | PASS | 4 new pages in `index.md`; book entity + `meta.md` both show Ch.5 as in-progress (◐ batch 7) consistently; exactly one schema-form `book-ingest` log entry. (Chapter-complete tick correctly deferred — Ch.5 spans batches 7–9.) |
| 8 — Extraction quality | good | 4/4 forward spot-checks Match; reverse omission sweep finds no silent omissions. |
| 9 — Synthesis-strategy declaration | N/A — SKIP | No ingest report yet (book in progress). |
| 10 — Notation hygiene | PASS | No notation on any reviewed page; vault opts in, so check fires and passes vacuously. |

## 3. WARNs and FAILs detail

None.

## 4. Extraction quality (Check 8)

**Part A — forward spot-checks (4):**

| Claim (wiki) | Source quote | Page | Verdict |
|---|---|---|---|
| Money "buys development credibility, which is convertible to influence" | "it buys development credibility, which is convertible to influence through the…" | p81 / p.68 | Match |
| OSQA costs "on the order of 5% to 10%" of the main contract | "expect on the order of 5% to 10%" | p91 / p.78 | Match |
| Keep developers "a couple of years, at a minimum" | "a couple of years, at a minimum" | p84 / p.71 | Match |
| Community scrutiny is "a free design board and QA department" | "think of it as a free design board and QA department" | p89 / p.76 | Match |

**Part B — reverse omission sweep:**

| Source heading/caveat | Disposition | Detail |
|---|---|---|
| The Economics of Open Source | In wiki | [[open-source-economics]] |
| Goals of Corporate Involvement (8 motivations) | In wiki | [[open-source-economics]] — taxonomy as decision criteria |
| Governments and Open Source | In wiki | [[government-and-open-source]] |
| Being Open Source From Day One … for Government | In wiki | [[government-and-open-source]] |
| Hire for the Long Term | In wiki | [[corporate-open-source-participation]] |
| Case study (CollabNet new-hire review) | Negative-space | case-study-specifics |
| Appear as Many, Not as One | In wiki | [[corporate-open-source-participation]] |
| Be Open About Your Motivations | In wiki | [[corporate-open-source-participation]] |
| Money Can't Buy You Love | In wiki | [[corporate-open-source-participation]] + enriched [[open-source-governance]] |
| Contracting | In wiki | [[open-source-contracting]] |
| Hiring From Within / Outside the Community | In wiki | [[open-source-contracting]] |
| Contracting and Transparency | In wiki | [[open-source-contracting]] |
| Review and Acceptance of Changes | In wiki | [[open-source-contracting]] — "free design board" |
| Case Study: CVS Password-Authentication | In wiki + negative-space | cautionary tale captured; specifics rejected (case-study-specifics) |
| Update Your RFI, RFP and Contract Language | In wiki | [[open-source-contracting]] |
| Open Source Quality Assurance (OSQA) | In wiki | [[open-source-contracting]] |

Nothing substantive omitted. Overall rating: **good**.

## 5. Compression-ratio diagnostic

Omitted — no ingest report exists yet (book in progress).

## 6. Pages reviewed

- `wiki/topics/open-source-economics.md` (new)
- `wiki/topics/corporate-open-source-participation.md` (new)
- `wiki/topics/government-and-open-source.md` (new)
- `wiki/topics/open-source-contracting.md` (new)
- `wiki/topics/open-source-governance.md` (enriched)
- `wiki/entities/books/producing-open-source-software-book.md`
- `wiki/index.md`, `wiki/log.md`, `raw-input/books/producing-open-source-software/meta.md`
