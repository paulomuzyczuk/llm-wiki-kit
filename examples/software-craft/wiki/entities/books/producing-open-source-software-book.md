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
ingest_status: complete (2026-06-24)
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
distribution form). Batch 13 completed Chapter 7 with its second half — releasing and
signing (approval-by-testing, personal-key OpenPGP signing, the web of trust, candidate
releases), maintaining multiple release lines (parallel maintenance, announced
end-of-life, support windows), security releases (the untestable release: existing
release plus the fix only, the "minor deception" of an in-flight release), atomic commits
(one logical change per commit, made near-mandatory by parallel maintenance), and release
planning (decoupling contents from dates, the corporate-vs-community deadline tension).
Chapters 1–7 are now fully ingested. Batch 14 opens Chapter 8 (Managing Participants) with its
first half — contributor motivation (intrinsic motivation beyond the paycheck, status norms that
must reward constructive action, "attention is the true currency"), delegation (as a political/
social tool: inquiry vs. assignment, follow-up, noticing interests), praise and criticism (both
forms of attention, specific and sparing), preventing territoriality (cookie licking, banning
source-file author tags, the core-to-periphery continuum), the automation ratio (automate what
machines can do — 10×+ payoff; automated testing as the highest-value case), treating every user
as a potential participant (the recruitment funnel; educate bad bug reports), and sharing
project management ("manager does not mean owner": responsibility without monopoly; the patch and
translation managers). Batch 15 completes Chapter 8 with its second half — transitions (noticing
the slow fade, the multistep ask-to-step-aside, privacy as the overriding factor), committers
(commit access as social authority over the authoritative copy: the Hippocratic "do no harm"
selection criterion, revoking access privately, partial/dormant access, and "avoid mystery" by
publishing the rules and roster), credit and attribution (credit as "the primary currency of the
free software world," distributed accurately through the records the VCS already keeps), and forks
(development vs. hard forks, why perception decides which side is "the fork," handling a fork
non-vindictively, and initiating one only as a last resort). Chapters 1–8 are now fully ingested.
Batch 16 opens Chapter 9 (Legal Matters) with its first half — the licensing terminology that
affects decisions (commercial≠proprietary, public domain vs. a license, FOSS/FLOSS), the *aspects*
on which licenses differ (proprietary-compatibility, free-license-compatibility, attribution,
trademark protection, patent snapback), copyleft (the GPL's two requirements that make "freedom
contagious," LGPL/AGPL reciprocity strength, the sole-copyright-holder exemption), permissive
licensing (MIT/BSD/Apache, MIT as default), license compatibility (GPL-compatibility as the
dominant axis; the DFSG/OSI/FSF certification tests), and choosing a well-recognized existing
license. Captured as principles + decision criteria (no per-license mechanics pages). Batch 17
completes Chapter 9 — and the book — with the legal matters *beyond* the code license:
contributor agreements (the do-nothing / CLA / copyright-assignment choice, and the DCO as the
minimal inbound=outbound CLA), proprietary relicensing (selling exceptions to copyleft vs. open
core, the "can't sue yourself" mechanic, and why it corrodes community), trademarks (a
name/logo regime separate from copyright — "what you may call things, not what you may do with
them" — and a centrally-controlled non-forkable resource), software patents ("the only real
threat" a project cannot route around; license patent-snapback clauses, non-enforcement pledges,
and the Open Invention Network as partial defenses), and Creative Commons licensing (the
instrument for a project's non-code assets, with ShareAlike as copyleft-for-content). All nine
chapters are now fully ingested; the book is complete.

## Chapter Index

| Ch. | Title | PDF pp. | Status | Wiki pages |
|---|---|---|---|---|
| 1 | Introduction | 14–21 | ✓ batch 2 | [[free-software-vs-open-source]], [[open-source-culture]] |
| 2 | Getting Started | 22–42 | ✓ batch 1, 3, 4 | [[code-review]], [[launching-an-open-source-project]], [[open-source-licensing]], [[setting-the-tone]], [[developing-in-the-open]] |
| 3 | Technical Infrastructure | 43–71 | ✓ batch 1, 5, 6 | [[version-control]], [[project-infrastructure]], [[project-hosting]], [[message-forums]], [[bug-tracking]], [[real-time-chat]], [[wikis]], [[translation-infrastructure]] |
| 4 | Social and Political Infrastructure | 72–79 | ✓ batch 2 | [[open-source-governance]], [[forkability]] |
| 5 | Organizations and Money | 80–106 | ✓ batch 7 (5a), 8 (5b), 9 (5c) | [[open-source-economics]], [[corporate-open-source-participation]], [[government-and-open-source]], [[open-source-contracting]], [[funding-non-programming-activities]], [[open-source-marketing]], [[innersourcing]], [[hiring-open-source-developers]], [[evaluating-open-source-projects]], [[crowdfunding-and-bounties]] |
| 6 | Communications | 107–131 | ✓ batch 10 (6a), 11 (6b) | [[written-communication]], [[facilitating-online-discussion]], [[difficult-people]], [[scaling-project-communication]], [[choosing-the-right-forum]], [[open-source-publicity]], [[security-vulnerability-disclosure]] |
| 7 | Packaging, Releasing, and Daily Development | 132–148 | ✓ batch 12 (7a), 13 (7b) | [[release-numbering]], [[release-branches]], [[stabilizing-a-release]], [[source-packaging]], [[releasing-and-signing]], [[maintaining-multiple-release-lines]], [[security-releases]], [[atomic-commits]], [[release-planning]] |
| 8 | Managing Participants | 149–170 | ✓ batch 14 (8a), 15 (8b) | [[contributor-motivation]], [[delegation-in-open-source]], [[praise-and-criticism]], [[preventing-territoriality]], [[the-automation-ratio]], [[treating-users-as-participants]], [[sharing-project-management]], [[transitions]], [[committers]], [[credit-and-attribution]], [[forks]] |
| 9 | Legal Matters | 171–190 | ✓ batch 16 (9a), 17 (9b) | [[copyleft]], [[permissive-licensing]], [[license-compatibility]], [[contributor-agreements]], [[proprietary-relicensing]], [[trademarks-in-open-source]], [[software-patents]], [[creative-commons-licensing]] (+ enriched [[open-source-licensing]], [[forkability]]) |

**Ingest complete (2026-06-24)** — all 9 chapters `✓ reviewed-clean`. End-of-book rollup:
[ingest-report-producing-open-source-software-2026-06-24](../../digests/ingest-report-producing-open-source-software-2026-06-24.md).

## Negative Space

- **Full CC BY-SA 4.0 legal deed (Appendix A)** (`book-metadata`): the appendix reproduces the
  complete public-license text; Batch 17 captured the load-bearing concepts (license elements,
  ShareAlike-as-content-copyleft, the patent/trademark carve-out) on [[creative-commons-licensing]]
  rather than transcribing the section-by-section legalese.
- **Per-item legal mechanics across Ch.9** (`too-granular`): consistent with the chapter's
  principles + decision criteria strategy, CLA/DCO form wording, trademark registration
  procedure, and general patent-law doctrine were rejected in favour of the governing principle
  and decision criteria on each page.
- **All nine chapters are now ingested.** Chapter 9 is the final chapter; once its `/book-review`
  is clean, the book reaches completion and the end-of-book ingest report is generated and linked
  under the chapter index.
