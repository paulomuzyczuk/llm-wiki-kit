---
title: Crowdfunding and Bounties
aliases: [crowdfunding, bounties, bounty-funding]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-economics]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Crowdfunding and Bounties

Fogel groups crowdfunding and bounties together "not because they are the same thing, but because
to the extent that they are problematic as ways of funding free software development, their problems
are similar"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=105), p. 92).
They sit at the margin of [[open-source-economics]]: real but minor next to contracted and salaried
work, and structurally mismatched to how open source actually sustains itself.

## The two mechanisms

- **Crowdfunding** is "many funders — often mostly individuals — coming together to fund a
  particular piece of development." Campaigns fall into two categories: **"all or nothing"** — each
  funder "pledges money toward a total threshold and the pledges are collected only if the threshold
  is met" — or **"keep it all,"** which "is essentially traditional donation: funds go immediately to
  the recipient whether or not a stated goal amount is ever met"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=105), p. 92); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=106), p. 93).
- **Bounties** are "one-time rewards for completing specific tasks, such as fixing a particular bug
  or implementing a new feature." They "are often offered directly by the interested parties, since
  there is no need for a pledge-collecting system"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=106), p. 93).

## The shared problem: one-time event vs. ongoing process

Both "have funded some open source work," but "they have not been a major economic force compared to
contracted or salaried development." The reason is structural: **they are "structured around
development as a one-time event rather than as an ongoing process."** That "would be problematic for
any kind of software development, but is especially so for open source development, which if anything
is … optimized more for low-intensity, long-term investment rather than for high-intensity burst
investment." Both mechanisms suit "high-intensity, one-time bursts of activity, and do not provide
for ongoing maintenance or investment past the completion of the campaign goal or prize condition"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=106), p. 93).

The decision criterion follows directly: a crowdfunding campaign "can sometimes be a good way to get
a project launched, but generally is not a way to fund development after the initial launch."
"Successive crowdfunding campaigns for later stages … will inevitably tire out even a willing and
supportive audience." Fogel's analogy is the long-running charity (e.g. US public radio) that "seek[s]
to develop sustaining funders … to provide a long-term, stable revenue stream, and then raise funds
for specific one-time efforts separately from that"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=106), p. 93).

## Techniques worth borrowing

If you do run a campaign, "take a close look at how other open source projects have run theirs"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=106), p. 93):

- **Tiered backer rewards.** Most platforms support "different rewards to backers at different
  monetary levels" — e.g. a mention in a SUPPORTERS file, or "at higher levels a mention on a
  thank-you page."
- **Dedicate a commit to a backer.** A more creative reward (Fogel credits Michael Bernstein): "offer
  to dedicate a commit to each backer at or above a certain level, by thanking the backer directly in
  the commit's log message." Its virtue is operational — "it's decentralized and easy to administer:
  any developer on the project can help fulfill that reward."
- **Discounted consulting — with a limit.** Individual developers "can also offer free or discounted
  consulting about the project as a reward." But "be careful not to sell too much of your time: the
  point of the campaign is to raise funds for development, not to turn the development team into a
  consulting team"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=106), p. 93).

## Pitfalls specific to free software

- **Don't sell early access.** A reward common to non-free campaigns — "a 'sneak preview' or 'beta
  access' to in-progress versions, before the public release" — "is not appropriate for free software
  projects." For open source "the public is supposed to already have access to in-progress work";
  access "should be limited by the time and interest of the parties seeking the information, not by
  the project." Borrow techniques, but remember that some "may not be suitable for an open source
  project that wants to keep the good will of its users and development community"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=106), p. 93).
- **Plan allocation before the money arrives.** "If your project accepts donations, do some public
  planning of how the money will be used before it comes in." Such discussions "go a lot more smoothly
  when held before there's actual money to spend; also, if there are significant disagreements, it's
  better to find that out when the money is still theoretical than when it's real"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=106), p. 93).

## Negative Space

- **Named platforms — Goteo, Kickstarter, Indiegogo, BountySource** (`tool-specific/perishable`):
  cited as current examples of all-or-nothing / keep-it-all / clearinghouse services; the durable
  distinction is the funding *model*, not the vendor.
- **Snowdrift.coop matching-pledge experiment footnote** (`source-underdeveloped`): flagged by Fogel
  himself as "unknowable as of this writing in mid-2015"; an in-progress experiment, not a settled
  mechanism.
- **Wikipedia "comparison of crowdfunding services" footnote** (`tool-specific/perishable`): a pointer
  to an external catalogue.

## See also

- [[open-source-economics]] — why crowdfunding and bounties are marginal next to salaried and
  contracted development; the "ongoing process" logic this page applies.
- [[funding-non-programming-activities]] — the more durable funding targets (testing, docs, infra)
  that ongoing money should reach.
- [[open-source-contracting]] — contracted development, the major funding mode these mechanisms are
  measured against.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 5 "Organizations and Money" —
  "Crowdfunding and Bounties" (printed pp. 92–93).
