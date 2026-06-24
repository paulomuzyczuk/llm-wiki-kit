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
- [[atomic-commits]] — one logical change per commit, nothing unrelated mixed in; the
  daily-development discipline that keeps merge, cherry-pick, change-voting, and revert
  clean, made near-mandatory by parallel release maintenance.

### Continuous integration & delivery

- [[continuous-integration]] — automated build-on-integration; the empirical reality
  (CI raises PR *throughput* more than it cuts per-PR latency), and how CI relates to
  version control and review. Plus Fogel: automated testing-on-commit *encourages*
  exploratory development, "don't break the build," and use your hosting site's standard CI.
- [[the-automation-ratio]] — "don't let humans do what machines could do": automating a
  common task pays back 10×+ because the small burden is multiplied across every developer
  and every repetition; automated regression/unit testing as the highest-value case, and the
  caveat that any process must not become a bottleneck.

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
- [[forks]] — the paired exercise of that right: development vs. hard forks, why perception
  decides which side is "the fork" (a "vote of confidence"), handling a fork non-vindictively
  to keep developers, and initiating one only as a last resort.
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
- [[praise-and-criticism]] — feedback as a management tool: praise and criticism are both
  forms of attention, most effective when specific, and devalued by inflation; criticize the
  work not the person, and praise sparingly (don't praise the normal).

### Release engineering & packaging

- [[release-numbering]] — release numbers as a compact signal to users who don't follow
  the project daily: the twofold purpose (communicate ordering + nature of change),
  major/minor/micro components, Semantic Versioning's compatibility rules, the even/odd
  stability convention, and "be consistent" above all.
- [[release-branches]] — why full-tree snapshots can't make a release, and the release
  branch as the structure that isolates release work from daily development: mechanics
  (branch from main, name the minor line, tag snapshots), parallel maintenance lines, and
  near-simultaneous releases for conservative vs. adventurous users.
- [[stabilizing-a-release]] — stabilization as a machine for saying "no": time-based vs.
  feature-based cadence, the two extremes (dictatorship by release owner vs. multi-vote
  change approval, Subversion's 3×+1/one-veto rule), the lightweight STATUS-file mechanics,
  and the release-manager (logistics) vs. release-owner (authority) distinction.
- [[source-packaging]] — source code as the canonical distribution form that
  unambiguously defines a release, and the "follow the conventional standard" principle
  (archive format + name-carries-the-release-number; conform to build/install
  conventions; binary packages must derive from an official source release).
- [[releasing-and-signing]] — the public release gate: approval by real testing (build on
  a clean system, run the suite), personal-key OpenPGP signing + checksums for tamper
  verification and web-of-trust paths, candidate releases for wide pre-blessing exposure,
  and release-announcement specifics.
- [[maintaining-multiple-release-lines]] — running several release lines in parallel: why
  a new line doesn't kill the old one, shipping a late bugfix on both, officially
  announced end-of-life, pledged vs. demand-gauged support windows, and per-line bug-tracker
  targets.
- [[security-releases]] — the release that can't be publicly tested: existing release plus
  the fix only, the "minor deception" of an in-flight release, and security-only numbering;
  the release-mechanics half of [[security-vulnerability-disclosure]].
- [[release-planning]] — decoupling release *contents* from *dates* to defuse the
  corporate-vs-community deadline tension, the inertial bias against scope creep, separate
  interim releases as a valve, and releasing often (every 3–6 months) to lower the stakes.

### Open-source ecosystem & participation

- [[open-source-participation]] — who actually makes open-source code: a small,
  organizationally-weighted "GitHub-elite" core, and the hybridisation of commercial and
  open-source production.
- [[contributor-motivation]] — why people work on free software beyond the paycheck (the
  built-in desire to earn respect through cooperation), why status norms must reward
  constructive action, and "attention is the true currency" — the resource that, unlike code,
  is not forkable.
- [[delegation-in-open-source]] — delegation as a political/social tool, not just workload
  spreading: every public request signals trust; distinguish inquiry from assignment; follow
  up no matter what; delegate even when you could do it faster, to draw people in.
- [[preventing-territoriality]] — keeping every area open to every contributor: why exclusive
  ownership creates single points of failure and "no trespassing" chill, authority granted by
  consensus never seized, cookie licking, and banning source-file author tags.
- [[treating-users-as-participants]] — the recruitment funnel: every interaction is a chance
  to gain a participant; educate (don't berate) bad bug reports; "the project runs on
  participation"; the one exception for genuinely rude users.
- [[sharing-project-management]] — share the management burden as a peer-to-peer network, not
  a hierarchy: "manager does not mean owner" (responsibility without monopoly, documented for
  handoff), and the patch and translation manager roles.
- [[committers]] — commit access as social authority over the authoritative release copy: the
  only formally distinct class in open source, the Hippocratic "do no harm" / good-judgement
  selection criterion, revoking access privately, partial and dormant access, and "avoid
  mystery" by publishing the rules and the roster.
- [[transitions]] — the craft of handing off a standing role when its holder fades: noticing
  the slow fade, the multistep guilt-free ask-to-step-aside, the transition happening when the
  new person starts, and privacy as the overriding factor.
- [[credit-and-attribution]] — credit as "the primary currency of the free software world,"
  distributed accurately through the records the VCS already keeps; routine acknowledgement vs.
  special thanks, and the individual-vs-group tension (err toward group).

### Project launch & licensing

- [[launching-an-open-source-project]] — turning a private vision into a public one:
  scaled presentation, "appearances matter," hacktivation energy, and the newcomer
  checklist (name, mission, license, status, downloads, repo, docs) — captured as what
  each item *signals*; plus Announcing (where to post, running-code-not-required, seed).
- [[developing-in-the-open]] — be open from Day One: "you open source your code, not your
  time"; why closed-then-open accumulates incompatible choices and a single large exposure
  event; and managing the siege mentality when opening a formerly closed project.
- [[open-source-licensing]] — the licensing anchor: "free" and "open source" name the same
  approved set; the one-question choice (permissive MIT vs. copyleft GPL vs. network-use AGPL);
  how to apply a license; plus the Ch.9 deepening — terminology (commercial≠proprietary, public
  domain), what licenses vary on (aspects), and choosing a well-recognized existing license.
- [[copyleft]] — reciprocal licensing: the GPL's two requirements that make "freedom
  contagious"; the copyleft-vs-everything-else dividing line; LGPL/AGPL reciprocity strength;
  the sole-copyright-holder exemption; and why to skip the "is the GPL really free?" holy war.
- [[permissive-licensing]] — non-reciprocal licensing (MIT/BSD/Apache): proprietary-compatible,
  often with attribution requirements; MIT as the default permissive choice and the MIT-vs-Apache
  trade-off.
- [[license-compatibility]] — whether differently-licensed code can be combined; GPL-compatibility
  as the dominant axis; and the DFSG/OSI/FSF/SPDX certification tests that answer it.

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
  choice, publicity, security vulnerability disclosure (6b). Batches 12–13 ingested all of Ch.7
  "Packaging, Releasing, and Daily Development" — release numbering, branches, stabilization,
  packaging (7a); releasing & signing, multiple release lines, security releases, atomic
  commits, release planning (7b). Batches 14–15 ingested all of Ch.8 "Managing Participants" —
  contributor motivation, delegation, praise & criticism, preventing territoriality, the automation
  ratio, treating users as participants, sharing project management (8a); transitions, committers,
  credit & attribution, forks (8b). Ch.1–8 complete; Ch.9 (Legal Matters) pending across batches
  16–17).

### Papers

- [[ci-pull-request-delivery-time-paper]] — Guo & Leitner 2019, *PeerJ CS* (CC BY 4.0).
- [[who-makes-open-source-code-paper]] — Mehler et al. 2024, *EPJ Data Science* (CC BY 4.0).
