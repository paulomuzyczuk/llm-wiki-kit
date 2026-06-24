---
title: Maintaining Multiple Release Lines
aliases: [parallel-release-lines, release-lines, end-of-life, support-window, maintenance-releases]
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

# Maintaining Multiple Release Lines

Most mature projects keep **several release lines alive in parallel** rather than
expecting everyone to track the newest code. After `1.0.0` ships, the `1.0.x` line
continues with micro (bugfix) releases — `1.0.1`, `1.0.2`, … — and **shipping `1.1.0`
is not sufficient reason to end it** ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=145), p. 132).
The vocabulary of series, minor lines, and micro releases comes from
[[release-numbering]]; this page is about the *policy* of running them at once.

## Why old lines outlive new ones

The governing reason is conservative users: some make it a **policy never to upgrade to
the first release in a new minor or major series**, letting others shake the bugs out of
`1.1.0` and waiting for `1.1.1`. That isn't selfish — they are forgoing the new line's
bugfixes and features too; they have simply decided to be careful ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=145), p. 132).

The practical consequence is a branching obligation. If a major bug in `1.0.3` is found
right as `1.1.0` is about to ship, it would be **too severe to put the fix only in
`1.1.0`** and tell every `1.0.x` user to make a major upgrade to get it. The friendly
move is to **release both `1.1.0` and `1.0.4`**, so cautious users get the fix without
being forced onto the new line ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=145), p. 132).

## End-of-life is an explicit, announced decision

A release line does not lapse silently. Once the new line (`1.1.x`) is well under way, a
project **may declare the old line end-of-life — but must announce it officially**. The
announcement can stand alone or ride along with a `1.1.x` release announcement; either
way, users need to know the old line is being phased out so they can plan their upgrades
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=145), p. 132).

Two common ways to decide *when* a line reaches end-of-life ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=145), p. 132):

- **A pledged support window.** The project commits in advance to support the previous
  line for a fixed span of time. In an open-source context, "support" means **accepting
  bug reports against that line and cutting maintenance releases when significant bugs
  are found** — not bespoke assistance.
- **Demand-gauged retirement.** The project gives no fixed window but **watches incoming
  bug reports** to estimate how many people still run the old line; when that share drops
  below some threshold, it declares end-of-life and stops supporting it.

## Wire the lines into the bug tracker

Parallel lines only work if reporters can file against the right one. For **each
release, provide a target version / milestone in the bug tracker** so a report lands
against the proper release. Crucially, **also provide a "development" or "latest"
target** for the most recent sources — because some people (not only active developers)
deliberately run ahead of the official releases and need somewhere to file
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=145), p. 132). See [[bug-tracking]] for the tracker
side of this.

## Negative Space

- **The specific `1.0.x` / `1.1.0` version numbers** (`illustrative-scaffolding`):
  worked numbers illustrating the parallel-line policy, not concepts; the durable points
  are "new line ≠ old line's death," "ship both on a late bug," and "announce EOL."
- **Exact support-window durations / report-share thresholds** (`too-granular`): the
  span of a pledge or the cutoff percentage is a per-project tuning decision; the page
  keeps the two *models* (pledged vs. demand-gauged), not any one project's numbers.

## See also

- [[release-numbering]] — the series / minor-line / micro vocabulary this policy
  operates over, and the "never end a line just because a newer one shipped" corollary.
- [[release-branches]] — the long-lived branches that make parallel maintenance possible.
- [[security-releases]] — a forced maintenance release that lands across every supported
  line at once.
- [[bug-tracking]] — where per-line target versions and the "development/latest" target
  are configured.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 7 "Packaging,
  Releasing, and Daily Development", §Maintaining Multiple Release Lines, printed p. 132.
