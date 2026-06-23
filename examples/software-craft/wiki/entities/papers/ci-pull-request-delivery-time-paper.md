---
title: Studying the Impact of CI on Pull Request Delivery Time in Open Source Projects — a Conceptual Replication
aliases: []
date: 2026-06-23
last_updated: 2026-06-23
type: paper
edition: null
doi: 10.7717/peerj-cs.245
topics: [continuous-integration, code-review]
project: null
source_count: 0
status: active
---

# Studying the Impact of CI on Pull Request Delivery Time in Open Source Projects

**Authors:** Yunfang Guo, Philipp Leitner (Chalmers | University of Gothenburg)
**Venue:** *PeerJ Computer Science* 5:e245 (2019)
**DOI:** [10.7717/peerj-cs.245](https://doi.org/10.7717/peerj-cs.245)
**License:** Creative Commons Attribution 4.0 (CC BY 4.0) · Open Access
**Source:** [ci-pull-request-delivery-time.pdf](../../../raw-input/papers/ci-pull-request-delivery-time.pdf)

## What it is

A conceptual replication of Bernardo, da Costa & Kulesza (2018), testing whether open
source projects deliver merged pull requests faster after adopting continuous
integration. It re-analyses the original data with a regression discontinuity design
(RDD), adds a "come-in time" variable, and introduces a **control group of projects that
never adopted CI** — the methodological gap that motivated the replication ([Guo & Leitner 2019](../../../raw-input/papers/ci-pull-request-delivery-time.pdf#page=21), p. 21).

## Key findings

- The per-PR delivery-time impact of CI is "only minor," consistent with the original
  study's small effect sizes ([Guo & Leitner 2019](../../../raw-input/papers/ci-pull-request-delivery-time.pdf#page=21), p. 21).
- Projects "do not so much speed up handling individual PRs, but rather manage to handle
  considerably more PRs per release after adopting CI" ([Guo & Leitner 2019](../../../raw-input/papers/ci-pull-request-delivery-time.pdf#page=19), p. 19).
- The best predictor of PR delivery time, before and after CI, is **when in the release
  cycle a PR is merged** — so projects "need to increase the number of releases to speed
  up PR delivery times rather than adopt CI" ([Guo & Leitner 2019](../../../raw-input/papers/ci-pull-request-delivery-time.pdf#page=21), p. 21).

## Cited by

- [[continuous-integration]] (anchor)
- [[code-review]] (empirical enrichment)
