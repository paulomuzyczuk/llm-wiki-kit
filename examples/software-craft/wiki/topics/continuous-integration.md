---
title: Continuous Integration
aliases: [ci, ci-cd]
date: 2026-06-23
last_updated: 2026-06-24
type: topic
topics: [continuous-integration, version-control, code-quality]
roles: [code-craftsperson, tech-lead]
source_tier: 1
project: null
source_count: 2
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

## Why it matters especially for open source (Fogel)

Fogel's *Producing Open Source Software* frames automated testing-on-every-change as one of
the highest-value applications of [[the-automation-ratio]], and gives the human reason CI
matters disproportionately in open source: automated testing "allows developers to feel
comfortable changing code in areas they are unfamiliar with, and thus encourages exploratory
development," and "makes people much more relaxed about refactoring large swaths of code"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=154), p. 141).
In a project of strangers, that confidence to touch unfamiliar code is what keeps
contribution flowing.

Two operational customs reinforce it. Almost all projects have a "Don't break the build!"
rule, with a corollary for test suites: "don't commit any change that causes tests to fail" —
failures "easiest to spot if there are automatic nightly or per-change runs of the entire test
suite, with the results posted publicly." And on tooling choice, Fogel's default is
conformity: "Unless you have a reason to do something different, your project should just use
one of the standard CI systems that other projects on that hosting site use," so that arriving
contributors are "already familiar with the CI setup"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=155), p. 142).

## Negative Space

- **RDD / "come-in time" statistical methodology** (`supporting-argument`): the regression
  discontinuity design and the added variable are the paper's method for reaching the
  finding, not standalone concepts.
- **Travis-CI-only study scope** (`tool-specific/perishable`): the empirical scope (Travis
  CI projects) is a generalizability caveat noted by the authors, not a durable concept.

## See also

- [[version-control]] — the substrate CI reacts to (commits, branches, test merges).
- [[code-review]] — the human-judgment counterpart to CI's mechanical build check.
- [[the-automation-ratio]] — the broader principle (automate what machines can do) that
  automated testing-on-commit instantiates.

## Sources

**Source entities:** [[ci-pull-request-delivery-time-paper]], [[producing-open-source-software-book]]

- Yunfang Guo & Philipp Leitner, "Studying the Impact of CI on Pull Request Delivery Time
  in Open Source Projects — a Conceptual Replication," *PeerJ Computer Science* 5:e245
  (2019), CC BY 4.0.
- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 8 "Managing Participants" —
  §Automated testing ("Don't break the build", use the standard CI of your hosting site;
  printed pp. 141–142).
