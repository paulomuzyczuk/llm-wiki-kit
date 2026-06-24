---
title: Ingest Report — Producing Open Source Software (2nd ed.)
aliases: []
date: 2026-06-24
last_updated: 2026-06-24
type: digest
topics: [software-craft, ingest-report, producing-open-source-software]
source_count: 1
status: active
---

# Ingest Report — *Producing Open Source Software* (Karl Fogel, 2nd ed.)

End-of-book rollup for the full ingest of Karl Fogel's *Producing Open Source Software*
(2nd ed., v2.3300, CC BY-SA 4.0), the kit's worked example source. Aggregated from `meta.md`,
`log.md`, `index.md`, the book entity, and the 18 per-batch review digests — not a fresh
extraction.

## §1 Scope

- **Chapters reviewed-clean: 9 / 9** (all terminal `✓ reviewed-clean`; no `(note only)`, no
  halted `[!]`).
- **Source span:** PDF pp. 14–190 (Ch.1 Introduction through Ch.9 Legal Matters + Appendix A
  Copyright); printed pp. 1–177.
- **Batches & sessions:** 17 batches across two working days (2026-06-23: batches 1–8 + parts
  of Ch.3/5; 2026-06-24: batches 9–17). One human-authorized batch per invocation; one
  `/book-review` per chapter-batch.
- **Synthesis strategies used:**
  - *Focused full synthesis* — batch 1 (Ch.3 §Version Control + Ch.2 §Code Review).
  - *Full synthesis* — Ch.1, Ch.2, Ch.4, Ch.5, Ch.6, Ch.7, Ch.8.
  - *Principles + decision criteria* — Ch.3 infrastructure remainder (batches 5–6) and Ch.9
    Legal Matters (batches 16–17), as reference-catalog chapters.

## §2 Output

### New pages (62)

**Ch.1 Introduction** — [[free-software-vs-open-source]], [[open-source-culture]]
**Ch.2 Getting Started** — [[code-review]], [[launching-an-open-source-project]],
[[open-source-licensing]], [[setting-the-tone]], [[developing-in-the-open]]
**Ch.3 Technical Infrastructure** — [[version-control]], [[project-infrastructure]],
[[project-hosting]], [[message-forums]], [[bug-tracking]], [[real-time-chat]], [[wikis]],
[[translation-infrastructure]]
**Ch.4 Social & Political Infrastructure** — [[open-source-governance]], [[forkability]]
**Ch.5 Organizations and Money** — [[open-source-economics]], [[corporate-open-source-participation]],
[[government-and-open-source]], [[open-source-contracting]], [[funding-non-programming-activities]],
[[open-source-marketing]], [[innersourcing]], [[hiring-open-source-developers]],
[[evaluating-open-source-projects]], [[crowdfunding-and-bounties]]
**Ch.6 Communications** — [[written-communication]], [[facilitating-online-discussion]],
[[difficult-people]], [[scaling-project-communication]], [[choosing-the-right-forum]],
[[open-source-publicity]], [[security-vulnerability-disclosure]]
**Ch.7 Packaging, Releasing & Daily Development** — [[release-numbering]], [[release-branches]],
[[stabilizing-a-release]], [[source-packaging]], [[releasing-and-signing]],
[[maintaining-multiple-release-lines]], [[security-releases]], [[atomic-commits]],
[[release-planning]]
**Ch.8 Managing Participants** — [[contributor-motivation]], [[delegation-in-open-source]],
[[praise-and-criticism]], [[preventing-territoriality]], [[the-automation-ratio]],
[[treating-users-as-participants]], [[sharing-project-management]], [[transitions]],
[[committers]], [[credit-and-attribution]], [[forks]]
**Ch.9 Legal Matters** — [[copyleft]], [[permissive-licensing]], [[license-compatibility]],
[[contributor-agreements]], [[proprietary-relicensing]], [[trademarks-in-open-source]],
[[software-patents]], [[creative-commons-licensing]]

### Enriched pages (cross-chapter convergence within the book)

| Page | Chapter(s) | Substance added |
|---|---|---|
| [[version-control]] | 3 (create), 4, 7 | "version control means you can relax"; release branches; atomic-commits link |
| [[open-source-licensing]] | 2 (create), 9a, 9b | Ch.9 terminology/aspects/choosing; "Beyond the code license" map to the five 9b regimes |
| [[open-source-governance]] | 4 (create), 5, 8 | money-and-influence; "politics is inevitable" (non-forkable resources) |
| [[forkability]] | 4 (create), 8, 9b | attention/credibility/influence not forkable; trademark as non-forkable resource; CA backstop |
| [[copyleft]] | 9a (create), 9b | ShareAlike as content-copyleft; "selling exceptions" works only on copyleft |
| [[code-review]] | 2 (create), 8 | review makes commit access low-stakes (committer selection) |
| [[source-packaging]] | 7a (create), 7b | build/install conventions; binary packages derive from source release |
| [[open-source-participation]] | 8 | the formal committer class; delegation, motivation |
| [[free-software-vs-open-source]] | 1 (create), 9a | copyleft forward-refs resolved |
| [[facilitating-online-discussion]] | 6a (create), 6b | pair-link to forum choice |
| [[praise-and-criticism]] | 8a (create), 8b | transitions pair-link |
| [[security-vulnerability-disclosure]] | 6b (create), 7b | repointed to [[security-releases]] |
| [[corporate-open-source-participation]] | 5a (create), 5c | foster pools of expertise; middle management |
| [[open-source-contracting]] | 5a (create), 5b | the New Developer Test |
| [[continuous-integration]] | 7, 8 (cross-source) | Fogel's automated-testing-on-commit; "don't break the build" |

## §3 Cross-book convergence

The primary payoff: three pages fuse Fogel's practitioner account with the vault's two
empirical papers, each reaching `source_count: 2`.

| Concept | Prior source(s) | This book's contribution |
|---|---|---|
| [[continuous-integration]] | Guo & Leitner 2019 (*CI PR delivery-time* paper) — empirical CI effect on PR latency | Fogel's **automation ratio** and automated-testing-on-commit as a craft norm ("don't break the build"); the *why* behind investing in CI |
| [[code-review]] | Guo & Leitner 2019 — review as a measured factor in delivery time | Fogel's **conspicuous code review** as a cultural practice that also makes commit access low-stakes |
| [[open-source-participation]] | Mehler et al. 2024 (*who makes open source code*) — the empirical GitHub contributor elite | Fogel's **formal committer class**, delegation, and motivation — the institutional counterpart to the measured elite |

### Convergence-misses (expected by the plan, did not materialise)

- **[[continuous-integration]] ← Ch.7b (testing & releasing).** The plan's convergence-watch
  expected Ch.7b to enrich CI. It did not: Fogel's "Testing and Releasing" is *manual* developer
  approval plus OpenPGP signing, distinct from automated CI/build (only a passing reference to the
  regression suite). Recorded in the batch-13 review rather than forced. CI was instead enriched
  from Ch.7/Ch.8's automation-ratio material.
- **[[code-review]] ← Ch.2b (setting the tone).** The §Practice Conspicuous Code Review material
  was fully ingested in batch 1, so batch-4's Ch.2b pass found nothing left to add (recorded as a
  batch-4 convergence-miss, not a gap).

## §4 Negative-space summary

Across 17 batches the recurring rejection categories (CLAUDE.md vocabulary) were:

- **`illustrative-scaffolding`** (most frequent) — Fogel's running examples (Scanley, Subversion,
  Hadoop), verbatim email threads, and case anecdotes (Iceweasel saga, fish-pedicure shop,
  video-card secrecy). Captured as principle, not narrative.
- **`tool-specific/perishable`** — named software, version-specific workflows, vendor lists
  (hosting providers, patch-queue tools, GnuPG mechanics, RedHat/OIN program terms).
- **`too-granular`** — sub-mechanics folded into parent pages (full license clause text, header
  munging, CLA/DCO form wording, CC deed defined-terms).
- **`foreshadowing`** — concepts named early, deliberately deferred to the chapter that develops
  them (resolved as dead wikilinks went live across batches).
- **`book-metadata`** — prefaces, the §Further Resources reading list, and the full CC BY-SA 4.0
  legal deed (Appendix A).
- Lower-frequency: `subsumed-by`, `supporting-argument`, `conceptual-tool-not-concept`,
  `case-study-specifics`, `out-of-scope`, `source-underdeveloped`, `foil`.

## §5 Review rollup

One row per review unit (chapter-batch). All units PASS; every WARN was fixed during or
immediately after its review. **Total unresolved across the book: 0.**

| Unit | Verdict | Issues found | Resolution | Digest |
|---|---|---|---|---|
| Ch.3+2 (batch 1) | PASS | none (8/8) | — | review-…-ch3-2026-06-23.md |
| Ch.1 (batch 2) | PASS | none (8/8) | — | review-…-ch1-2026-06-23.md |
| Ch.4 (batch 2) | PASS | 1 WARN (polls-vs-votes capture) | fixed in-review | review-…-ch4-2026-06-23.md |
| Ch.2 (batch 3) | PASS | none (8/8) | — | review-…-ch2-2026-06-23.md |
| Ch.2 (batch 4) | PASS | none (8/8); code-review convergence-miss | recorded | review-…-ch2-2026-06-23-batch4.md |
| Ch.3 (batch 5) | PASS | none (8/8) | — | review-…-ch3-2026-06-23-batch5.md |
| Ch.3 (batch 6) | PASS | none (8/8) | — | review-…-ch3-2026-06-23-batch6.md |
| Ch.5 (batch 7) | PASS | none | — | review-…-ch5-2026-06-23-batch7.md |
| Ch.5 (batch 8) | PASS | none | — | review-…-ch5-2026-06-23-batch8.md |
| Ch.5 (batch 9) | PASS | none | — | review-…-ch5-2026-06-24-batch9.md |
| Ch.6 (batch 10) | PASS | none | — | review-…-ch6-2026-06-24-batch10.md |
| Ch.6 (batch 11) | PASS | none | — | review-…-ch6-2026-06-24-batch11.md |
| Ch.7 (batch 12) | PASS | 1 spurious anchor (#page=133) | fixed, clean re-run | review-…-ch7-2026-06-24-batch12.md |
| Ch.7 (batch 13) | PASS | 3 release-planning anchors | fixed pre-commit | review-…-ch7-2026-06-24.md |
| Ch.8 (batch 14) | PASS | 1 anchor split (territoriality) | fixed pre-commit | review-…-ch8-2026-06-24-batch14.md |
| Ch.8 (batch 15) | PASS | 2 Check-1 anchor FAILs | fixed, clean re-run | review-…-ch8-2026-06-24-batch15.md |
| Ch.9 (batch 16) | PASS | 1 WARN (lawyer-caveat omission) | fixed in-review | review-…-ch9-2026-06-24-batch16.md |
| Ch.9 (batch 17) | PASS | 1 Check-8 WARN (Further Resources omission) | logged post-review as book-metadata | review-…-ch9-2026-06-24-batch17.md |

## §6 Gaps surfaced

No new field-level knowledge gaps were surfaced by batch 17 — Ch.9b is reference-catalog legal
material fully dispositioned into pages or negative space. The book did surface two standing
cross-source observations already captured as convergence pages (not gaps): the manual-vs-automated
testing distinction ([[continuous-integration]]) and the formal-vs-empirical contributor framing
([[open-source-participation]]). A book-level note is filed to `gaps.md` §1 recording that Fogel's
legal chapter is an explicit *introduction* (the author defers deep licensing/patent/trademark law
to specialist resources), so the vault's legal coverage is principle-level by design.

## §7 Final state — self-audit

| Write | Landed |
|---|---|
| `meta.md` ticks | ✓ all 9 chapters `[x] … ✓ reviewed-clean`; no bare `[x]`, no `[!]` |
| Book entity | ✓ chapter index all `✓`; `ingest_status: complete (2026-06-24)`; report linked under index |
| `index.md` | ✓ 62 page entries across the book's subject sections; entity entry marked full-book complete |
| `log.md` | ✓ per-chapter `book-ingest` + `digest` lines for all 17 batches; this completion line appended |
| Review digests | ✓ 18 digests present, all PASS, 0 unresolved |
| `topics-authority.md` | ✓ all 62 concepts + subjects registered; batch-17 concepts seeded |
| `gaps.md` | ✓ book-level legal-coverage note filed to §1 |
