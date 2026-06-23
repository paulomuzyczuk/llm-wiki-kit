---
title: Bug Tracking
aliases: [issue-tracking, ticket-tracker, defect-tracker, issue-tracker]
date: 2026-06-23
last_updated: 2026-06-23
type: topic
topics: [bug-tracking, project-infrastructure, software-collaboration]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Bug Tracking

A project's bug tracker is one of its principal public faces — "as much a public
face of the project as the repository, mailing lists or web pages." Anyone may
file, read, or browse tickets, so the tracker is where outsiders form their first
impression of a project's health ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=65), p. 52).
This page captures the *policy* of what a tracker is for and the *decision
criteria* for choosing and running one; per-tool mechanics (status-field names,
specific tracker products) are out of scope. The tracker is part of the
[[project-infrastructure]] minimum toolset and is closely coupled to
[[message-forums]] and [[version-control]].

## The Tracker Holds "Tickets," Not Just Bugs

The term *bug tracker* is misleading. The same system tracks bug reports, new
feature requests, one-time tasks, and unsolicited patches — really anything that
has distinct beginning and end states, optional transition states between, and
that accrues information over its lifetime. That generality is why the tool is
variously called an issue, ticket, defect, artifact, or request tracker ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=63), p. 50).

The useful distinction — which most projects blur but which matters when reasoning
about the tool — is between the **ticket** (the tracker's ongoing record of a
discovery, its diagnosis, discussion, and eventual resolution) and the underlying
**behavior or goal** the ticket is tracking (the bug or feature itself). One is
the artifact in the database; the other is the thing in the world ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=63), p. 50).

## The Ticket Life Cycle as Coordination, Not Bookkeeping

Tickets move through a roughly invariant life cycle — filed (→ *open*,
unverified, unassigned); commented on and clarified; **reproduced**; diagnosed;
scheduled; and finally fixed and closed. The shape is the same across trackers and
is not specific to open source, but it has implications for how open-source
projects coordinate ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=64), p. 51).

Two steps carry most of the social weight:

- **Reproduction is the pivotal moment.** When someone other than the filer makes
  the bug happen, that both proves the bug is genuine *and* confirms to the
  original filer that their report mattered — an act of community validation, not
  just a status change ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=64), p. 51).
- **Diagnosis must be recorded in the ticket.** If the diagnoser steps away,
  someone else should be able to pick up where she left off. Priority and
  release-blocking status are also set here so they surface early ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=64), p. 51).

### Handling the Common Variations Without Alienating Reporters

The life cycle's common deviations — closed-as-invalid (a user misunderstanding),
closed-as-duplicate (with the *regression* case where a fixed bug returns and the
original ticket is reopened while new reports close as duplicates), and
reopened-after-a-bad-fix — each carry a discipline. The load-bearing one is
attitudinal: as a project gains users, invalid tickets pile up and developers tend
to close them with increasingly short-tempered responses. Guard against this. No
individual reporter is responsible for the *aggregate* trend; the statistical
pattern is visible only from the developers' side, never the user's ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=64), p. 51).

## Acknowledge Every Ticket, Promptly

Because anyone may be watching a ticket, the project never knows how many people
await progress on it. The rate of *resolution* is constrained by developer
capacity, but the project should at minimum **acknowledge** each ticket the moment
it appears. Even a ticket that then lingers benefits from an early human response:
it tells the reporter a person registered their effort (filing a ticket usually
costs more than posting an email), and it pulls the issue into the project's
collective awareness so developers watch for related instances ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=65), p. 52).

## Decision Criteria for Tracker Features

The tracker's centrality dictates three technical requirements ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=65), p. 52):

- **Email integration** — every change, including the initial filing, should emit
  a notification to an appropriate set of recipients, so tracker activity folds
  into people's daily email flow.
- **Contact without compulsion** — the filing form should *record* a reporter's
  email or contact info but should not *require* real identity, since some people
  prefer to report anonymously; the value of anonymity outweighs the friction it
  removes.
- **APIs are non-negotiable.** A tracker you cannot drive programmatically cannot
  be extended or, in the long run, used scalably. APIs let a project graft custom
  behaviors onto the tracker, and — increasingly important now that many projects
  use the built-in tracker of a proprietary [[project-hosting]] site — they are the
  escape hatch that lets you take your ticket history elsewhere. Treat
  exportability as insurance against lock-in even if you never exercise it.

## A Tracker Is Not the Development List

Email integration tempts people to treat the sum of all tickets and their email
traffic as equivalent to the development [[message-forums]]. It is not. Bug traffic
and the development list serve different purposes, and conflating them is a forum
mistake developed further in Ch.6 ("Choose the Right Forum") ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=65), p. 52).

## Pre-Filtering: Keeping the Database Clean

Every ticket database eventually drowns in duplicate or invalid tickets from
well-meaning but inexperienced users. A prominent front-page notice (how to tell a
real bug, how to search for existing reports, how to report well) helps for a
while but does not scale with the user base. Two practices do the real work
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=66), p. 53):

- **Knowledgeable watchers on the incoming queue.** This technique is used nearly
  universally — even huge databases arrange for *someone* to see each ticket as it
  arrives, distributing the watch by category (e.g. routing to package
  maintainers) so the burden is shared and every ticket gets a timely response.
- **The "buddy system."** Strongly encourage (it cannot be fully automated, so it
  cannot be required) reporters to confirm a problem with a second person — on a
  forum or in chat — *before* filing. A second pair of eyes catches non-bugs,
  already-fixed issues, and duplicates early. Often it is enough to ask "Did you
  search the tracker first?" — many people simply never think to.

The buddy system's purpose is *training*, not gatekeeping: watchers should bounce
unbuddied tickets back gently — thank the filer, point them to the guidelines,
approve a clearly-valid ticket anyway rather than waste the work, and otherwise
ask them to reopen with a confirmation reference. Misfilings never stop entirely;
the only way to stop them completely is to close the tracker to non-developers, a
cure worse than the disease. Cleaning invalid tickets is permanent routine
maintenance, best spread across as many people as possible ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=66), p. 53).

## Negative Space

- **The full step-by-step ticket life cycle and its named states**
  (`too-granular`): the six numbered steps and per-tracker state labels
  (unverified, unstarted, assigned-to-a-fake-user) are mechanics beneath the
  decision-criteria altitude; the page keeps only the two pivotal steps
  (reproduction, recorded diagnosis) and the coordination principle.
- **The Debian bug tracker's 996,003-ticket count** (`illustrative-scaffolding`):
  a concrete example of the "someone sees every ticket" technique at scale; the
  principle is retained, the figure is not.
- **The exact unbuddied-ticket response steps** (`too-granular`): the
  respond/approve/close-with-reopen-instructions procedure is operational recipe;
  the page keeps the training-not-gatekeeping principle behind it.
- **Issue-manager and "Treat Every User as a Potential Participant" cross-refs**
  (`foreshadowing`): named here but developed in Ch.6/Ch.8; left as forward
  references rather than paged.

## Sources

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch.3 "Technical
  Infrastructure" — "Bug Tracker," "Interaction with Email," and "Pre-Filtering
  the Bug Tracker" (PDF pp. 63–66 / printed pp. 50–53).
- **Source entities:** [[producing-open-source-software-book]]

## See Also

- [[project-infrastructure]] · [[message-forums]] · [[version-control]] · [[project-hosting]] · [[real-time-chat]]
