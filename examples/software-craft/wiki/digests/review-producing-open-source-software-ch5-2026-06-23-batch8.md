---
title: Review — Producing Open Source Software Ch.5 (batch 8 [5b])
aliases: []
source_tier: 1
topics: [software-craft, book-review, producing-open-source-software]
date: 2026-06-23
last_updated: 2026-06-23
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software Ch.5 (batch 8 [5b])

Scope: batch 8 of the multi-batch Ch.5 ingest — §Funding Non-Programming Activities +
§Marketing (PDF pp. 92–98, printed pp. 79–85). Pages created: [[funding-non-programming-activities]],
[[open-source-marketing]]. Page enriched: [[open-source-contracting]] (The New Developer Test).
Ch.5 remains in progress (batch 9 covers §Open Source and the Organization → end of chapter), so
chapter-complete tick is intentionally deferred — same mid-chapter posture as the batch 7 review.

## 1. Aggregate score

**8/8 applicable checks PASS**, 0 WARN, 0 FAIL. Check 9 N/A (book in progress — no ingest report
yet). Check 10 PASS (notation hygiene declared by CLAUDE.md; no notation present on these pages).

## 2. Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density | PASS | Every H2/H3 with original claims carries a PDF-page + printed-page citation; all 7 distinct anchors (pp. 92–98) verified against source; tails match the PDF's printed footers (offset −13). |
| 2 — Wikilink integrity | PASS | All `[[wikilinks]]` resolve; both new pages carry `## See also` and the `**Source entities:** [[producing-open-source-software-book]]` backlink. No conflated concept pair. |
| 3 — Negative-space discipline | PASS | 9 negative-space items logged across the two pages, every label drawn verbatim from the CLAUDE.md table. |
| 4 — Stance preservation | PASS | Foils framed as foils: "Community/Enterprise Edition" mislabeling, "you can't fake it," and competitor-bashing all carry negative framing. |
| 5 — Enrichment-not-replacement | PASS | open-source-contracting: New Developer Test added as a new H2 before Negative Space; all prior OSQA citations intact; Sources + See also extended, not overwritten. |
| 6 — Frontmatter completeness | PASS | All schema fields present on both new pages; `roles: [tech-lead]`, `source_tier: 1`, `source_count: 1`, `type: topic`. |
| 7 — Index/log consistency | PASS | Both new pages in index.md; entity chapter index + meta annotated for batch 8; exactly one book-ingest log line appended. Chapter-complete tick deferred (multi-batch chapter). |
| 8 — Extraction quality | good | 3 forward spot-checks Match; reverse omission sweep shows every batch-8 heading dispositioned. |
| 9 — Synthesis-strategy declaration | N/A — SKIP | No ingest report yet (book in progress). |
| 10 — Notation hygiene | PASS | CLAUDE.md opts in; no notation on these pages → sub-checks N/A. |

## 3. WARNs and FAILs detail

None.

## 4. Extraction quality (Check 8)

### Part A — Forward spot-checks

1. **Documentation staffing** (funding-non-programming-activities, p. 94 / printed 81).
   Source: "A medium-level user is probably the right person to write good documentation."
   Wiki: renders the medium-level-user heuristic verbatim with the "recent enough… past them"
   framing. **Match.**
2. **Cost-of-total-ownership inversion** (open-source-marketing, p. 96 / printed 83).
   Source: "'cost of total ownership', that is, how much does it cost a company to be totally
   owned…" Wiki: quotes the inversion and "customers are not owned — they are the owners."
   **Match.**
3. **Commerciality of open source** (open-source-marketing, p. 98 / printed 85).
   Source: "commercial by definition" (the license guarantees freedom for any commercial purpose).
   Wiki: quotes "commercial by definition" and ties it to the procurement-language harm. **Match.**

No ASCII figure reproduction; no statistic/date derived beyond the source.

### Part B — Reverse omission sweep

| Source heading/caveat (pp. 92–98) | Disposition | Detail |
|---|---|---|
| The "New Developer" Test | In wiki | [[open-source-contracting]] (new H2) |
| Don't Surprise Your Lawyers | In wiki | funding-non-programming-activities §Legal advice |
| Funding Non-Programming Activities (intro / bridging) | In wiki | funding… §The bridging principle |
| Technical Quality Assurance | In wiki | funding… §Professional testing |
| Legal Advice and Protection | In wiki | funding… §Legal advice |
| Documentation and Usability | In wiki | funding… §Documentation and usability |
| Funding User Experience (UX) Work | In wiki | funding… §UX work |
| Providing Build Farms and Development Servers | In wiki | funding… §Infrastructure |
| Running Security Audits | In wiki | funding… §Security audits |
| Sponsoring Conferences, Hackathons | In wiki | funding… §Sponsoring in-person meetings |
| Marketing (intro) | In wiki | open-source-marketing (lede) |
| Open Source and Freedom from Vendor Lock-In | In wiki | marketing §The structural advantage / §Cost of total ownership |
| Remember That You Are Being Watched | In wiki | marketing §Remember that you are being watched |
| Case Study: You Can't Fake It | Negative-space entry | illustrative-scaffolding (Singer 5) |
| Don't Bash Competing Vendors' Efforts | In wiki | marketing §Don't bash competing vendors |
| "Commercial" vs "Proprietary" | In wiki | marketing §Terminology integrity |

Nothing substantive omitted. (Dirk Reiners email, Global Megacorp analogy, marketing arms-race
aside, and the Publicity/Don't-Bash cross-refs all carry explicit negative-space labels.)

### Part C — Overall rating

**good** — no mismatches, no unsourced derivations, no silent omissions.

## 5. Compression-ratio diagnostic

Omitted — no ingest report exists yet (book in progress).

## 6. Pages reviewed

- wiki/topics/funding-non-programming-activities.md (new)
- wiki/topics/open-source-marketing.md (new)
- wiki/topics/open-source-contracting.md (enriched)
- wiki/entities/books/producing-open-source-software-book.md
- wiki/index.md, wiki/log.md, raw-input/books/producing-open-source-software/meta.md
- raw-input/books/producing-open-source-software/producing-open-source-software.pdf (pp. 92–98, spot-checks)
