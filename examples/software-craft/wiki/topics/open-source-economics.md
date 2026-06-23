---
title: Open-Source Economics
aliases: [economics-of-open-source, paid-developers, money-and-influence]
date: 2026-06-23
last_updated: 2026-06-23
type: topic
topics: [open-source-economics, open-source-participation]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Open-Source Economics

Open source "is incompatible with one particular business model — monopoly-controlled
royalty streams based on per-copy sales — [but] it is compatible with all the others, and
indeed is better suited to some of them than proprietary software is"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=80), p. 67).
This page is the economic *why* behind funded open source — why most of it is paid work, and
how money translates (and fails to translate) into influence over a project whose decisions
are governed by [[open-source-governance]] and capped by [[forkability]].

## Most free software is written by paid developers

The surprise that "most free software is written by paid developers, not by volunteers"
dissolves once the underlying economics are stated plainly: "a company needs a particular
piece of software to be maintained and developed, and does not need monopoly control of that
software." Monopoly is often *disadvantageous*, "because then the entire burden of
maintenance would fall on that one company, instead of being shared with others who have the
same needs." Most companies need a web server but "almost no companies need exclusive control
over the development of their web server" — the same holds for office suites, kernels, and
networking tools, "just as historically it has also been true of electric grids, roads, sewer
systems, and other goods that everyone needs but no one needs to own. Just as we expect road
workers to be paid, we should expect software developers to be paid as well"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=80), p. 67).

## Informal subsidy and unofficial consortia

Paid work predates formal corporate involvement. When "a system administrator writes a
network analysis tool to help her do her job, then posts it online and gets bug fixes and
feature contributions from other system administrators, what's happened is that an unofficial
consortium has been formed." Its "funding comes from the sysadmins' salaries; its office
space and network bandwidth are donated, albeit unknowingly, by the organizations those
people work for." This informal subsidy continues today alongside the now-formalized
corporate kind ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=80), p. 67).
The central tension that formalization creates is "how the hierarchical command structures of
corporations and the polyarchical, non-coercive communities of free software projects can
work productively with each other"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=80), p. 67).

## Financial backing is welcomed, and credibility is contagious

Money is "generally welcomed by open source development communities." Paid developers mean
"bug reports are more likely to be listened to, that needed work is more likely to get done,
and that the project will be less vulnerable to the Forces of Chaos (e.g., a key developer
suddenly losing interest)." A reinforcing dynamic: "credibility is contagious, to a point."
When a large company visibly backs a project, others assume it "will receive adequate support
in its early stages," and their resulting willingness to invest "can then make this a
self-fulfilling prophecy"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=80), p. 67).

## Money buys credibility, not influence directly

The hazard is that "money can also bring a perception of control." Mishandled, it splits a
project "into in-group and out-group developers": if unpaid contributors sense that design
decisions go "to the highest bidder, they'll leave for a project that seems more like a
meritocracy." The decline is silent — "they may never complain overtly," there will "simply
be less and less noise from sources outside the main funded group," fewer large outside
contributions and fewer unexpected design opinions. "People sense what's expected of them,
and live up (or down) to those expectations"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=81), p. 68).

So money "buys influence" only indirectly: "it doesn't buy influence directly. Instead, it
buys development credibility, which is convertible to influence through the project's
decision-making processes." This is the structural difference from a commercial transaction,
where "your counterparty has enough control to guarantee the delivery of the goods." In an
open source project the work "can only be accepted based on its own merits and on how it fits
into the community's vision." What money *can* purchase are "things that lead to influence" —
"the most obvious example is programmers." Hire good ones who "stick around long enough to get
experience with the software and credibility in the community," and they influence the project
"by the same means as any other member" — a vote, a voting block, and respect beyond their
votes. Crucially, "there is no need for paid developers to disguise their motives" — a
company's reasons "are no less legitimate than anyone else's," but their weight is set "by its
representatives' status in the project, rather than by [the] company's size, budget, or
business plan"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=81), p. 68).

## Goals of corporate involvement

Corporate support springs from several overlapping, "not mutually exclusive" motivations —
useful as a checklist for reading *why* a given funder is at the table
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=81), p. 68):

- **Share the burden** — organizations with related needs "pool their resources… and create
  or join an open source project," dividing development cost while benefits "accrue to all";
  this "happens often among for-profit competitors too"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=81), p. 68).
- **Ensure maintenance of product infrastructure** — a company whose services depend on an
  open program has an interest in keeping it "actively maintained"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=81), p. 68).
- **Establish a standard** — "releasing an open source implementation… is usually the most
  effective way to get buy-in" for a technical standard
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=82), p. 69).
- **Create an ecosystem** in which the investor is "more likely to flourish."
- **Support hardware sales** — hardware value "is directly related to the amount of software
  available for" it.
- **Undermine a competitor** — "usually not the sole reason… but it can be a factor."
- **Marketing** — association with a popular project "can be good brand management," for
  customers and for "potential employees"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=82), p. 69).
- **Proprietary relicensing** — offering the software under a proprietary license to resellers
  *and* a free license to everyone else. Fogel flags it as "controversial because it is not an
  open source model, but rather yokes funding for open source development to a monopoly-based
  revenue stream"; it "requires more care… and… is usually incompatible with the presence of a
  committed and involved ecosystem of developers from outside your organization." (Deeper
  treatment is deferred to Ch.9 — see [[open-source-licensing]].)
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=82), p. 69).

## The funder's relationship and clarity of goals

Business model "is not the only factor." The *historical relationship* matters: "did the
company start the project, or did it join an existing development effort?" Both must earn
credibility, but "there's a bit more earning to be done in the latter case." The organization
also "needs to have clear goals" — leadership, "one voice in the community," or merely "a
couple of committers… able to fix customers' bugs." These goals shape every later choice;
"every project is a human environment… you will always have to play by ear, but following the
principles in this chapter will increase the likelihood of things turning out the way you
want" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=82), p. 69); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=83), p. 70).

## Negative Space

- **Proprietary-relicensing deep treatment** (`foreshadowing`): captured here only as one
  motivation in the taxonomy; the licensing mechanics and trade-offs are forward-referenced to
  Ch.9 "Legal Matters" and will enrich [[open-source-licensing]].
- **Wikipedia "business models for open source" list** (`tool-specific/perishable`): cited in
  a footnote as an "incomplete list"; the durable point (open source is compatible with every
  model except per-copy monopoly) is captured, the catalogue is not.
- **MySQL as a relicensing example** (`illustrative-scaffolding`): named to make proprietary
  relicensing concrete; the concept is captured, the example is not paged.
- **Google/Android copy-modify-merge footnote** (`illustrative-scaffolding`): an example of a
  funder keeping its own long-lived branch and merging with upstream; illustrates "ensure
  maintenance," not a separate concept.

## See also

- [[corporate-open-source-participation]] — the behavioral playbook for *how* a funder should
  act once the economic decision to participate is made.
- [[open-source-contracting]] — buying specific work without being able to buy its acceptance.
- [[government-and-open-source]] — how the economics shift for public-sector organizations.
- [[open-source-governance]] — the decision-making processes through which credibility becomes
  influence; see "Funding strains the benevolent-dictator model."
- [[forkability]] — the exit right that ultimately caps any funder's leverage.
- [[open-source-participation]] — who actually writes the code these funders pay for.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 5 "Organizations and Money" —
  "The Economics of Open Source," "Goals of Corporate Involvement" (printed pp. 67–70).
