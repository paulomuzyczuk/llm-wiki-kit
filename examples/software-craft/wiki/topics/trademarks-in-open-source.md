---
title: Trademarks in Open Source
aliases: [trademark, certification-marks, project-name-protection]
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

# Trademarks in Open Source

A **trademark** protects a project's *name and logo* — what others may call a thing — and is
entirely separate from the copyright license that governs the code itself. Fogel's headline:
"Trademark law as applied to open source projects does not differ significantly from trademark
law as applied elsewhere." This surprises people who assume that freely copyable code is
inconsistent with controlling a name or logo; "it is consistent, however"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=181), p. 168).

## What a trademark is — and isn't

Trademarks "are about truth in labeling and, to some degree, about endorsement." A trademarked
name or symbol lets an entity "signal, in an easily recognizable way, that they approve of a
particular product." (A **certification mark** is the variant an entity applies to *someone
else's* product to signal it meets the certifier's standards.) The load-bearing distinction:

> **Trademarks do not restrict copying, modification, or redistribution.** "Trademark is
> unrelated to copyright, and does not govern the same actions that copyright governs.
> Trademark is about what you may publicly call things, not about what you may do with those
> things nor with whom you may share them"
> ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=181), p. 168).

This is the whole reconciliation: an open source license grants freedom to *use* the code; a
trademark constrains only the *labeling* of the result. The two never collide because they
govern different actions. It is even consistent to license the logo *artwork* under a fully
free license while retaining the *trademark* on the logo — the copyright and the mark are
distinct rights over the same image.

## Two case studies, two outcomes

The book uses paired examples to show the boundary
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=181), p. 168):

- **Firefox → Iceweasel (enforcement).** Debian was free to *package* Firefox (it is free
  software) but needed Mozilla's permission to call it "Firefox" and use the Firefox logo —
  those are Mozilla's trademarks. When Debian's packaging changes left it unable to comply with
  Mozilla's trademark-usage requirements, Mozilla withdrew permission to use the name and
  branding. Debian did not have to drop the software; it "simply changed the name to
  'Iceweasel' and used a different logo." The underlying code stayed Mozilla's Firefox code,
  free to modify "because of the code's open source license."
- **GNOME logo → the fish-pedicure shop (non-enforcement).** A mobile fish-pedicure business
  used a modified GNOME logo (the foot turned into a fish). GNOME actively enforces its marks,
  but its director saw no infringement: the business was "so distant from what the GNOME
  Project does that there was no possibility of confusion … or dilution." And because GNOME's
  images are under a free copyright license, the company was "free to make their modifications
  … and display the results." No trademark violation (no confusion within GNOME's domain) and no
  copyright violation (the artwork is free)
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=182), p. 169).

The decision criterion for *enforcing* a mark is therefore the ordinary trademark test:
likelihood of confusion or dilution *within the project's own domain of activity* — not whether
the underlying material is free.

## A trademark is a non-forkable resource

The deeper governance point: registering and holding trademarks for an open source project is
legitimate, but the owner "should [not] do whatever they want with the marks, ignoring what
other participants … have to say." Fogel classes a trademark with the project's other
**"centrally-controlled non-forkable resource[s]"**: use it "in a way that harms a significant
portion of the project's community" and "expect complaints and pushback"; use it "in a way that
supports the goals of the project" and most participants will treat that use "as itself a form
of contribution"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=182), p. 169).
Unlike the code, the name cannot be forked away from an abusive holder — which is exactly why
its stewardship is a community-political matter (see [[forkability]]).

## Negative Space

- **Trademark registration/enforcement procedure** (`out-of-scope`): the legal mechanics of
  registering or litigating a mark are general trademark law; Fogel explicitly scopes the
  chapter as an introduction and points to specialist resources.
- **Iceweasel rename saga details** (`illustrative-scaffolding`): the specific Debian/Mozilla
  disagreement and its later resolution are cited to illustrate name-vs-code separation, not
  paged.
- **Fish-pedicure anecdote color** (`illustrative-scaffolding`): the memorable example carries
  the confusion/dilution test; the story itself is not a concept.

## See also

- [[forkability]] — trademarks as the canonical "centrally-controlled non-forkable resource";
  the name cannot be copied away the way the code can.
- [[open-source-licensing]] — trademark protection appears there as one license *aspect* (a type
  of attribution requirement); this page is the standalone legal regime.
- [[creative-commons-licensing]] — the GNOME case turns on artwork being under a free copyright
  license while the mark is retained; CC public licenses explicitly do *not* license trademark
  rights.
- [[software-patents]] — the paired Ch. 9b regime; unlike a trademark (rename and move on) or
  copyright (rewrite), a patent is "the only real threat" a project cannot route around.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 9 "Legal Matters" —
  "Trademarks" (truth-in-labeling and endorsement, certification marks, trademark vs. copyright),
  and the case studies "Mozilla Firefox, the Debian Project, and Iceweasel" and "The GNOME Logo
  and the Fish Pedicure Shop" (printed pp. 168–169).
