---
title: Evaluating Open-Source Projects
aliases: [project-evaluation, evaluating-projects, project-health-signals]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-participation, open-source-governance]
roles: [tech-lead, system-designer]
source_tier: 1
project: null
source_count: 1
status: active
---

# Evaluating Open-Source Projects

Launching a project is "inextricably linked to the problem of evaluating existing open source
projects." You "can't know whether you need to start a new project until you've evaluated what's
out there" (the "But First, Look Around" discipline of [[launching-an-open-source-project]]), and
even a new project "will usually still be building on existing open source components" and choosing
between competitors that "implement the same basic functionality." That choice "is not just a
technical choice; it's also about social health and general level of project maturity"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=104), p. 91).

Evaluation "is an art, not a science," but experienced people use shortcuts. Fogel reports that
when he applied these techniques and "then checked in with that project months or years later," he
"generally found its current status to be in line with what the evaluation predicted"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=104), p. 91); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=105), p. 92).
The unifying idea: **read the signals that reflect a living community, not the vanity metrics.**

## Look at bug-tracker activity first

"The most reliable reflections of project health can usually be found in the bug tracker." Look at
"the rate of issue filings and the number of unique filers (because that's a proxy for the size and
level of engagement of the user base)." Look at "how often project developers respond in bug
tickets, and at how they respond": are they constructive, do they "interact well with both the
reporter and with other developers," is responsiveness "well-distributed throughout the development
team," and are they "inviting technically promising reporters to try becoming contributors"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=105), p. 92).

A deliberate inversion of intuition: **"More bug reports is better"** (see [[bug-tracking]]), and the
**rate at which bugs are *closed* "is not as important as you might think."** "In a healthy project
with an active user base, bug reports are often filed faster than the development team can close
them, especially when the user base is growing. The relevant signal is not the rate of resolution,
but how project developers respond to and organize the influx of reports"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=105), p. 92).

## Measure commit diversity, not commit rate

"Look at the distribution of commits across committers, not just at the raw frequency of commits."
Commit rate "isn't very informative — knowing the number of commits per week could just tell you
that someone keeps making typos and then correcting them." The richer signal, if you have time to
read individual commits, is "how often one developer's commit is a response to (i.e., refers to)
some other developer's previous commit. This tells you that group code review is going on, and the
more of that you see, the better the project is doing"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=105), p. 92).
This is the [[code-review]] signal read from the outside, via [[version-control]] history.

## Evaluate organizational diversity

Beyond individual identities, "see if you can tell how many different organizations are
participating — in particular, commercial organizations. If a number of different sources of money
are all investing in a project, that's a sign that that project is going to be around for the long
term." Fogel ties this to the **"bus factor"** discussed under social and political infrastructure
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=105), p. 92).
The economic reading of this signal is [[open-source-economics]]: multiple funders mean shared
maintenance burden and resilience to any one backer leaving.

## Discussion forums, news, and releases

- **Discussion forums.** Scan them "for signs of a functional community." On a long thread,
  "spot check responses from core developers coming late in the thread. Are they summarizing
  constructively, or taking steps to bring the thread to a decision while remaining polite?" A lot
  of "flame wars" is a warning that "energy is going into argument instead of into development"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=105), p. 92).
- **News, announcements, and releases.** "Any project that is functioning well will usually have
  made announcements within the past few months" — check the front page, news feed, microblog
  accounts. "If things are quiet on stage, they're probably quiet backstage too"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=105), p. 92).

## Reading the two sides of a fork

Fogel found these signals "particularly useful when evaluating the two sides of a recent fork.
Even in a recent fork, it is often possible to tell, just by looking at some of the signals
described above, which side will flourish over the long term"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=105), p. 92).
This is the practical companion to [[forkability]]: when a project does split, the same
community-health reading predicts the winner.

## Negative Space

- **The "art, not science" disclaimer beyond the listed signals** (`supporting-argument`): Fogel
  frames the list as "a brief introduction"; the durable signals are captured, the hedge is not a
  separate concept.
- **Specific channels named (Twitter / microblog accounts)** (`tool-specific/perishable`): cited as
  example places to check for news; the principle ("recent public activity = health") is what
  carries.

## See also

- [[bug-tracking]] — the primary health signal; why "more bug reports is better" and why close-rate
  misleads.
- [[version-control]] — where commit-diversity and commit-as-review-response signals are read.
- [[forkability]] — evaluating which side of a fork will flourish using these same signals.
- [[open-source-economics]] — why organizational diversity (multiple funders) predicts longevity.
- [[launching-an-open-source-project]] — "But First, Look Around": evaluation is the precondition for
  deciding to start anything new.
- [[hiring-open-source-developers]] — the same forensic reading of public activity, applied to a
  candidate rather than a project.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 5 "Organizations and Money" —
  "Evaluating Open Source Projects" (printed pp. 91–92).
