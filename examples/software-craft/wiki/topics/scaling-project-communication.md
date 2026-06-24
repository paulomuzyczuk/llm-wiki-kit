---
title: Scaling Project Communication
aliases: [handling-growth, communication-scalability, conspicuous-archives, codifying-tradition, treat-resources-like-archives]
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

# Scaling Project Communication

As a project gets more popular the number of people seeking information rises far faster
than the number able to provide it, and the usual open-source model of *massively
parallelized support* — everyone watching one forum, learning by observing exchanges —
does not scale ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=119), p. 106). This page covers how to absorb that
growth: split forums before they choke, and make information durable, findable, and
self-service so the average reader finds what they need *without asking*. It is the
infrastructure-side complement to [[facilitating-online-discussion]] (in-thread
behaviour) and [[choosing-the-right-forum]] (venue selection).

## The Scalability Problem and the Quiet Failure Mode

A user/discussion mailing list works well up to a few thousand users or a couple of
hundred posts a day; past that it breaks down, because *every subscriber sees every
post*, so once daily volume exceeds what a reader can process the list becomes a burden
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=119), p. 106). The same logic governs chat rooms and any
forum where a group hears questions from individuals.

The failure is not an explosion but a **quiet negative-feedback effect**: experienced
people rationally unsubscribe or stop asking because they can see they won't be heard in
the noise, so activity *appears* to stay manageable — precisely because the capable
people have left and the inexperienced stay behind. A side effect of running an
unscalable model as you grow is therefore that the *average quality of communication
falls* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=120), p. 107). The two strategies below counter it.

## Strategy 1 — Split Forums Before They Choke

Recognize when *parts* of a forum are not suffering unbounded growth even though the
whole is, and separate those parts into specialized forums — "don't let the good be
dragged down by the bad" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=120), p. 107). Most projects start with one
general list on which design, "how do I X?" user questions, and bug-processing threads
all mix; over time these resolve into distinct topic families with little cross-over,
which means they can be divided into separate forums *without harmful balkanization* —
the test is that threads rarely cross the topic boundary.

Division is two steps: create the new venue, then spend whatever time it takes *gently
and visibly* nagging people to use it — always telling a sender when a post went to the
wrong place, and doing so in public so others learn to help route. A web page listing all
forums lets responses just link to the guide ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=120), p. 107).

## Strategy 2 — Make Information Durable and Findable

The second strategy is an ongoing, project-lifetime process: keep many automated sources
of information available, organized, current, and easy to find, so that the percentage of
readers who must *ask* keeps dropping ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=120), p. 107). The next three
sections are its mechanics.

### Conspicuous Use of Archives

Nearly all project communication except private chat is archived, and the archives are
public, searchable, and have **referential stability**: once information sits at a URL it
stays there forever ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=120), p. 107). Use them as much *and as
conspicuously* as possible: even when you know an answer, if it's in the archives, dig it
up and link it. Each visible reference teaches someone the archives exist, reinforces the
norm against duplicating information (one answer in one place is easier to re-find), and
strengthens the resource's search-engine ranking. When an archived answer has gone stale,
the classiest fix is to post a new complete answer and *explicitly obsolete* the old one
by linking it — since no archiving software offers an "obsoleted-by" tag
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=121), p. 108).

The archives' value goes beyond technical answers: **if a project's formal guidelines are
its statutory law, the archives are its common law** — a record of every decision and how
it was reached. Re-opening a recurring discussion without first searching the archives is
now effectively obligatory; cite the prior threads even if they went nowhere, both to show
you did your homework and to prove you're adding something new ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=121), p. 108).

### Treat All Resources Like Archives

The same organizing principle — every piece of information at a stable, findable address
(permalink) — applies to *all* project resources, not just mailing-list archives. Fogel
derives the requirements from how people actually use a FAQ ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=121), p. 108):
because people search it, browse it, link others to specific entries, and occasionally add
to it, a good resource must have five properties — **direct searchability, availability to
major search engines, browsability (a table of contents), referential stability (per-entry
permalinks), and editability** ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=122), p. 109). Mailing-list archive
software acquired these natively long ago; web pages, the source tree, and the bug tracker
often need extra effort to reach the same standard.

### Codifying Tradition

As a project accumulates history, each newcomer faces a larger **acculturation burden** —
not because newcomers got worse, but because veterans absorbed the conventions gradually
and underestimate how much tradition has piled up ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=122), p. 109). Keeping
the guidelines current — especially the *communications* conventions, which change most as
the project grows — rests on two habits: watch for repeated patterns of confusion (a
recurring confusion signals a missing written guideline), and don't tire of repeating
yourself, or sound tired, since newcomers keep arriving ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=122), p. 109).

Treat every web page, message, and chat room as **advertising space for the project's own
resources**, with content tuned to who reads it (a user chat banner targets people wanting
an answer *right now*; a mailing-list footer carries subscribe links and a FAQ pointer that
reach far more readers than just subscribers) ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=122), p. 109). Writing the
guidelines is not enough — **you must put them where they'll be seen and format them so
their introductory status is obvious**: Subversion cut its rate of bogus bug filings by
reformatting the tracker's front page so the "discuss before filing" injunction stood out
in huge bold red letters, which also kept responders in a better mood
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=123), p. 110). See [[bug-tracking]] on pre-filtering the tracker.

Finally, establish **canonical referral forms** for common entities and use them
everywhere: Subversion's `r12908` for a revision is easy to type, visually distinctive,
and *machine-parsable* (it can only mean a revision, so tools can auto-link it), whereas
"revision 12908" is ambiguous and line-breakable ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=123), p. 110). Consistent
patterns let readers absorb conventions by imitation and reduce the questions they must ask;
the larger the project, the more this consistency matters ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=124), p. 111).

## Negative Space

- **Probabilistic-mailing-list thought experiment** (`illustrative-scaffolding`): Fogel's
  footnote musing about a list that sends each thread to a random subset of subscribers is
  a speculative aside, not a developed mechanism.
- **The "frobnicate / defrobnicate Scanley indexes" worked example** (`illustrative-scaffolding`):
  the fictional obsolete-the-old-post exchange illustrates archive etiquette; the principle
  is captured, the recipe is not.
- **Git commit-ID syntax convention** (`tool-specific/perishable`): the "commit c03dd89305,
  first 8–10 hash chars / 12 for busy projects" detail is mechanics of one VCS, subsumed by
  the canonical-referral principle.
- **Message-ID-header citation mechanics** (`too-granular`): the advice to include archive
  URL + Message-ID when citing a list message is a sub-bullet under canonical referral.
- **Stack Overflow / Chris Beams commit-message footnote pointers** (`source-underdeveloped`):
  external links offered without developed treatment.

## See also

- [[facilitating-online-discussion]] — the in-thread counterpart: keeping a single
  discussion productive (the Bikeshed Effect, holy wars, the noisy minority).
- [[choosing-the-right-forum]] — venue selection and routing, the other half of managing
  communication structure as a project grows.
- [[message-forums]] / [[bug-tracking]] — the specific venues whose archives and front
  pages this page tells you to organize.
- [[setting-the-tone]] — codifying tradition is how early precedents become durable norms.

## Sources

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Chapter 6 "Communications" —
  §Handling Growth, §Conspicuous Use of Archives, §Treat All Resources Like Archives,
  §Codifying Tradition (PDF pp. 119–124 / printed pp. 106–111).
- **Source entities:** [[producing-open-source-software-book]]
