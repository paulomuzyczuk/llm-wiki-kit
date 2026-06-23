---
title: Corporate Open-Source Participation
aliases: [corporate-involvement, being-a-good-corporate-citizen, appear-as-many-not-one, money-cant-buy-love]
date: 2026-06-23
last_updated: 2026-06-23
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

## Negative Space

- **CollabNet / Mike Pilato / Subversion specifics** (`case-study-specifics`): the dates,
  names, and timeline are illustrative; the precedent-setting principle is captured.
- **Danese Cooper / Sun / Tomcat footnote** (`illustrative-scaffolding`): a parallel
  commit-access story cited in a footnote, not a separate concept.
- **"The Smaller the Topic, the Longer the Debate" cross-reference** (`foreshadowing`):
  pointed at people "who like to object just to stay in shape"; the bikeshedding concept is
  developed in Ch.6 (Communications), not yet ingested.

## See also

- [[open-source-economics]] — why money buys credibility rather than control, the premise this
  whole playbook rests on.
- [[open-source-governance]] — how funding strains the benevolent-dictator model; where earned
  credibility converts to votes.
- [[open-source-contracting]] — the same "earn acceptance, don't buy it" logic applied to
  contracted work.
- [[code-review]] — public review is where a funded newcomer earns reputation (supervised
  engagement) and where corporate developers visibly behave as individuals.
- [[setting-the-tone]] — precedent-setting as the mechanism behind "make yourself the same size
  as everyone else."

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 5 "Organizations and Money" —
  "Hire for the Long Term," "Appear as Many, Not as One," "Be Open About Your Motivations,"
  "Money Can't Buy You Love" (printed pp. 71–74).
