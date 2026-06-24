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
  beyond coders, and writing it down. Also: how *funding* strains the benevolent-dictator
  model (Ch.5).
- [[forkability]] — the right to fork as the ceiling on all project power; why the
  *possibility* matters more than the rare act, and why there are no true dictators.
- [[setting-the-tone]] — culture is transmitted, not legislated: set precedents early so
  useful behaviors become self-perpetuating "in-group" norms; public-by-default discussion,
  nipping rudeness in the bud, and codes of conduct.

### Open-source economics & organizations

- [[open-source-economics]] — why most free software is written by paid developers (companies
  need software maintained, not monopolized), informal subsidy and "unofficial consortia,"
  why money buys *credibility* (convertible to influence) rather than influence directly, and
  the taxonomy of corporate-involvement goals.
- [[corporate-open-source-participation]] — the behavioral playbook for a funder: hire for the
  long term, "appear as many, not as one," be open about your motivations (honest-broker
  behavior), "money can't buy you love," plus organizational engagement — retire the
  instant-adoption and casual-code-reuse myths, foster pools of expertise (avoid single-vendor
  lock-in), don't let publicity drive the schedule, and the key role of middle management.
- [[innersourcing]] — open-source practices inside one company's boundary: real benefits (less
  context-switching, morale, a first step to real participation) but not true open source, because
  it removes the "external supply of freedom" (forkability) and fails the "portable résumé" test.
- [[hiring-open-source-developers]] — the public-résumé hiring advantage: ask for the candidate's
  open-source profile, read the social record (review tone, bug-ticket conduct) not just commits,
  treat missing experience as a question; and "hiring for influence" with its dual loyalty —
  influence travels with the person, not the employer.
- [[evaluating-open-source-projects]] — reading project health (an art, not a science): bug-tracker
  activity first ("more bug reports is better," close-rate misleads), commit *diversity* not rate,
  organizational diversity / bus factor, forum tone, and recent news — also how to call the two
  sides of a fork.
- [[crowdfunding-and-bounties]] — marginal funding modes: all-or-nothing vs. keep-it-all
  crowdfunding and one-time bounties; both mismatch open source's ongoing-process nature; useful at
  launch, not for sustained development; borrowable techniques and the "don't sell early access"
  pitfall.
- [[government-and-open-source]] — why "government is different" (outsourced expertise, slow
  procurement, risk-aversion, publicity hunger) and the adjustments that follow, including why
  open-from-day-one matters even more for public-sector projects.
- [[open-source-contracting]] — you can buy work but not its acceptance: best-effort
  integration clauses, hire-from-within vs. -outside, contract transparency, community review
  as a "free design board," RFP/RFI language, and Open Source Quality Assurance (OSQA),
  including the New Developer Test.
- [[funding-non-programming-activities]] — where a funder's money does the most good off the
  code path: professional testing (dual-ticket bridging), legal counsel engaged early,
  documentation by a medium-level user, UX as an attitude not a checkbox, donated CI/build
  farms, security audits, and sponsoring in-person meetings — all unified by the
  translate-between-worlds bridging principle.
- [[open-source-marketing]] — marketing open source under public scrutiny: the vendor-lock-in
  advantage ("product and vendor are not the same") and "cost of total ownership," "you are
  being watched" (audit every claim), don't bash competing vendors, and "commercial vs
  proprietary" terminology integrity (don't mislabel open core as "Community/Enterprise Edition").

### Open-source communication & conflict

- [[written-communication]] — clear writing as the load-bearing open-source skill: "you are
  what you write," plain-text/formatting and content conventions, terseness leavened because
  "feelings affect productivity," what counts as rude (direct criticism and blunt questions
  don't; skimping on promised criticism does), and the consistent screen name as your online
  "face."
- [[facilitating-online-discussion]] — keeping group threads productive: post only with a
  purpose, steer with "we" and a positive next action, the Bikeshed Effect (debate grows as
  topic complexity shrinks), defusing holy wars, countering the noisy-minority effect with
  quantitative evidence, and why not to bash competing projects.
- [[difficult-people]] — the obstructionist who manipulates process rather than being overtly
  rude (filibuster, sealioning, summary-blocking); usually driven by insecurity, often best
  tolerated, and when not, defeated by an archive-grounded quantitative case — never an
  accusation.
- [[scaling-project-communication]] — why massively-parallelized support doesn't scale (the
  quiet negative-feedback failure, not an explosion), and the two responses: split forums
  before they choke, and make information durable/findable via conspicuous archives, the
  "treat all resources like archives" properties, and codifying tradition.
- [[choosing-the-right-forum]] — matching the conversation to the venue (chat vs. dev list
  vs. bug ticket), the convergent/divergent rule for when to move a discussion, cross-linking
  the old and new venue, and open source as a writer-responsible culture.
- [[open-source-publicity]] — the internal-to-PR continuum, the announcement channels and
  why they fire simultaneously, scaling the noise to an event's real importance, and
  engineering a "meant-to-be-quoted" lead so word of mouth stays accurate.
- [[security-vulnerability-disclosure]] — the coordinated openness-vs-secrecy process:
  private intake on a controlled channel, develop the fix quietly (never commit publicly
  early), CVE/CVSS naming and scoring, pre-notification of high-value users, and a
  simultaneous public fix-and-announce.

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
  (Batches 1–6: Ch.1–Ch.4 fully ingested — code review, launch, licensing, setting the tone,
  developing in the open, and the complete Ch.3 technical-infrastructure toolset. Batch 7
  opened Ch.5 "Organizations and Money" — economics, corporate/government involvement, hiring,
  contracting; Batch 8 added Ch.5's non-code half — funding non-programming activities and
  marketing; Batch 9 completed Ch.5. Batches 10–11 ingested all of Ch.6 "Communications" —
  written culture, facilitating discussion, difficult people (6a); scaling communication, forum
  choice, publicity, security vulnerability disclosure (6b). Ch.1–6 complete; Ch.7–9 pending).

### Papers

- [[ci-pull-request-delivery-time-paper]] — Guo & Leitner 2019, *PeerJ CS* (CC BY 4.0).
- [[who-makes-open-source-code-paper]] — Mehler et al. 2024, *EPJ Data Science* (CC BY 4.0).
