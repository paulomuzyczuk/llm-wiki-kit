---
title: Open-Source Governance
aliases: [governance-model, benevolent-dictator, consensus-democracy]
date: 2026-06-23
last_updated: 2026-06-23
type: topic
topics: [open-source-governance, software-collaboration]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Open-Source Governance

Governance is how a project "actually make[s] decisions on a day-to-day basis" and resolves
conflict — the structural properties shared by projects that are successful "not just in
terms of technical quality, but in terms of operational health and survivability."
*Operational health* is the ongoing ability to absorb new code and contributors and respond
to bug reports; *survivability* is the project's "ability to continue independently of any
individual participant or sponsor" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=72), p. 59).
Whether formal or informal, healthy governance produces the same thing: "a sense of
institutional permanence, supported by habits and procedures that are well understood by
everyone who participates" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=72), p. 59).
All of it operates *under the ceiling* set by [[forkability]].

## Two idealized models on a continuum

Fogel presents two "somewhat idealized extremes," with most projects "somewhere along a
continuum between them" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=73), p. 60).

### Benevolent dictator

Final authority rests with one person "expected to use it wisely." The label is misleading:
a better framing is "community-approved arbitrator" or "judge." Crucially, benevolent
dictators (BDs) "commonly do not dictate much" — they "let things work themselves out
through discussion and experimentation," participating as regular developers and often
deferring to area maintainers, and only "put[ting] her foot down" when no consensus can
form and the group *wants* a decision so work can proceed. "Reluctance to make decisions by
fiat is a trait shared by almost all successful benevolent dictators; it is one of the
reasons they manage to keep the role" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=73), p. 60).

The role's qualifications are social, not technical supremacy: "self-restraint," a
sensitivity to how much one's words weigh, and the ability "to recognize and endorse good
design when encountered" — not necessarily to produce it on demand or to be the sharpest
coder. BDs are often founders, but that is "more a correlation than a cause." The model is
right "if it's simply obvious to everyone who should be the BD"; if no candidate is obvious,
the project "should probably use a decentralized decision-making process"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=73), p. 60).

### Consensus-based democracy

Older projects "tend to move away from the benevolent dictatorship model and toward more
openly democratic systems" because group governance is more "evolutionarily stable": vesting
power in one person means "N − 1 people… choosing to decrease their individual influence,"
which they rarely do, and the move "rarely moves back"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=73), p. 60); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=74), p. 61).
Two elements recur: the group "works by consensus most of the time," with "a formal voting
mechanism to fall back on when consensus cannot be reached"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=74), p. 61).

## Consensus as the default

Consensus is "an agreement that everyone is willing to live with," and it is "not an
ambiguous state: a group has reached consensus… when someone proposes that consensus has
been reached and no one contradicts the assertion." It blends into ordinary technical
discussion — a concluding summary post doubles as "an implicit proposal of consensus." For
small changes the proposal is implicit: a spontaneous bugfix commit *is* a proposal of
consensus, and "silence is consent" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=74), p. 61).
This low-formality default is underwritten by reversibility — see
[[version-control]]'s "Version Control Means You Can Relax."

## Voting — a last resort

When a debate "just won't consense," the fallback is a vote — but Fogel is emphatic that it
should be "very rare — a last resort." Voting "ends discussion, and thereby ends creative
thinking about the problem"; while discussion continues, someone may still "come up with a
new solution everyone likes." Even absent a new proposal, "it's still usually better to
broker a compromise than to hold a vote," because after a compromise "everyone is a little
bit unhappy," whereas a vote leaves winners and losers
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=75), p. 62); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=76), p. 63).

Mechanics that matter when a vote is unavoidable:

- **Build the ballot from the debate.** The "honest broker" who has been posting periodic
  summaries of the disagreement can convert those summaries "into prototypes for a ballot
  sheet" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=75), p. 62).
- **Prefer approval voting.** "A good choice in most cases is approval voting" — each voter
  votes for as many options as they like — because "comprehensibility is an important factor
  when choosing a voting method" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=75), p. 62).
- **Vote in public.** "There is no need for secrecy or anonymity in a vote about matters
  that have been debated publicly anyway"; public tallies are recorded in the archives
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=75), p. 62).
- **Routine votes are exempt** from the reluctance rule — e.g. release-stabilization votes
  function "more of a communications mechanism," and procedural elections are normal
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=76), p. 63).

## Electorate: voters, maintainers, and non-coders

Having a vote forces the question of *who* votes, which "forces the project to officially
recognize some people as being more involved." A common solution is to attach voting to
commit access; full committers "must be chosen not only as programmers, but as members of
the electorate," so a technically skilled but "disruptive or obstructionist" candidate is a
risk ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=76), p. 63).
But committers need not equal voters: people who "provide legal help, or organize events, or
manage the bug tracker, or write documentation" may deserve a vote, so Fogel recommends
expanding "committer" to **maintainer** — "what matters is their good judgement and the
trust of their peers," not whether they write code
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=76), p. 63).
Adding maintainers is "one of the rare instances where secrecy is appropriate": the vote
happens on a private list so a passed-over candidate's "feelings and reputations" aren't
exposed ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=76), p. 63).
For some questions the electorate is deliberately *widened* instead — e.g. asking all
mailing-list subscribers whether an interface matches real usage. These are "really polls
rather than votes," though developers "may choose to treat the result as binding"; with any
poll, "make it clear to the participants that there's a write-in option," since an
unanticipated answer "may turn out to be the most important result"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=77), p. 64).

## Vetoes

Some projects allow a **veto** — "somewhere between a very strong objection and a
filibuster" — to halt a hasty change "long enough for everyone to discuss it more." Any veto
"should be accompanied by a thorough explanation"; one without is "invalid on arrival." The
hazard is *veto abuse*, countered by "being very reluctant to use vetoes yourself" and
gently calling out overuse, with the reminder that vetoes "are binding for only as long as
the group agrees they are." The "-1" notation comes from the Apache Software Foundation
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=77), p. 64).

## Writing it down

Once a project's conventions "become so great that you need to record it somewhere," the
governing rule is that the document **describes** rather than **creates** the agreements:
"it is not the source of the agreements, it is merely a description of them," and should
"contain no surprises," ideally linking to the mailing-list threads it codifies. It
typically lives at the repository root as `CONTRIBUTING.md` or `DEVELOPMENT.md`
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=77), p. 64).
Two cautions: "don't try to be comprehensive" — obvious admonitions like "be polite" are
useless because no one violating them stops on account of a document; base it instead "on
the questions that newcomers ask most often." And make clear "the rules can be
reconsidered," since the document is "a living reflection of the group's intentions, not a
source of frustration" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=78), p. 65).

## Formalizing as a legal entity

Successful projects sometimes need legal existence — to accept donations, hold
infrastructure, enforce trademarks. Fogel's advice: with "a few exceptional" exceptions,
"it is much better to join an existing organization" — an umbrella non-profit whose
economies of scale and experience beat anything a single project could build. The governing
principle is separation: the legal entity "is there to handle things the developers don't
want to handle, not to interfere" with technical decisions, even if it formally owns the
project's copyrights and trademarks ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=79), p. 66).

## Negative Space

- **Specific umbrella organizations** (`tool-specific/perishable`): the named list (Software
  Freedom Conservancy, Apache, Eclipse, SPI, Linux Foundation) and U.S. 501(c) tax
  distinctions are perishable specifics, captured as "join an existing umbrella org" rather
  than paged.
- **Voting-system taxonomy** (`too-granular`): Condorcet, Borda, IRV, score voting, and
  Arrow's Impossibility Theorem are a sidebar the author explicitly warns against "geeking
  out" on; the durable takeaway is "prefer approval voting for comprehensibility."
- **"Linking to emails" / archive-citation mechanics** (`too-granular`): a practical sidebar
  on how to cite mail threads, a bullet under documentation practice, not a concept.
- **Example governance documents** (`illustrative-scaffolding`): LibreOffice, Subversion,
  and ASF guides cited as models, not concepts to page.

## See also

- [[forkability]] — the right of exit that caps every governance arrangement here from
  above.
- [[version-control]] — reversibility ("you can relax") is what lets consensus stay
  informal.
- [[open-source-culture]] — the "influence ∝ contribution" ethic these structures
  operationalize.
- [[code-review]] — the per-change discussion in which most consensus is actually reached.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 4 "Social and Political
  Infrastructure" — Benevolent Dictators; Consensus-based Democracy; voting and vetoes;
  Writing It All Down; Joining or Creating a Non-Profit (printed pp. 59–66).
