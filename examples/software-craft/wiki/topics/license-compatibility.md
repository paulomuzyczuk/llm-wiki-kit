---
title: License Compatibility
aliases: [gpl-compatibility, mixing-licenses, dfsg-compliant, osi-approved, license-certification]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-licensing]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# License Compatibility

**Compatibility** is the question of whether code under one license "can be combined with code
under another, and the result distributed under either license without violating the terms of
the other"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=174), p. 161).
Because open-source code is meant to be reused and combined, compatibility is a first-class
license-choice criterion — pick a license that mixes with the code you expect to draw on.

## The shape of the compatibility landscape

Most commonly-used [[permissive-licensing|non-reciprocal]] licenses "are compatible with each
other." Some are also compatible with some [[copyleft]] licenses: a work combining permissive
and copyleft code "can be distributed as a combined work under the copyleft license (since
that's the license that places more conditions), with the original code in each case remaining
under its original license." The recurring friction "come[s] up between some non-reciprocal
license and the GNU General Public License"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=174), p. 161).

## GPL-compatibility is the dominant axis

The compatibility question that actually bites in practice is **GPL-compatibility**. The GPL's
"You may not impose any further restrictions" clause (see [[copyleft]]) makes it incompatible
with any otherwise-free license that adds its own demand — a credit clause, for instance. So:

- If you want your code "to be able to be mixed freely with GPLed code, then you should pick a
  GPL-compatible license"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=175), p. 162).
- "Most of the GPL-compatible open source licenses are also proprietary-compatible" — such code
  can go into a GPL program *and* into a proprietary program. The two resulting derivatives are
  not compatible with each other, "but that concern applies only to the derivative works, not
  to the code you distribute in the first place"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=175), p. 162).
- **AGPL caveat:** AGPL-3.0 is compatible with GPL-3.0 but "not directly compatible with
  GPL-2.0." Most GPL-2.0 code carries the "or any later version" option and can simply shift to
  GPL-3.0 to mix; code licensed *strictly* under GPL-2.0 cannot
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=177), p. 164).

This is why [[permissive-licensing|MIT]] makes a strong default: it is "fully compatible with
all versions of the GNU General Public License," whereas the Apache 2.0 GPL-compatibility story
is qualified.

## Certification tests: how to know where a license stands

Rather than reason about a license from scratch, consult the standing lists maintained by the
certifying bodies. Each answers a slightly different question
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=172), p. 159):

- **DFSG-compliant** (Debian Free Software Guidelines) — "a widely-used test for whether a given
  license is truly open source." Debian invested heavily in constructing the test, so it "ha[s]
  proven very robust," with no serious objection from the FSF or OSI. Knowing a license is
  DFSG-compliant tells you "it guarantees all the important freedoms (such as forkability even
  against the original author's wishes)" — the link to [[forkability]].
- **OSI-approved** — approval by the Open Source Initiative. Membership of the OSI list is "an
  unambiguous state: a license either is or isn't on the list." The OSI definition derives from
  the DFSG, "and any license that meets one definition almost always meets the other."
- **FSF license list** — categorizes licenses "not only by whether they are free, but whether
  they are compatible with the GNU General Public License" — the one list that directly answers
  the GPL-compatibility question
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=175), p. 162).
- **SPDX** — the Software Package Data Exchange maintains the canonical list of license
  abbreviations together with their OSI/FSF approval status
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=175), p. 162).

The practical rule: the three definitions (DFSG, OSD, Free Software Definition) "delineate the
same freedoms," so for any license you are likely to use, being on one list implies the others
— with only "niche" exceptions of no practical consequence.

## Negative Space

- **Pairwise compatibility matrix** (`too-granular`): which specific license pairs combine, and
  under which terms, is deferred to the certifying bodies' lists rather than tabulated here.
- **DFSG / OSI / FSF list URLs and contents** (`tool-specific/perishable`): the canonical lists
  live online and change; the page captures *what each test certifies*, not its current entries.
- **CAL-1.0 data-portability controversy** (`source-underdeveloped`): the one recent license
  whose Open-Source-Definition status is disputed is a footnote edge case, not a compatibility
  principle.

## See also

- [[copyleft]] — the "no further restrictions" clause is the root cause of GPL-incompatibility.
- [[permissive-licensing]] — most permissive licenses are mutually and GPL-compatible; MIT is
  fully GPL-compatible, Apache 2.0 only partly.
- [[open-source-licensing]] — the anchor; compatibility is one of the "aspects" a license choice
  weighs.
- [[forkability]] — DFSG-compliance certifies the right to fork against the author's wishes.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 9 "Legal Matters" —
  "Terminology" (DFSG-compliant, OSI-approved, the FSF list), "Aspects of Licenses"
  (compatibility with other free licenses), "The GPL and License Compatibility" (GPL-compatibility
  as a choice criterion, the FSF compatibility list), and the AGPL/GPL-2.0 compatibility note
  (printed pp. 159–164).
