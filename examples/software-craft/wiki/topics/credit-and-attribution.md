---
title: Credit and Attribution
aliases: [credit, attribution, crediting-contributors, giving-credit]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-participation, open-source-culture]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Credit and Attribution

"Credit is the primary currency of the free software world." Where [[contributor-motivation]]
establishes that *attention* is what keeps people engaged, this page is about its recorded,
attributable form — credit — and the discipline of distributing it accurately. Fogel: "I don't
know many developers who would be happy doing all their work anonymously, or under someone
else's name"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=166), p. 153).

## Why credit has force

The motive is part tangible, part not. Tangibly, "one's reputation in a project roughly governs
how much influence one has," and participation "can also indirectly have monetary value, because
many employers now look for it on résumés" (the basis of [[hiring-open-source-developers]]).
Intangibly — "perhaps even more powerful" — "people simply want to be appreciated, and
instinctively look for signs that their work was recognized by others." Hence "the promise of
credit is therefore one of best motivators the project has. When small contributions are
acknowledged, people come back to do more"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=166), p. 153).

## Use the tools that already record who did what

The project's [[version-control|collaborative development software]] "keeps accurate records of
who did what, when"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=166), p. 153),
so credit should ride on those mechanisms — "and be specific about the nature of the
contribution." Don't write "Thanks to J. Random" when you could write "Thanks to J. Random… for
the bug report and reproduction recipe"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=167), p. 154).
Subversion ran "an informal but consistent policy of crediting the reporter of a bug" in the
ticket or the fixing commit's log message — distinct from the committer, whose name the VCS
already records. A survey found "a little over 10% of commits" credited someone by name, and
"slightly over two-thirds of people who later became committers themselves were credited in
this way… before becoming a committer." It doesn't prove causation, but "it surely can't hurt
to set up an atmosphere in which people know they can count on their contributions being
publicly acknowledged"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=167), p. 154).

## Routine acknowledgement versus special thanks

Credit and *thanks* are not the same act. Acknowledging work in the flow of discussion — "Daniel's
recent changes to the delta code mean we can now implement feature X" — both identifies the
change and credits him. But "posting solely to thank Daniel… serves no immediate practical
purpose," because the contribution is already recorded. "Thanks are effective largely by how much
they stand out from the default, background level of favorable comment," so indiscriminate thanks
causes **credit inflation** — the same dilution dynamic [[praise-and-criticism]] describes for
praise. Three guidelines keep thanks meaningful
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=167), p. 154):

- **The more ephemeral the forum, the freer you should feel to thank.** A passing thanks in chat
  or an aside in an email is fine; a standalone thank-you email, web-page gratitude, or thanks in
  code comments is not (the last "would only be a distraction from the primary purpose of
  comments").
- **The less involved someone is, the more appropriate it is to thank them.** Counterintuitive
  but deliberate: thanks marks someone contributing "even more than you thought she would," so
  constantly thanking regulars "would be to express a lower expectation of them than they have of
  themselves." (Exception: roles with periodic intense bursts, like the release manager.)
- **Gratitude should be specific.** "Don't thank people just for being great… Thank them for
  something they did that was out of the ordinary," and say why.

## The standing tension: individual credit vs. group effort

"There is always a tension between making sure that people's individual contributions are
recognized, and making sure the project is a group effort rather than a collection of individual
glories." There's no formula — "just remain aware of this tension and try to err on the side of
group, and things won't get out of hand"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=167), p. 154).

## Negative Space

- **The Contribulyzer / Subversion crediting-convention specifics** (`tool-specific/perishable`):
  the named tool and the exact 10.57%-of-commits figure are the project-specific instantiation of
  the durable claim — credit via the records you already keep, specifically — not concepts to page.
- **Thanks-inflation guidance overlap with praise** (`subsumed-by` [[praise-and-criticism]]): the
  "specific, sparing, don't-praise-the-normal" discipline is the same one praise-and-criticism
  develops; captured here only in its credit-specific form (routine acknowledgement vs. special
  thanks) and cross-linked rather than restated.

## See also

- [[contributor-motivation]] — attention as the underlying currency; credit is its recorded,
  attributable form.
- [[praise-and-criticism]] — the parallel discipline for feedback; both are diluted by inflation
  and both should be specific.
- [[hiring-open-source-developers]] — the résumé value that makes credit tangibly worth something.
- [[committers]] — the published roster (`MAINTAINERS`/`COMMITTERS`) as the formal counterpart to
  informal log-message credit.
- [[version-control]] — the records of "who did what, when" that credit should be built on.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 8 "Managing Participants" —
  §Credit (printed pp. 153–154).
