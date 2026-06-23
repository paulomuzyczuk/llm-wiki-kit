---
title: Government and Open Source
aliases: [government-open-source, public-sector-open-source, open-source-in-government]
date: 2026-06-23
last_updated: 2026-06-23
type: topic
topics: [open-source-economics, open-source-governance]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Government and Open Source

Most of the advice for organizations funding open source applies to government agencies too —
but "government is different," in structural ways that change how the advice must be applied.
Fogel's claim, drawn from working with U.S. federal, state, and municipal agencies, is that
the principles still hold; agencies simply need "certain adjustments… to compensate for the
structural idiosyncrasies"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=83), p. 70).

## Government is structurally different

Four traits set public-sector organizations apart from individuals and private firms
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=83), p. 70):

- **They don't try to retain technical expertise in-house** — "that's what contractors are
  for." This collides with [[corporate-open-source-participation]]'s "hire for the long term,"
  whose entire premise is keeping developers around to accumulate credibility.
- **Procurement and employment policies are "labyrinthine and… inflexible,"** which "can make
  it difficult for a government agency to be nimbly responsive in an open source development
  community."
- **They are "unusually risk-averse."** Somewhere above sits an elected official who
  "reasonably, sees an open source project as just another exposed surface for opponents to
  attack" — because "when development happens in public, the inevitable false starts and wrong
  turns are also public."
- **They "hunger for well-timed and well-controlled publicity events."** The complement of
  risk-aversion: officials know "most people aren't paying much attention most of the time," so
  they want the rare moments of attention to "see something good" — which can push actions
  earlier or later than project health warrants.

"There are good reasons for all of these things; they've been true for decades or even
centuries, and they're not going to change" — so the burden of adjustment falls on how the
project is run, not on the agency's structure
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=83), p. 70).

## Open-source from day one is especially important for government

[[developing-in-the-open]]'s case against opening a project late applies "especially" to
government code. Because "elected officials and those who work for them are understandably
sensitive to negative public comments," even a conscientious team opening previously-closed
code lives under "a worrying cloud of uncertainty… How can they ever know they've got it all
cleaned up?" That worry "is an energy drain: it causes the team to spend time chasing down
ghosts," and "unconsciously avoid steps that might risk revealing real problems." Crucially,
while private firms "sometimes have competitive reasons to stay behind the curtain until their
first release," government projects "should not have that motivation for starting out closed,
at least in theory, and they have even more to lose"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=84), p. 71).

## The key adjustment areas

Rather than special rules, Fogel points government readers to the handful of chapter sections
that matter most for compensating for the structural traits above
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=83), p. 70):

- Updating RFI / RFP / contract language and Open Source Quality Assurance (OSQA) — both
  developed in [[open-source-contracting]], and especially load-bearing given that government
  agencies rely on contractors rather than in-house staff.
- "Don't Surprise Your Lawyers"; "Open Source and Freedom from Vendor Lock-In"; "Dispel Myths
  Within Your Organization"; "Don't Let Publicity Events Drive Project Schedule"; and "The Key
  Role of Middle Management" — sections later in Ch.5, not yet ingested.

The throughline: a government agency's *defaults* (outsourced expertise, slow procurement,
risk-aversion, publicity sensitivity) all push toward the failure modes the rest of the book
warns against, so the agency must consciously counter each one.

## Negative Space

- **Specific resource sites** (`tool-specific/perishable`): 18F, David A. Wheeler's site, Ben
  Balter's post — named as "good starting points," explicitly perishable and U.S.-centric;
  captured as "external resources exist," not paged.
- **Later Ch.5 government sections** (`foreshadowing`): "Dispel Myths Within Your
  Organization," "The Key Role of Middle Management," "Don't Let Publicity Events Drive Project
  Schedule" (printed pp. 85–88) fall in a later batch; listed as adjustment areas, developed
  when ingested.

## See also

- [[developing-in-the-open]] — the open-from-day-one argument this page intensifies for
  government; exposure events are especially damaging in public-sector projects.
- [[open-source-contracting]] — RFP language and OSQA, the adjustment areas most relevant to
  contractor-dependent agencies.
- [[open-source-economics]] — the general funder economics that government participation is a
  special case of.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 5 "Organizations and Money" —
  "Governments and Open Source," "Being Open Source From Day One is Especially Important for
  Government Projects" (printed pp. 70–71).
