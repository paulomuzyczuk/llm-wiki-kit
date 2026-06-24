---
title: Open Source Licensing
aliases: [choosing-a-license, applying-a-license, software-license]
date: 2026-06-23
last_updated: 2026-06-24
type: topic
topics: [open-source-licensing, open-source-culture]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Open Source Licensing

A license is what makes "free software" or "open source software" a legally meaningful
status rather than a slogan: it grants the freedoms and disclaims the warranty. (Fogel's own
caveat applies throughout: he "[is] not a lawyer," and "nothing in this book should be construed
as formal legal advice" — for that, "hire a lawyer or be one"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=171), p. 158).)
This page
captures Fogel's "very quick, very rough guide to choosing a license" from the launch
chapter — the decision criteria and how to apply the result
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=32), p. 19).
The deeper legal treatment from Ch. 9 "Legal Matters" enriches this anchor below: the
terminology that affects the decision, the *aspects* on which licenses differ, and the fuller
*choosing-a-license* guidance. The two license **families** — reciprocal and permissive — have
their own pages: [[copyleft]] and [[permissive-licensing]], bridged by [[license-compatibility]].
Copyrights, trademarks, and patents remain Ch. 9b territory (batch 17).

## "Free" and "open source" licenses are the same set

The terms "free software license" and "open source license" are "essentially synonymous."
Technically the first names licenses the Free Software Foundation confirms as meeting the
**Free Software Definition**'s four freedoms, and the second names those the Open Source
Initiative confirms as meeting the **Open Source Definition** — but "the two definitions
delineate the same freedoms," so "the two organizations have approved the same set of
licenses." A handful of exotic edge cases differ, but "for any license you are likely to be
using, the terms 'OSI-approved' and 'FSF-approved' can be treated as implying each other"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=32), p. 19).
This synonymy is a *licensing* fact; the *motivational* split behind the two names is
covered in [[free-software-vs-open-source]].

## The choice reduces to one question

There are "a great many free software licenses," but most "were written to satisfy the
particular legal needs of some corporation or person" and can be ignored; in most cases a
project should pick one of the few common licenses
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=32), p. 19).
The decision criterion is a single question — *are you willing to let your code be used in
proprietary programs?*

- **Yes / don't mind → a permissive "do anything" license.** Use "an MIT-style license,"
  the simplest of the minimal licenses "that do little more than assert nominal copyright
  … and specify that the code comes with no warranty"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=33), p. 20).
- **No → the GNU General Public License (GPL), version 3.** Copyleft that prevents the
  code being absorbed into proprietary software. It is "probably the most widely recognized
  free software license in the world," and that recognition is itself an advantage: many
  users and contributors "won't have to spend extra time to read and understand your
  license"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=33), p. 20).
- **No, and the software is used over a network → the GNU Affero GPL (AGPL).** "Just the
  GPL with one extra clause establishing network accessibility as a form of distribution,"
  closing the gap where a hosted service is used but never distributed client-side
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=33), p. 20).

The deeper trade-offs — copyleft's reach, license compatibility, mixing code under
different licenses — are flagged here and developed in Ch. 9.

## Applying a license

Choosing is not enough; the license must be *applied* in two places
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=33), p. 20):

1. **State it on the front page.** Name the license and link to its full text — this
   "tells the public what license you intend the software to be released under." This is
   the licensing half of the launch checklist's "state that the project is free" item (see
   [[launching-an-open-source-project]]).
2. **Include it in the software.** Put the full license text in a `LICENSE` (or `COPYING`)
   file in the source tree, and "at the top of each source file put a short notice in a
   comment, naming the copyright date, holder, and license, and saying where to find the
   full text." The front-page statement alone is "not quite sufficient for legal purposes."

The per-file notice and `LICENSE` file together are the standard pattern; the exact wording
varies by license (the GPL ships its own recommended header).

## Terminology that affects the decision (Ch. 9)

A licensing discussion surfaces "many different words for the same thing." A few distinctions
are decision-relevant rather than pedantic
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=171), p. 158):

- **FOSS / F/OSS / FLOSS** are just longer spellings of "free / open source software" — all
  "mean the same thing." The naming choice signals stance (see [[free-software-vs-open-source]]),
  not a different legal status
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=172), p. 159).
- **Commercial ≠ proprietary.** Using "commercial" as a synonym for "proprietary" is
  "carelessness." *"Free software is always commercial software"* — it can be sold, as long as
  buyers aren't restricted from giving away copies
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=172), p. 159).
  It can also be commercialised "by selling support, services, and certification"; there are
  "billion-dollar companies built on free software," so it is "neither inherently anti-commercial
  nor anti-corporate. It is merely anti-proprietary, or if you prefer anti-monopoly"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=173), p. 160).
  This is the licensing-side basis for the [[open-source-marketing]] / [[open-source-economics]]
  distinction between commercial and proprietary.
- **Proprietary ≈ closed-source.** The two are effectively synonyms; "closed-source" merely adds
  that the source can't be seen. But source *visibility* "is not the issue; the important question
  is what you're allowed to do with it: if you can't copy, modify, and redistribute, then it's
  not open source"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=172), p. 159).
- **Public domain vs. a license.** A public-domain work has *no copyright holder*, so technically
  it is one way to make software "free." But "there are usually good reasons to use a license
  instead" — even free software benefits from terms that protect both the copyright holder and
  recipients, exactly what the next aspects describe
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=173), p. 160).

The two **license families** — [[copyleft|reciprocal/copyleft]] and
[[permissive-licensing|non-reciprocal/permissive]] — are the load-bearing terminology and have
their own pages.

## What licenses vary on (Aspects)

"In the important respects" all free licenses say the same things: anyone may see, use, modify,
and redistribute the code, in original or modified form, and the authors "provide no warranties
whatsoever." The differences "boil down to a few oft-recurring issues" — the dimensions to weigh
when choosing
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=173), p. 160):

- **Compatibility with proprietary licenses** — whether the code may go into a closed-source
  program. This is the [[copyleft]] vs. [[permissive-licensing]] split and "the sharpest dividing
  line in licensing."
- **Compatibility with other free licenses** — whether the code may be combined with code under a
  different free license; in practice this means GPL-compatibility (see [[license-compatibility]]).
- **Attribution requirements** — a notice giving credit to the authors must accompany use; these
  licenses are "often still proprietary-compatible," demanding credit rather than freedom.
- **Protection of trademark** — "a type of attribution requirement": the original name may not be
  used to identify derivative works without permission. (Trademark itself is Ch. 9b — batch 17.)
- **Patent snapback** — clauses (GPL-3.0, Apache-2.0, MPL-2.0, …) that grant patent licenses with
  the contribution and revoke them if the user initiates patent litigation, "to prevent people
  from using patent law to take away the rights granted under copyright law." (Patents proper are
  Ch. 9b.)

The common thread: each places "certain easily satisfiable demands on the recipient in exchange
for the recipient's right to use the code"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=174), p. 161).

## Choosing a license: use an existing, well-recognized one

Beyond the one-question shortcut above, Ch. 9 adds a governing principle and a fuller menu.
**Use an existing license — and not just any existing license, but one of the widely-used,
well-recognized ones.** Two reasons
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=175), p. 162):

1. **Familiarity lowers the barrier to entry.** People "won't feel they have to read the legalese"
   for a license they've already read elsewhere.
2. **Quality.** These licenses "are the products of much thought and experience," mostly revisions
   of their own earlier versions — "unlikely you could do better even with a team of lawyers."

Fogel's recommended set, "in roughly descending order from strong copyleft … to completely
non-copyleft," with his defaults in **bold**
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=176), p. 163):

| License | Family |
|---|---|
| **GPL-3.0** — GNU General Public License v3 | strong copyleft (default copyleft) |
| **AGPL-3.0** — GNU Affero GPL v3 | copyleft + network use (default for network code) |
| MPL-2.0 — Mozilla Public License 2.0 | weak copyleft |
| LGPL-3.0 — GNU Lesser GPL v3 | weak copyleft (libraries) |
| EPL-1.0 — Eclipse Public License 1.0 | weak copyleft |
| Apache-2.0 — Apache License 2.0 | permissive + patent defenses |
| **MIT** | permissive (default non-copyleft) |
| BSD-2-Clause | permissive |

The default decision: want copyleft → GPL-3.0 (or AGPL-3.0 for network code); want permissive →
MIT. The [[copyleft]] and [[permissive-licensing]] pages develop *why* and the MIT-vs-Apache
trade-off.

**The "or any later version" option.** The GPL lets you license under the current version while
granting downstream the option to redistribute "under any later (i.e., future) version." It
future-proofs the license — others "can do it … to keep the software license up-to-date" or to
solve unanticipated compatibility problems — and frees you from maintaining the license "forever."
Whether to grant it "depends largely on how likely you think the Free Software Foundation is to
make GPL revisions that you would approve of." Fogel generally includes it; the Linux kernel
famously does *not* (GPL-2.0 only). "This book cannot answer the question … you now know that you
have the choice"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=177), p. 164).

## Negative Space

- **Detailed legal implications of each license** (now ingested from Ch. 9): copyleft reach,
  license compatibility, and how a license affects mixing code are developed on [[copyleft]],
  [[permissive-licensing]], and [[license-compatibility]] rather than enumerated per-license here
  (the *principles + decision criteria* strategy: no per-license mechanics pages).
- **Verbatim GPL header text** (`too-granular`): the multi-paragraph "This program is free
  software…" notice is reproduced in the source as one example; captured here as "ship a
  per-file copyright/license notice," not transcribed.
- **FSD/OSD edge-case differences** (`too-granular`): the rare clauses on which the two
  definitions formally diverge are noted as existing but "exotic edge cases" (incl. the disputed
  CAL-1.0), not enumerated.
- **Copyrights, trademarks, patents** (`foreshadowing`): named in the chapter heading and
  introduced here only as license *aspects* (attribution, trademark protection, patent snapback);
  their full treatment is Ch. 9b territory (batch 17).

## See also

- [[copyleft]] — the reciprocal license family (GPL/AGPL/LGPL); "freedom made contagious."
- [[permissive-licensing]] — the non-reciprocal family (MIT/BSD/Apache); proprietary-compatible.
- [[license-compatibility]] — whether differently-licensed code can be combined; GPL-compatibility
  and the DFSG/OSI/FSF certification tests.
- [[launching-an-open-source-project]] — the launch checklist this licensing guide serves;
  "state that the project is free" is its hook.
- [[free-software-vs-open-source]] — the historical/motivational reason two names map to
  one set of licenses.
- [[forkability]] — a free license is the legal substrate that makes the right to fork
  real.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 2 "Getting Started" —
  "Choosing a License and Applying It": free/open synonymy, the "Do Anything" (MIT) vs.
  GPL vs. AGPL decision, and how to apply a license (printed pp. 19–20).
- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 9 "Legal Matters" —
  "Terminology" (FOSS/FLOSS, commercial≠proprietary, public domain), "Aspects of Licenses"
  (the dimensions licenses vary on), and "Choosing a License" (use an existing well-recognized
  license, the recommended list, the "or any later version" option) (printed pp. 158–164).
