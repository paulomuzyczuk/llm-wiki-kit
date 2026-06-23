---
title: Review — Producing Open Source Software Ch.2 (batch 3)
aliases: []
source_tier: 1
topics: [book-review, producing-open-source-software]
date: 2026-06-23
last_updated: 2026-06-23
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software Ch.2 (batch 3)

Scope: batch-3 output for Ch.2 "Getting Started" — §"Starting From What You Have"
(printed pp. 9–18) and §"Choosing a License and Applying It" (printed pp. 19–20),
synthesis strategy *full synthesis*. Pages under review: the two pages created by this
batch. (Ch.2 also carries [[code-review]] from batch 1 and remains `[~]` partial pending
batch 4 / Ch.2b.)

## 1. Aggregate score

**8/8 applicable checks PASS** — 0 WARN, 0 FAIL. Check 9 N/A (book in progress, no ingest
report yet); Check 8 diagnostic = **good**.

## 2. Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density & anchor accuracy | PASS | Every H2/H3 with original claims cited; all 14 distinct anchors verified against the PDF; offset PDF=printed+13 holds on every tail; paths use `../../` (correct topics depth). |
| 2 — Wikilink integrity | PASS | All live links resolve; 4 deliberate dead links (forward-refs); both pages have `## See also` + `**Source entities:**` backlink. |
| 3 — Negative-space discipline | PASS | Both pages carry `## Negative Space`; log entry lists 8 rejections, all with valid CLAUDE.md labels. |
| 4 — Stance preservation | PASS | "tyranny pretending to be a democracy" and status-hype framed as foils, not peer options. |
| 5 — Enrichment-not-replacement | PASS | Both pages newly created — N/A, nothing overwritten. |
| 6 — Frontmatter completeness | PASS | All 11 schema fields present on both; `last_updated` = today; `type: topic`; topics resolve to authority subjects. |
| 7 — Index & log consistency | PASS | Both pages in `index.md`; entity + meta updated; exactly one ch.2 batch-3 log entry. See note. |
| 8 — Extraction quality | good | 3/3 forward spot-checks Match; reverse sweep shows no load-bearing silent omission. |
| 9 — Synthesis-strategy declaration | N/A | No ingest-report yet (book in progress). |
| 10 — Notation hygiene | PASS | Vault opts in; neither page contains notation → all sub-checks N/A. |

## 3. Warns and fails detail

None.

**Check 7 note (not a defect):** Ch.2 is a multi-batch chapter (batches 1, 3, 4). It is
correctly held at `[~]` / `◑ batch 1, 3` rather than marked complete — marking it complete
would be wrong while Ch.2b (batch 4) is pending. All batch-3 pages are indexed and logged.

**Check 2 note:** deliberate dead links `[[bug-tracking]]`, `[[canned-hosting]]`,
`[[project-infrastructure]]`, `[[release-engineering]]` point at concepts scheduled for
later batches (Ch.3/5/6/7). Acceptable per the dead-link rule.

## 4. Extraction quality (Check 8)

**Part A — forward spot-checks (3/3 Match):**

1. **Hacktivation energy** (PDF p.23 / printed p.10). Source: "the amount of energy a
   newcomer must put in before she starts getting something back." Wiki renders the same
   definition verbatim. **Match.**
2. **AGPL** (PDF p.33 / printed p.20). Source: "is just the GPL with one extra clause
   establishing network accessibility as a form of distribution…". Wiki: "Just the GPL
   with one extra clause establishing network accessibility as a form of distribution."
   **Match.**
3. **Image-based evidence** (PDF p.31 / printed p.18). Source: "screenshot or video can be
   more convincing than paragraphs of descriptive text … because it is proof that…". Wiki
   renders the same claim. **Match.**

All three anchors (`#page=23/33/31`) and tails (p.10/20/18) confirmed correct.

**Part B — reverse omission sweep:**

| Source heading / caveat (pp. 9–20) | Disposition | Detail |
|---|---|---|
| Ch.2 intro — scaled presentation; appearances matter | In wiki | [[launching-an-open-source-project]] §Scaled presentation, §Appearances matter |
| What We Mean by Users and Developers | In wiki (compressed) | Relational user/developer distinction referenced in intro + comms-channels item |
| But First, Look Around | In wiki | §But first, look around |
| Starting From What You Have | In wiki | Page intro + §Hacktivation energy |
| Choose a Good Name / Own the Name in Namespaces | In wiki | Checklist item "A good name" |
| Have a Clear Mission Statement | In wiki | Checklist item |
| State That the Project is Free | In wiki | Checklist item + [[open-source-licensing]] |
| Features and Requirements List | In wiki | Checklist item |
| Development Status | In wiki | Checklist item |
| — Development Status Should Always Reflect Reality | In wiki | §Honest status beats hype |
| — Alpha and Beta | Negative-space | `too-granular` (logged) |
| Downloads | In wiki | Checklist item |
| Version Control and Bug Tracker Access | In wiki | Checklist item |
| Communications Channels | In wiki | Checklist item |
| Developer Guidelines | In wiki | Checklist item |
| Documentation | In wiki | Checklist item |
| — Maintaining a FAQ | Negative-space | `too-granular` (logged) |
| — Availability of Documentation | In wiki (compressed) | Subsumed under documentation item (online + in-distribution) |
| Developer Documentation | In wiki + neg-space | Distinction captured inline; `subsumed-by` (logged) |
| Demos, Screenshots, Videos / Keep Videos Brief | In wiki | Checklist item + scaled-presentation example |
| Hosting | In wiki | Checklist item |
| Choosing a License and Applying It (+ synonyms, Do-Anything, GPL, AGPL, How to Apply) | In wiki | [[open-source-licensing]] |

Nothing substantive omitted. Two headings ("What We Mean by Users and Developers",
"Availability of Documentation") are legitimately compressed mechanics/definitional asides
under the principles-and-criteria treatment of the checklist; no framework-altering claim
is lost.

**Part C — overall rating: good.**

## 5. Compression-ratio diagnostic

Omitted — no ingest-report exists yet (book in progress).

## 6. Pages reviewed

- `wiki/topics/launching-an-open-source-project.md` (created)
- `wiki/topics/open-source-licensing.md` (created)
- `wiki/entities/books/producing-open-source-software-book.md`
- `wiki/index.md`, `wiki/log.md`, `raw-input/books/producing-open-source-software/meta.md`
- Source: `raw-input/books/producing-open-source-software/producing-open-source-software.pdf` pp. 22–33
