---
title: InnerSourcing
aliases: [innersource, inner-source]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-participation, open-source-culture]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# InnerSourcing

**InnerSource** (or **innersourcing**) is "using standard open source development practices
only within the boundaries of an organization." A company might move all its projects to
private repositories and declare that, internally, "any engineer can report bugs and contribute
pull requests to any project anywhere else in the company." It "often includes serious efforts
at internal cultural change" — managers encouraging developers to speak their mind on technical
and process issues, developers given more latitude to choose what they work on
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=102), p. 89).

The concept matters here as the **boundary case** of open-source method: it keeps the tools and
the collaboration habits while removing the one thing — [[forkability]] — that makes those
habits load-bearing. That makes it both genuinely useful and routinely overclaimed.

## What it buys

Drawing on interviews Fogel conducted in early 2016 with open-source specialists at medium- and
large-sized technology companies, the reported benefits were "pretty consistent from company to
company": innersourcing "really can make a positive difference, in several ways, but it's also
definitely not the same as true open source"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=102), p. 89).

- **Lower context-switching for staff who also work upstream.** For a company whose engineers
  already participate in external open-source projects — and must therefore use "typical open
  source collaboration tools and adhere to open source standards" — moving internal
  infrastructure in the same direction means "less context-switching overhead for existing
  staff, an easier onboarding process for new hires, and often improved technical compatibility
  between internal and external projects"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=103), p. 90).
- **Morale, expertise spread, efficiency.** When paired with "a real commitment to reduce
  managerial and organizational barriers" to cross-company participation, innersourcing "can
  improve morale, help spread expertise around the company and make software development more
  efficient"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=103), p. 90).
- **A first step toward real participation.** It is "often used as the first 'baby steps' toward
  genuine corporate participation in open source projects" — an intermediate stage for a
  traditionally closed company "still figuring out how to do open source participation"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=103), p. 90).

## Why it is not open source

The interviewed managers reported that innersourced projects "don't have the provocative,
uncontrolled energy of truly open source projects, because all the actors in innersourcing are,
ultimately, embedded in the same hierarchical authority structure." Fogel's diagnosis is
structural, not motivational
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=103), p. 90):

- **Open-source dynamics require "the potential for totally permissionless modification"** — the
  state where "you don't have to worry what someone else might think of a fork." When software
  "only circulates within a given management hierarchy, then that potential for permissionless
  collaboration vanishes — and with it, the potential for true open source behavior vanishes
  too." The governing permission structure "is not just a matter of the code's license: it's
  also about power: whom you report to, what others in the hierarchy might think about your
  changes"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=103), p. 90).
- **An "external supply of freedom" is the missing ingredient.** "In the long run, the dynamics
  of open source collaboration require an external supply of freedom. There must always be people
  who could, in principle, fork or do whatever they want without worrying about consequences to
  the original authors' organization. When that external freedom is removed, everything changes"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=103), p. 90).
  This is the same latent check [[forkability]] describes — innersource simply deletes it.
- **It fails the "portable résumé" test.** An employee "can't take the code with her, and her
  work will not be publicly visible." If she leaves, "she will be alienated from the fruits of
  her work, which means that her motivation to personally invest is reduced" — the inverse of the
  hiring advantage in [[hiring-open-source-developers]]
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=103), p. 90).

The practical upshot: innersourcing "can be very beneficial on its own terms," but the two
"shouldn't be conflated." Don't "imagine that innersourcing is somehow 'just like open source,
but inside our company'. They're two different things"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=103), p. 90).

## Negative Space

- **"Move everything to GitHub private repos" example** (`illustrative-scaffolding`): the
  concrete tooling picture is used to make the definition vivid; the durable point is "open
  source practices minus the public boundary."
- **InnerSourceCommons / Danese Cooper resources footnote** (`tool-specific/perishable`): a
  pointer to organized InnerSource resources, not a concept.
- **Interview provenance — James Vasile, O'Reilly introductions** (`illustrative-scaffolding`):
  sourcing detail for the 2016 interviews, not part of the concept.

## See also

- [[forkability]] — the "external supply of freedom" innersource removes; the exact reason
  innersource is not open source.
- [[corporate-open-source-participation]] — innersource as the "baby steps" precursor to genuine
  upstream participation.
- [[open-source-culture]] — the "culture by choice" whose permissionless exit innersource cannot
  reproduce inside a hierarchy.
- [[hiring-open-source-developers]] — the "portable résumé" advantage innersource forfeits.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 5 "Organizations and Money" —
  "InnerSourcing" (printed pp. 89–90).
