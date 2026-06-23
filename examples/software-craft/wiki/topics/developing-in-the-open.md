---
title: Developing in the Open
aliases: [open-from-day-one, develop-in-the-open, opening-a-closed-project, transparency-by-default]
date: 2026-06-23
last_updated: 2026-06-23
type: topic
topics: [software-collaboration, open-source-culture]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Developing in the Open

"Start your project out in the open from the very first day. The longer a project is run in
a closed source manner, the harder it is to open source later"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=38), p. 25).
This is the artifact-and-infrastructure counterpart to the discussion norm in
[[setting-the-tone]]: not just *talk* in public, but do the whole of development in public
from Day One.

## Openness is about artifacts, not obligations

A common objection conflates being open source with being on the hook for community
management — the belief that "'open source' means 'strangers distracting us with
questions.'" That is "optional — it's something you might do down the road, if and when it
makes sense for your project. It's under your control"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=38), p. 25).
The principle that resolves the tension is Fogel's: **"You open source your code, not your
time."** Code "is infinitely replicable; your time is not, and you may protect it however
you need to. You get to determine the point at which engaging with outside users and
developers makes sense"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=39), p. 26).

Concretely, **"in the open"** means these are publicly accessible in standard formats from
day one: "the code repository, bug tracker, design documents, user documentation, wiki (if
any), and developer discussion forums," the code under an open source license, and the
team's "day-to-day work … in the publicly visible area." It does **not** require letting
strangers commit to your repository, accepting bug reports from anyone, responding to every
report or question, or reviewing every patch — "you're free to choose your own QA process"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=39), p. 26).

## Why closed-then-open is costly: incompatible choices accumulate

Fogel identifies a single underlying cause for the difficulty of opening up late: "At each
step in a project, programmers face a choice: to do that step in a manner compatible with a
hypothetical future open-sourcing, or … incompatible." Every incompatible choice makes the
project "just a little bit harder to open source" — and developers "can't help choosing the
latter occasionally," because the present-day pressures of shipping always outweigh a
hypothetical future event. In Ward Cunningham's phrase, they "incur 'technical debt' … with
the intention of paying back that debt later"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=38), p. 25).

When it is finally time to open up, the accumulated debt surfaces as concrete blockers —
secrets and customer-specific configuration checked into history, confidential sample data,
embarrassing code comments, internal correspondence, license-incompatible dependencies,
documentation in unpublishable formats, non-portable build dependencies, and known
modularity violations. The deeper cost is not the cleanup labor but the **extra
decision-making**: e.g., whether to scrub the entire version history or release only a
**"top-skim"** (a fresh history started from the sanitized current revision). "Neither
method is wrong or right — and that's the problem": each accumulated artifact "is one more
discussion to have and one more decision to make," and the resulting thrashing "is part of
the cost"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=39), p. 26).

## Waiting creates one large exposure event

The second cost of opening a developed codebase is that "it creates a needlessly large
exposure event." Whatever issues exist — corner-cutting, security vulnerabilities — "they
are all exposed to public scrutiny at once," turning the open-sourcing into "an opportunity
for the technical blogosphere to pounce"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=39), p. 26).

Developing in the open inverts this. Changes "come in one at a time, so problems are handled
as they come up (and are often caught sooner, since there are more eyeballs on the code)" —
the same continuous-review dynamic that motivates [[code-review]]. Because exposure happens
"at a low, continuous rate," observers forgive the occasional flawed checkin: "Everyone's
been there … these tradeoffs are inevitable." As long as technical debt is recorded in
FIXME comments and bug reports and security issues are handled promptly, "it's fine" —
whereas the same issues surfacing "suddenly all at once" invite unsympathetic pile-on
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=39), p. 26).
Fogel notes the exposure-event concern "apply[ies] even more strongly to government software
projects."

The reassuring conclusion: these are "all unforced errors. A project incurs little extra
cost by avoiding them in the simplest way possible: by running in the open from Day One"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=39), p. 26).

## Opening a formerly closed project

If it is "too late for that" and you must open an existing project — "perhaps with active
developers accustomed to working in a closed-source environment" — predictable issues arise,
and preparing for them "can save a lot of time and trouble." They split into two kinds
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=40), p. 27):

- **Mechanical issues**, for which the "in the open" list above "can serve as a checklist":
  replace proprietary libraries with open source equivalents; release a top-skim version
  when version history holds confidential content; and so on.
- **Social and managerial issues**, "often more significant in the long run than the mere
  mechanical concerns."

The central social risk is a **siege mentality** among the existing team. Seen from their
side, code formerly reviewed only by colleagues who "knew the software more or less equally
well" is now exposed "to the scrutiny of random strangers, who will form judgements based
only on the code," ask questions that expose documentation gaps ("this is inevitable"), and
point out flaws "in front of his colleagues." Because peer review reliably finds bugs in any
program "above a certain size" (see [[code-review]]) while newcomers "won't be subject to
much peer review at first" — they can't contribute code until they know the project — "it
may feel like all the criticism is incoming, never outgoing"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=40), p. 27).

Prevention is mostly expectation-management and modeling
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=40), p. 27):

- **Warn everyone in advance**, "explain it, tell them that the initial discomfort is
  perfectly normal, and reassure them that it's going to get better" — some of this
  privately before opening, some as public reminders that this is a new way of working.
- **Lead by example.** Telling developers to answer more newbie questions "isn't going to
  help"; "the way to get them to participate is to participate yourself." Answer questions
  on the public lists, and when you lack the expertise, "visibly hand it off to a developer
  who does — and watch to make sure she follows up."
- **Pull lapses back into the open.** Longtime developers will "lapse into private
  discussions, since that's what they're used to"; stay subscribed to the internal lists so
  you can move such threads to the public ones "right away" — the
  [[setting-the-tone|avoid-private-discussions]] norm applied to a team in transition.

Mixing the newly-arriving unpaid developers with the existing paid team is itself a topic
deferred to Ch.5 (Organizations and Money).

## Negative Space

- **The full list of artifacts found when opening late** (`illustrative-scaffolding`):
  checked-in passwords, confidential sample data, overly-honest code comments, internal
  correspondence, etc. — enumerated to make the "incompatible choices accumulate" claim
  vivid; the claim is captured, the catalogue is not paged.
- **Technical-debt definition / Cunningham attribution** (`too-granular`): named to label
  the accumulation mechanism; the concept belongs to general engineering, not this page.
- **Top-skim mechanics** (`tool-specific/perishable`): how to rewrite or restart version
  history is a VCS operation; captured as a *decision* (scrub-all vs. top-skim) here, with
  mechanics belonging to [[version-control]].
- **Government-project emphasis** (`foreshadowing`): "Being Open Source From Day One is
  Especially Important for Government Projects" is cross-referenced to Ch.5/Ch.3 material not
  yet ingested — noted, not developed.

## See also

- [[setting-the-tone]] — the discussion-level transparency norm and the broader culture this
  artifact-level openness sits inside.
- [[code-review]] — the continuous-low-rate-exposure benefit and the peer-review pressure
  the siege-mentality risk turns on.
- [[version-control]] — where top-skim vs. full-history-scrub is actually executed; the
  public repository is item one of "in the open."
- [[launching-an-open-source-project]] — the launch checklist whose artifacts this page says
  must be public from Day One.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 2 "Getting Started" —
  "Be Open From Day One," "Waiting Just Creates an Exposure Event," and "Opening a Formerly
  Closed Project" (printed pp. 25–28).
