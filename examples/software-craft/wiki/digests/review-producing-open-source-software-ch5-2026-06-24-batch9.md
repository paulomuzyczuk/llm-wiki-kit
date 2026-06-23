---
title: Review — Producing Open Source Software Ch.5 (batch 9)
aliases: []
source_tier: 1
topics: [software-craft, book-review, producing-open-source-software]
date: 2026-06-24
last_updated: 2026-06-24
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software Ch.5 (batch 9 [5c])

Scope: batch 9 output only — the most recent `book-ingest | … ch.5 |` entry
([2026-06-24]). Pages: created [[innersourcing]], [[hiring-open-source-developers]],
[[evaluating-open-source-projects]], [[crowdfunding-and-bounties]]; enriched
[[corporate-open-source-participation]].

## Aggregate score

**8/8 applicable PASS, 0 warn, 0 fail** (Check 9 N/A — book in progress; Check 10 PASS — no
notation). Clean on run #2; run #1 found 5 mis-paged citation anchors (Check 1 FAIL), all fixed
before this verdict — see "Run #1 → run #2" below.

## Results table

| # | Check | Verdict | Note |
|---|---|---|---|
| 1 | Citation density & anchor accuracy | PASS | 41 anchor/tail pairs verified against the PDF; 0 mismatches; all tails = #page − 13 |
| 2 | Wikilink integrity | PASS | all links resolve; every page has See also + `**Source entities:**` backlink |
| 3 | Negative-space discipline | PASS | each page has `## Negative Space`; log lists items with valid categories |
| 4 | Stance preservation | PASS | innersource framed as beneficial-but-not-OSS; pitfalls framed as foils |
| 5 | Enrichment-not-replacement | PASS | corporate page: prior sections + citations intact, new content as new H2s |
| 6 | Frontmatter completeness | PASS | all fields present; `last_updated: 2026-06-24`; topics resolve to preferred subjects |
| 7 | Index & log consistency | PASS | 4 new index entries; Ch.5 ticked in meta + entity; one book-ingest log line |
| 8 | Extraction quality (diagnostic) | good | forward spot-checks match; reverse sweep finds no silent omissions |
| 9 | Synthesis-strategy declaration | N/A | no ingest-report yet (book in progress) |
| 10 | Notation hygiene | PASS | no notation on any batch-9 page |

## Run #1 → run #2 (Check 1 fixes applied)

Run #1 FAILed Check 1: five citations pointed at the wrong PDF page because the cited block
overflows a page boundary (offset PDF = printed + 13 is constant, but a printed page spills onto
the next PDF page, so the section's quoted sentence can sit one PDF page later/earlier than its
heading). All five were corrected and re-verified:

1. `hiring-open-source-developers.md` "Read the social record" — `#page=104, p.91` → **`#page=103,
   p.90`** ("threaded view", "negative reactions" are on PDF p.103).
2. `crowdfunding-and-bounties.md` intro — `#page=106, p.93` → **`#page=105, p.92`** ("not because
   they are the same thing … problems are similar" is on PDF p.105).
3. `crowdfunding-and-bounties.md` "two mechanisms" crowdfunding bullet — `#page=106` only → **both
   `#page=105, p.92` and `#page=106, p.93`** (definition spans the page break: "many funders …
   development" on p.105, "keep it all"/"threshold" on p.106).
4. `corporate-open-source-participation.md` publicity section — dropped an erroneous trailing
   `#page=102, p.89`; "first priority is the software"/"perfect accuracy" are on **PDF p.101**.
5. `corporate-open-source-participation.md` middle-management opening — split: "key role …
   succeed or fail" cited to **`#page=101, p.88`** (it sits at the bottom of p.101), the body
   retained at `#page=102, p.89`.

## Extraction quality (Check 8)

**Part A — forward spot-checks:**
- *innersourcing* — wiki: "external supply of freedom … people who could, in principle, fork."
  Source p.103: "require an external supply of freedom. There must always be people who could, in
  principle, fork…" — **Match** (anchor 103/90 correct).
- *evaluating* — wiki: "More bug reports is better"; close-rate "not as important as you might
  think." Source p.105: verbatim — **Match** (anchor 105/92 correct).
- *hiring* — wiki: "influence travel with the person, not with the employer." Source p.104:
  verbatim — **Match** (anchor 104/91 correct).

**Part B — reverse omission sweep:**

| Source heading / caveat (printed pp. 87–93) | Disposition | Detail |
|---|---|---|
| Adoption myth ("pick up and use right away") | In wiki | corporate "Two myths to retire" |
| Casual code-reuse myth | In wiki | corporate "Two myths to retire" |
| Foster Pools of Expertise in Multiple Places | In wiki | corporate (new H2) |
| Establish Contact Early With Relevant Communities | In wiki | corporate (folded into Foster Pools H2) |
| Don't Let Publicity Events Drive Project Schedule | In wiki | corporate (new H2) |
| The Key Role of Middle Management | In wiki | corporate (new H2) |
| InnerSourcing | In wiki | [[innersourcing]] |
| Hiring Open Source Developers | In wiki | [[hiring-open-source-developers]] |
| Hiring for Influence | In wiki | [[hiring-open-source-developers]] |
| Evaluating Open Source Projects | In wiki | [[evaluating-open-source-projects]] |
| Crowdfunding and Bounties | In wiki | [[crowdfunding-and-bounties]] |
| GeoNode case report; Oracle/MS support; Snowdrift; named platforms | Negative-space | logged (case-study-specifics / illustrative-scaffolding / source-underdeveloped / tool-specific) |

No silent omissions. **Overall Check 8 rating: good.**

## Pair-and-split note

Crowdfunding and bounties are co-located on one page ([[crowdfunding-and-bounties]]). Considered
against pair-and-split and judged PASS: they are not a precision/recall-style dichotomy but two
instances of "burst funding" that Fogel deliberately treats under one section heading because they
share the same structural weakness (one-time event vs. ongoing process); each retains an alias
(`crowdfunding`, `bounties`) and its own definition bullet, so both stay independently retrievable.

## Pages reviewed

- wiki/topics/innersourcing.md
- wiki/topics/hiring-open-source-developers.md
- wiki/topics/evaluating-open-source-projects.md
- wiki/topics/crowdfunding-and-bounties.md
- wiki/topics/corporate-open-source-participation.md
- wiki/entities/books/producing-open-source-software-book.md
- wiki/index.md, wiki/log.md, raw-input/books/producing-open-source-software/meta.md
