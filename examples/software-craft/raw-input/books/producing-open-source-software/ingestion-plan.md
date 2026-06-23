---
title: Ingestion Plan — Producing Open Source Software (2nd ed.)
book: producing-open-source-software
date: 2026-06-23
status: approved
---

# Ingestion Plan — Producing Open Source Software (2nd ed.)

> **Full-book ingestion (revised 2026-06-23).** This plan supersedes the original
> "Batch 1 only" example scope. The whole book is now scheduled across 17 batches so the
> complete book-ingest workflow is reproduced end to end. Batch 1 (Version Control + Code
> Review) is already ingested and reviewed clean; Batches 2–17 cover the remainder.
>
> The source is **CC BY-SA 4.0** (Karl Fogel's canonical free edition,
> https://producingoss.com/, v2.3300), so full synthesis with attribution is permitted —
> the original "don't reproduce the book" caveat is lifted. As chapters complete, the
> "example stops after Batch 1" framing notes in `meta.md` and the book entity page are
> updated to reflect full coverage.

## Sizing basis

- Measured density: **~1,200 raw tokens/PDF page** (913,784 chars / 4 over 190 pp),
  ≈ 2.3× the planner's 525/page default → **~2,400 effective tokens/page** after the 2×
  ingestion-consumption doubling.
- At that density the "≤30 pages/batch" default ceiling becomes **~12–15 pages/batch**.
  Every chapter ≥ ~15 pp is split on a section boundary; no batch carries a
  compaction-risk flag.
- Printed page = PDF page − 13 (front matter occupies PDF pp. 1–13).

## Chapter assessment

| Ch. | Title | PDF pp (count) | Type | Density read |
|---|---|---|---|---|
| 1 | Introduction | 14–21 (8) | foundational | Free-software history + framing; light synthesis weight |
| 2 | Getting Started | 22–42 (21) | methodology | Project setup, licensing, setting the tone (Code Review done in Batch 1) |
| 3 | Technical Infrastructure | 43–71 (29) | reference-catalog | Tooling spine (Version Control done in Batch 1) |
| 4 | Social and Political Infrastructure | 72–79 (8) | foundational | Governance models, forkability as the check on power |
| 5 | Organizations and Money | 80–106 (27) | applied-domain | Funding, corporate/government participation, conflicts of interest |
| 6 | Communications | 107–131 (25) | methodology | Written-culture norms, conflict handling, scaling discussion |
| 7 | Packaging, Releasing, Daily Development | 132–148 (17) | methodology | Release mechanics, versioning, daily development flow |
| 8 | Managing Participants | 149–170 (22) | methodology | Delegation, committers, transitions, forking |
| 9 | Legal Matters | 171–190 (20) | reference-catalog | Licenses, copyright, trademarks, patents |

## Scope decisions

- **Full-book synthesis.** All chapters are scheduled; the example is no longer capped at
  a Chapter 3 slice. Permitted because the source is CC BY-SA 4.0 (attribution already on
  the book entity and README).
- **Reference-catalog chapters get principles + decision criteria, not mechanics.** The
  Ch.3 remainder (forums, bug tracker, chat, wikis) and Ch.9 (licenses) capture governing
  principles and when-to-use logic, not per-tool or per-license mechanics.
- **All ≥~15pp chapters split on section boundaries** (Ch.5, 6, 7, 8, 9), so no batch runs
  hot on this dense prose. Splits land on real section headers (see Batches below).

## Batches

Strategy only — chapter completion is tracked in `meta.md`, not here.

| Batch | Content | PDF pp | ~pp | Synthesis strategy |
|---|---|---|---|---|
| 1 ✅ | Ch.3 §Version Control + Ch.2 §Practice Conspicuous Code Review | 55–62 + 37 | done | Focused full synthesis → [[version-control]], [[code-review]] *(ingested + reviewed clean 8/8)* |
| 2 | Ch.1 Introduction **+** Ch.4 Social & Political Infrastructure | 14–21 + 72–79 | 16 | Full synthesis (foundational pair: free-software history + governance/forkability) |
| 3 | Ch.2a — Starting From What You Have + Choosing & Applying a License | 22–33 | 12 | Full synthesis |
| 4 | Ch.2b — Setting the Tone (excl. Code Review, done) + Opening a Formerly Closed Project + Announcing | 34–42 | 9 | Full synthesis |
| 5 | Ch.3a rem. — What a Project Needs, Web Site, Canned Hosting, Message Forums / Mailing Lists | 43–54 | 12 | Principles + decision criteria |
| 6 | Ch.3b rem. — Bug Tracker, Real-Time Chat, Wikis, Translation, Social Networking | 63–71 | 9 | Principles + decision criteria |
| 7 | Ch.5a — Economics of OSS, Corporate/Government involvement, Hire for Long Term, Contracting | 80–91 | 12 | Full synthesis |
| 8 | Ch.5b — Funding Non-Programming Activities, Marketing | 92–99 | 8 | Full synthesis |
| 9 | Ch.5c — Open Source & the Organization, Hiring OSS Developers, Evaluating Projects, Crowdfunding & Bounties | 100–106 | 7 | Full synthesis |
| 10 | Ch.6a — Written Culture, Avoiding Common Pitfalls, Difficult People | 107–118 | 12 | Full synthesis |
| 11 | Ch.6b — Handling Growth, Choose the Right Forum, Publicity | 119–131 | 13 | Full synthesis |
| 12 | Ch.7a — Release Numbering, Release Branches, Stabilizing a Release, Packaging | 132–140 | 9 | Full synthesis |
| 13 | Ch.7b — Testing & Releasing, Maintaining Multiple Release Lines, Security Releases, Daily Development, Planning Releases | 141–148 | 8 | Full synthesis |
| 14 | Ch.8a — Delegation, The Automation Ratio, Sharing Management Tasks | 149–159 | 11 | Full synthesis |
| 15 | Ch.8b — Transitions, Committers, Forking | 160–170 | 11 | Full synthesis |
| 16 | Ch.9a — Terminology, Aspects of Licenses, The GPL & License Compatibility, Choosing a License, The GNU GPL | 171–180 | 10 | Principles + decision criteria |
| 17 | Ch.9b — Contributor Agreements, Proprietary Relicensing, Trademarks, Patents, Creative Commons Public Licenses | 181–190 | 10 | Principles + decision criteria |

## Convergence watch (for the reviewer)

Existing pages expected to be **enriched** (not replaced) as later batches land:

- [[code-review]] — Ch.2b (setting the tone), Ch.8b (committers / reviewing contributions).
- [[version-control]] — Ch.4 ("Version Control Means You Can Relax"), Ch.7a (release branches).
- [[open-source-participation]] — Ch.8a/8b (delegation, committership, motivation).
- [[continuous-integration]] — Ch.7b (testing & releasing, daily development).

Likely **new** anchor pages (graining decided at ingest): open-source governance &
forkability (Ch.4), open-source licensing (Ch.2/Ch.9), project communication norms &
conflict handling (Ch.6), release management & versioning (Ch.7), committership &
delegation (Ch.8), open-source economics & funding (Ch.5).
