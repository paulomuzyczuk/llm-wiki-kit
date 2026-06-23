---
title: Wikis
aliases: [project-wiki, wiki]
date: 2026-06-23
last_updated: 2026-06-23
type: topic
topics: [project-infrastructure, software-collaboration]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Wikis

A wiki offers the lowest possible barrier to contribution: click, edit, and the
software handles versioning, credit, notification, and publication. That openness
is the appeal and also the trap — a wiki magnifies whatever organizational
discipline (or its absence) is present from the start. This page captures the
*principles* of running a project wiki and the *decision criteria* for choosing
one; wiki markup and per-product administration are out of scope. The wiki is one
of the [[project-infrastructure]] surfaces and shares its spam problem with
[[message-forums]] ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=68), p. 55).

## Collaborative Editing Does Not Auto-Aggregate to Quality

Project wikis fail for two recurring reasons: lack of consistent organization and
editing (a mess of outdated, redundant pages) and lack of clarity about who a given
page's audience is. The governing fallacy to reject is that because many people
each add good content, the *sum* must also be good. It will not be: an individually
fine paragraph is not good if embedded in a disorganized whole. Quality is a
property of the structured whole, not the additive parts ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=69), p. 56).

The practices that follow from this ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=69), p. 56):

- **Establish organization and layout from the outset** so visitors instinctively
  know where their contribution fits.
- **Keep the intended audience visible** on every page.
- **Document the standards in the wiki itself** and point editors to them, so
  guidance has a home.
- **Prime the wiki with well-written content.** Contributors imitate the patterns
  in front of them, so the wiki amplifies early failings; seed it with a template
  to follow rather than setting it up and hoping.

Wikipedia is the shining example *and* a misleading one — it works because its
administrators laid a thorough foundation for cooperation (documentation, dispute
resolution, authorization controls) and because it commands editorial attention no
other wiki receives. The transferable lesson is not its scale but its deliberate
groundwork: getting strangers to tailor their writing to a common vision is
designed, not hoped for ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=69), p. 56).

## Never Allow Anonymous Editing

The era of open, anonymous wiki editing is over: any open wiki other than Wikipedia
"will be covered completely with spam in approximately 3 milliseconds." All edits
must come from registered users — configure the software to enforce this if it does
not by default — and even then watch for accounts registered under false pretenses
to spam. (Wikipedia is the exception only because of its unusual editor volume and
a funded anti-spam organization behind it.) This is the same mandatory-spam-
prevention posture that governs [[message-forums]] ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=69), p. 56).

## Choosing a Wiki: Default to the Built-In One

The decision criterion is integration over independence ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=69), p. 56):

- **If you are on a [[project-hosting]] site, use its built-in wiki.** It
  integrates automatically with your repository permissions and reuses the site's
  account system, so you avoid a separate registration surface (and a separate spam
  vector).
- **If self-hosting, favor a standardized markup over a wiki-specific one.**
  Prefer Markdown — which contributors already know from the hosting sites — so no
  one must learn a bespoke wiki syntax. Fogel advises *against* MediaWiki for most
  projects: its administration is tuned to Wikipedia's needs rather than a small
  editing community's, and its supposed familiarity advantage is largely illusory
  now that wikis trend toward rich-text editing and Markdown plugins are common.

## Negative Space

- **Named wiki software and comparison tools** (`tool-specific/perishable`):
  DokuWiki, MediaWiki, the WikiMatrix "Wiki Choice Wizard," and Wikipedia's
  comparison page are perishable references; the criteria (built-in first,
  Markdown over wiki syntax) are what generalize.
- **The Emacs Wiki bot-question countermeasure** (`illustrative-scaffolding`): a
  single example of allowing non-registered editing behind an anti-bot challenge;
  the rule (registered users only) is retained, the exception's mechanics are not.
- **Wiki markup syntaxes** (`too-granular`): the diversity of wiki markup dialects
  is configuration detail; the page keeps only the "prefer Markdown" decision.

## Sources

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch.3 "Technical
  Infrastructure" — "Wikis," "Wikis and Spam," and "Choosing a Wiki"
  (PDF pp. 68–70 / printed pp. 55–57).
- **Source entities:** [[producing-open-source-software-book]]

## See Also

- [[project-infrastructure]] · [[message-forums]] · [[project-hosting]]
