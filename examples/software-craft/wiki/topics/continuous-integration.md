---
title: Continuous Integration
aliases: [ci, ci-cd]
date: 2026-06-23
last_updated: 2026-06-23
type: topic
topics: [continuous-integration, version-control, code-quality]
roles: [code-craftsperson, tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Continuous Integration

**Continuous integration** (CI) is a practice originating in Agile and Extreme
Programming in which developers integrate work to the mainline several times a day, "each
integration… then verified by an automated build" ([Guo & Leitner 2019](../../raw-input/papers/ci-pull-request-delivery-time.pdf#page=4), p. 4).
In the pull-request development model, a CI system "automatically merges the PR into a
test branch and runs the tests to check if the PR breaks the build," after which "one or
more rounds of code review" follow ([Guo & Leitner 2019](../../raw-input/papers/ci-pull-request-delivery-time.pdf#page=4), p. 4).

CI is thus layered directly on [[version-control]] (it reacts to commits and branches) and
sits beside [[code-review]] as the **mechanical** half of pre-merge quality control — the
automated build is to machines what conspicuous review is to humans.

## The central promise — and what the evidence shows

The headline reason teams adopt CI is speed: that "new features or bug fixes can be
delivered more quickly" ([Guo & Leitner 2019](../../raw-input/papers/ci-pull-request-delivery-time.pdf#page=1), p. 1).
The empirical picture is more qualified. Studying open-source projects' pull-request
delivery time, Guo & Leitner find:

- The per-PR delivery-time impact of CI is "only minor," echoing the small effect sizes
  of the original study they replicate ([Guo & Leitner 2019](../../raw-input/papers/ci-pull-request-delivery-time.pdf#page=21), p. 21).
- The real shift is throughput, not latency: projects "do not so much speed up handling
  individual PRs, but rather manage to handle considerably more PRs per release after
  adopting CI" ([Guo & Leitner 2019](../../raw-input/papers/ci-pull-request-delivery-time.pdf#page=19), p. 19).
- The dominant predictor of delivery time — before and after CI — is **when in the release
  cycle a PR is merged**, leading the authors to conclude projects "need to increase the
  number of releases to speed up PR delivery times rather than adopt CI" ([Guo & Leitner 2019](../../raw-input/papers/ci-pull-request-delivery-time.pdf#page=21), p. 21).

The practical reading: CI earns its keep as a **quality and scalability** mechanism
(catching broken builds, absorbing more change per release), not primarily as a way to
make any single change ship faster.

## Negative Space

- **RDD / "come-in time" statistical methodology** (`supporting-argument`): the regression
  discontinuity design and the added variable are the paper's method for reaching the
  finding, not standalone concepts.
- **Travis-CI-only study scope** (`tool-specific/perishable`): the empirical scope (Travis
  CI projects) is a generalizability caveat noted by the authors, not a durable concept.

## See also

- [[version-control]] — the substrate CI reacts to (commits, branches, test merges).
- [[code-review]] — the human-judgment counterpart to CI's mechanical build check.

## Sources

**Source entities:** [[ci-pull-request-delivery-time-paper]]

- Yunfang Guo & Philipp Leitner, "Studying the Impact of CI on Pull Request Delivery Time
  in Open Source Projects — a Conceptual Replication," *PeerJ Computer Science* 5:e245
  (2019), CC BY 4.0.
