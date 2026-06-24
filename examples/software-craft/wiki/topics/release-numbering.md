---
title: Release Numbering
aliases: [release-versioning, semantic-versioning, semver, version-numbers, even-odd-strategy]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [release-engineering]
roles: [tech-lead, product-engineer]
source_tier: 1
project: null
source_count: 1
status: active
---

# Release Numbering

A release number is a compact signal to people who **don't** follow the project
daily. Every release means some old bugs are fixed (the one thing users can count
on), some new bugs are added, and possibly new features, changed configuration
options, or outright incompatible changes — so experienced users approach a new
release with trepidation, and the number's job is to tell them in advance how much
to worry ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=132), p. 119); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=133), p. 120).

## The twofold purpose

Release numbering exists to do two things at once: **unambiguously communicate the
ordering** of releases within a series (which of two came later), and **indicate as
compactly as possible the degree and nature of the changes** in each release ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=133), p. 120).
Numbering strategy is "one of the oldest bikeshed discussions around" (see
[[facilitating-online-discussion]] on the Bikeshed Effect) and no single standard
will ever win — but one principle is universally agreed: **be consistent.** Pick a
scheme, document it, and stick to it ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=133), p. 120).

The audience point is load-bearing: the project's core developers already know what
changed and what APIs moved, so they are *not* the audience for release numbers.
The number matters most for users who don't follow daily discussion — and who are
therefore underrepresented in any project debate about how strictly to adhere to a
scheme. When numbering, "it's better to be overly strict than overly lax" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=133), p. 120).

### When you may skip semantic numbers

The whole discipline applies only where release-number *semantics* matter. A project
that offers no API predictability anyway, or practices continuous development with
auto-deployment (as some JavaScript projects do), can reasonably let git commit IDs
double as release identifiers. The decision should be based on **how users actually
deploy and upgrade the software**, not on developer convenience ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=133), p. 120).

## Number components

Release numbers are groups of digits separated by dots, and **the dots are
separators, not decimal points** — `5.3.9` is followed by `5.3.10`, not `5.4`. The
Linux kernel famously hinted otherwise with its `0.95`…`0.99` march toward `1.0`,
but the non-decimal convention is now a firm standard ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=133), p. 120).
There is no hard limit on the number of components, but most projects stop at three
or four.

In a typical three-component system `major.minor.micro`:

- **major** — an increment marks major changes and compatibility boundaries.
- **minor** — an increment marks minor changes (typically new features).
- **micro** (also called the **patch** number) — an increment marks really trivial
  changes, normally bug fixes only ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=134), p. 121).

The vocabulary of *series* and *lines* follows from this: a **major series** is all
releases sharing a major number; a **minor line** is all releases sharing the same
major *and* minor number. So `2.4.0` and `2.4.2` are in the same minor line (though
not adjacent if `2.4.1` shipped between them), while `2.4.0` and `3.4.1` are not,
despite both having minor number `4` ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=134), p. 121).
A fourth component, where used, is usually a finer-grained patch number or a **build
number** incremented on every build — most useful when binary packages are the
default distribution method and the project wants to link each bug report to a
specific build ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=134), p. 121).

### Pre-release qualifiers

A numeric version may carry a descriptive qualifier — **Alpha**, **Beta**, or **RC**
(Release Candidate) — meaning this release *precedes* a future release with the same
number minus the qualifier (so `2.3.0 (Alpha)` leads eventually to `2.3.0`). To allow
several candidates in a row, qualifiers take numeric meta-qualifiers: `Alpha 1`,
`Alpha 2`, `Beta 1`, … `RC 1`, `RC 2` (RC *always* carries a meta-qualifier). Stick
to those three widely-recognised labels rather than inventing plainer-sounding
alternatives — there's no reason to do things gratuitously differently from everyone
else ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=133), p. 120); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=134), p. 121).

## Semantic Versioning

The most-used set of rules for *what kind of change is allowed under which
increment* is now formalised as Semantic Versioning (semver.org). In the
three-component system:

1. **Micro** changes (within a minor line) must be both forward- and
   backward-compatible — bug fixes only, or very small enhancements; no new features.
2. **Minor** changes (within a major line) must be backward-compatible but need not
   be forward-compatible; introducing new features is normal, but not too many at
   once.
3. **Major** changes mark compatibility boundaries — a new major release may be
   forward- *and* backward-incompatible, and is expected to carry new features or
   whole new feature sets ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=134), p. 121); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=135), p. 122).

What "compatible" means depends on the software, but it is rarely ambiguous in
context. The same rules apply across whichever **compatibility domains** the software
exposes — client/server protocols, on-disk **data formats**, and published **APIs**
(source and binary). The promise is that an informed user "need never wonder whether
or not it's safe to upgrade in place" — she can look at the numbers and know
instantly ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=135), p. 122).
The price of the scheme is that you "don't get a chance for a fresh start until you
increment the major number," which makes up-front extensible design valuable but is
otherwise an inescapable cost of distributing software ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=135), p. 122).

> **Source note.** Fogel flags that the semver.org standard "apparently does not
> include the forward-compatibility requirement for increments in the micro (patch)
> number," so his rule 1 is slightly stricter than semver as published ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=134), p. 121).

Pre-1.0 releases are understood to be exempt: a project in initial development can
ship `0.1`, `0.2`, `0.3` with arbitrarily large differences between them, and micro
numbers there are optional. State the exemption explicitly in your policy ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=135), p. 122).

## The even/odd strategy

An alternative convention overloads the **minor number's parity** to signal
stability: **even means stable, odd means unstable.** Micro increments still mean bug
fixes and major increments still mean big changes; only the minor number carries the
extra bit. Users can tell from `2.4.21` that it's safe for a production web server
while `2.5.1` should stay on experimental machines. The development team fields bug
reports from the unstable (odd) series, and when it settles, increments the minor
number to even, resets micro to `0`, and ships a presumably stable package ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=135), p. 122); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=136), p. 123).

Used by the Linux kernel (historically) among others, the scheme forces the minor
number to increment about twice as often as otherwise, with no real harm. It suits
projects with **very long release cycles and conservative users who value stability
over new features**. It is not the only way to expose unstable code for testing — see
[[stabilizing-a-release]] for the more common branch-marking approach ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=136), p. 123).

## Negative Space

- **Per-project numbering recipes** (`too-granular`): the exact component count and
  per-component meaning a given project picks is a local decision; the page captures
  the governing conventions, not any one project's table.
- **Linux `0.95`…`0.99` and kernel even/odd history** (`illustrative-scaffolding`):
  used to illustrate the not-decimal-points and parity conventions, not concepts in
  their own right.
- **semver.org spec text** (`tool-specific/perishable`): the external standard's
  exact clauses live at the spec; the page records the principle and Fogel's one
  point of divergence.

## See also

- [[stabilizing-a-release]] — the process that decides which changes earn a given
  micro/minor increment.
- [[release-branches]] — the version-control structure the numbered releases are cut
  from.
- [[open-source-licensing]] — the other thing a release must declare unambiguously.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 7 "Packaging,
  Releasing, and Daily Development", §Release Numbering (incl. Release Number
  Components, Semantic Versioning, The Even/Odd Strategy), printed pp. 119–123.
