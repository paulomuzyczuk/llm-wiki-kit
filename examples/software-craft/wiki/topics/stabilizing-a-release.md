---
title: Stabilizing a Release
aliases: [release-stabilization, release-owner, change-voting, release-manager, time-based-releases]
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

# Stabilizing a Release

**Stabilization** is the process of getting a release branch into a releasable state:
deciding which changes will be in the release, which will not, and shaping the branch
content accordingly ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=137), p. 124).
All the grief is in the word "deciding."

## The core problem: a machine for saying "no"

The natural failure mode is the **last-minute feature rush** — as soon as a release
looks imminent, developers scramble to finish their changes so as not to miss the
boat, which is the exact opposite of what release time needs: more changes crammed in
late means less stable code and (usually) more new bugs ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=137), p. 124).

Hence the defining insight: **stabilizing a release is mostly about creating
mechanisms for saying "no."** The structural danger is asymmetric motivation — each
person wants their own favourite change admitted, so there are always plenty of
people motivated to *allow* changes and not enough motivated to *resist* them. The
open-source-specific trick is to find ways of saying "no" that don't produce too many
hurt feelings or disappointed developers, yet still keep deserving changes flowing in
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=138), p. 125).

Rough criteria for what may enter a stabilizing branch are widely agreed: fixes for
severe bugs (especially those without workarounds), documentation updates, error-
message fixes, and certain low-risk or non-core changes. But "no amount of
formalization can obviate the need for human judgement" — there will always be
borderline calls ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=138), p. 125).

### Time-based vs. feature-based releases

A project's release *cadence* is an orthogonal choice. **Time-based releases** ship on
an absolutely regular rhythm (e.g. every six months) no matter what is ready —
anything unfinished is simply left out, and developers who missed the deadline "wait
for the next train," which is easy to accept because the next train is known to be
coming. **Feature-based releases** ship when a target set of features is done. The
stabilization advice here applies to both, but time-based releases imply a *stricter*
gateway policy at all times — development work must stay isolated from the release
branch until truly ready, or unfinished code is hard to extricate at release time
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=137), p. 124).

## Two mechanisms at the extremes

Fogel describes two well-tested systems at opposite ends of a spectrum; projects
should feel free to invent arrangements in between.

### Dictatorship by release owner

The group agrees to let **one person be the release owner**, with final say over what
goes in. Discussion and argument are normal, but the group must grant that person
genuine authority to decide. The role needs someone with the **technical competence**
to understand every change *and* the **social standing and people skills** to steer
the discussions without causing hurt feelings ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=138), p. 125).
The characteristic move is "I don't think there's anything wrong with this change, but
we haven't had enough time to test it, so it shouldn't go into this release" — easier
to land when the owner has broad technical knowledge and can name a concrete
destabilization risk ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=138), p. 125).

Crucially, the **release owner need not be the project leader** (see
[[open-source-governance]] on benevolent dictators) — and sometimes it's good that
they aren't, since the skills differ and a separate owner provides a counterbalance.
If the two roles are split, the project leader should remember that overriding the
release owner undermines that authority, which alone is usually reason enough to let
the release owner win a disagreement ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=138), p. 125).

### Voting on changes

At the opposite extreme, developers **vote** on which changes to include. Because the
most important function of stabilization is to *exclude* changes, the voting system
must be designed so that getting a change *in* takes positive action by **multiple**
developers — more than a simple majority. Otherwise one self-vote with no opposition
would suffice, and a bad dynamic sets in: everyone votes for their own changes but is
reluctant to vote against others' for fear of retaliation ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=138), p. 125).
Requiring subgroups to cooperate both increases review and depersonalises rejection —
with enough people involved, "the discussion becomes about the change and less about
the individuals" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=138), p. 125).

The long-running **Subversion** system is the recommended balance: a change reaches
the release branch only with **at least three `+1` votes and none against**; a single
`-1` is a **veto** (see [[open-source-governance]] on vetoes). Every vote needs a
justification. Because release procedure is deliberately biased toward conservatism,
veto justifications are sometimes *procedural* rather than technical — a change might
be well-written and bug-free yet vetoed from a micro release simply for being too big
or subtly breaking the compatibility guidelines, and such vetoes are even allowed on a
reviewer's gut feeling that the change "needed more testing" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=138), p. 125); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=139), p. 126).

## Running a change-voting system

The physical mechanics should be **as lightweight as possible** — skip dedicated
e-voting software and just keep a plain-text `STATUS` (or `VOTES`) file in the release
branch. It lists each proposed change with its votes for and against and any notes;
any developer may propose a change, and proposing is separate from voting for ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=139), p. 126).
A change is referenced by its **commit/revision ID** (or, on a Git hosting platform, a
merge/pull-request ID) on the main branch — if it were already on the release branch
there'd be nothing to vote on ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=139), p. 126).

Those proposing or voting for a change are **responsible for making it apply cleanly**
to the release branch. If it conflicts, the entry points to a temporary branch holding
a conflict-adjusted version — but it still cites the *original* revisions as the
canonical handle, because they carry the original log messages and are easiest to
review. Naming the original revisions (rather than re-describing the change) upholds
the **singularity of information** principle (see [[version-control]]) ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=139), p. 126); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=140), p. 127).

## The release manager

Whatever the decision system, in practice one or two people end up driving the
release. This **release manager** role is distinct from a release owner — it carries
*no* final say over changes. Merging approved changes can be done by any developer
(spreading the burden is often better), but release managers track how many changes
are under consideration, approved, or likely to be approved; gently nag for reviews
and votes when important changes risk being left out for lack of attention; and often
merge approved batches themselves — though they're not obligated to do all the work
unless they've committed to it. When the release is ready to ship, they handle the
logistics: building the final packages, collecting digital signatures, uploading, and
making the public announcement (see [[open-source-publicity]]) ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=140), p. 127).

## Negative Space

- **Verbatim `STATUS`-file entry format** (`too-granular`): the exact field layout
  (`Justification:`, `Notes:`, `Votes:`) is one project's convention; the page keeps
  the principle that all evaluation info is accessible and voting is lightweight.
- **Subversion 1.1.4 `libsvn_fs_fs` example** (`illustrative-scaffolding`): a
  real-life entry used to demonstrate conflict-adjusted backports, not a concept.
- **Michlmayr release-management thesis/talk links** (`tool-specific/perishable`):
  external further-reading pointers, not synthesised content.

## See also

- [[release-branches]] — the branch this process operates on.
- [[release-numbering]] — what a stabilized release gets named, and the compatibility
  rules that drive procedural vetoes.
- [[open-source-governance]] — vetoes, benevolent dictators, and the consensus
  machinery the release-owner/voting split specialises.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 7 "Packaging,
  Releasing, and Daily Development", §Stabilizing a Release (incl. Time-Based vs
  Feature-Based Releases, Dictatorship by Release Owner, Voting on Changes, Managing
  Collaborative Release Stabilization, Release Manager), printed pp. 124–127.
