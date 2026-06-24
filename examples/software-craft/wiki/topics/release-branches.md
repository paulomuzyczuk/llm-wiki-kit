---
title: Release Branches
aliases: [release-branch, branching-for-release, maintenance-branch]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [release-engineering, version-control]
roles: [code-craftsperson, tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Release Branches

From a developer's point of view a free-software project is in a state of
**continuous release**: developers run the latest code, update daily or more often,
and expect any change they commit to reach every other developer within a day or two
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=136), p. 123).
So how does such a project cut a *formal* release? Not by snapshotting the main tree
at a moment in time — and a **release branch** is the structure that solves the
problem.

## Why full-tree snapshots fail

Releasing by snapshotting the whole development tree breaks in two ways:

- **There may be no clean moment.** New features lie around half-finished; a
  controversial bug-fix may be under debate exactly when the snapshot is due. You
  cannot just wait for the debate to end, because another unrelated debate can start
  meanwhile — the wait "is not guaranteed to halt" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=136), p. 123).
- **It freezes development even when the tree is releasable.** Between `3.5.0` and
  `3.5.1` (mostly bug-fixes), compatibility rules forbid adding features — so forcing
  everyone to work only on the release tree leaves feature-developers choosing
  between sitting idle and working on things they don't care about, which makes them
  "irate" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=136), p. 123).

This is the parallelize-independent-tasks principle from the chapter's opening: open
source can't afford a master schedule where some activities exclude others, because
the result is developers sitting idle — and "a bored developer is likely to soon be
an ex-developer" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=132), p. 119).

## The release branch as isolation

The solution is to **always use a release branch** — a branch in the version-control
system (see [[version-control]]) on which the code destined for the release is
isolated from mainline development ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=136), p. 123).
The concept is not original to free software — proprietary shops use release branches
too — but in closed-source environments they are sometimes treated as a dispensable
luxury, abandoned under deadline pressure so the team can scramble to stabilize the
main tree ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=136), p. 123).

In open source the release branch is **close to a necessity**, for three reasons:

- Developers expect to merge finished work to the common main branch immediately; a
  main branch artificially **frozen** to release-related changes only "slows overall
  development momentum" and frustrates people whose work is delayed from the shared
  arena ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=136), p. 123).
- The **release itself suffers** if the few people working on it hurry just so
  everyone else can get back to normal on main ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=136), p. 123).
- A release branch **facilitates developer autonomy**: contributors can give some
  attention to the release on their own schedule, the same way they choose to engage
  with any feature or bugfix branch ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=136), p. 123).

## Mechanics

The exact commands depend on the version-control system, but the concepts are the
same everywhere:

- The release branch **sprouts from main**, where developers' changes are first
  integrated unfettered by release constraints ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=137), p. 124).
- **Name the branch for the minor line, not a point release** — `1.0.x` (with a
  literal `x`) rather than `1.0.0` — so the same branch serves as the source for
  every micro release in that line ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=137), p. 124).
- When the branch is stabilized (see [[stabilizing-a-release]]), **tag a snapshot**
  (e.g. `1.0.0`). The tag records the exact source state of that release — useful
  when a developer needs to compare against an old version while chasing a bug. The
  next micro release is prepared on the same `1.0.x` branch and tagged `1.0.1`, and
  so on ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=137), p. 124).
- When it's time for `1.1.x`, **make a new branch from main.** Maintenance then
  continues in parallel along both `1.0.x` and `1.1.x`, with releases cut
  independently from each line while new development happens on main or in
  short-lived feature branches ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=137), p. 124).

It is not unusual to publish **near-simultaneous releases from two lines**: a `1.0.6`
for conservative administrators not ready to jump to `1.1`, alongside `1.1` itself
for more adventurous users who want the latest features at the risk of greater
instability ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=137), p. 124).

## The point of it

This is not the only valid branch strategy, but whatever a project adopts, the
purpose is constant: **isolate release work from the fluctuations of daily
development, and give the project a physical entity — the release branch — around
which to organize its release process** ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=137), p. 124).

## Negative Space

- **VCS-specific branch/tag commands** (`too-granular`): how to create and manage
  branches in a particular system is explicitly out of the book's scope; the page
  keeps the system-independent semantics.
- **`3.5.0`/`1.0.x`/Subversion line examples** (`illustrative-scaffolding`): concrete
  version strings used to explain the mechanics, not concepts.

## See also

- [[version-control]] — branches as the underlying mechanism; the release branch is a
  specialised, long-lived application of it.
- [[stabilizing-a-release]] — what happens *on* the release branch to make it shippable.
- [[release-numbering]] — the numbering that names the tags cut from each branch.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 7 "Packaging,
  Releasing, and Daily Development", §Release Branches (incl. Mechanics of Release
  Branches) and chapter opening on parallelizing tasks, printed pp. 119–124.
