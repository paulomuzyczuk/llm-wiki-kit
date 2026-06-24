---
title: Code Review
aliases: [peer-review, conspicuous-code-review]
date: 2026-06-23
last_updated: 2026-06-24
type: topic
topics: [code-review, software-collaboration, code-quality]
roles: [code-craftsperson, tech-lead]
source_tier: 1
project: null
source_count: 2
status: active
---

# Code Review

**Commit review** (often just *code review*) is "the practice of reviewing commits as
they come in, looking for bugs and possible improvements" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=37), p. 24).
Fogel's emphasis is deliberate: review **changes as they arrive**, not in-place code
already sitting in the tree.

## Why review changes, not static code

Two reasons ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=37), p. 24):

1. **It works better socially.** A reviewer is reacting to work you did *recently*, so
   you are "maximally interested in hearing what she has to say"; six months later you
   may neither care nor remember the change well.
2. **A change is a gateway to the rest of the code.** Reviewing a diff "often causes one
   to look at the surrounding code, at the affected callers and callees elsewhere, at
   related module interfaces" — so change-review pulls reviewers into the broader codebase
   anyway.

## What it accomplishes

Code review is "the most direct example of peer review in the open source world." Its
quality argument is blunt: "Every bug that ships in a piece of software got there by
being committed and not detected; therefore, the more eyes watch commits, the fewer bugs
will ship" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=37), p. 24).
It also serves an **indirect, motivational** purpose: reviewing someone's commit confirms
"that what they do matters," and "people do their best work when they know that others
will take the time to evaluate it" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=37), p. 24).

## Make it a public, standing practice

- **Reviews should be public.** Even two developers in the same room should send the
  review "to the appropriate online review forum instead," because seeing review happen
  reminds everyone "that review is an expected, regular activity" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=37), p. 24).
- **Start from the very first commit.** The defects easiest to catch in a diff are
  "security vulnerabilities, memory leaks, insufficient comments or API documentation,
  off-by-one errors, caller/callee discipline mismatches" — problems that need little
  surrounding context; larger structural issues become visible once "the memory of past
  diffs informs the review of present diffs" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=38), p. 25).
- **It is infrastructure-backed.** Effective change-by-change review needs **commit
  notifications** so every commit emits its log message and diff; the review itself
  happens on a mailing list or in a review tool such as Gerrit or "the GitHub 'pull
  request' interface" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=37), p. 24).

## Boundary

Code review does not "absolve programmers of the responsibility to review and test their
changes before committing; no one should depend on code review to catch things she ought
to have caught on her own" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=38), p. 25).
Review is the human-judgment layer; the mechanical pre-commit safety net is the job of
[[continuous-integration]]. Both ride on the branch/pull-request workflow of
[[version-control]].

## Empirical note — review in the CI/PR pipeline

In the pull-request development model, review is one stage of a pipeline whose throughput
is increasingly automated around it. Studying that pipeline empirically, Guo & Leitner
find that adopting [[continuous-integration]] does "not so much speed up handling
individual PRs, but rather [lets projects] manage to handle considerably more PRs per
release" ([Guo & Leitner 2019](../../raw-input/papers/ci-pull-request-delivery-time.pdf#page=19), p. 19),
and that the strongest predictor of how fast a merged PR ships is **when in the release
cycle it lands**, not CI adoption per se ([Guo & Leitner 2019](../../raw-input/papers/ci-pull-request-delivery-time.pdf#page=21), p. 21).
The practical implication for review: the bottleneck a growing project should watch is
*throughput of the whole change pipeline*, not the latency of any single review.

## Review is what makes commit access low-stakes

Standing commit review also changes what is at risk when a project grants commit access (see
[[committers]]). Fogel notes that because everything is under version control and reviewed, "the
penalty for adding a committer you shouldn't have added is not so much the problems it could
cause in the code (review would spot those quickly anyway), but that it might eventually force
the project to revoke the person's commit access"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=165), p. 152).
The practical consequence: review absorbs the *code* risk of a wrong grant, so committer
selection can be judged on judgement and conduct rather than treated as the last line of defense
for code quality. Review is the safety net; commit access is a social trust decision sitting on
top of it.

## Negative Space

- **Subversion / Greg Stein case study** (`illustrative-scaffolding`): the anecdote of
  one developer reviewing every commit until the habit spread illustrates *how a review
  culture takes hold*; the transferable claim (lead by example; review becomes expected
  behavior) is captured above, the narrative is not paged.
- **Commit-notification mechanics** (`too-granular`): the specific email/notification
  plumbing is a sub-detail of [[version-control]] tooling, noted there rather than here.

## See also

- [[version-control]] — the substrate code review runs on; the pull/merge request is the review hand-off point.
- [[continuous-integration]] — the mechanical complement to human review.
- [[committers]] — who is granted the authority to commit; review is what makes that grant a
  low-stakes, conduct-based decision rather than a code-quality gate.
- [[llm-assisted-maintenance]] — an additional, never-fatigued reviewer layered above human
  review and CI: audit the code not the PR description, with the human signing off.

## Sources

**Source entities:** [[producing-open-source-software-book]], [[ci-pull-request-delivery-time-paper]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 2 "Getting Started",
  §Practice Conspicuous Code Review (printed pp. 24–25).
- Yunfang Guo & Philipp Leitner, "Studying the Impact of CI on Pull Request Delivery Time
  in Open Source Projects," *PeerJ Computer Science* 5:e245 (2019), pp. 19, 21 — empirical
  note on review throughput.
