---
title: Producing Open Source Software — How to Run a Successful Free Software Project
aliases: []
date: 2026-06-23
last_updated: 2026-06-24
type: book
edition: 2nd Edition (v2.3300, 05 Feb 2023)
isbn: null
doi: null
topics: [open-source-governance, project-infrastructure, open-source-participation]
project: null
source_count: 0
status: active
---

# Producing Open Source Software — How to Run a Successful Free Software Project

**Author:** Karl Fogel
**Edition:** 2nd Edition, version 2.3300 (05 Feb 2023)
**License:** Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)
**Source:** [producing-open-source-software.pdf](../../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf) · home site: https://producingoss.com/

> "The fact that a person knows how to write good code, or is even a true virtuoso
> at it, does not mean that he knows how to *run a project*."
> — Karl Fogel

## Why It Matters

Fogel's book is the practitioner reference for the *non-code* half of open-source
work: the technical infrastructure, social conventions, governance models, and
release discipline that decide whether a free-software project thrives or stalls.
Where most craft books are about writing better code, this one is about building the
collaborative machine *around* the code — which makes it the natural spine for this
vault's open-source-collaboration topics.

This book is also the worked **example source** for the kit. It is being ingested in
full across 17 batches (see `ingestion-plan.md`) so the complete book-ingest workflow is
reproduced end to end; permitted because the source is CC BY-SA 4.0. Batches 1–4 (Ch.3
§Version Control + Ch.2 §Code Review; Ch.1 + Ch.4; Ch.2a §Starting From What You Have +
§Choosing a License; Ch.2b §Setting the Tone + §Opening a Formerly Closed Project +
§Announcing) are complete — Chapter 2 is now fully ingested. Batch 5 added the Ch.3
infrastructure remainder (what a project needs, web site, canned hosting, message
forums) as principles + decision criteria; Batch 6 completed Ch.3 (bug tracker, real-time
chat, wikis, translation, social networking). Chapters 1–4 are now fully ingested. Batch 7
opened Ch.5 (the economics of open source, corporate/government involvement, hiring for the
long term, and contracting) as full synthesis; Batch 8 added the non-code half of Ch.5 —
funding non-programming activities (testing, docs, UX, infra, security, events) and marketing
(the vendor-lock-in advantage, "you are being watched," open core / terminology integrity). Batch 9
completed Ch.5 with "Open Source and the Organization" (foster pools of expertise, publicity-vs-schedule,
middle management), innersourcing, hiring open-source developers, evaluating projects, and
crowdfunding/bounties — Chapter 5 is now fully ingested. Batch 10 opens Chapter 6
(Communications) with its first half — written culture (clear writing as the load-bearing
skill, "you are what you write," recognizing rudeness, the online "face"), avoiding common
pitfalls (the Bikeshed Effect, holy wars, the noisy-minority effect), and handling difficult
people (obstructionists who manipulate process rather than merely being rude). Batch 11
completed Chapter 6 with its second half — scaling project communication (the quiet
negative-feedback failure of massively-parallelized support, splitting forums, conspicuous
archives, codifying tradition), choosing the right forum (forum-appropriateness, the
convergent/divergent rule, writer-responsible culture), open-source publicity (announcement
channels and the meant-to-be-quoted portion), and security vulnerability disclosure (the
coordinated openness-vs-secrecy process: private intake, quiet fix, CVE/CVSS, pre-notification,
simultaneous public release). Chapters 1–6 are now fully ingested. Batch 12 opens Chapter 7
(Packaging, Releasing, and Daily Development) with its first half — release numbering
(the twofold purpose, major/minor/micro components, Semantic Versioning, the even/odd
stability convention), release branches (why full-tree snapshots fail, the branch as
release-work isolation, parallel maintenance lines), stabilizing a release (the machine
for saying "no": release-owner dictatorship vs. multi-vote approval, time-based vs.
feature-based cadence, the release manager), and packaging (source as the canonical
distribution form). Chapter 7 continues in batch 13; Chapters 8–9 follow.

## Chapter Index

| Ch. | Title | PDF pp. | Status | Wiki pages |
|---|---|---|---|---|
| 1 | Introduction | 14–21 | ✓ batch 2 | [[free-software-vs-open-source]], [[open-source-culture]] |
| 2 | Getting Started | 22–42 | ✓ batch 1, 3, 4 | [[code-review]], [[launching-an-open-source-project]], [[open-source-licensing]], [[setting-the-tone]], [[developing-in-the-open]] |
| 3 | Technical Infrastructure | 43–71 | ✓ batch 1, 5, 6 | [[version-control]], [[project-infrastructure]], [[project-hosting]], [[message-forums]], [[bug-tracking]], [[real-time-chat]], [[wikis]], [[translation-infrastructure]] |
| 4 | Social and Political Infrastructure | 72–79 | ✓ batch 2 | [[open-source-governance]], [[forkability]] |
| 5 | Organizations and Money | 80–106 | ✓ batch 7 (5a), 8 (5b), 9 (5c) | [[open-source-economics]], [[corporate-open-source-participation]], [[government-and-open-source]], [[open-source-contracting]], [[funding-non-programming-activities]], [[open-source-marketing]], [[innersourcing]], [[hiring-open-source-developers]], [[evaluating-open-source-projects]], [[crowdfunding-and-bounties]] |
| 6 | Communications | 107–131 | ✓ batch 10 (6a), 11 (6b) | [[written-communication]], [[facilitating-online-discussion]], [[difficult-people]], [[scaling-project-communication]], [[choosing-the-right-forum]], [[open-source-publicity]], [[security-vulnerability-disclosure]] |
| 7 | Packaging, Releasing, and Daily Development | 132–148 | ⏳ batch 12 (7a) | [[release-numbering]], [[release-branches]], [[stabilizing-a-release]], [[source-packaging]] |
| 8 | Managing Participants | 149–170 | — | |
| 9 | Legal Matters | 171–190 | — | |

## Negative Space

- **Chapter 7 second half + Chapters 8–9** (`source-underdeveloped`): not yet ingested —
  Ch.7's remainder (testing & releasing, multiple release lines, security releases, daily
  development) is batch 13; Chapters 8–9 are scheduled across Batches 14–17 in
  `ingestion-plan.md`. The chapter index above tracks live progress; the ⏳ on Ch.7 marks
  a chapter partially ingested, and un-ticked chapters are pending, not deliberately excluded.
