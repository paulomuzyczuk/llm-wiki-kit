---
title: Review — Producing Open Source Software Ch.7 (batch 12 [7a])
aliases: []
source_tier: 1
topics: [release-engineering, book-review, producing-open-source-software]
date: 2026-06-24
last_updated: 2026-06-24
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software Ch.7 (batch 12 [7a])

**Scope:** Ch.7 "Packaging, Releasing, and Daily Development", first half (§Release
Numbering, §Release Branches, §Stabilizing a Release, §Packaging), PDF pp. 132–140
(printed pp. 119–127). Full synthesis; Packaging captured as governing principle only.

## Aggregate score

**8/8 applicable PASS**, 0 WARN, 0 FAIL. Check 9 N/A (no ingest-report yet — book in
progress). Check 10 fires (vault opts into notation hygiene) → PASS, no notation on any
page. One Check 1 anchor inaccuracy found on run #1 and fixed; clean on run #2.

## Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density & anchor accuracy | PASS | Every H2/H3 with original claims cited at PDF-page granularity; all #page anchors + printed-page tails verified against the PDF's own footers (offset −13 confirmed). Run #1: one spurious `#page=133, p.120` anchor on release-branches' parallelize/bored-developer claim (content is wholly on PDF 132) — removed; clean on run #2. |
| 2 — Wikilink integrity | PASS | All wikilinks resolve; each page has ## See also + book-entity backlink; reciprocal links among the three paired release pages present. Pair-and-split honored. |
| 3 — Negative-space discipline | PASS | All four pages carry ## Negative Space; log entry enumerates rejections with valid CLAUDE.md categories. |
| 4 — Stance preservation | PASS | Full-tree snapshots and the last-minute feature rush framed as failure modes, not peer options. |
| 5 — Enrichment-not-replacement | PASS | version-control gained a new H2 ("Branches for release isolation"); prior content/citations intact. launching + security-vuln cross-refs repointed only. |
| 6 — Frontmatter completeness | PASS | All schema fields present; last_updated 2026-06-24; type topic; topics:[release-engineering] (valid subject); roles valid. |
| 7 — Index & log consistency | PASS | 4 new index entries; one book-ingest log entry in schema form; meta.md Ch.7 ticked [x] (bare — chapter continues batch 13); book entity shows ⏳ batch 12 (7a) with the 4 pages. Partial-chapter marking per multi-batch convention (cf. Ch.5/Ch.6 batches). |
| 8 — Extraction quality | good | 3/3 forward spot-checks Match; reverse sweep clean (table below). |
| 9 — Synthesis-strategy declaration | N/A — SKIP | No ingest-report-*.md yet; book in progress. |
| 10 — Notation hygiene | PASS | No display/inline math, formal logic, or pseudocode on any page (release-number strings like "2.6.0" are not notation). |

## Warns and fails detail

**Run #1 — Check 1 (resolved).** release-branches.md cited the chapter-opening
parallelize/bored-developer claim with two anchors, `#page=132, p.119` and
`#page=133, p.120`. Grep of PDF 133 confirms none of `bored`/`parallelizing`/`master`/
`idle` appears there; the entire claim is on PDF 132. Fix applied: dropped the spurious
`#page=133, p.120` anchor, leaving `#page=132, p.119`. Re-verified clean.

No outstanding WARNs or FAILs.

## Extraction quality (Check 8)

**Forward spot-checks — 3/3 Match:**

| Claim (wiki) | Source sentence (<15 words) | Verdict |
|---|---|---|
| Subversion release vote: ≥3 `+1`, none against; one `-1` = veto (stabilizing-a-release) | "at least three developers must vote in favor of it, and none against" (PDF 138 / p.125) | Match |
| Even/odd: even stable, odd unstable (release-numbering) | "even means stable, odd means unstable" (PDF 135 / p.122) | Match |
| Semver micro = bug fixes only, both-way compatible (release-numbering) | "must be both forward- and backward-compatible. The changes should be bug fixes only" (PDF 134 / p.121) | Match |

**Reverse omission sweep:**

| Source heading / caveat | Disposition | Detail |
|---|---|---|
| Ch.7 intro — parallelize independent tasks | In wiki | [[release-branches]] (the principle motivating release branches) + [[release-numbering]] (bored-developer) |
| Release Numbering | In wiki | [[release-numbering]] |
| — Some Projects Just Need Release Identifiers | In wiki | [[release-numbering]] §"When you may skip semantic numbers" |
| — Release Number Components | In wiki | [[release-numbering]] §"Number components" (incl. Alpha/Beta/RC qualifiers) |
| — Semantic Versioning | In wiki | [[release-numbering]] §"Semantic Versioning" (incl. semver.org forward-compat divergence note) |
| — The Even/Odd Strategy | In wiki | [[release-numbering]] §"The even/odd strategy" |
| Release Branches | In wiki | [[release-branches]] |
| — Mechanics of Release Branches | In wiki | [[release-branches]] §"Mechanics" |
| Stabilizing a Release | In wiki | [[stabilizing-a-release]] |
| — Time-Based vs Feature-Based Releases | In wiki | [[stabilizing-a-release]] §"Time-based vs. feature-based releases" |
| — Dictatorship by Release Owner | In wiki | [[stabilizing-a-release]] §"Dictatorship by release owner" |
| — Voting on Changes | In wiki | [[stabilizing-a-release]] §"Voting on changes" |
| — Managing Collaborative Release Stabilization | In wiki | [[stabilizing-a-release]] §"Running a change-voting system" (STATUS file, singularity of information) |
| — Release Manager | In wiki | [[stabilizing-a-release]] §"The release manager" |
| Packaging | In wiki | [[source-packaging]] (governing principle) |
| — Format | In wiki | [[source-packaging]] |
| — Name and Layout (Name) | In wiki | [[source-packaging]] (Name); Layout detail (README/INSTALL/CHANGES, working-copy rule) on printed p.128+ → negative-space (too-granular), batch 13 |
| Michlmayr time-based-release further reading | Negative-space entry | tool-specific/perishable (log) |

Nothing substantive omitted within batch scope. Overall rating: **good**.

## Pages reviewed

- wiki/topics/release-numbering.md (created)
- wiki/topics/release-branches.md (created)
- wiki/topics/stabilizing-a-release.md (created)
- wiki/topics/source-packaging.md (created)
- wiki/topics/version-control.md (enriched)
- wiki/topics/launching-an-open-source-project.md (cross-ref repointed)
- wiki/topics/security-vulnerability-disclosure.md (cross-ref repointed)
- wiki/entities/books/producing-open-source-software-book.md
- wiki/index.md, wiki/log.md, wiki/topics-authority.md
