---
title: Atomic Commits
aliases: [single-logical-change, one-change-per-commit, commit-hygiene, semantically-unified-commit]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [version-control]
roles: [code-craftsperson, tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Atomic Commits

**Make each commit a single logical change, and never mix unrelated changes in the same
commit.** When a change is too big or too disruptive for one commit, break it across N
commits where **each commit is a well-partitioned subset of the whole and includes
nothing unrelated to it** ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=146), p. 133).
This is a [[version-control]] discipline that is *generally* advisable; maintaining
parallel releases (see [[maintaining-multiple-release-lines]]) is what turns it from
"recommended" into "practically mandatory."

## Why parallel maintenance makes it mandatory

A tangled commit becomes a liability the moment someone needs to **port just one of its
changes to a maintenance branch**. Consider a commit that bundles four unrelated things:
a fix for issue #1729, an unrelated removal of obsolete comments, a separate error-check
fix, and some website typo tweaks ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=146), p. 133).

When a maintainer needs only the error-check fix on an upcoming maintenance release, she
**cannot cleanly grab it via the VCS merge functionality**, because the system was told
all four changes are one logical unit. The damage shows up even before any merge: merely
**listing the change for voting** (see [[stabilizing-a-release]]) becomes a chore —
instead of citing one revision number, the proposer has to carve out a special branch
just to isolate the relevant slice, work everyone else then has to wade through ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=146), p. 133).
That tangled commit should have been **four separate commits**, of which only the
error-check fix would be the one proposed for the maintenance branch ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=147), p. 134).

This is the practical face of [[version-control]]'s "a change is the basic unit of
information": if the unit is impure, every downstream operation that addresses changes
by their identity — cherry-pick, merge, propose-for-vote — inherits the impurity.

## The benefits hold even without release branches

Release stabilization is not the only reason for the discipline. A **semantically
unified commit is easier to review** (see [[code-review]]) because a reviewer can hold
one intention in mind, and **easier to revert** if it turns out to be wrong — in some
version-control systems a revert is itself just a special kind of merge, so the same
clean-boundary requirement applies ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=147), p. 134).
The summary verdict: **a little up-front discipline on each developer's part saves the
project a lot of headache later** ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=147), p. 134).

## Negative Space

- **The verbatim example commit message and its file/function annotations**
  (`illustrative-scaffolding`): the `ui/repl.py` / `indexer/index.py` / `BuildDir`
  detail demonstrates a tangled commit; the page keeps the four-way decomposition
  principle, not the sample diff.
- **VCS-specific revert-as-merge mechanics** (`tool-specific/perishable`): whether a
  given system implements revert as a merge is a per-tool detail; the durable point is
  that unified commits are cheaper to undo.

## See also

- [[version-control]] — the substrate this discipline keeps clean; "a change is the
  basic unit of information" is the principle atomic commits protect.
- [[stabilizing-a-release]] — change-voting and porting both address commits by
  identity, which only works if each commit is one logical change.
- [[maintaining-multiple-release-lines]] — the parallel-maintenance context that makes
  the discipline near-mandatory.
- [[code-review]] — unified commits are the ones a reviewer can actually reason about.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 7 "Packaging,
  Releasing, and Daily Development", §Releases and Daily Development, printed pp. 133–134.
