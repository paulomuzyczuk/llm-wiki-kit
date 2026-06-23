---
title: Version Control
aliases: [vcs, source-control, revision-control]
date: 2026-06-23
last_updated: 2026-06-23
type: topic
topics: [version-control, project-infrastructure, software-collaboration]
roles: [code-craftsperson, tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Version Control

A **version control system** (VCS, or revision control system) is "a combination of
technologies and practices for tracking and controlling changes to a project's files,
in particular to source code, documentation, and web pages" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=55), p. 42).
Its core is **change management**: identifying each discrete change, annotating it with
metadata (date, author), and replaying those facts to whoever asks. Framed this way, a
VCS is fundamentally **a communications mechanism in which a change is the basic unit of
information** ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=55), p. 42).

## Why it is load-bearing

Version control is near-universal because it "helps with virtually every aspect of
running a project: inter-developer communications, release management, bug management,
code stability and experimental development efforts, and attribution and authorization
of changes" — it is "a central coordinating force" across all of them ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=55), p. 42).
The social expectation is now strong enough that a project not under version control
"probably will not [be taken] seriously" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=55), p. 42).

## Centralized vs. decentralized

The pivotal distinction is **when and where commits are published**. In *centralized*
systems (e.g. Subversion) a commit is "automatically and unavoidably pushed up to a
predetermined central repository"; in *decentralized* systems (e.g. Git, Mercurial) "the
developer chooses when and where to push commits" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=56), p. 43).
Decentralized systems give each developer their own full repository, so which repository
is "authoritative" becomes a matter of **social convention rather than technical
enforcement** ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=56), p. 43).
Decentralized version control is the modern default for open source, which benefits from
the peer-to-peer relationship between developers' repositories ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=56), p. 43).

For a project with no prior opinion, Fogel's flat recommendation is **Git, hosted on
GitHub** — "the de facto standard," whose familiarity itself "sends the signal that your
project is ready for participants" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=58), p. 45).
Choosing something most developers won't recognize carries a real adoption cost: a
smaller support community and an unfamiliar workflow ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=58), p. 45).

## Operating practices

- **Version everything editable, in one place.** Source, web pages, docs, FAQ, design
  notes — "any piece of information that could change" — belong under version control
  together, so contributors "only have to learn one mechanism for submitting changes"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=59), p. 46).
  The exception is **generated files**: version the templates, not their output, or
  people forget to regenerate and "the resulting inconsistencies will cause endless
  confusion" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=59), p. 46).
- **Browsability.** The repository should be viewable on the web — current files, past
  revisions, diffs, log messages — because it is "a lightweight portal to project data,"
  and **canonical URLs** for a given commit or the latest revision make technical
  discussion "completely unambiguous" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=59), p. 46); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=60), p. 47).
- **Use branches to avoid bottlenecks.** Branches "turn a scarce resource — working room
  in the project's code — into an abundant one," letting a developer try a change in
  isolation and then invite review (in GitHub terms, a *pull request*) before merging
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=60), p. 47).
  But a branch is "a slight drain on the community's attention," so most branches "should
  be to merge their changes back into the main line and disappear, as soon as possible"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=60), p. 47).
- **Singularity of information — never commit the same change twice.** A change "should
  enter the version control system exactly once"; to apply it elsewhere, *merge* it from
  its original entry point rather than re-committing a textually identical change, which
  "would make accurate bookkeeping and release management much harder" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=60), p. 47).

## Relationship to review and integration

Version control is the substrate the project's collaboration loop runs on. The
branch-and-merge workflow makes change **reviewable before it lands** — the pull/merge
request is literally "an invitation" to examine a branch before merging it ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=60), p. 47) —
which is the hand-off point to [[code-review]] and, downstream, to
[[continuous-integration]].

## Negative Space

- **VCS vocabulary glossary** (`too-granular`): the source's per-term definitions
  (`commit`, `push`, `pull`/`fetch`, `repository`, `clone`/`checkout`, `working copy`,
  `revision`/`changeset`, `diff`, `tag`, `branch`, `merge`, `conflict`, `revert`, `lock`)
  are reference vocabulary, captured as the bullets above rather than as separate pages.
- **lock-modify-unlock vs. copy-modify-merge models** (`subsumed-by`): the concurrency
  models are a sub-distinction of centralized-vs-decentralized; the operative takeaway
  (copy-modify-merge suits open source) is folded into that section.
- **Specific hosting/forge tool comparisons** (`tool-specific/perishable`): named
  services and forge systems are perishable recommendations, not durable concepts.

## See also

- [[code-review]] — the human-judgment layer that rides on the branch/pull-request workflow.
- [[continuous-integration]] — the mechanical pre-commit/pre-merge safety net layered on version control.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 3 "Technical
  Infrastructure", §Version Control (printed pp. 42–47).
