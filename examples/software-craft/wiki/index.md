# Software Craft Wiki — Index

The retrieval surface for this vault. Pages are grouped by **subject** (what they are
about), not by the source or batch they arrived in — collocation is the point of an
index. Curated role maps-of-content live under **Navigation** as a browse layer above
this flat list.

## Navigation

- [[role-code-craftsperson]] — the pages most worth reading for someone writing,
  reviewing, or improving code day to day.

## Topics by subject

### Version control & collaboration

- [[version-control]] — change management as a project's communications backbone;
  centralized vs. decentralized, Git/GitHub as default, version-everything, branches,
  singularity of information. Also its governance effect: reversibility ("you can relax")
  keeps consensus informal.
- [[code-review]] — conspicuous commit review as standing peer-review practice: review
  changes as they arrive, keep it public, more eyes → fewer bugs. Enriched with empirical
  CI/PR-pipeline findings.

### Continuous integration & delivery

- [[continuous-integration]] — automated build-on-integration; the empirical reality
  (CI raises PR *throughput* more than it cuts per-PR latency), and how CI relates to
  version control and review.

### Project infrastructure & tooling

- [[project-infrastructure]] — the collaboration-tool spine of a project: information
  management as the antidote to Brooks' Law, the minimum standard toolset (web site,
  forums, version control, bug tracking, chat), "beware over-automation," and social
  networking as return-on-attention (microblogs yes, mainstream platforms rarely).
- [[project-hosting]] — the build-vs-buy decision for project infrastructure: canned
  hosting's convenience-vs-control trade-off, "if unsure, use canned hosting," GitHub as
  default, and the durable no-lock-in criterion (data export + programmatic access).
- [[message-forums]] — when a project needs dedicated forums vs. the bug tracker, forum
  software/archiving selection criteria, mandatory layered spam prevention, and the
  "settle tooling debates early" governance lesson (the Reply-to debate).
- [[bug-tracking]] — the tracker as a project's public face: it holds "tickets" (bugs,
  features, tasks), reproduction as the pivotal life-cycle moment, acknowledge-every-ticket,
  feature criteria (email, optional identity, APIs/no-lock-in), and pre-filtering via the
  buddy system + knowledgeable watchers.
- [[real-time-chat]] — choosing chat (imitate neighbors, prefer Matrix/IRC bridging, avoid
  Slack), nick-flagging as the convention that makes busy rooms usable, start-with-one-room
  growth, pastes out of band, and bots/commit-notifications as social utility.
- [[wikis]] — collaborative editing doesn't auto-aggregate to quality (organize early,
  prime with content), never allow anonymous editing (spam), and default to the hosting
  site's built-in wiki / prefer Markdown over wiki syntax.
- [[translation-infrastructure]] — when to adopt a translation platform (recruit
  non-developer linguists), open-vs-proprietary platform choice, and the i18n
  (code-prepared-for-translation) vs. l10n (the actual locale translation) distinction.

### Open-source governance & culture

- [[free-software-vs-open-source]] — same software, two motives: the FSF's moral "free as
  in freedom" framing vs. the OSI's pragmatic marketing one, the history that produced
  them, and the "contribution trumps the contributor" truce that lets both coexist.
- [[open-source-culture]] — open source as a culture by choice: the cohesion principle
  (influence ∝ contribution), subtle-but-real management, "not a panacea," and failures of
  cultural navigation.
- [[open-source-governance]] — how projects actually decide: benevolent-dictator vs.
  consensus-democracy, consensus-by-default, voting/vetoes as last resort, maintainers
  beyond coders, and writing it down.
- [[forkability]] — the right to fork as the ceiling on all project power; why the
  *possibility* matters more than the rare act, and why there are no true dictators.
- [[setting-the-tone]] — culture is transmitted, not legislated: set precedents early so
  useful behaviors become self-perpetuating "in-group" norms; public-by-default discussion,
  nipping rudeness in the bud, and codes of conduct.

### Open-source ecosystem & participation

- [[open-source-participation]] — who actually makes open-source code: a small,
  organizationally-weighted "GitHub-elite" core, and the hybridisation of commercial and
  open-source production.

### Project launch & licensing

- [[launching-an-open-source-project]] — turning a private vision into a public one:
  scaled presentation, "appearances matter," hacktivation energy, and the newcomer
  checklist (name, mission, license, status, downloads, repo, docs) — captured as what
  each item *signals*; plus Announcing (where to post, running-code-not-required, seed).
- [[developing-in-the-open]] — be open from Day One: "you open source your code, not your
  time"; why closed-then-open accumulates incompatible choices and a single large exposure
  event; and managing the siege mentality when opening a formerly closed project.
- [[open-source-licensing]] — Fogel's quick license guide: "free" and "open source"
  name the same approved set; the one-question choice (permissive MIT vs. copyleft GPL
  vs. network-use AGPL); and how to apply a license. Anchor to be enriched by Ch.9.

## Source entities

### Books

- [[producing-open-source-software-book]] — Karl Fogel, *Producing Open Source Software*
  (2nd ed., CC BY-SA 4.0). The example's primary source; full-book ingest in progress
  (Batches 1–6: Ch.1, Ch.2, Ch.3, and Ch.4 fully ingested — code review, launch, licensing,
  setting the tone, developing in the open, and the complete Ch.3 technical-infrastructure
  toolset; Chapters 5–9 pending).

### Papers

- [[ci-pull-request-delivery-time-paper]] — Guo & Leitner 2019, *PeerJ CS* (CC BY 4.0).
- [[who-makes-open-source-code-paper]] — Mehler et al. 2024, *EPJ Data Science* (CC BY 4.0).
