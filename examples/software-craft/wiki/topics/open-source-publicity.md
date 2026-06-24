---
title: Open Source Publicity
aliases: [publicity, announcing-releases, meant-to-be-quoted, announcement-channels]
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

# Open Source Publicity

In free software there is a **smooth continuum between purely internal discussion and
public-relations statements**, because the audience is not strictly bounded: posts are
publicly accessible, so the project never has full control over the impression the world
forms — a Hacker News poster or Slashdot editor can put millions of eyes on a post no one
expected to leave the project ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=125), p. 112). In practice the risk is small,
and the announcements the project most wants publicized *are* the ones that get publicized
— provided you use the right mechanisms to signal relative newsworthiness. This page covers
deliberate announcement practice; [[security-vulnerability-disclosure]] covers the special
case where openness is deferred, and [[open-source-marketing]] covers messaging under public
scrutiny.

## Announcing Releases and Major Events

For a major announcement there are a few main channels, and they should fire as nearly
**simultaneously** as possible ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=125), p. 112):

1. **The project front page** — seen by more people than any other part of the project; put
   a brief blurb there that links to the full press release.
2. **A "News" / "Press Releases" area** — the detailed write-up. Structure it as a single,
   canonical, *linkable* "announcement object" (one web page or discrete blog entry per
   release) that other sites can point to and that stays distinct from other releases.
3. **Microblog/RSS broadcast** — push it through any relevant social handles and news feeds
   (RSS should fire automatically on publish if set up properly).
4. **Forums** — post as appropriate (the mechanics are those covered under launch
   announcing; see [[launching-an-open-source-project]]).
5. **The `announce` mailing list** — a low-traffic, *moderated* list reserved for major
   announcements (new releases, fundraising drives, security advisories, direction shifts).
   Because it is low-traffic and high-value it typically has the highest subscribership of
   any project list, which is exactly why it must not be abused.

Fire these as close to simultaneously as possible to keep the window of inconsistency small
— people get confused seeing an announcement on the list but not yet on the home page; queue
the email, web edits, and feed updates and release them in a row ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=125), p. 112).
For a **less important event** you can drop some or all of these outlets — the world notices
it in proportion to its actual importance — e.g. merely *setting* the next release date is
worth an email to the daily lists (not the announce list) and a status-page update, no more
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=125), p. 112).

## Engineer the Meant-to-Be-Quoted Portion

Word of mouth gives very broad distribution — lurkers who never post on your lists are not
silent elsewhere — so construct even minor announcements to encourage *accurate* informal
re-transmission ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=126), p. 113). Concretely: a post you expect to be
quoted should have a **clearly meant-to-be-quoted portion**, the way a formal press release
does. Lead with a short first paragraph carrying the two or three most important facts (e.g.
the release date and the headline feature) plus a URL for more; if that paragraph is the
only thing that crosses someone's screen, you're still doing well, and you gain some control
over *what* gets quoted ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=126), p. 113).

## Negative Space

- **The Scanley "version 2.0 in mid-August" sample announcement** (`illustrative-scaffolding`):
  the worked email demonstrates the meant-to-be-quoted lead; the principle is captured, the
  verbatim text is not.
- **Specific aggregator names — Hacker News, Slashdot** (`tool-specific/perishable`): cited
  to illustrate the unbounded-audience point; the venues are perishable, the dynamic is the
  concept.
- **`announce@` list naming convention** (`too-granular`): the standard list name is a
  detail under the announce-list channel, not a standalone concept.

## See also

- [[security-vulnerability-disclosure]] — the inverse case: an announcement deliberately
  held back until a coordinated go-public moment.
- [[open-source-marketing]] — messaging and credibility under "you are being watched";
  publicity is the distribution side, marketing the message side.
- [[launching-an-open-source-project]] — first-announcement mechanics (where to post,
  seeding) referenced by channel 4 above.
- [[scaling-project-communication]] — announcements are also project-resource "advertising
  space" (codifying tradition).

## Sources

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Chapter 6 "Communications" —
  §Publicity, §Announcing Releases and Other Major Events (PDF pp. 125–126 / printed pp. 112–113).
- **Source entities:** [[producing-open-source-software-book]]
