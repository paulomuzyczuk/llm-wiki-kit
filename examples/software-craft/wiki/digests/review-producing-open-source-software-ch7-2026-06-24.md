---
title: Review — Producing Open Source Software Ch.7
aliases: []
source_tier: 1
topics: [software-craft, book-review, producing-open-source-software]
date: 2026-06-24
last_updated: 2026-06-24
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software, Ch.7 (batch 13 [7b], completing Chapter 7)

**Aggregate: 8/8 applicable checks PASS, 0 WARN, 0 FAIL.** Check 9 N/A (no
ingest-report yet — book in progress, Chapters 8–9 remain). Check 10 PASS (vault opts
into notation hygiene, but no batch-13 page contains notation). Check 8 (diagnostic):
**good**.

This review covers the second-half batch of Chapter 7 (§Testing and Releasing,
§Maintaining Multiple Release Lines, §Security Releases, §Releases and Daily Development,
§Planning Releases; plus the §Compilation/§Binary-Packages packaging principle
enrichment), PDF pp. 142–148 / printed pp. 129–135. Batch 13 completes Chapter 7.

## Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density | PASS | Every claim-bearing H2/H3 carries a PDF-page + printed-page citation; all paths use the `../../raw-input` topics depth; every (page,tail) pair offset = 13, consistent with the verified printed markers 128–135. |
| 2 — Wikilink integrity | PASS | All 18 distinct wikilink targets resolve; every page has `## See also` + `**Source entities:** [[producing-open-source-software-book]]`. Pair-and-split satisfied: security-releases↔security-vulnerability-disclosure and atomic-commits↔version-control bridged reciprocally. |
| 3 — Negative-space discipline | PASS | Log entry lists 13 rejections, all using valid CLAUDE.md labels (too-granular, tool-specific/perishable, illustrative-scaffolding, foreshadowing); each new page has `## Negative Space`. |
| 4 — Stance preservation | PASS | The "ill-thought-out commit" is framed as a foil/anti-pattern in [[atomic-commits]]; the security-release "minor deception" is framed as a necessary constraint, not endorsed sloppiness. |
| 5 — Enrichment-not-replacement | PASS | [[source-packaging]] gained two new H2 sections, prior p.127/PDF140 citations intact; [[version-control]] and [[security-vulnerability-disclosure]] kept all prior citations (PDF 55–74, 126–130 still present), additions are new bullets/sections only. |
| 6 — Frontmatter completeness | PASS | All 11 schema fields present on every new page; `roles:` present on all (topic pages); `last_updated: 2026-06-24` on every created/modified page; `type: topic`. |
| 7 — Index & log consistency | PASS | 5 new pages in `index.md`; Ch.7 marked ✓ (batch 12, 13) in book entity; Ch.7 ticked in `meta.md`; exactly one batch-13 `book-ingest` log entry in schema form. |
| 8 — Extraction quality | good (diagnostic) | 4/4 forward spot-checks + 1 extra = Match; reverse omission sweep clean (table below). |
| 9 — Synthesis-strategy declaration | N/A — SKIP | No `ingest-report-producing-open-source-software-*.md` yet (book in progress). |
| 10 — Notation hygiene | PASS | Vault opts in, but no batch-13 page contains display/inline math, formal operators, or pseudocode → all sub-checks inapplicable. |

## Check 8 — Extraction quality detail

### Part A — Forward spot-checks

1. **[[releasing-and-signing]]** — "tested and approved by some minimum number of
   developers, usually three or more" (p.131 / PDF 144). Source (p.144): *"it should be
   tested and approved by some minimum number of developers, usually three or more."*
   Wiki renders identically. **Match.**
2. **[[maintaining-multiple-release-lines]]** — "releasing 1.1.0 is not sufficient
   reason to end the 1.0.x line" (p.132 / PDF 145). Source (p.145): *"is not sufficient
   reason to end the 1.0.x line."* **Match.**
3. **[[security-releases]]** — "existing release plus the fixes for the security bug,
   with no other changes" (p.132 / PDF 145). Source (p.145): verbatim. **Match.**
4. **[[source-packaging]]** (enriched) — packagers "should always base their binary
   packages on an official source release" (p.130 / PDF 143). Source (p.143): verbatim;
   confirmed on PDF 143, not 144. **Match.**
5. **[[atomic-commits]]** — "The original commit really should have been four separate
   commits" (p.134 / PDF 147). Source (p.147): verbatim. **Match.**

No ASCII figure reproductions. All anchors re-confirmed in-source during spot-checks.

### Part B — Reverse omission sweep

| Source heading / caveat (pp. 128–135) | Disposition | Detail |
|---|---|---|
| CHANGES / NEWS file + changelist | Negative-space + partial in-wiki | Per-file layout `too-granular` (log); changelist-in-announcement captured in [[releasing-and-signing]] |
| "release must not be a working copy" rule | Negative-space | `too-granular` (log) — packaging mechanic |
| To Capitalize or Not to Capitalize | Subsumed | Covered by [[source-packaging]] "Name" principle (no-surprises unpacked dir name) |
| Pre-Releases (package naming) | Subsumed | Qualifier semantics in [[release-numbering]]; package-name carry in [[source-packaging]] |
| Compilation and Installation | In wiki | [[source-packaging]] §"Conform to the standard build and install procedure" |
| Binary Packages | In wiki | [[source-packaging]] §"Binary packages must derive from an official source release" |
| Testing and Releasing | In wiki | [[releasing-and-signing]] (approval-by-testing, signing, hashing) |
| Candidate Releases | In wiki | [[releasing-and-signing]] §"Candidate releases: exposure before the blessing" |
| Announcing Releases | In wiki | [[releasing-and-signing]] §"Announcing a release" |
| Maintaining Multiple Release Lines | In wiki | [[maintaining-multiple-release-lines]] |
| Security Releases | In wiki | [[security-releases]] |
| Releases and Daily Development | In wiki | [[atomic-commits]] |
| Planning Releases | In wiki | [[release-planning]] |
| Caveat: "no amount of formalization obviates human judgement" (carried from 7a) | In wiki | Already in [[stabilizing-a-release]] (batch 12) |
| Caveat: bonds-of-obligation run both ways (packagers) | In wiki | [[source-packaging]] binary-packages section |

Nothing substantive silently omitted. The §Digital-signature/hash *mechanics* and
GnuPG key-management are author-declared out-of-scope and correctly logged as
`too-granular`.

## Convergence note

The ingestion plan flagged [[continuous-integration]] as a Ch.7b convergence target
(testing & releasing, daily development). It was **not** enriched: Fogel's "Testing and
Releasing" is *manual developer approval + OpenPGP signing*, structurally distinct from
automated CI/build-on-integration (the source only cross-refs the regression suite in
passing). Recorded as a convergence-miss in the log rather than forced. This is a
correct disposition, not an omission.

## Pages reviewed

- Created: [[releasing-and-signing]], [[maintaining-multiple-release-lines]],
  [[security-releases]], [[atomic-commits]], [[release-planning]]
- Enriched: [[source-packaging]], [[version-control]], [[security-vulnerability-disclosure]]
- Operational: `wiki/index.md`, `wiki/log.md`, `wiki/topics-authority.md`,
  `raw-input/books/producing-open-source-software/meta.md`,
  `wiki/entities/books/producing-open-source-software-book.md`
