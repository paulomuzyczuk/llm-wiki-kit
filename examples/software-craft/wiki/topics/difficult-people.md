---
title: Handling Difficult People
aliases: [handling-difficult-people, obstructionists, filibuster, sealioning]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-communication, open-source-governance]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Handling Difficult People

A "difficult" person is **not the same as a rude one** — and the distinction is the whole
point. Rude people are merely annoying, and the handling is already covered: name the
rudeness the first time, then either ignore them or treat them like anyone else. If they
persist, they usually make themselves unpopular enough to lose all influence, so rudeness
is *self-containing* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=117), p. 104). This pairs with the
"Recognizing Rudeness" treatment in [[written-communication]] and the "nip rudeness in the
bud" discipline in [[setting-the-tone]]: those handle rudeness; *this* page handles the
harder case.

The genuinely difficult are people who are **not overtly rude but who manipulate or abuse
the project's processes** in ways that cost others time and energy without benefiting the
project ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=117), p. 104). This is more insidious than rudeness
because neither the behavior nor its damage is obvious to casual observers — a property
that shapes the entire response.

## The Pattern: Hunting for Wedgepoints

Difficult people look for **wedgepoints** in the project's procedures to gain more
influence than they would otherwise have ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=117), p. 104). Two classic forms:

- **The filibuster** — someone, always sounding as reasonable as possible, keeps insisting
  the matter "isn't ready for resolution" and floats more and more possible solutions or
  new angles on old ones, precisely *because he senses a consensus or ballot is about to
  form and dislikes where it's headed* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=117), p. 104). A named
  subspecies is **sealioning**: repeated insistence that more evidence is needed, or
  endless ostensibly-clarifying questions whose real purpose is delay ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=117), p. 104).
- **Obstructing the summary** — when a non-converging debate is at least being summarized
  so everyone can refer to the points of disagreement, the obstructionist (foreseeing an
  unwelcome result) relentlessly complicates *what should go in the summary*, objecting to
  reasonable suggestions or injecting unexpected new items ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=117), p. 104).

Because these maneuvers exploit consensus and voting procedures directly, difficult people
are a standing threat to [[open-source-governance]]'s decision-making — the manipulation
targets exactly the moment a decision is about to crystallize.

## Understanding the Mentality

Countering the behavior starts with understanding it, and the key insight is that **people
generally do not do this consciously** — no one resolves to "cynically manipulate
procedural forms to be an irritating obstructionist" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=117), p. 104). The
behavior is usually prompted by **insecurity** — a feeling (not necessarily grounded in
reality) of being shut out of group decisions, of not being taken seriously, in severe
cases of an imagined conspiracy or exclusive club. That feeling justifies, in the person's
own mind, interpreting rules with maximum literalness and formally manipulating procedure
so that everyone is *forced* to take him seriously; in the extreme, he believes he is
fighting a lonely battle to save the project from itself ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=118), p. 105).
This is why the handling strategy avoids accusation: the person is not a cartoon villain
but someone acting out insecurity.

## The Handling Strategy

Two structural facts govern the response: not everyone notices the attack at the same time
(some won't see it without strong evidence), so neutralizing it means *marshaling enough
evidence to persuade others*, not just yourself — and then distributing that evidence
thoughtfully ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=118), p. 105). The steps:

1. **Often, just tolerate it.** Because fighting is so much work, treat a mild case like a
   *parasitic but mild disease*: if it isn't too debilitating, the project can stay infected,
   and the "medicine" may have worse side effects than the disease ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=118), p. 105).
2. **When it gets too damaging, build a case on neutral, quantitative data.** Start
   gathering notes on the patterns, *including references to public archives* — one of the
   reasons projects keep records is exactly this ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=118), p. 105).
3. **Ask before you tell.** Have private conversations with other participants, but first
   ask what *they've* observed rather than announcing your conclusion. This is your last
   chance at unfiltered feedback — once you start openly naming the problem, opinion
   polarizes and no one can recall what they used to think ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=118), p. 105).
4. **If others see it too, act — cautiously, and never accuse.** It is easy for this kind
   of person to make *you* look like the aggressor. Never charge them with maliciously
   abusing procedure, paranoia, or the other things you privately suspect. Your strategy is
   to *appear more reasonable and more concerned with the project's overall welfare than
   they are*, aiming to either reform the behavior or get the person to leave permanently
   ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=118), p. 105). Gathering allies privately first may help — or
   may backfire as an improper "whispering campaign," depending on the people involved.

The governing caution: although the other person is the one behaving destructively, **you**
will look destructive if you make a public charge you can't back up. Have plenty of
examples, say it *as gently as possible while still being direct*, and remember the goal is
not to persuade the difficult person — *that's okay as long as you persuade everyone else*
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=118), p. 105). The evidence-first, accuse-never method is the same
quantitative move that defeats the [[facilitating-online-discussion]] "Noisy Minority"
effect: let the numbers and the archive record reshape others' perception, rather than
asserting bad intent.

## Negative Space

- **The Subversion "Energy Sink" case study** (`case-study-specifics`) — Brian Fitzpatrick's
  private mail showing "J. Random" as the third-most-active poster despite no code or
  documentation; the *generalizable method* (a case built on neutral archive data) is
  captured above, the specific names, dates, and poster counts are not.
- **Amy Hoy's "Help Vampires" essay** (`source-underdeveloped`) — cited in a footnote as a
  vivid description of one difficult-person subspecies; a pointer, not a developed treatment.
- **Codes-of-conduct escalation** (`subsumed-by` [[setting-the-tone]]) — for behavior that
  goes beyond what this page covers, Fogel defers to the Codes of Conduct mechanism, treated
  with project-tone setting rather than duplicated here.

## See also

- [[written-communication]] — the "Recognizing Rudeness" pair: rudeness is self-containing;
  difficult people are the harder, process-manipulating case.
- [[facilitating-online-discussion]] — ordinary unproductive threads vs. deliberate
  obstruction; the noisy-minority counter uses the same quantitative move.
- [[open-source-governance]] — the consensus and voting processes that obstructionists target
  at the moment a decision is about to form.
- [[setting-the-tone]] — codes of conduct, the escalation path for behavior beyond what this
  page's gentle-but-direct method handles.

## Sources

- Karl Fogel, *Producing Open Source Software* (2nd ed., v2.3300), Chapter 6
  "Communications" — §Difficult People, §Handling Difficult People (incl. the Case study
  setup), PDF pp. 117–118 (printed pp. 104–105).
- **Source entities:** [[producing-open-source-software-book]]
