---
title: Free Software vs. Open Source
aliases: [open-source-definition, free-vs-open-source]
date: 2026-06-23
last_updated: 2026-06-24
type: topic
topics: [open-source-culture, open-source-governance]
roles: [tech-lead, product-engineer]
source_tier: 1
project: null
source_count: 1
status: active
---

# Free Software vs. Open Source

"Free software" and "open source" name the *same* software and the same licenses; they
differ in the **motive each foregrounds**. The distinction is not pedantic trivia — it
maps onto two communities of belief that coexist inside most projects, and understanding
it "is key to managing a project well" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=21), p. 8).

## The ambiguity in the word "free"

English collapses two ideas that other languages separate: *gratis* (zero price) and
*libre* (freedom to use, share, and modify). All free software is zero-cost — once a
recipient can redistribute at no charge, the price is "effectively driven to zero
immediately" — but **not all zero-cost software is free**: the 1990s browsers Netscape
and Microsoft gave away were no more free "than shrink-wrapped software bought in a store;
they merely had a lower price" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=19), p. 6).
The standard clarifying formula became *"It's free as in freedom — think free speech, not
free beer"* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=19), p. 6).

## Two camps, one codebase

The deeper split is moral vs. pragmatic. One camp takes Richard Stallman's view — that the
freedom to share and modify is the point, so "if you stop talking about freedom, you've
left out the core issue." The other holds that the software's **quality** is its strongest
argument and is "uncomfortable with proclaiming proprietary software inherently bad"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=19), p. 6).
In 1998 the term *open source* was coined by Christine Peterson, and the **Open Source
Initiative (OSI)** was formed explicitly as "a marketing program for free software" —
pitching it "on solid pragmatic grounds rather than ideological tub-thumping" because "talk
of morals and the social benefits of sharing would never fly in corporate boardrooms"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=20), p. 7).

The practical resolution is that the **contribution trumps the contributor**: most projects
contain programmers from both camps, so "it is rare for a free software / open source
developer to openly question the basic motivations of others." Work is evaluated "on
technical grounds, and respond[ed] on technical grounds," regardless of whether its author
is paid, ideological, or résumé-building ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=21), p. 8).
This norm is the cultural keystone treated in [[open-source-culture]].

## Why the history matters

Fogel's book is "a practical guide, not an anthropological study," but argues that "a
working knowledge of the origins of today's free software culture is an essential
foundation for any practical advice" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=16), p. 3).
The compressed arc:

- **Early sharing was the default.** When hardware was the only asset worth protecting,
  manufacturers "tolerated and even encouraged" customers swapping patches, because better
  software made the hardware more attractive ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=16), p. 3).
- **Proprietary enclosure.** As high-level languages let one program run on many machines,
  software — not hardware — became the differentiator. Suppliers "clamped down," denying
  source access or imposing non-disclosure agreements ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=17), p. 4).
- **Conscious resistance.** Stallman left MIT's AI Lab to found the GNU Project and Free
  Software Foundation, and wrote the **GNU General Public License (GPL)** — "a clever piece
  of legal judo" that uses copyright to force the opposite of copyright: copies and
  derivative works, *if distributed at all*, must carry the same license, so no one "even
  the author" can re-close the code ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=17), p. 4).
  This reciprocal ("copyleft") mechanism is developed under [[copyleft]] / [[open-source-licensing]] (Ch. 9).
- **Accidental resistance.** BSD, the X Window System, and Knuth's TeX produced major free
  software with *no* ideological program — driven by distributed volunteer effort, vendor
  self-interest in standardization, or one author's need for a better tool
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=18), p. 5).

The takeaway for a maintainer: the FSF's lasting contribution "was not only in the code
they wrote, but in their political rhetoric" — tying code to a message so that even
dissenters had to engage it ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=18), p. 5).

## Negative Space

- **GPL / license mechanics** (`foreshadowing`, now resolved): the reciprocal-vs-permissive
  license machinery is named here only as history; its developed treatment landed with Ch. 9 on
  [[copyleft]] / [[permissive-licensing]] / [[open-source-licensing]], not paged from this chapter.
- **History particulars** (`illustrative-scaffolding`): AT&T Unix, 386BSD-vs-Linux timing,
  Emacs/GCC adoption, the AI Lab's collapse — narrative illustration of the arc, compressed
  to the bullets above rather than paged.
- **The "free" trademark/branding debates** (`out-of-scope` for craft): the OSI-vs-FSF
  organizational politics beyond the managerial takeaway are movement history, not a
  practice a maintainer applies.

## See also

- [[open-source-culture]] — the cohesion norms ("influence ∝ contribution") this
  terminological truce rests on.
- [[open-source-governance]] — how the "contribution trumps contributor" ethic becomes
  concrete decision-making structure.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 1 "Introduction" —
  History; "Free" Versus "Open Source"; The Situation Today (printed pp. 1–8).
