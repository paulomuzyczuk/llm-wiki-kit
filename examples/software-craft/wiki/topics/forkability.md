---
title: Forkability
aliases: [right-to-fork]
date: 2026-06-23
last_updated: 2026-06-24
type: topic
topics: [open-source-governance, open-source-culture]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Forkability

**Forkability** is "the ability of anyone to take a copy of the source code and use it to
start a competing project, known as a fork." Fogel calls it "the indispensable ingredient
that binds developers together on a free software project, and makes them willing to
compromise when necessary" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=72), p. 59).
It is guaranteed by license: "a key property of all open source licenses is that they do
not give one party more power than any other in deciding how the code can be changed or
used" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=72), p. 59).

## The possibility matters more than the act

The central paradox: "the possibility of forks is usually a much greater force in free
software projects than actual forks are. Actual forks are very rare." Because a fork is
"usually bad for everyone," the dynamic is self-limiting — "the more serious the threat of
a fork becomes, the more willing people are to compromise to avoid it"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=72), p. 59).
Forkability is thus a *latent* check: it shapes behavior precisely by rarely being
exercised.

## Why there are no true dictators

Forkability is why even a project's "benevolent dictator" is not a dictator in the ordinary
sense. Fogel's image: "imagine a ruler whose subjects could copy her entire territory at
any time and move to the copy to rule as they see fit" — such a ruler "would govern very
differently." Hence "even projects that are not formally organized as democracies are, in
practice, democracies when it comes to important decisions," captured in his chain
**"Replicability implies forkability, and forkability implies consensus"**
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=72), p. 59).
A leader's authority is real only because followers "choose to do so, in a situation where
they really do have freedom of choice."

A direct consequence: **control of the canonical repository is not the source of power**.
Commit-privilege control "affects only that copy of the project on that site"; prolonged
abuse "would simply lead to developers moving over to a different copy of the project"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=73), p. 60).
Forkability rests on the same property that makes decentralized [[version-control]]
authoritative-by-convention rather than by enforcement: anyone can hold a full copy.

## What forkability does *not* protect: attention and influence

Ch.8 sharpens the limit of the concept. Forkability guarantees free exit from the *code*, but
the things contributors actually compete for are not the code. "Attention, credibility, and
influence in the project very much are" a shared resource — and "they are by definition not
copyable, and therefore not forkable"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=149), p. 136).
You can fork the repository, but you cannot fork your standing in the community you leave. This
is why a fork is "usually bad for everyone" and why politics over influence persists *beneath*
the forkability ceiling — the subject of [[contributor-motivation]] and the people-management
craft in [[open-source-governance]]'s "politics is inevitable" framing.

## A ceiling on power, not a substitute for governance

Forkability sets an *upper limit* on how much power anyone can exert, but "doesn't mean
there aren't important differences in how projects are governed." Routing every dispute to
the last-resort question of "who might consider a fork" would "get tiresome very quickly,
and sap energy away from real work" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=72), p. 59).
The day-to-day decision machinery that lives *below* that ceiling is the subject of
[[open-source-governance]].

## Negative Space

- **Development forks vs. hard forks** (`too-granular` *here*): Ch. 4 flags the terminological
  distinction but defers it — the "fork" relevant to forkability is the hard fork. The full
  distinction is now developed in its own page, [[forks]] (Ch. 8 §Forks).
- **Forks as an event/how-to**: the mechanics and case histories of actually forking — handling,
  initiating, which-side-is-the-fork — are *not* this page's subject; they are ingested as the
  paired page [[forks]] (Ch. 8). Forkability is the latent right; [[forks]] is its exercise.
- **Bus factor / survivability metric** (`too-granular`): a named gauge of survivability
  folded into [[open-source-governance]]'s framing, not a standalone concept.

## See also

- [[forks]] — the paired concept: what happens when the latent right to fork is actually
  exercised (development vs. hard forks, handling and initiating one).
- [[open-source-governance]] — the decision-making structures forkability bounds from
  above.
- [[version-control]] — the replicability (every developer holds a full repository) that
  makes forkability mechanically possible.
- [[open-source-culture]] — the "culture by choice," whose free exit forkability formalizes.
- [[contributor-motivation]] — the attention, credibility, and influence that, unlike code,
  cannot be forked.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 4 "Social and Political
  Infrastructure", §Forkability (printed pp. 59–60); Ch. 8 "Managing Participants" — chapter
  introduction on the non-forkability of attention, credibility, and influence (printed
  p. 136).
