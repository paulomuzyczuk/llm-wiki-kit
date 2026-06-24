---
title: Message Forums / Mailing Lists
aliases: [mailing-lists, discussion-forums]
date: 2026-06-23
last_updated: 2026-06-24
type: topic
topics: [project-infrastructure, software-collaboration]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Message Forums / Mailing Lists

A project's message forums are usually its most active communications channel and
its "medium of record." Because email-based mailing lists and web-based forums
have largely converged, Fogel uses the terms interchangeably to mean any
message-based forum where posts are threaded, people can subscribe, archives can
be browsed, and the forum is reachable by both email and web browser ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=48), p. 35).
This page captures the *decision criteria* for forums; per-feature mechanics
(header fields, Subject-prefix munging) are out of scope. The broader question of
*how* to communicate well in these forums belongs to Ch.6 (Communications) and is
forward-referenced below.

## When a Project Needs Dedicated Forums

**Decision criterion — defer until obviously needed.** A small, focused project
organized around a single repository can often get by on the email-gateway
features of its [[bug-tracking]] tool: when a non-bug topic comes up, someone
opens a ticket and discusses it there. If you think your project will be fine
without forums, skip them — it becomes obvious quickly if you do need them ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=48), p. 35).

Larger and more complex projects almost always benefit from dedicated forums, for
two reasons: many conversations are not attached to any specific bug, and the
larger the project the more important it is to keep the bug tracker focused on
actual bugs by giving everything else its own home ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=48), p. 35).

**The cross-accessibility minimum bar.** Modern forum systems must let users
subscribe by email *and* read on the web; cross-accessibility between the two is
now the minimum acceptable standard, not a luxury ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=48), p. 35).

**Guide newcomers to the right forum.** The forum is often a user's first contact
beyond the web pages, and before experiencing the forum she must first *find* the
right one. Give the project a prominent description of every public forum so
newcomers can choose where to read or post. The organizing principle is to
separate forums by audience and purpose — typically a user list, a developer
list, a low-traffic announcements list, an automated-notifications list, and a
private security list ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=48), p. 35).

## Choosing Forum Software

The point of evaluating forum software is to recognize that forum management is a
complex, largely-solved problem; you need not become an expert but should expect
it to claim your attention from time to time. Look for at least these capabilities
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=49), p. 36):

- **Both email- and web-based access** — subscribe and post by email, read and
  thread on the web.
- **Moderation features** — software support that makes human spam-checking of
  posts (especially first-time posts) manageable.
- **A rich administrative interface** — beyond spam moderation: removing obsolete
  / bouncing addresses and similar upkeep; weak admin tooling is a reason to
  switch.
- **Header manipulation** — adding or adjusting standard headers that subscribers'
  mail-filtering rules rely on.
- **Archiving** — storing all posts and making them available on the web.

## Spam Prevention Is Mandatory

A list with no spam prevention is quickly submerged into unusability, so
prevention is non-negotiable. It is two distinct functions: keeping spam *off* the
list, and keeping the list from becoming a *source* of harvestable addresses for
spammers ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=49), p. 36).

For filtering posts, three techniques are best used in tandem, in order of
increasing human cost ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=50), p. 37):

1. **Auto-allow posts from subscribers.** Cheap and effective — but posts that are
   *not* auto-approved must go to a moderation queue, never be discarded:
   non-subscribers should still be able to post (a question should not require
   subscribing), and even subscribers sometimes post from a different address.
   Email addresses are not a reliable identity.
2. **Run posts through spam-detection software.** Never perfect — there is a
   permanent arms race — but it greatly reduces what reaches the human queue, and
   any reduction in queue length is a saving of human time.
3. **Human moderation.** The last stage for mail that is neither auto-allowed nor
   filtered out. When confirming a sender, prefer to allow *all future* posts from
   them, not just the one — a valid poster is unlikely to turn spammer, and this
   steadily reduces the moderation burden.

**Use the moderation channel only for moderation.** Moderation is strictly for
removing spam and clearly misdirected posts — never for privately answering a
question that belongs on the list, even when you know the answer. Doing so
deprives the community of an accurate picture of what people are asking and of the
chance to answer or learn from the answer. (This is a special case of the Ch.6
principle of avoiding private discussions.) ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=50), p. 37)

## Archiving: Criteria for an Archiver

Every forum should be fully archived: new discussions routinely reference old
ones, search engines surface archived answers to strangers' problems, and
archives give new participants history and context. When choosing or configuring
an archiver, evaluate it against four properties ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=54), p. 41):

- **Prompt updating** — ideally a post is archived the instant it appears on the
  list; nightly batch updating is far too laggy for an active list.
- **Referential stability** — once a message lives at a URL it should stay there
  *forever*, even across rebuilds or restores. Stable URLs are what let search
  engines index the archive and let other documents (the bug tracker, project
  pages) link into it reliably.
- **Thread support** — you must be able to move from any message to its thread,
  and each thread should have its own URL.
- **Searchability** — search over bodies as well as authors and subjects; an
  archiver without search is close to useless.

## A Governance Lesson: Settle Tooling Debates Early

The "Great Reply-to Debate" — whether the list software should rewrite the
`Reply-to` header to redirect replies back to the list — is Fogel's canonical
example of an infrastructure choice with **no universally right answer.** The
substantive caution is that using technology to force collaboration can backfire:
rewriting `Reply-to` creates the "Can't Find My Way Back Home" problem for posters
who rely on that header, and worse, it violates users' learned expectation that
"reply to author" is private — leading to confidential replies landing
accidentally on the public list. Fogel's own mild preference is therefore to leave
the sender's `Reply-to` untouched ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=52), p. 39).

The transferable principle is procedural, not technical: **settle this kind of
debate one way early, then refuse to relitigate it.** Keep a canned, discussion-
ending response ready; never insist your choice is the only sensible one; note
that it is an old debate with good arguments on both sides; and when it inevitably
resurfaces, point people to the archived prior discussion rather than re-running
it ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=53), p. 40).

## Negative Space

- **The verbatim Scanley forum-description block** (`illustrative-scaffolding`): a
  full sample "here are our lists" announcement; the principle (separate forums by
  audience/purpose, describe them prominently) is captured without the sample
  text.
- **Header-management mechanics** (`too-granular`): the `List-Help` / `List-Id` /
  `List-Post` header set, `To`-vs-`Subject` filtering, and the Subject-prefix
  munging trade-off are configuration detail beneath the decision-criteria
  altitude of this page.
- **The full Reply-to mechanics and "Two Fantasies"** (`too-granular`): the
  header-rewrite specifics and speculative reply-to-list / per-subscriber features
  are mechanics; the governance lesson is what generalizes.
- **Named software and filters** (`tool-specific/perishable`): Discourse, Google
  Groups, SpamAssassin, Mutt, Evolution are perishable tool names cited as
  examples, not concepts.
- **Communicating well *within* forums** (`foreshadowing`): avoiding private
  discussions and conspicuous use of archives are developed in Ch.6
  (Communications), not here.

## Sources

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch.3 "Technical
  Infrastructure" — "Message Forums / Mailing Lists," including "Choosing the
  Right Forum Management Software," "Spam Prevention," "The Great Reply-to
  Debate," and "Archiving" (PDF pp. 48–54 / printed pp. 35–41).
- **Source entities:** [[producing-open-source-software-book]]

## See also

- [[project-infrastructure]] — the toolset forums are the primary discussion channel of.
- [[project-hosting]] — the canned-hosting site that typically provisions the lists.
- [[bug-tracking]] — the structured-state counterpart; the list is conversation, the
  tracker is state.
