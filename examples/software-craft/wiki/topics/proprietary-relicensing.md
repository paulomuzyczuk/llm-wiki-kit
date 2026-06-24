---
title: Proprietary Relicensing
aliases: [selling-exceptions, open-core, freemium-open-source, dual-licensing]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-economics, open-source-licensing]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Proprietary Relicensing

**Proprietary relicensing** is a business scheme in which "an open source version of the
software is available under the usual open source terms, while a proprietary version is
available for a fee"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=179), p. 166).
Fogel treats it as a real but cautionary option: he documents how it works and why companies
reach for it, then argues at length that it "inevitably ha[s] a negative effect on the level of
community engagement and the level of technical quality on the open source side"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=181), p. 168).
(He flags the terminology: this is "sometimes also called dual licensing," but that term is
ambiguous — it has also meant releasing under two or more *open source* licenses at once — so he
prefers "proprietary relicensing.")

## The legal mechanic: you can't sue yourself

The scheme looks paradoxical — how can a copyright holder offer software proprietarily if its
GPL terms require the code to be available under less restrictive terms? The answer is the same
asymmetry that powers [[copyleft]]'s sole-copyright-holder exemption: "the GPL's terms are
something the copyright holder imposes on everyone else; the owner is therefore free to decide
not to apply those terms to itself." Put plainly, "one always has the right to not sue one's
self for copyright infringement" — a feature of copyright law, not of any particular license
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=180), p. 167).
This is why relicensing requires the company to hold rights to *all* the code, which in turn
forces it to collect [[contributor-agreements]] from every contributor.

## Two kinds (decision criteria)

There are two distinct models, answering "why would anyone want a proprietary version when an
open source version is already out there?"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=179), p. 166):

- **Selling exceptions to copyleft.** Typically used with *code libraries*. The copyright
  holder sees that some users "want to incorporate it into their own proprietary applications"
  and "sells them a promise to not enforce the redistribution requirements" of the copyleft
  license. The downstream user can then embed the library in a closed product "without worry
  that they might be forced to share the source code to their full product." This **only works
  under a copyleft-style license** (in practice the GPL or AGPL) — there is no exception to sell
  if the code is already permissive. The canonical example is the MySQL database engine
  (GPL v2, with a paid proprietary license once from MySQL AB, later Oracle).
- **Open core / freemium.** An open source version is used "to drive sales of a presumably
  fancier proprietary version." Usually the company offering the proprietary version is also the
  primary maintainer of the open source one. In practice they sell paid support only for the
  proprietary version, so they "can charge two fees: a subscription fee for the software itself
  and a fee for the support services." The open-core marketing pitfalls connect to
  [[open-source-marketing]]
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=180), p. 167).

## Why Fogel advises against it

Both varieties "tend to suffer from several problems"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=180), p. 167):

- **It breaks the contribution dynamic through asymmetry.** Outside contributors are
  "effectively contributing to two distinct entities: the free version … and the proprietary
  version." Unlike a permissive license, where *anyone* may build proprietary works, here "only
  one party has that right," so participants "are thus being asked to contribute to an
  asymmetric result." The required contributor agreement — which must grant the company
  "special, one-sided rights" — "starkly confronts contributors with the imbalance," and some
  decline to sign.
- **Drift toward the "shakedown."** Many companies that start with a clean offer "have
  eventually graduated to something closer to a 'shakedown' model," pressuring anyone who makes
  "commercially significant use of the code" to buy a proprietary license. Fogel reports this
  off-the-record from "multiple sources, at different projects and different companies," and
  warns "the temptation to undermine the open source license will be overwhelming to the point
  of being impossible to resist."
- **A self-fulfilling motivational collapse.** Outside developers sense that "most of the
  salaried development attention is going to the proprietary version anyway," so contributing to
  the open version feels like "a fool's game." As they stay away, the company "sees less reason
  to invest in the open source codebase," which discourages contributors further — a downward
  spiral. The empirical result: proprietarily relicensed projects "do not get truly active
  development communities with external participants"; they get "occasional small-scale bug
  fixes" and do "most of the hard work themselves."

The decision criterion Fogel leaves the reader: if business reasons push you toward it anyway,
go in knowing the community cost and try to mitigate it — but expect the open source side to
stay shallow.

## Negative Space

- **MySQL / MySQL AB / Oracle corporate history** (`illustrative-scaffolding`): one named
  example of "selling exceptions"; the principle, not the company timeline, is retained.
- **App Store / GPL distribution-restriction edge case** (`tool-specific/perishable`): a
  footnote on how storefront terms can force pro-forma relicensing of copylefted code; a
  perishable platform-specific wrinkle, not the concept.
- **SaaS hosting detail of the support-fee model** (`too-granular`): the parenthetical that
  both versions are "usually hosted as SaaS" is a delivery detail under open core, not its own
  idea.

## See also

- [[copyleft]] — the sole-copyright-holder exemption ("you can't sue yourself") that makes
  relicensing legally possible, and the only license family "selling exceptions" applies to.
- [[contributor-agreements]] — the one-sided agreement a relicensing company must collect; the
  DCO's inbound=outbound rule is the structural opposite.
- [[open-source-marketing]] — the marketing pitfalls of the open-core / "commercial vs.
  proprietary" framing.
- [[open-source-economics]] — the broader question of how money and open source projects
  interact.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 9 "Legal Matters" —
  "Proprietary Relicensing" (the two kinds: selling exceptions and open core/freemium; the
  "can't sue yourself" mechanic) and "Problems with Proprietary Relicensing" (asymmetry,
  the shakedown drift, the motivational spiral) (printed pp. 166–168).
