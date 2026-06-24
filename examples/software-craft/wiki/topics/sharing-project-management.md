---
title: Sharing Project Management
aliases: [management-roles, manager-not-owner, sharing-management-tasks, patch-manager, translation-manager]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-governance, open-source-participation]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Sharing Project Management

As a project grows, the bottleneck shifts from code to coordination — and the same logic that
makes [[delegation-in-open-source|delegation]] worthwhile applies to the management work
itself. Fogel: "Share the management burden as well as the technical burden of running the
project. As a project becomes more complex, an increasing proportion of the work becomes about
managing people and information flow. There is no reason not to share that burden"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=158), p. 145).

Sharing management "does not necessarily require a top-down hierarchy"; in practice the shape
"tends to be more of a peer-to-peer network topology than a military-style command structure."
Roles arise both ways — "sometimes management roles are formalized and sometimes they happen
spontaneously." Subversion ran a patch manager, a translation manager, documentation managers,
unofficial issue managers, and a release manager
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=158), p. 145).

## "Manager" does not mean "owner"

The defining constraint on every such role: "none of them requires exclusive control over the
domain in question." The issue manager doesn't bar others from the ticket database; the FAQ
manager doesn't insist on being the only editor. "These roles are all about responsibility
without monopoly" — the same anti-[[preventing-territoriality|territoriality]] principle
applied to management. Two duties follow: a domain manager should "notice when other people
are working in that domain, and train them to do the things the way the manager does," and
should "document the processes by which they do their work, so that when one leaves, someone
else can pick up the slack right away"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=158), p. 145).

When two people want the same role, "there is no one right way to handle this." Fogel's
preferred technique is not to decree a winner but "to ask the multiple candidates to settle it
among themselves" — they usually will, "and will be more satisfied with the result than if a
decision had been imposed." Co-management "is fine if it works," and if it doesn't "you're
right back where you started" and can try again
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=158), p. 145).

## Patch (pull-request) manager

In a project receiving many patches, "keeping track of which patches have arrived and what has
been decided about them can be a nightmare." A posted patch can be reviewed and bounced back,
spark a design discussion, or "be met with utter silence" — and silence is the danger: "it's
very easy for a patch to be ignored permanently without any single person intending for that to
happen," discouraging the author and onlookers alike
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=158), p. 145).

The patch manager's job is "to make sure that patches don't 'slip through the cracks'… by
following every patch through to some sort of stable state." If it ends in a commit, he does
nothing; if it ends in a final version with no commit, "he creates or updates a ticket to point
to the final version… so that there is a permanent record"; if it gets no reaction, he waits a
few days and follows up. The value is removing second-guessing: each developer "can make the
decision that is right for her at the moment she first sees the patch," trusting the manager to
catch whatever she drops. Because "this system works only if people can depend on the patch
manager being there without fail, the role should be held formally"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=158), p. 145); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=159), p. 146).
The deeper reason this role matters: "The true currency of open source projects is attention" —
even an unlanded patch must be seen to keep its author engaged (see [[contributor-motivation]])
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=159), p. 146).

## Translation manager

A translation manager "did not actually write the translations himself" — he "managed teams of
other translators," coordinating among them and between them and the rest of the project.
Translators "are a different demographic from developers": often with "little or no experience
working in a version control repository," yet "in other respects… often the best kind of
participant: people with specific domain knowledge who saw a need and chose to get involved."
The manager makes translation happen "in a way that does not interfere unnecessarily with
regular development," and represents the translators as a body when the developers need to be
told of technical changes. (The supporting tooling is in [[translation-infrastructure]].)
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=159), p. 146).

## Negative Space

- **Per-role operational recipes** (`too-granular`): the detailed mechanics of each manager
  role (and the further documentation/issue/FAQ managers that continue past this batch's page
  range) are captured as the governing principle — *responsibility without monopoly,
  documented for handoff* — rather than as one page per role.
- **Release manager** (`subsumed-by` [[stabilizing-a-release]]): Fogel explicitly defers it to
  the release-owner/release-manager treatment already ingested in Ch. 7.
- **Patch-queue tools** (`tool-specific/perishable`): TopGit, patchwork, Quilt, StGit, Gerrit,
  ReviewBoard are named footnote options, not durable concepts.

## See also

- [[open-source-governance]] — the decision structures these shared roles operate within.
- [[delegation-in-open-source]] — sharing single tasks, of which standing roles are the
  scaled-up form.
- [[preventing-territoriality]] — "responsibility without monopoly," the same principle for
  managers.
- [[stabilizing-a-release]] — the release-manager/release-owner role deferred to here.
- [[translation-infrastructure]] — the tooling the translation manager coordinates.
- [[contributor-motivation]] — "attention is the currency" the patch manager protects.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 8 "Managing Participants" —
  §Share Management Tasks as Well as Technical Tasks, §"Manager" Does Not Mean "Owner",
  §Patch Manager, §Translation Manager (printed pp. 145–146).
