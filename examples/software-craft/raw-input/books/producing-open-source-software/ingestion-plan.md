---
title: Ingestion Plan — Producing Open Source Software (2nd ed.)
book: producing-open-source-software
date: 2026-06-23
status: approved
---

# Ingestion Plan — Producing Open Source Software (2nd ed.)

> **Example-vault scope.** This is a public *example* vault for the kit. The plan
> covers the whole book for realism, but only **Batch 1** is intended to run — a
> focused slice of Chapter 3 — enough to demonstrate the pipeline's real output
> (synthesized pages, two-part citations, negative space, cross-source enrichment)
> without reproducing the book.

## Chapter assessment

| Ch. | Title | PDF pp | Type | Density read |
|---|---|---|---|---|
| 1 | Introduction | 14–21 (8) | foundational | Framing; mostly orientation, light synthesis weight |
| 2 | Getting Started | 22–42 (21) | methodology | Project setup + first-impressions practices (incl. conspicuous code review) |
| 3 | Technical Infrastructure | 43–71 (29) | reference-catalog | Tooling spine: version control, code review, bug tracker, forums, chat, wikis |
| 4 | Social and Political Infrastructure | 72–79 (8) | foundational | Governance models, forkability as the check on power |
| 5 | Organizations and Money | 80–106 (27) | applied-domain | Funding, corporate participation, conflicts of interest |
| 6 | Communications | 107–131 (25) | methodology | Written-culture norms, conflict handling, scaling discussion |
| 7 | Packaging, Releasing, Daily Development | 132–148 (17) | methodology | Release mechanics, committing, daily development flow |
| 8 | Managing Participants | 149–170 (22) | methodology | Delegation, committers, transitions, difficult people |
| 9 | Legal Matters | 171–190 (20) | reference-catalog | Licenses, copyright, trademarks, patents |

## Scope decisions

- **Batch 1 is a focused synthesis of Chapter 3**, restricted to the **Version
  Control** and **Code Review** sections (Ch.3's software-craft core, and the
  strongest intersection with the two queued CI/contribution papers). Output: two
  topic pages — [[version-control]], [[code-review]].
- The remaining Ch.3 tooling sections (Bug Tracker, Mailing Lists, real-time chat,
  Wikis) and Chapters 1–2, 4–9 are **out of scope for this example** and recorded as
  `source-underdeveloped` negative space on the book entity. A real vault would
  schedule them as Batches 2–N below.

## Batches

| Batch | Chapters | PDF pp | Synthesis strategy |
|---|---|---|---|
| 1 | Ch.3 — Version Control + Code Review (focused) | 43–71 (focus ≈ 53–66) | Focused full synthesis of two sections → [[version-control]], [[code-review]] |
| 2–9 | Ch.1, 2, 4, 5, 6, 7, 8, 9 | — | **Not scheduled** — example stops after Batch 1 |

## Convergence watch (for the reviewer)

- [[version-control]] and [[code-review]] are expected to be **enriched by two
  open-access papers** ingested after this batch:
  - *Studying the impact of CI on PR delivery time* (Guo & Leitner 2019, PeerJ CS) —
    enriches both pages with empirical findings, and anchors a new [[continuous-integration]] page.
  - *Who makes open source code?* (Mehler et al. 2024, EPJ Data Science) — anchors a
    new [[open-source-participation]] page; light cross-links only.
- These cross-source enrichments are the example's demonstration of
  **enrichment-not-replacement** across a book and a peer-reviewed paper on one page.
