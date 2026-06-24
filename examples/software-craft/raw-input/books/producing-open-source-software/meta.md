---
title: Producing Open Source Software — How to Run a Successful Free Software Project
author: Karl Fogel
edition: 2nd Edition
version: 2.3300 (05 Feb 2023)
isbn: null
doi: null
source_url: https://producingoss.com/
license: CC BY-SA 4.0
slug: producing-open-source-software
---

# Producing Open Source Software (2nd ed.) — ingest meta

Karl Fogel's practitioner guide to running free/open-source software projects.
Source is the canonical free edition (CC BY-SA 4.0) from https://producingoss.com/,
version 2.3300 (05 Feb 2023). Printed page numbers are present in the PDF; the
**PDF-page = printed-page + 13** offset holds throughout (front matter occupies
PDF pp. 1–13).

## Chapter → PDF-page map

PDF page indices (not printed). Printed page = PDF page − 13.

| Chapter | Title | PDF pp. | Printed pp. |
|---|---|---|---|
| Front matter | Title, copyright, dedication, preface, TOC | 1–13 | i–vi |
| 1 | Introduction | 14–21 | 1–8 |
| 2 | Getting Started | 22–42 | 9–29 |
| 3 | Technical Infrastructure | 43–71 | 30–58 |
| 4 | Social and Political Infrastructure | 72–79 | 59–66 |
| 5 | Organizations and Money: Businesses, Non-Profits, and Governments | 80–106 | 67–93 |
| 6 | Communications | 107–131 | 94–118 |
| 7 | Packaging, Releasing, and Daily Development | 132–148 | 119–135 |
| 8 | Managing Participants | 149–170 | 136–157 |
| 9 | Legal Matters: Licenses, Copyrights, Trademarks and Patents | 171–190 | 158–177 |

## Ingest status

- [x] Ch.1 — Introduction  (batch 2: full synthesis → [[free-software-vs-open-source]], [[open-source-culture]]) ✓ reviewed-clean
- [x] Ch.2 — Getting Started  (batch 1: §Practice Conspicuous Code Review → [[code-review]]; batch 3: §Starting From What You Have + §Choosing a License → [[launching-an-open-source-project]], [[open-source-licensing]]; batch 4: §Setting the Tone + §Opening a Formerly Closed Project + §Announcing → [[setting-the-tone]], [[developing-in-the-open]], enriched [[launching-an-open-source-project]]) ✓ reviewed-clean
- [x] Ch.3 — Technical Infrastructure  (batch 1: §Version Control → [[version-control]]; batch 5: §What a Project Needs + §Web Site + §Canned Hosting + §Message Forums/Mailing Lists [principles + decision criteria] → [[project-infrastructure]], [[project-hosting]], [[message-forums]]; batch 6: §Bug Tracker + §Real-Time Chat + §Wikis + §Translation + §Social Networking [principles + decision criteria] → [[bug-tracking]], [[real-time-chat]], [[wikis]], [[translation-infrastructure]], enriched [[project-infrastructure]]) ✓ reviewed-clean
- [x] Ch.4 — Social and Political Infrastructure  (batch 2: full synthesis → [[open-source-governance]], [[forkability]]; enriched [[version-control]]) ✓ reviewed-clean
- [x] Ch.5 — Organizations and Money  (batch 7 [5a]: full synthesis → [[open-source-economics]], [[corporate-open-source-participation]], [[government-and-open-source]], [[open-source-contracting]]; enriched [[open-source-governance]]. batch 8 [5b]: full synthesis → [[funding-non-programming-activities]], [[open-source-marketing]]; enriched [[open-source-contracting]] (New Developer Test). batch 9 [5c]: full synthesis → [[innersourcing]], [[hiring-open-source-developers]], [[evaluating-open-source-projects]], [[crowdfunding-and-bounties]]; enriched [[corporate-open-source-participation]] (Open Source and the Organization — foster pools of expertise, publicity-vs-schedule, middle management) — completes Ch.5) ✓ reviewed-clean
- [x] Ch.6 — Communications  (batch 10 [6a]: full synthesis → [[written-communication]], [[facilitating-online-discussion]], [[difficult-people]]; batch 11 [6b]: full synthesis → [[scaling-project-communication]], [[choosing-the-right-forum]], [[open-source-publicity]], [[security-vulnerability-disclosure]]; enriched [[facilitating-online-discussion]] (pair-link to forum choice) — completes Ch.6) ✓ reviewed-clean
- [x] Ch.7 — Packaging, Releasing, and Daily Development  (batch 12 [7a]: §Release Numbering + §Release Branches + §Stabilizing a Release + §Packaging [principle] → [[release-numbering]], [[release-branches]], [[stabilizing-a-release]], [[source-packaging]]; enriched [[version-control]] (release branches). batch 13 [7b]: §Testing and Releasing + §Maintaining Multiple Release Lines + §Security Releases + §Releases and Daily Development + §Planning Releases → [[releasing-and-signing]], [[maintaining-multiple-release-lines]], [[security-releases]], [[atomic-commits]], [[release-planning]]; enriched [[source-packaging]] (build conventions + binary packages), [[version-control]] (atomic-commits link), [[security-vulnerability-disclosure]] (repointed → [[security-releases]]) — completes Ch.7) ✓ reviewed-clean
- [x] Ch.8 — Managing Participants  (batch 14 [8a]: §Community and Motivation + §Delegation (+ inquiry-vs-assignment, follow-up, notice-interests) + §Praise and Criticism + §Prevent Territoriality + §The Automation Ratio + §Treat Every User as a Potential Participant + §Share Management Tasks, full synthesis → [[contributor-motivation]], [[delegation-in-open-source]], [[praise-and-criticism]], [[preventing-territoriality]], [[the-automation-ratio]], [[treating-users-as-participants]], [[sharing-project-management]]; enriched [[open-source-governance]] (politics is inevitable), [[forkability]] (attention/credibility/influence not forkable), [[continuous-integration]] (automated testing — Fogel), [[open-source-participation]] (cross-refs). batch 15 [8b]: §Transitions + §Committers (+ Credit) + §Forks, full synthesis → [[transitions]], [[committers]], [[forks]], [[credit-and-attribution]]; enriched [[forkability]] (pair-link to [[forks]]), [[praise-and-criticism]] (transitions pair-link), [[open-source-participation]] (the formal committer class), [[code-review]] (review makes commit access low-stakes) — completes Ch.8) ✓ reviewed-clean
- [ ] Ch.9 — Legal Matters  (batch 16 [9a]: §Terminology + §Aspects of Licenses + §The GPL and License Compatibility + §Choosing a License + §The GNU GPL (incl. AGPL, "or any later version", §Copyright Holder Is Special, §Is the GPL Free or Not Free?), principles + decision criteria → [[copyleft]], [[permissive-licensing]], [[license-compatibility]]; enriched [[open-source-licensing]] (terminology, aspects, choosing a license), [[free-software-vs-open-source]] (copyleft links resolved). ⏳ partial — completes batch 17 [9b]: Contributor Agreements, Proprietary Relicensing, Trademarks, Patents, Creative Commons)

> This is a public **example** vault. As of 2026-06-23 it is being ingested in full
> across 17 batches (see `ingestion-plan.md`) so the complete book-ingest workflow is
> reproduced end to end. Batches 1–4 are done — Batch 1 (Ch.3 §Version Control + Ch.2
> §Code Review), Batch 2 (Ch.1 + Ch.4), Batch 3 (Ch.2a launch + licensing), Batch 4 (Ch.2b
> setting the tone + opening a closed project + announcing, completing Chapter 2), Batch 5
> (Ch.3a remainder — what a project needs, web site, canned hosting, message forums, as
> principles + decision criteria), Batch 6 (Ch.3b remainder — bug tracker, real-time chat,
> wikis, translation, social networking, completing Chapter 3); Chapter 5 (Organizations and
> Money) is fully ingested across Batches 7–9. Chapter 6 (Communications) is fully ingested
> across Batches 10–11 — 6a (written culture, avoiding common pitfalls, difficult people) and
> 6b (scaling project communication, choosing the right forum, publicity, security vulnerability
> disclosure). Batch 12 opens Chapter 7 (Packaging, Releasing, and Daily Development) with its
> first half — release numbering, release branches, stabilizing a release, and the packaging
> principle. Batch 13 completes Chapter 7 with its second half — releasing and signing,
> maintaining multiple release lines, security releases, atomic commits, and release planning.
> Chapters 1–7 are now fully ingested. Batch 14 opened Chapter 8 (Managing Participants) with
> its first half — contributor motivation, delegation, praise and criticism, preventing
> territoriality, the automation ratio, treating users as participants, and sharing project
> management. Batch 15 completes Chapter 8 with its second half — transitions (the role-handoff
> craft), committers (commit access: choosing, revoking, partial/dormant access, avoid-mystery),
> credit and attribution (credit as the recorded currency), and forks (development vs. hard
> forks, handling and initiating one). Chapters 1–8 are now fully ingested; the remaining
> chapter (9, Legal Matters) follows across Batches 16–17 under the plan.
