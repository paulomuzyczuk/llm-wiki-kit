---
title: Project Infrastructure
aliases: [technical-infrastructure, collaboration-tools, what-a-project-needs]
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

# Project Infrastructure

The collaboration technology a free-software project runs on — the tools that
"support the selective capture and integration of digitally-expressed human
intentions about a shared project." Fogel's governing claim is that skill with
these tools, and skill at persuading others to use them, is itself a determinant
of project success ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=43), p. 30).
This page captures the *principles* of project infrastructure and the *decision
criteria* for assembling it; per-tool mechanics are deliberately out of scope
(see [[version-control]], [[bug-tracking]], [[message-forums]], [[project-hosting]]
for the individual tools).

## Information Management as the Antidote to Brooks' Law

The reason infrastructure matters more as a project grows is Brooks' Law: adding
people to a late project makes it later, because communication complexity rises
as the *square* of the number of participants. Smart information management is
what keeps a growing project from collapsing under that weight — when hundreds of
people can no longer each stay aware of what everyone else is doing, the tooling
must carry the load that face-to-face awareness carried at small scale ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=43), p. 30).

The operative principle: because almost all communication in an open-source
project happens *in writing*, well-run projects evolve elaborate systems for
routing and labeling information, minimizing repetition, storing and retrieving
data, correcting bad or obsolete information, and associating related pieces as
new connections are noticed. The communications media themselves should do as
much of the routing, labeling, and recording as possible; humans should label and
route accurately on first entry so the software can make maximal use of that
metadata thereafter ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=43), p. 30).

## Technical Skills Plus People Skills

Promoting good information management is never purely technical. The technical
skills are essential because information-management software always needs
configuration plus ongoing maintenance as new needs arise; the people skills are
essential because the human community also needs maintenance — participants must
be encouraged, at the right times and in the right ways, to keep the project's
information well organized. The more invested a contributor is, the more complex
and specialized the techniques she will be willing to learn ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=44), p. 31).

### Beware Over-Automation

The counterweight to all of the above: do not automate things that genuinely
require human attention. Infrastructure is important, but what makes a project
work is *care* — and intelligent expression of that care — by the humans
involved. The right way to think about technical infrastructure is that it exists
to give humans easy opportunities to apply that care, not to substitute for it
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=44), p. 31).

## What a Project Needs: the Minimum Standard Toolset

Most open-source projects offer at least this minimum set, where each tool
addresses a distinct need but all of them must be made to interoperate ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=44), p. 31):

- **Web site** — primarily a one-way conduit of information from the project out
  to the public and participants; also a portal to the other tools.
- **Message forums / mailing lists** — usually the most active communications
  forum and the project's "medium of record." See [[message-forums]].
- **Version control** — lets developers manage code changes (reverting, change
  porting) and lets everyone watch what is happening to the code. See
  [[version-control]].
- **Bug tracking** — lets developers track work, coordinate, and plan releases,
  and lets anyone query bug status or record reproduction information; usable for
  tasks, releases, and features too, not only bugs. See [[bug-tracking]].
- **Real-time chat** — a place for quick, lightweight discussion and Q&A, not
  always fully archived. See [[real-time-chat]].

The decision criterion that follows from "they must work together": rather than
assemble and integrate these tools yourself, you can often adopt a [[project-hosting]]
service that ships them pre-integrated ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=44), p. 31).

## The Web Site: Two Audiences, One Gateway First

The "web site," for infrastructure purposes, means the pages that help people
*participate* as developers and documenters — which may differ from the
user-facing site. Users and developers have different needs and (statistically)
different mentalities, so a one-size-fits-all site ends up serving neither well.
The two should cross-link; in particular the user-facing site must carry a clear
link into the developers' area, since most new developers arrive at the user
pages first ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=44), p. 31).

**Decision criterion — start unified, split late.** A large multi-faceted project
may warrant separate gateways (e.g. one "get involved" page for all contributor
types and a narrower "developers" page for coders), but at the beginning it
probably does not. Begin with a single unified contributor gateway aimed at all
the contributor types you expect, and divide it only once it grows unwieldy.
Watch for this actively: long-time participants are naturally desensitized to
weaknesses in introductory pages, so listen for newcomers' complaints rather than
trusting your own read ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=45), p. 32).

Technically there is little to setting up the site. Its job is to present a clear,
welcoming overview of the project and to *bind together* the collaboration tools
(version control, bug tracker, and so on) — which is again why many projects
simply use a [[project-hosting]] service for the developer-facing entry point
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=45), p. 32).

## Social Networking Services: Projects Already Do It

Open-source projects make surprisingly limited use of mainstream "social
networking" platforms — but that is a definitional artifact, not an omission. Most
of the infrastructure these projects have refined for decades (forums, trackers,
chat) *is* social-networking software; it predates the term and is well-tuned to
what projects actually need. The reason a project rarely has much of a presence on,
say, Facebook is simply that Facebook's services are *not* tuned to those needs
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=71), p. 58).

The decision criterion is return on attention. Lightweight services pay off:
microblogs (Twitter and similar) suit short announcements that are easily forwarded
and replied to, giving a project a conversational channel with its community; event
services help arrange in-person meetups. Beyond those, most projects do not invest
in a large mainstream-social-media presence — individual developers may, but for
the *project* the reward does not appear high enough to justify the time and
attention ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=71), p. 58).

## Negative Space

- **The parliamentary-procedure analogy** (`conceptual-tool-not-concept`): Fogel
  frames written-culture information management as "parliamentary procedure on
  steroids," with an extended comparison to minutes, agendas, and committee
  reports. The analogy is a rhetorical device for the writing-is-the-record
  principle, not a domain concept of its own; the principle is captured above.
- **The LibreOffice "Get Involved" / "Developers" walkthrough** (`illustrative-scaffolding`):
  a specific worked example of the two-audience gateway idea; the principle, not
  the example, is retained.
- **Bug tracker and real-time chat as developed treatments** (`subsumed-by`):
  named here as part of the minimum toolset and now developed on their own pages
  ([[bug-tracking]], [[real-time-chat]]) as of batch 6; this page keeps only the
  one-line toolset entries.
- **Named microblog/event services** (`tool-specific/perishable`): Twitter,
  @AskLibreOffice, Eventbrite, and Meetup are perishable examples cited for the
  social-networking section; the return-on-attention criterion is what generalizes.
- **Generic web-hosting setup mechanics** (`tool-specific/perishable`): "web
  hosting is easy to come by" and layout particulars are not generalizable
  infrastructure principles.

## Sources

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch.3 "Technical
  Infrastructure" — chapter introduction, "What a Project Needs," and "Web Site"
  (PDF pp. 43–45 / printed pp. 30–32); "Social Networking Services" (PDF p. 71 /
  printed p. 58, batch 6).
- **Source entities:** [[producing-open-source-software-book]]

## See Also

- [[version-control]] · [[message-forums]] · [[project-hosting]] · [[bug-tracking]] · [[real-time-chat]] · [[wikis]] · [[translation-infrastructure]]
