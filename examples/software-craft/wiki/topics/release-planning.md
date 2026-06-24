---
title: Release Planning
aliases: [planning-releases, release-cadence, decoupling-contents-from-dates, release-frequency]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [release-engineering]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Release Planning

Release planning is where open-source projects have historically diverged most sharply
from proprietary ones — and the divergence is rooted in **what each kind of project is
optimizing for** ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=147), p. 134).

## The structural difference: relationships over deadlines

Proprietary projects usually have **firmer deadlines** — a customer was promised an
upgrade by a date, a release must align with a marketing push, or investors need to see
results before funding more. Free-software projects instead prioritize **maintaining a
cooperative working atmosphere among many parties**, some of whom may be business
competitors with one another; preserving that working relationship is more important
than any single party's deadline ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=147), p. 134).

The tension is not hypothetical: many open-source projects are **corporately funded** and
therefore feel deadline-conscious management. That pressure is often a good thing, but it
pits the developers who care about a specific release date against everyone else, who may
have features they want finished or testing they want done first. There is **no general
solution except discussion and compromise** — but the friction can be *minimized*
structurally ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=147), p. 134).

## The core technique: decouple contents from dates

The central move is to **separate the question of what a release contains from the
question of when it ships**. Steer discussion toward *which* releases the project will
make in the near-to-medium term and *what features* go in each — **without, at first,
talking about dates** (beyond rough guesses with wide error margins) ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=147), p. 134).

Nailing down feature sets early pays off twice:

- It **reduces the complexity** of any individual release discussion and improves
  predictability.
- It creates an **inertial bias against scope creep**: once a release's contents are
  reasonably defined, the **onus is on whoever proposes to expand it** to justify the
  addition — even though the date may not be set yet. Once contents are settled, the
  date conversation becomes much easier ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=147), p. 134).

This pairs with the cadence choice in [[stabilizing-a-release]] (time-based vs.
feature-based releases): defining contents first is what makes a feature-based scheme
tractable, and time-based releases sidestep the date fight entirely.

## An alternative valve: separate interim releases

When corporate timing and community timing genuinely cannot be reconciled, a company can
**make its own separate interim releases for its customers**. As long as these are
**clearly distinguished from the project's official releases**, they can themselves be
public and open source and do the project no harm (this is the same logic as the paid
interim releases discussed under [[open-source-economics]]). The cost is real, though:
maintaining a separate release line means **overhead in tracking and porting changes back
and forth**, so it only works when the company can dedicate enough people to release
management to absorb it ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=147), p. 134).

## Govern the plan without controlling it

Two attitudes keep planning collaborative rather than coercive ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=147), p. 134):

- **Never present a suggestion or decision as written in stone.** When assigning a ticket
  to a future release, invite discussion and dissent in the comments and be genuinely
  open to persuasion. **Never exercise control merely for the sake of it** — the more
  deeply others feel they can participate in planning (this is the
  share-management-tasks principle developed in Ch.8), the more readily they will share
  *your* priorities on the things that truly matter to you ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=147), p. 134).
- **Release fairly often.** Even outside a formal time-based scheme, frequent releases
  lower the stakes of any one of them. When releases are far apart, each one's importance
  is magnified and developers are "crushed" when their code misses the window, knowing
  how long the next chance is. A gap of roughly **three to six months** is usually about
  right, though maintenance lines may cut micro releases faster when there is demand
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=148), p. 135).

## Negative Space

- **The `1.1.3`-style ticket-assignment example** (`illustrative-scaffolding`): worked
  scenarios illustrating decoupling and dissent-invitation, not concepts.
- **Share-management-tasks treatment** (`foreshadowing` → Ch.8): release planning
  references participatory delegation, but the concept itself is developed in Ch.8
  (batch 14); left as a forward pointer here.

## See also

- [[stabilizing-a-release]] — time-based vs. feature-based cadence, the choice this
  planning discipline feeds into.
- [[corporate-open-source-participation]] — the deadline-conscious corporate sponsor
  whose timing pressure release planning has to absorb.
- [[open-source-economics]] — the paid / interim-release model the "separate interim
  releases" valve draws on.
- [[maintaining-multiple-release-lines]] — frequent releases and maintenance micro
  releases as the other tension-lowering lever.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 7 "Packaging,
  Releasing, and Daily Development", §Planning Releases, printed pp. 134–135.
