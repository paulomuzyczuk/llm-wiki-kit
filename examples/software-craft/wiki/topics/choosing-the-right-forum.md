---
title: Choosing the Right Forum
aliases: [forum-appropriateness, forum-routing, cross-link-between-forums, writer-responsible-culture, convergent-vs-divergent]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-communication]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Choosing the Right Forum

One of the trickiest parts of running a project is getting people to be deliberate about
*which venue* they use for a given conversation — tricky because it isn't obvious that it
matters: participants focus on what's being said, not on whether the forum lets other
interested parties take part ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=124), p. 111). This is the venue-selection
counterpart to [[facilitating-online-discussion]] (how to behave *inside* a thread) and a
sibling of [[scaling-project-communication]] (organizing communication structure as the
project grows).

## Match the Forum to the Conversation

Each forum has a shape that suits some conversations and not others ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=124), p. 111):

- **Real-time chat** is great for quick questions, opportunistic synchronization, and
  reminders — but a *poor* place to make project-wide decisions, because the participants
  are just whoever happened to be in the room, which depends on time zone and schedule.
- **The development mailing list** is the right place for formal project-wide decisions:
  it is archived and every interested party gets a chance to see and respond, even though
  email is worse than chat for quick back-and-forth.
- **A bug ticket** is a trap for scope creep. Because trackers are email-integrated,
  people treat an in-ticket discussion as if it were on the dev list — but anyone not
  already watching that ticket, or explicitly @-mentioned in, never learns it is happening.
  Topics that outgrow the single bug then get decided without the people who should have
  had a chance to weigh in.

## The Convergent-vs-Divergent Rule of Thumb

The fix is to encourage **conscious, intentional forum changes**: when a discussion grows
beyond its original venue's scope, someone should ask that it move to a more appropriate
forum (usually the main development list) ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=124), p. 111). Doing this yourself
isn't enough — you have to build a *culture* where everyone watches for forum
appropriateness and feels comfortable raising it, which means documenting the practice and
reminding people of it often, especially early on.

The decision heuristic: **if the conversation looks convergent, leave it where it is; if
it looks likely to diverge** — widening into philosophy about how the software should
behave, or design questions beyond the one bug — before it converges, ask that it move to a
better forum ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=124), p. 111).

## Cross-Link When a Discussion Moves

When a conversation moves, **cross-link both ends**: link to the new mailing-list thread
from the ticket, and mention the original ticket at the start of the new thread. This lets
someone following the ticket reach the later discussion, and lets someone who finds the
ticket a year later follow it to where the conversation went ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=124), p. 111). It is
also fine to paste the final summary of the list discussion back into the ticket (with a
link to the message containing it), so a later reader sees the conclusion without detective
work — the usual "two masters" duplication problem doesn't apply, because both archives and
ticket comments are treated as static anyway ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=125), p. 112).

## Writer-Responsible Culture

The person moving a discussion may find the cross-linking slightly laborious, but open
source is fundamentally a **writer-responsible culture**: it is more important to make
things easy for the tens or hundreds of people who may *read* the discussion than for the
three or five *writing* it ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=125), p. 112). This is the principle that
justifies all the small per-message efforts — cross-links, canonical references, archive
pointers — that fall on the writer for the reader's benefit.

## Negative Space

- **GitHub @-mention auto-subscribe mechanic** (`tool-specific/perishable`): the footnote
  that "@kfogel in a comment adds that person to the ticket's email thread" is platform
  mechanics; the conceptual point (people get pulled into ticket discussions) is captured.
- **"Two masters" data-duplication problem** (`subsumed-by`): named only to say it
  *doesn't* apply here; the general principle lives where data integrity is the topic, not
  on this page.

## See also

- [[facilitating-online-discussion]] — the paired skill: keeping the discussion itself
  productive once you're in the right forum.
- [[scaling-project-communication]] — splitting and organizing forums as the project grows
  (Strategy 1 there is the structural version of forum choice).
- [[message-forums]] / [[real-time-chat]] / [[bug-tracking]] — the venues being chosen
  between.

## Sources

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Chapter 6 "Communications" —
  §Choose the Right Forum, §Cross-Link Between Forums (PDF pp. 124–125 / printed pp. 111–112).
- **Source entities:** [[producing-open-source-software-book]]
