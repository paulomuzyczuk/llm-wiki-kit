---
title: Creative Commons Licensing
aliases: [cc-licenses, cc-by-sa, creative-commons, content-licensing]
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

# Creative Commons Licensing

**Creative Commons (CC) public licenses** are the content-world counterpart to open source
software licenses: "a standard set of terms and conditions that creators and other rights
holders may use to share original works of authorship and other material subject to copyright."
They apply the same copyright-permission model — a licensor grants the public defined freedoms —
to the *non-code* assets of a project: documentation, images, logos, and media. This book is
itself published under one: the **Creative Commons Attribution-ShareAlike 4.0 International
License (CC BY-SA 4.0)**
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=185), p. 172).

## A CC license is composed of named elements

A Creative Commons license is built from **License Elements** — "the license attributes listed
in the name of a Creative Commons Public License." The two elements of CC BY-SA are
**Attribution (BY)** and **ShareAlike (SA)**
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=186), p. 173).
In the license's own summary, the work is free "to Share — to copy, distribute and transmit"
and "to Remix — to adapt," under two conditions
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=185), p. 172):

- **Attribution.** You must credit the work "in the manner specified by the author" — but not in
  any way suggesting endorsement of you or your use.
- **ShareAlike.** "If you alter, transform, or build upon this work, you may distribute the
  resulting work only under the same, similar or a compatible license."

The licensor's grant is "worldwide, royalty-free … irrevocable," and the licenses are designed
to be permanent: "Our licenses are irrevocable"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=185), p. 172).

## ShareAlike is copyleft for content

ShareAlike is the direct analogue of [[copyleft]]'s reciprocity, transposed from code to
creative works. Adaptations may not be locked down: "The Adapter's License You apply must be a
Creative Commons license with the same License Elements, this version or later, or a BY-SA
Compatible License"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=188), p. 175).
A **BY-SA Compatible License** is one "approved by Creative Commons as essentially the
equivalent of this Public License." The same "freedom made contagious" logic that the GPL
applies to derivative code, CC BY-SA applies to derivative content — which is why it, not a
permissive CC variant, is the natural choice for a project (or book) that wants its
documentation to stay as free as its code.

## CC licenses cover copyright only — not patents or trademarks

A decision-relevant boundary: a CC license grants copyright permissions and "certain other
rights" *only*. Explicitly, **"Patent and trademark rights are not licensed under this Public
License"**
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=187), p. 174).
This is exactly the separation that lets the [[trademarks-in-open-source|GNOME case]] work:
artwork released under a free copyright license can still carry a retained trademark, because
the content license never touched the mark. The same carve-out keeps CC distinct from
[[software-patents]] concerns. (Moral, publicity, and privacy rights are likewise outside the
grant.)

## When to use CC (decision criteria)

The governing principle the book *demonstrates by example*: **license a project's code under an
OSI-approved software license, and its non-code creative works under a Creative Commons license.**
CC public licenses are "intended for use by those authorized to give the public permission to
use material in ways otherwise restricted by copyright" — the natural fit for prose, diagrams,
art, and media rather than executable code. Choose the BY-SA combination when you want
attribution preserved *and* downstream adaptations kept equally free; the standard CC guidance
applies (the licenses are irrevocable, so the licensor "should read and understand the terms …
before applying," and "should secure all rights necessary before applying")
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=185), p. 172).

## Negative Space

- **Full CC BY-SA 4.0 legal text** (`book-metadata`): the appendix reproduces the complete
  public-license deed (Definitions, Scope, License Conditions, Disclaimer, Term, Interpretation);
  this page captures the load-bearing concepts — license elements, ShareAlike reciprocity, the
  patent/trademark carve-out — not the section-by-section legalese.
- **The wider CC element menu (NonCommercial, NoDerivatives)** (`source-underdeveloped`): the
  source reproduces only the BY-SA license actually applied to the book, so the full family of
  CC elements (and the fact that NC/ND variants are *not* "free" in the FSD/OSD sense) is outside
  what this source grounds; noted, not synthesized.
- **Sui Generis Database Rights / Effective Technological Measures definitions**
  (`too-granular`): jurisdiction-specific defined terms in the deed, not project-level decision
  criteria.
- **30-day cure / automatic-reinstatement mechanics** (`too-granular`): a termination detail of
  the deed, subordinate to the license-choice decision this page serves.

## See also

- [[copyleft]] — ShareAlike is the content-side analogue of GPL reciprocity; both make freedom
  contagious to derivatives.
- [[permissive-licensing]] — the non-reciprocal alternative for code; a CC BY (attribution-only)
  license is the rough content analogue, where keeping derivatives free is not required.
- [[trademarks-in-open-source]] — CC's patent/trademark carve-out is what lets free artwork
  coexist with a retained mark (the GNOME logo case).
- [[software-patents]] — the regime CC explicitly does not license.
- [[open-source-licensing]] — the software-license decision CC complements for a project's
  non-code assets.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Appendix A "Copyright" — the
  Creative Commons Attribution-ShareAlike 4.0 International Public License under which the book
  is released: the license summary, "Using Creative Commons Public Licenses," License Elements
  (§1g), the patent/trademark exclusion (§2(b)(2)), and the ShareAlike condition (§3(b))
  (printed pp. 171–175).
