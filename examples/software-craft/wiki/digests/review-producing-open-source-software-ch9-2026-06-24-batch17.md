---
title: Review — Producing Open Source Software Ch.9 (batch 17 [9b])
aliases: []
source_tier: 1
topics: [software-craft, book-review, producing-open-source-software]
date: 2026-06-24
last_updated: 2026-06-24
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software, Ch.9 "Legal Matters" (batch 17 [9b])

Reviews the batch-17 ingest completing Chapter 9 (PDF pp. 178–190 / printed 165–177):
the legal matters beyond the code license. Strategy: principles + decision criteria.

## Aggregate score

**8/8 applicable scored checks PASS, 0 warn, 0 fail** (Check 9 N/A — end-of-book ingest
report not yet written at review time; Check 10 PASS — no notation on any page). Check 8
(diagnostic, excluded from score): **minor-issues** — 1 silent-omission WARN ("Further
Resources" external reading list), addressed by the orchestrator post-review (see below).

## Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density & anchor accuracy | PASS | Every claim-bearing H2/intro carries an inline citation; all 10 distinct #page anchors (178–188) confirmed in-source; every printed tail = page−13, consistent with PDF footers 165–177. |
| 2 — Wikilink integrity | PASS | All wikilinks resolve; each new page has `## See also` + `**Source entities:** [[…-book]]`. Pair-and-split reciprocal: trademarks↔patents, copyleft↔creative-commons, contributor-agreements↔proprietary-relicensing. |
| 3 — Negative-space discipline | PASS | Every new page has `## Negative Space`; all labels (too-granular, tool-specific/perishable, illustrative-scaffolding, out-of-scope, book-metadata, source-underdeveloped) are from the CLAUDE.md table. |
| 4 — Stance preservation | PASS | "Doing nothing" framed as not-recommended/risky; proprietary relicensing framed as cautionary (Fogel advises against), not a neutral peer option. |
| 5 — Enrichment-not-replacement | PASS | copyleft/forkability/open-source-licensing gained new H2 sections; all prior citations (copyleft 173–179, forkability 72/73/149, licensing 32/33/171–177) preserved; forward-refs resolved to live links. |
| 6 — Frontmatter completeness | PASS | All 11 schema fields present on all 5 new pages; `last_updated: 2026-06-24`; `type: topic`; topics resolve to seeded subjects; roles=tech-lead. |
| 7 — Index & log consistency | PASS | 5 new index entries; Ch.9 marked ✓ in entity chapter index; meta.md ticked [x]; exactly one batch-17 book-ingest log entry. |
| 8 — Extraction quality | minor-issues | Forward spot-checks 4/4 Match; reverse sweep clean except "Further Resources" (book-metadata) unlogged → 1 silent-omission WARN (diagnostic). |
| 9 — Synthesis-strategy declaration | N/A — SKIP | End-of-book ingest report not yet generated at review time (Phase 6 follows). |
| 10 — Notation hygiene | PASS | Vault opts into notation hygiene, but no page contains notation (no display/inline math, formal logic, or pseudocode) → all sub-checks N/A. |

## Warns and fails detail

- **Check 8 — silent omission (WARN, diagnostic):** the source H2 "Further Resources" (printed
  p. 171 — an external reading list: OSI license page, Heather Meeker's *Open (Source) for
  Business*, Van Lindberg's *Intellectual Property and Open Source*, David Wheeler's
  GPL-compatibility essay) is absent from the wiki and was not recorded in the batch-17
  negative-space log. It is legitimately `book-metadata` (a curated external-resource list, not a
  domain concept). **Fix:** add a `book-metadata` negative-space note for "Further Resources" to
  the batch-17 log entry. *(Applied by the orchestrator after this review; disposition becomes
  "negative-space entry," not silent omission.)*

## Extraction quality (Check 8)

**Part A — forward spot-checks (4/4 Match):**

1. **contributor-agreements** — copyright assignment. Source (PDF 178): "This way is the most
   burdensome for contributors, and some contributors simply refuse to do it; only a few projects
   still ask for assignment, and I don't recommend that any project require it these days." Wiki
   renders CA as "the most burdensome … some contributors simply refuse," only a few still ask,
   not recommended. **Match.** (Anchor 178/p.165 confirmed.)
2. **software-patents** — the central claim. Source (PDF 182): "they pose the only real threat
   against which the free software community cannot defend itself." Wiki: "the only real threat
   against which the free software community cannot defend itself." **Match.** (Anchor 182/p.169.)
3. **proprietary-relicensing** — the legal mechanic. Source (PDF 180): "one always has the right
   to not sue one's self for copyright infringement." Wiki quotes it verbatim and ties it to the
   copyleft sole-holder exemption. **Match.** (Anchor 180/p.167.)
4. **creative-commons-licensing** — the carve-out. Source (PDF 187, §2(b)(2)): "Patent and
   trademark rights are not licensed under this Public License." Wiki quotes it exactly. **Match.**
   (Anchor 187/p.174.)

**Part B — reverse omission sweep:**

| Source heading / caveat | Disposition | Detail |
|---|---|---|
| Contributor Agreements (H2) | In wiki | [[contributor-agreements]] |
| Doing Nothing (H3) | In wiki | [[contributor-agreements]] §three options (option 1) + SCO risk |
| Contributor License Agreements (H3) | In wiki | [[contributor-agreements]] §What a CLA actually grants |
| Developer Certificate of Origin / DCO (H3) | In wiki | [[contributor-agreements]] §The DCO: the minimal CLA |
| Proprietary Relicensing (H2) | In wiki | [[proprietary-relicensing]] (two kinds + mechanic) |
| Problems with Proprietary Relicensing (H3) | In wiki | [[proprietary-relicensing]] §Why Fogel advises against it |
| Trademarks (H2) | In wiki | [[trademarks-in-open-source]] |
| Case study: Firefox / Debian / Iceweasel (H3) | In wiki | [[trademarks-in-open-source]] §Two case studies |
| Case study: GNOME Logo / Fish Pedicure (H3) | In wiki | [[trademarks-in-open-source]] §Two case studies |
| Patents (H2) | In wiki | [[software-patents]] |
| Further Resources (H2) | WARN: silent omission → resolved | book-metadata external reading list; negative-space note added to log post-review |
| Appendix A: Copyright / CC BY-SA Public License | In wiki + negative-space | concepts on [[creative-commons-licensing]]; full legal deed logged as `book-metadata` |

**Part C — overall rating:** `minor-issues` (1 diagnostic WARN, not framework-altering;
resolved post-review).

## Pages reviewed

- wiki/topics/contributor-agreements.md (created)
- wiki/topics/proprietary-relicensing.md (created)
- wiki/topics/trademarks-in-open-source.md (created)
- wiki/topics/software-patents.md (created)
- wiki/topics/creative-commons-licensing.md (created)
- wiki/topics/copyleft.md (enriched)
- wiki/topics/forkability.md (enriched)
- wiki/topics/open-source-licensing.md (enriched)
- wiki/entities/books/producing-open-source-software-book.md
- wiki/index.md, wiki/log.md, raw-input/books/producing-open-source-software/meta.md
