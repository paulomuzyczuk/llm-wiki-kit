---
title: Open Source Licensing
aliases: [choosing-a-license, applying-a-license, software-license]
date: 2026-06-23
last_updated: 2026-06-23
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
status rather than a slogan: it grants the freedoms and disclaims the warranty. This page
captures Fogel's "very quick, very rough guide to choosing a license" from the launch
chapter — the decision criteria and how to apply the result. The detailed legal mechanics
(license families, compatibility, copyrights, trademarks, patents) are deferred to Ch. 9
"Legal Matters" and will enrich this anchor in a later batch
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=32), p. 19).

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

## Negative Space

- **Detailed legal implications of each license** (`foreshadowing`): copyleft reach,
  license compatibility, how a license affects mixing code — explicitly deferred by Fogel
  to Ch. 9 and to be ingested in a later batch into this page.
- **Verbatim GPL header text** (`too-granular`): the multi-paragraph "This program is free
  software…" notice is reproduced in the source as one example; captured here as "ship a
  per-file copyright/license notice," not transcribed.
- **FSD/OSD edge-case differences** (`too-granular`): the rare clauses on which the two
  definitions formally diverge (e.g. redistribution-under-identical-terms) are noted as
  existing but "exotic edge cases," not enumerated.
- **Copyrights, trademarks, patents** (`foreshadowing`): named in the chapter heading but
  not treated here; Ch. 9 territory.

## See also

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
  GPL vs. AGPL decision, and how to apply a license (printed pp. 19–20). Detailed legal
  treatment deferred to Ch. 9 "Legal Matters."
