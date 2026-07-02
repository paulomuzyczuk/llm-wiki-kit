---
title: Eval Golden Set — software-craft — 2026-07-02
date: 2026-07-02
type: digest
status: active
---

# Eval Golden Set — software-craft — 2026-07-02

Phase 1 artifact of `/vault-evaluator` (see the skill's Phase 1). **Frozen benchmark:**
this file is immutable; every evaluation of this vault reuses this exact set, which is
what makes results comparable across users, models, and time. Phases 2–5 have not been
run against it in this repository — no answers, scores, or report exist yet, and no
`eval` log entry is written until a run completes.

Generated from THIS vault's `index.md`, `gaps.md`, and Negative Space records. Another
vault needs its own set — these questions are meaningless against a different corpus.

**Composition:** 30 scored (6 factual / 12 cross-source synthesis / 12 applied
judgment, of which 3 are role-specific through the [[role-code-craftsperson]] lens)
+ 4 abstention controls. Cross-book requirement: 6 synthesis questions require
combining Fogel with at least one paper or the tier-2 article. All entries
`origin: generated`; human-authored additions (flagged `origin: human`) may be
appended at the approval gate of a run, before any condition executes.

**Corpus:** [[producing-open-source-software-book]] (Fogel, all 9 chapters),
[[ci-pull-request-delivery-time-paper]] (Guo & Leitner 2019),
[[who-makes-open-source-code-paper]] (Mehler et al. 2024), and the tier-2
[[llm-assisted-maintenance]] article (Akita). Ground-truth pointers name the source
and chapter/section; exact page anchors live in the two-part citations on the
authoritative pages listed per question.

---

## Type 1 — Single-source factual

### Q1
**Q:** According to Fogel, what is the minimum standard set of collaboration tools
every open-source project needs?
**Pages:** [[project-infrastructure]] · **Ground truth:** Fogel ch. 3 (Technical
Infrastructure), opening sections.
**Rubric:** must list web site, forums, version control, bug tracking, real-time
chat; bad answers invent extras (CI, wikis) as *mandatory* or drop bug tracking.

### Q2
**Q:** What are the three components of a conventional release number, and what do
Semantic Versioning's rules say each one signals?
**Pages:** [[release-numbering]] · **Ground truth:** Fogel ch. 7 (Release Numbering);
SemVer rules as captured on the page.
**Rubric:** major/minor/micro with compatibility semantics (major = incompatible,
minor = compatible additions, micro = fixes); bad answers swap minor/micro semantics.

### Q3
**Q:** What are the two requirements the GPL imposes that make it "contagious," in
this vault's framing?
**Pages:** [[copyleft]] · **Ground truth:** Fogel ch. 9 (copyleft sections).
**Rubric:** derivative works must carry the same license + source must be made
available; bad answers conflate copyleft with "must publish all your code."

### Q4
**Q:** During release stabilization, what was Subversion's change-approval rule, as
recorded here?
**Pages:** [[stabilizing-a-release]] · **Ground truth:** Fogel ch. 7 (Stabilizing a
Release).
**Rubric:** three +1s and no vetoes (one veto blocks) for a change to enter the
release; bad answers misstate the counts or attribute it to release-manager fiat.

### Q5
**Q:** What does the Mehler et al. paper find about who actually writes open-source
code?
**Pages:** [[open-source-participation]] · **Ground truth:**
[[who-makes-open-source-code-paper]], core findings.
**Rubric:** a small, organizationally-weighted "GitHub-elite" core produces most
code; commercial/open-source production is hybridized; bad answers describe a flat
volunteer crowd.

### Q6
**Q:** What are a project's three options for establishing rights over incoming
contributions, and which does this vault's source recommend?
**Pages:** [[contributor-agreements]] · **Ground truth:** Fogel ch. 9 (contributor
agreements).
**Rubric:** do nothing (risky) / CLA (recommended) / copyright assignment (heavy),
with the DCO as minimal CLA; bad answers claim assignment is required or omit the
do-nothing baseline.

---

## Type 2 — Cross-source synthesis

### Q7 *(cross-book)*
**Q:** Fogel treats commit review as a social practice; Guo & Leitner measure review
inside a CI/PR pipeline. Where do the practitioner advice and the empirical findings
agree, and where is the tension?
**Pages:** [[code-review]], [[continuous-integration]] · **Ground truth:** Fogel
ch. 2 (review-every-commit) + [[ci-pull-request-delivery-time-paper]].
**Rubric:** must name the agreement (review as standing practice, visible and
prompt) and the tension (CI raises throughput more than it cuts per-PR latency —
speed benefits are not where intuition puts them); bad answers only summarize one
side.

### Q8 *(cross-book)*
**Q:** Fogel claims automating a common task pays back tenfold; the CI paper measures
what CI actually changes. Combining both, what does "CI pays off" concretely mean —
and what would be a wrong reason to adopt it?
**Pages:** [[the-automation-ratio]], [[continuous-integration]] · **Ground truth:**
Fogel ch. 8 (automation ratio) + [[ci-pull-request-delivery-time-paper]].
**Rubric:** payoff = burden × developers × repetitions, realized as throughput;
wrong reason = expecting per-PR latency to collapse; bad answers treat the 10× claim
as a latency claim.

### Q9
**Q:** This vault says there are "no true dictators" in open source. Reconstruct the
argument across the pages on forkability, forks, and governance — and explain why
innersourcing breaks it.
**Pages:** [[forkability]], [[forks]], [[open-source-governance]], [[innersourcing]]
· **Ground truth:** Fogel chs. 4, 8 (forks), 5 (innersourcing discussion).
**Rubric:** the *possibility* of forking caps all power; perception decides which
side "is" the fork; innersourcing removes the external supply of freedom so the cap
disappears; bad answers treat actual forks (rather than forkability) as the
mechanism.

### Q10
**Q:** "Attention is the true currency." Unify what this vault says about attention
across contributor motivation, credit, and praise/criticism into one economy — what
appreciates it, what debases it?
**Pages:** [[contributor-motivation]], [[credit-and-attribution]],
[[praise-and-criticism]] · **Ground truth:** Fogel chs. 6, 8.
**Rubric:** attention/credit as non-forkable currency; specificity appreciates it;
inflation (routine praise, inaccurate credit) debases it; bad answers list the three
pages without the currency mechanism connecting them.

### Q11 *(cross-book)*
**Q:** Fogel argues most free software is written by paid developers; Mehler et al.
measure who commits. Do the practitioner claim and the data agree — and what does
each add that the other cannot?
**Pages:** [[open-source-economics]], [[open-source-participation]] · **Ground
truth:** Fogel ch. 5 + [[who-makes-open-source-code-paper]].
**Rubric:** agreement on organizational weight; Fogel supplies the *why* (companies
need maintenance, not monopoly), the paper the *measured shape* (elite
concentration); bad answers frame them as contradicting.

### Q12 *(cross-book)*
**Q:** The vault claims open-source work is a "portable résumé" and a hiring signal.
Stress-test that claim against the participation data: if a small elite writes most
code, what does the public-résumé hiring advantage actually select for?
**Pages:** [[hiring-open-source-developers]], [[innersourcing]],
[[open-source-participation]] · **Ground truth:** Fogel ch. 5 +
[[who-makes-open-source-code-paper]].
**Rubric:** must connect résumé-reading advice (social record, not just commits) to
elite concentration (selection skews toward the already-visible); innersourcing
fails the portability test; bad answers ignore the concentration finding.

### Q13
**Q:** Reconstruct the complete timeline of a security vulnerability in an
open-source project — from the private report arriving to users running the fix —
and mark where the communication process hands off to release mechanics.
**Pages:** [[security-vulnerability-disclosure]], [[security-releases]] · **Ground
truth:** Fogel chs. 6, 7 (security sections).
**Rubric:** private intake → quiet fix (no early public commits) → CVE/CVSS →
pre-notification → simultaneous fix-and-announce; hand-off at the release built as
existing-release-plus-fix-only with security-only numbering; bad answers publish the
fix before the announce or skip pre-notification.

### Q14
**Q:** Why does maintaining several release lines in parallel make atomic commits
"near-mandatory," in this vault's account? Trace the mechanism through branching and
multi-line maintenance.
**Pages:** [[atomic-commits]], [[release-branches]],
[[maintaining-multiple-release-lines]] · **Ground truth:** Fogel ch. 7.
**Rubric:** cherry-picking a fix onto multiple lines requires one-logical-change
commits; mixed commits make ports and reverts unsafe; bad answers justify atomic
commits only by "cleanliness."

### Q15 *(cross-book, tier-mixed)*
**Q:** The Akita article proposes LLM review that "audits the code, not the author's
description." Does that preserve or replace Fogel's more-eyes review principle?
Answer with the vault's own tier caveat in view.
**Pages:** [[llm-assisted-maintenance]], [[code-review]] · **Ground truth:** Akita
article (tier-2) + Fogel ch. 2.
**Rubric:** preserves the function (independent scrutiny of the change) while
changing the economics; human sign-off keeps the social layer; must note the
tier-2/practitioner-blog status of the claim; bad answers present the LLM claim with
book-grade authority.

### Q16
**Q:** This vault describes project communication as something that fails quietly,
not explosively. Assemble its scaling model: what breaks, what are the two
structural responses, and how does the bug tracker participate?
**Pages:** [[scaling-project-communication]], [[choosing-the-right-forum]],
[[bug-tracking]] · **Ground truth:** Fogel chs. 3, 6.
**Rubric:** quiet negative-feedback failure; split forums before they choke +
durable/findable archives; tracker pre-filtering (buddy system, watchers) as load
shedding; bad answers propose "more moderators" as the model.

### Q17
**Q:** A company wants standing in a project it depends on. Combine the vault's
economics, governance, and corporate-behavior pages into the mechanism: what does
money actually buy, and how does a funder gain influence without breaking
governance?
**Pages:** [[open-source-economics]], [[open-source-governance]],
[[corporate-open-source-participation]] · **Ground truth:** Fogel ch. 5.
**Rubric:** money buys credibility, convertible to influence only through
contribution conduct ("appear as many, not as one," honest-broker behavior); funding
strains the benevolent-dictator model; bad answers say money buys influence
directly.

### Q18 *(cross-book)*
**Q:** Reconcile the vault's doctrine that the source release is the canonical
distribution form with the tier-2 advice to ship many install paths. What stays
fixed, what multiplies, and under what constraint?
**Pages:** [[source-packaging]], [[installation-surface]],
[[releasing-and-signing]] · **Ground truth:** Fogel ch. 7 + Akita article (tier-2).
**Rubric:** the signed source release stays canonical; packages multiply via
"compile once, repackage many"; constraint: every binary derives from the official
source release (plus signing/notarization cost per platform); bad answers treat the
install paths as alternative canonical forms.

---

## Type 3 — Applied judgment

### Q19
**Q:** A six-person team is open-sourcing an internal tool next quarter. Using what
this vault covers, design their review, CI, and release setup — and say which parts
to automate first and why.
**Pages:** [[code-review]], [[continuous-integration]], [[the-automation-ratio]],
[[project-hosting]], [[release-numbering]] · **Ground truth:** Fogel chs. 2, 3, 7, 8
+ [[ci-pull-request-delivery-time-paper]].
**Rubric:** commit review as standing practice, hosting-site standard CI, automation
priority by the ratio (testing first), consistent versioning; must justify
automation order, not just list tools.

### Q20
**Q:** You depend on an upstream project and your employer wants you to gain
influence in it over the next 12 months. Lay out the playbook — and the two things
that would backfire worst.
**Pages:** [[corporate-open-source-participation]], [[open-source-economics]],
[[contributor-motivation]], [[setting-the-tone]] · **Ground truth:** Fogel chs. 2,
5, 8.
**Rubric:** long-term hires, distributed presence, open motivations, credibility via
sustained contribution; backfires: publicity-driven schedules, appearing as one bloc
/ buying influence overtly; bad answers propose sponsorship as the lever.

### Q21
**Q:** You're releasing a new library and want wide corporate adoption but fear a
cloud vendor shipping a proprietary fork. Which licensing approach does this vault's
reasoning point to, and what trade-off are you accepting?
**Pages:** [[open-source-licensing]], [[copyleft]], [[permissive-licensing]],
[[license-compatibility]], [[proprietary-relicensing]] · **Ground truth:** Fogel
ch. 9.
**Rubric:** must frame it as the one-question choice (permissive vs copyleft vs
network-use), map the fear to AGPL/copyleft and adoption to permissive, state the
accepted trade-off explicitly, and stay at decision-criteria level (the vault's
legal coverage is principle-level); bad answers name a license with no trade-off or
invent legal mechanics.

### Q22
**Q:** A project founder is visibly fading — slow replies, missed releases. As a
core contributor, how do you handle the next three months?
**Pages:** [[transitions]], [[sharing-project-management]], [[committers]],
[[delegation-in-open-source]] · **Ground truth:** Fogel ch. 8.
**Rubric:** notice-the-fade pattern, guilt-free multistep ask-to-step-aside, privacy
overriding, transition happens when the successor starts, manager ≠ owner; bad
answers propose a public vote or an immediate fork.

### Q23
**Q:** A security researcher just emailed your project a critical vulnerability.
Walk through the next 30 days.
**Pages:** [[security-vulnerability-disclosure]], [[security-releases]],
[[maintaining-multiple-release-lines]] · **Ground truth:** Fogel chs. 6, 7.
**Rubric:** controlled-channel intake and acknowledgement, quiet fix, CVE/CVSS,
pre-notification, simultaneous release + announce, fix shipped on all supported
lines; bad answers commit the fix publicly early.

### Q24
**Q:** You must choose between two open-source dependencies with similar features.
One has many open bugs and a slightly chaotic forum; the other has few bugs and low
traffic. Using this vault's evaluation criteria, which signals matter and which
mislead?
**Pages:** [[evaluating-open-source-projects]], [[bug-tracking]], [[forks]] ·
**Ground truth:** Fogel chs. 3, 5, 8.
**Rubric:** more bug reports is better (usage signal), close-rate misleads, commit
*diversity* and bus factor over commit rate, forum tone; bad answers pick the
low-bug project on bug count.

### Q25 *(role: code-craftsperson)*
**Q:** As a code-craftsperson, what should change about your commit habits the day
your project starts maintaining parallel release lines?
**Pages:** [[role-code-craftsperson]], [[atomic-commits]], [[release-branches]] ·
**Ground truth:** Fogel ch. 7.
**Rubric:** strictly one logical change per commit (ports/cherry-picks depend on
it), nothing unrelated mixed in, commit messages that make per-line porting
decisions cheap; bad answers discuss branching strategy instead of commit
discipline.

### Q26 *(role: code-craftsperson)*
**Q:** As a code-craftsperson, your project just enabled LLM-generated pull
requests and your review queue tripled. Adapt your review practice using this
vault — what do you keep, what do you delegate to machines, and what must stay
human?
**Pages:** [[role-code-craftsperson]], [[code-review]],
[[llm-assisted-maintenance]], [[the-automation-ratio]] · **Ground truth:** Fogel
chs. 2, 8 + Akita article (tier-2).
**Rubric:** keep conspicuous public review; delegate description-vs-code auditing
and mechanical checks; human sign-off retained; automation justified by the ratio;
must carry the tier-2 caveat on the LLM claims.

### Q27 *(role: code-craftsperson)*
**Q:** As a code-craftsperson, a first-time contributor submits a working but messy
patch that ignores your conventions. What do you do — concretely — and why does the
vault say the handling matters more than the patch?
**Pages:** [[role-code-craftsperson]], [[treating-users-as-participants]],
[[code-review]], [[praise-and-criticism]] · **Ground truth:** Fogel chs. 2, 6, 8.
**Rubric:** educate-don't-berate, specific criticism of the work not the person,
the interaction as a recruitment moment ("the project runs on participation");
bad answers either merge silently or reject on style alone.

### Q28
**Q:** A government agency wants to open-source its new procurement system and
proposes developing privately for a year first "to get it right." Advise them using
this vault.
**Pages:** [[government-and-open-source]], [[developing-in-the-open]],
[[open-source-contracting]] · **Ground truth:** Fogel ch. 5 + ch. 2.
**Rubric:** open-from-day-one matters *more* for public-sector projects; the
closed-then-open costs (incompatible choices, single exposure event); contracting
adjustments (best-effort integration, OSQA/New Developer Test); bad answers accept
the private year with process tweaks.

### Q29
**Q:** A well-funded company just assigned five paid developers to your
volunteer-run project, full time, starting Monday. What risks does this vault
predict, and how do you absorb the help without losing the project?
**Pages:** [[corporate-open-source-participation]], [[preventing-territoriality]],
[[committers]], [[evaluating-open-source-projects]] · **Ground truth:** Fogel
chs. 4, 5, 8.
**Rubric:** single-vendor lock-in / organizational-diversity risk, "appear as many
not as one" applied in reverse, commit access earned by judgment not employer, keep
areas open to all; bad answers either refuse the help or hand over subsystems.

### Q30
**Q:** A long-time contributor is technically excellent but has started
filibustering decisions they dislike — endless process objections, never overt
rudeness. The community is exhausted. What does this vault prescribe?
**Pages:** [[difficult-people]], [[facilitating-online-discussion]],
[[setting-the-tone]] · **Ground truth:** Fogel ch. 6.
**Rubric:** identify the pattern (process manipulation, often insecurity-driven),
tolerate when cheap, else build the archive-grounded quantitative case — never an
accusation; steer threads with purpose and positive next actions; bad answers
propose an immediate ban or a public confrontation.

---

## Type 4 — Abstention controls *(unscored; classification only)*

### N1
**Q:** What are the operative legal steps and documents required to relicense an
existing GPL project to MIT?
**Expected:** ABSTAIN. `gaps.md` §1 records that legal coverage is principle-level
by design — Fogel defers operative mechanics to specialist resources (Meeker,
Lindberg, OSI). A good answer states the boundary, cites the gap record, and offers
the decision-criteria view ([[open-source-licensing]], [[license-compatibility]])
as what the vault *can* say.

### N2
**Q:** Explain the regression discontinuity design the CI paper used to establish
its delivery-time findings.
**Expected:** ABSTAIN. The [[continuous-integration]] page's Negative Space records
the RDD methodology as `supporting-argument` — deliberately not paged. A good
answer names that record and offers the paper's *findings* instead.

### N3
**Q:** Tell me the story of how Subversion's commit-review culture got started —
who did what, and how it spread.
**Expected:** ABSTAIN. The [[code-review]] page's Negative Space records the
Greg Stein anecdote as `illustrative-scaffolding`: the transferable claim (lead by
example; review becomes expected) is captured, the narrative deliberately is not.
A good answer states exactly that split.

### N4
**Q:** What does this vault recommend on monorepo versus polyrepo repository
strategy?
**Expected:** ABSTAIN. Not covered anywhere in the corpus — adjacent to
[[version-control]] and [[atomic-commits]] but absent from all four sources. A good
answer says so plainly and may suggest it as a `gaps.md` §2 candidate; any concrete
recommendation is a hallucination.
