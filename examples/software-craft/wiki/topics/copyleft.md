---
title: Copyleft (Reciprocal Licensing)
aliases: [reciprocal-licensing, share-alike, viral-license]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-licensing, open-source-culture]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Copyleft (Reciprocal Licensing)

A **copyleft** (or *reciprocal*) license "not only grants the freedoms under discussion
here but furthermore requires that those freedoms apply to any derivative works." The
canonical example is the GNU General Public License (GPL), which stipulates that any
derivative work must also be licensed under the GPL
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=173), p. 160).
Its opposite is the [[permissive-licensing]] (non-reciprocal) family, which grants the same
freedoms but does **not** require derivatives to stay free.

## The sharpest dividing line in licensing

Of all the dimensions on which licenses vary (see [[open-source-licensing]] §*What licenses
vary on*), the one that matters most is "between proprietary-incompatible and
proprietary-compatible licenses, that is, between the copyleft licenses and everything
else"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=174), p. 161).
A copyleft license forbids the covered code being absorbed into a closed-source program; a
permissive one permits it. Every other licensing distinction is secondary to this one.

## How reciprocity works: freedom made contagious

Because the GPL's authors' primary goal is the promotion of free software, they "deliberately
crafted the license to prevent proprietary programs from being distributed with GPLed code in
them." Two requirements do the work
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=175), p. 162):

1. **Any derivative work** — any work containing a nontrivial amount of GPLed code — "must
   itself be distributed under the GPL."
2. **No additional restrictions** may be placed on redistribution of the original or a
   derivative work. The exact language: *"You may not impose any further restrictions on the
   exercise of the rights granted or affirmed under this License."*

Through these two clauses "the GPL makes freedom contagious": once code is GPL-licensed, the
reciprocal terms "are passed on to anything else the code gets incorporated into, making it
effectively impossible to use GPLed code in closed-source programs"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=175), p. 162).
Some call this property *viral*; Fogel prefers **reciprocal** — "more descriptive and less
connotative of disease"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=175), p. 162).

The second clause has a side effect: the "no further restrictions" language makes the GPL
**incompatible with certain other free licenses** — typically those that add their own
requirement, such as a credit clause. From the FSF's point of view this second-order
consequence is desirable, since it nudges other projects toward the GPL too. The practical
upshot is a license-choice constraint, developed under [[license-compatibility]]
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=175), p. 162).

## The copyright holder is special

A common misunderstanding is that licensing under the GPL or AGPL obliges you to hand source
to anyone who asks. It does not. "If you are the sole copyright holder in a piece of software,
then you are not bound by the copyright terms you chose, because (essentially) you can't be
forced to sue yourself for copyright infringement." You can enforce the terms on others, but
decide for yourself whether they apply to you — you never "distributed" the software to
yourself, so the redistribution requirements never attach
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=177), p. 164).

This holds only while you own the *whole* copyright. Once you incorporate others' GPL/AGPL
code and distribute the result, you are no longer the sole holder and are "as bound by the
original terms as anyone else"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=177), p. 164).
This asymmetry is the legal hinge that makes [[proprietary-relicensing]] possible — the
owner-only exemption a company exploits to sell a closed version of its own copyleft code
(Ch. 9b).

## Tuning reciprocity strength: LGPL and AGPL

Copyleft is not all-or-nothing; the GNU family offers variants that dial reciprocity up or
down for specific situations
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=176), p. 163):

- **LGPL (Lesser GPL) — weaker reciprocity, for libraries.** When a library is meant to be
  linked into other programs, full GPL reciprocity may be too strong. The LGPL "has weaker
  reciprocity requirements than the GPL, and can be mixed more easily with non-free code."
  Use it when strategy calls for adoption even inside proprietary programs — e.g. "when you're
  trying to unseat a competing, proprietary library that offers the same functionality."
- **AGPL — reciprocity extended to network use.** The plain GPL is triggered by
  *distribution*; hosted "cloud" services let a provider modify GPLed code yet never
  distribute it, escaping the share-back obligation. The Affero GPL (2007) "is just the GPL-3.0
  with one extra clause about network interaction" — a *Remote Network Interaction* clause
  requiring that users interacting with a modified version "remotely through a computer
  network" be offered its Corresponding Source. The FSF recommends the AGPL "for any software
  that will commonly be run over a network"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=177), p. 164).

## Don't fight the "is the GPL really free?" holy war

Choosing the GPL invites a recurring dispute: because copyleft restricts *how* you
redistribute (you may not relicense), some argue it is "less free" than permissive licenses,
and therefore worse. Fogel flags this as a classic holy war (see [[facilitating-online-discussion]])
and advises maintainers to refuse it in project forums: "Don't attempt to prove that the GPL
is less free, as free, or more free than other licenses. Instead, emphasize the specific
reasons your project chose" it — recognizability, or the enforcement of freedom on derivative
works
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=178), p. 165).
His own view, offered as an aside: "The only restriction the GPL imposes is that it prevents
people from imposing further restrictions" — so calling that *less* freedom "has always seemed
perverse"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=178), p. 165).

## Reciprocity beyond code: ShareAlike and selling exceptions (Ch. 9b)

Two Ch. 9b developments extend the copyleft idea in opposite directions:

- **ShareAlike is copyleft for *content*.** Creative Commons' ShareAlike element applies the same
  "derivatives must stay equally free" rule to non-code works (documentation, art, media): an
  adaptation must carry "a Creative Commons license with the same License Elements … or a BY-SA
  Compatible License"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=188), p. 175).
  The copyleft principle is license-family-agnostic — see [[creative-commons-licensing]].
- **Copyleft is the *only* license family you can "sell exceptions" to.** Because the reciprocal
  terms are what a downstream proprietary user needs waived, the sole-copyright-holder exemption
  above is exactly what a company exploits to offer a paid proprietary version of its own
  copyleft code. There is nothing to sell under a permissive license. The scheme and its
  community costs are developed in [[proprietary-relicensing]]
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=179), p. 166).

## Negative Space

- **Full GPL clause text / per-clause walkthrough** (`too-granular`): the page captures the
  two load-bearing requirements and their effect, not the license's complete wording.
- **The "or any later version" decision** (`subsumed-by`): the licensor's choice of whether to
  grant downstream the option to use future GPL versions is a *choosing*-time decision, captured
  on [[open-source-licensing]] rather than here.
- **Linux-kernel-on-GPLv2-without-"or-later" example** (`illustrative-scaffolding`): Torvalds'
  refusal to move to GPLv3 illustrates the "or any later version" choice; the principle, not the
  case, is retained.
- **"viral" pejorative debate** (`supporting-argument`): the connotation argument is reduced to
  Fogel's term preference ("reciprocal"), not reproduced as a position piece.
- **GPL-2.0 vs GPL-3.0 migration mechanics** (`too-granular`): version-shifting steps belong to
  applying a license, not to the copyleft principle.

## See also

- [[permissive-licensing]] — the non-reciprocal opposite; the two together are the primary
  license-type split a project chooses between.
- [[license-compatibility]] — why the "no further restrictions" clause makes the GPL
  incompatible with some otherwise-free licenses, and the GPL-compatibility choice criterion.
- [[open-source-licensing]] — the anchor: terminology, what licenses vary on, and how to choose.
- [[forkability]] — copyleft guarantees the *right* a fork relies on, even against the original
  author's wishes.
- [[free-software-vs-open-source]] — Stallman's GPL "legal judo" as the origin of copyleft.
- [[proprietary-relicensing]] — the business scheme the sole-copyright-holder exemption enables;
  "selling exceptions" works only on copyleft code.
- [[creative-commons-licensing]] — ShareAlike as copyleft transposed from code to content.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 9 "Legal Matters" —
  "Aspects of Licenses" (reciprocal/copyleft definition), "The GPL and License Compatibility"
  (the two requirements, freedom contagious, reciprocal vs. viral), "The GNU General Public
  License" (LGPL for libraries, the AGPL for server-side code), "The Copyright Holder Is
  Special," and "Is the GPL Free or Not Free?" (printed pp. 160–165).
