---
title: Translation Infrastructure
aliases: [i18n, l10n, internationalization, localization, translation-platform]
date: 2026-06-23
last_updated: 2026-06-23
type: topic
topics: [project-infrastructure, software-collaboration, open-source-participation]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Translation Infrastructure

Translation work in an open-source project means rendering not just documentation
but the software's run-time interface and error messages into different languages,
so each user can interact in their preferred language. Dedicated web-based
translation platforms exist to organize and integrate this work. This page captures
the *decision criteria* for using such a platform and the i18n/l10n terminology
needed to reason about it; specific platform mechanics are out of scope. It is a
[[project-infrastructure]] surface whose primary value is widening
[[open-source-participation]] to non-developer contributors ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=70), p. 57).

## When to Use a Translation Platform

A separate platform is **not strictly necessary** — translators could work
directly in the project's repository like any other developer. The decision
criterion is the contributor population, not the technology ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=70), p. 57):

- **Translation is a specialized skill held by people who often lack development
  expertise.** A dedicated platform removes the requirement that a translator be
  comfortable with the project's development tools, lowering the barrier to entry.
- **Translators' methods are roughly the same from project to project,** so the
  work is highly amenable to a purpose-built environment optimized for translation
  rather than general code development.

So the trade-off is: adopt a platform when you want to recruit linguistic
contributors who are not developers; skip it when your translators are already
comfortable in the repository.

## Choosing a Platform: Weigh Open-Source Against Convenience

Platform choice carries the same open-vs-proprietary tension as
[[project-hosting]]. Some zero-cost options for open-source projects are
proprietary; several fully open-source platforms also exist. The criterion Fogel
surfaces is contributor investment: translators may prefer to invest their time
learning a *fully open-source* platform rather than a proprietary one, even when
the proprietary option is free of charge — a consideration that parallels the
no-lock-in reasoning applied to hosting ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=70), p. 57).

## Internationalization (i18n) vs. Localization (l10n)

These two terms are easily confused and name distinct, sequential activities; both
are defined here because reasoning about translation infrastructure requires the
distinction ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=70), p. 57):

- **Internationalization (i18n)** — preparing the source code so the program *can*
  be translated: marking all user-visible strings so they can be automatically
  replaced by translated versions when the software is deployed in a "locale." i18n
  performs *no* actual translation; it puts the program into a form that lets
  localizers work. ("18" = the letters between the initial *i* and final *n*.)
- **Localization (l10n)** — supplying the actual translation into a specific
  language, plus the other adaptations a locale needs (measurement units, monetary
  units). It is "localization" rather than "translation" because it is broader than
  language, and its target audience is a *locale*, which need not map to any
  geography or polity (localizing for Yiddish says nothing about where or by whom
  the software runs, only that they know Yiddish).

The dependency is one-directional: l10n is impossible until i18n has exposed the
strings. i18n is the developer's enabling work; l10n is the localizer's
content work.

## Negative Space

- **Named translation platforms and the Transifex history**
  (`tool-specific/perishable`): Transifex, Lokalise, Weblate, Zanata,
  translatewiki, Launchpad Translations and the 2013 Transifex-went-proprietary
  episode are perishable references; the criteria (use a platform to recruit
  non-developer translators; prefer fully open-source for contributor buy-in) are
  what generalize.
- **Translation-manager role mechanics** (`foreshadowing`): the "Translation
  Manager" cross-reference points to Ch.8 management material, not developed here.

## Sources

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch.3 "Technical
  Infrastructure" — "Translation Infrastructure" and the "Internationalization
  (i18n) and Localization (l10n)" sidebar (PDF p. 70 / printed p. 57).
- **Source entities:** [[producing-open-source-software-book]]

## See Also

- [[project-infrastructure]] · [[open-source-participation]] · [[project-hosting]]
