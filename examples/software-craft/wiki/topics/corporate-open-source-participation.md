---
title: Corporate Open-Source Participation
aliases: [corporate-involvement, being-a-good-corporate-citizen, appear-as-many-not-one, money-cant-buy-love]
date: 2026-06-23
last_updated: 2026-06-24
type: topic
topics: [open-source-participation, open-source-economics]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Corporate Open-Source Participation

Once an organization decides to fund a project (the *why* is [[open-source-economics]]), the
question becomes *how to behave* in a community it cannot command. Because money buys
credibility rather than control, a funder's influence is earned the same way any contributor's
is — and is just as easily forfeited. The principles below are all variations on one move:
**make the company the same size as everyone else.**

## Hire for the long term

"If you're managing programmers on an open source project, keep them there long enough that
they acquire both technical and political expertise — a couple of years, at a minimum."
Churn is costly everywhere, "but the penalty is even stronger in open source projects:
outgoing developers take with them not only their knowledge of the code, but also their status
in the community and the human relationships they have made there"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=84), p. 71).

The reason is that **"the credibility a developer has accumulated cannot be transferred."** An
incoming developer "can't inherit commit access from an outgoing one" (see "Money Can't Buy
You Love" below) — but commit access "is only the most easily quantifiable manifestation of
lost influence." A long-timer "knows all the old arguments that have been hashed and rehashed
on the discussion lists"; a newcomer who re-raises settled topics costs the organization
credibility ("Can't they remember anything?") and "will have no political feel for the
project's personalities"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=84), p. 71).

Train newcomers through **supervised engagement**: the new developer should be "in direct
contact with the public development community from the very first day, starting off with bug
fixes and cleanup tasks" — work that builds reputation "yet not spark any long and involved
design discussions." Meanwhile "one or more experienced developers should be… reading every
post the newcomer makes," to "spot potential rocks before the newcomer runs aground," with
private encouragement alongside the public review
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=84), p. 71).

## Appear as many, not as one

"Your developers should strive to appear in the project's public forums as individual
participants, rather than as a monolithic corporate presence" — not for appearance's sake but
because "individuals are the only sort of entity that open source projects are structurally
equipped to deal with. An individual contributor can have discussions, submit patches, acquire
credibility, vote… A company cannot"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=85), p. 72).

Decentralized behavior also "avoid[s] stimulating centralization of opposition." Let your
developers "disagree with each other on the mailing lists," review each other's code publicly,
and avoid "always voting as a bloc," lest others feel "there should be an organized effort to
keep them in check." Fogel distinguishes "actually being decentralized" from "simply striving
to appear that way": coordinating behind the scenes is fine — e.g. having several people
"chime in with agreement early on" to give a proposal momentum — "as long as objections are
still taken seriously." Orchestrated agreement "is no less sincere for having been coordinated
beforehand," provided it is "not used to prejudicially snuff out opposing arguments"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=85), p. 72).

## Be open about your motivations

"Be as open about your organization's goals as you can without compromising business
secrets." If customers are "clamoring for" a feature, "just say so outright." This "runs
counter to the instinct… that knowledge is power," but stating your goal plainly is strength:
"you have already laid your cards on the table," and concrete real-world scenarios "can have a
dramatic effect on the debate"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=85), p. 72).

A funder with customer data can supply "a countervailing force" to feature debates that
otherwise "drift farther and farther from any mooring in actual user experience" and get
"determined by whoever was the most articulate, or the most persistent, or the most senior."
The discipline is **"honest broker" behavior**: "focus your initial posts on the problem,
rather than on one particular solution," present "as many reasonable solutions as you can,"
and let your preferred one win on merit — "if the solution you prefer really is superior, other
developers will recognize that on their own eventually." Advocating a specific solution is
allowed, but "you must have the patience to see the analysis you've already done internally
repeated on the public development lists"; signaling that decisions were made "behind closed
doors… is a recipe for resentment." Knowing more than everyone else is itself "a disadvantage"
— it creates a distancing effect — so "the earlier you can get everyone else thinking about
things in the same terms as you do, the smaller this… will be"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=86), p. 73).

## Money can't buy you love

"If you're a paid developer on a project, then set guidelines early on about what the money
can and cannot buy." Not by protesting one's incorruptibility, but by being "on the lookout
for opportunities to defuse the tensions that could be created by money"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=86), p. 73).

The canonical example is Subversion's hiring of Mike Pilato. The project already had a policy:
a new developer submits patches until committers propose her for direct commit access. CollabNet,
the primary funder, could probably have granted Pilato commit access on day one without
objection — "but we knew we'd be setting a precedent. If we granted Mike commit access by fiat,
we'd be saying that CollabNet had the right to ignore project guidelines, simply because it was
the primary funder," gradually leaving non-salaried developers "feeling disenfranchised." So
Pilato "agreed to start out… like any other new developer, without commit access," and the team
announced on the list that this was deliberate. After weeks of activity he was proposed and
accepted "as we knew he would be." The lesson: "that kind of consistency gets you a credibility
that money could never buy," which is "immunization against having one's motives questioned."
By observing all guidelines from the start, "the funder makes itself the same size as everyone
else" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=87), p. 74).

This is also where funding and governance interact: the **benevolent-dictator model is
"slightly harder to pull off in the presence of funding,"** especially if the dictator works
for the funder — see [[open-source-governance]]'s "Funding strains the benevolent-dictator
model" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=87), p. 74).

## Two myths to retire

Organizations new to open source carry two expectations Fogel debunks. **Instant adoption:**
releasing a project you're excited about "doesn't necessarily mean other entities are going to
adopt that software right away," because "adopting any software involves costs. Indeed, merely
evaluating software involves costs." Adopters "take a closer look based on their schedule, not
yours," so expect "a trickle of early adopters over the first year or so … than … a flood of
them immediately." The few you get "should be cultivated because they will provide the
word-of-mouth that gets you more adopters"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=100), p. 87).

**Casual code reuse:** "open source licenses are still licenses," virtually all requiring
attribution and inclusion of the license; copyleft licenses can pull "the entire derivative work
… under the same open source license," and some carry patent clauses. So incorporating open
source code into separately-licensed software "cannot be done casually." Organizations "usually
need a formal process for doing so, one that involves review by someone who understands the legal
issues and the possible interactions between licenses" — see [[open-source-licensing]]
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=100), p. 87).

## Foster pools of expertise in multiple places

A procurement reflex from the proprietary world is to assume "there is exactly one authoritative
provider of expert support." But "that's not how open source works. One of the great strengths of
open source is the availability of support from multiple, competing providers." Support "is
fundamentally a marketplace, not an add-on feature that just happens to come with the software
license." Having "a commercial relationship with just one of those sources" is fine, but treating
that provider as the single source of truth recreates the lock-in open source dissolves
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=100), p. 87).

This goal "should even influence how you structure contracts" (see [[open-source-contracting]]).
If you hire a firm to build open source software, "have a few of your own programmers working
alongside them if possible, so that you accumulate some in-house expertise" — not because you
won't reuse the firm, but "so that you'll have a better bargaining position and not be locked in."
The general law: "the more people in different organizations who know the code, the healthier it
is for the project, and the better position you are in." Where you lack the in-house ability even
"to perform knowledgeable review," Fogel recommends a third party providing independent
"deployability and maintainability review" — Open Source Quality Assurance (OSQA)
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=100), p. 87); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=101), p. 88).

A complementary move is to **establish contact early with relevant communities.** Interested
technical communities "are almost always out there" — geospatial, fintech, medical-data, and so
on. Beyond the initial announcement, "when your project runs across a design issue that you
suspect others may have encountered before, it's fine to ask them how they handled it, as long as
you do your homework" first. You "can also arrange small-scale contracts with developers who are
active in related projects," serving two goals at once: "improving your project's quality while
also establishing mindshare in places that may be strategically useful later"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=101), p. 88).

## Don't let publicity events drive the project schedule

With "an active developer community you do lose some control over the exact timing of events …
especially the scheduling of releases." You can still exert control, but "there are other things
you lose if you exercise that control in the wrong way" — forcing a release date can drive away an
outside release manager and the developers doing release work, buying "fine-grained control … at
the cost of lower quality releases and the possible loss of some of your development community."
The general principle: "if you have publicity needs related to an open source project, you
generally shouldn't let those needs drive the project's schedule"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=101), p. 88).

Two non-exclusive ways to win that independence: **let project events drive publicity** (prepare
announcements ahead but publish them "based on when the release is actually done"), or **create
publicity events not bound to development milestones** — "new support offerings, new partnership
announcements, major deployments, conference appearances, hackathons." A tempting third way —
bringing the community into scheduling "so that through consensus you are able schedule certain
milestones accurately" — "rarely works," the lone exception being a project genuinely committed to
time-based releases (and only if your organization "must also be willing to abide by that
schedule"). A community's "first priority is the software itself," and the outcome of its
decision-making "cannot be anticipated with perfect accuracy, by definition"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=101), p. 88).

## The key role of middle management

For "long-term organizational engagement," the middle layer of management "will play a key role in
determining whether you succeed or fail"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=101), p. 88).
Supervising programmers on open source projects "is more
complex than supervising programmers on purely internal projects," because much of their work and
schedule is "strongly influenced by external factors not under the control of management." Each
such developer "has two unrelated audiences to satisfy: her employer … and her colleagues in the
open source project." A manager insensitive to this dynamic lets developers "feel like they're
being pulled in conflicting directions"; good management prevents the avoidable cases and, for the
unavoidable ones, gives "the developer clarity and a way to handle the conflict"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=102), p. 89).

Middle managers are "to some degree responsible for the … open source brand identity … of the
organization itself," an "entire extra constituency to satisfy." They are also best positioned to
serve as a **"communications conduit and information filter"** between project and company:
project activity "is most useful to the organization if there is a filtered channel by which the
most interesting activities can be communicated to the relevant stakeholders." Programmers
themselves are "often not best suited to serve as this conduit" — deep on their projects but with
"a less complete view of the organization's interests." Managers can hold "the requisite
bidirectional sensitivity." Fogel's strongest recommendation: such managers should ideally "have
had direct, personal experience as participants in some open source project" — not necessarily the
same one, since "the situations and tensions … tend to be similar," but first-hand experience
somewhere ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=102), p. 89).

## Negative Space

- **CollabNet / Mike Pilato / Subversion specifics** (`case-study-specifics`): the dates,
  names, and timeline are illustrative; the precedent-setting principle is captured.
- **Danese Cooper / Sun / Tomcat footnote** (`illustrative-scaffolding`): a parallel
  commit-access story cited in a footnote, not a separate concept.
- **"The Smaller the Topic, the Longer the Debate" cross-reference** (`foreshadowing`):
  pointed at people "who like to object just to stay in shape"; the bikeshedding concept is
  developed in Ch.6 (Communications), not yet ingested.
- **GeoNode / Open Data for Resilience Initiative case report** (`case-study-specifics`): a World
  Bank report cited to ground "foster in-house expertise"; the technique is captured, the case is
  not paged.
- **Named third-party support markets — Oracle / Microsoft examples** (`illustrative-scaffolding`):
  used to contrast single-giant proprietary support with open source's fluid marketplace.
- **"Press conference for 1.0" anecdote** (`illustrative-scaffolding`): a real-life example of
  publicity colliding with a slipped release; illustrates "don't let publicity drive schedule."
- **Time-based vs. feature-based releases cross-reference** (`foreshadowing`): the release-cadence
  mechanics are developed in Ch.7 (Packaging, Releasing, and Daily Development), not yet ingested.

## See also

- [[open-source-economics]] — why money buys credibility rather than control, the premise this
  whole playbook rests on.
- [[open-source-governance]] — how funding strains the benevolent-dictator model; where earned
  credibility converts to votes.
- [[open-source-contracting]] — the same "earn acceptance, don't buy it" logic applied to
  contracted work; where "foster in-house expertise" shapes contract structure.
- [[innersourcing]] — the "baby steps" precursor to genuine upstream participation, and why it
  isn't the real thing.
- [[hiring-open-source-developers]] — "hire for the long term" and the middle-management
  sensitivity that an influential hire's dual loyalty demands.
- [[code-review]] — public review is where a funded newcomer earns reputation (supervised
  engagement) and where corporate developers visibly behave as individuals.
- [[setting-the-tone]] — precedent-setting as the mechanism behind "make yourself the same size
  as everyone else."

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 5 "Organizations and Money" —
  "Hire for the Long Term," "Appear as Many, Not as One," "Be Open About Your Motivations,"
  "Money Can't Buy You Love" (printed pp. 71–74); "Open Source and the Organization" — adoption
  and code-reuse myths, "Foster Pools of Expertise in Multiple Places," "Establish Contact Early
  With Relevant Communities," "Don't Let Publicity Events Drive Project Schedule," "The Key Role
  of Middle Management" (printed pp. 87–89).
