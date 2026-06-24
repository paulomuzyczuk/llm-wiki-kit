---
title: Preventing Territoriality
aliases: [territoriality, cookie-licking, author-tags, code-ownership, no-trespassing]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-participation, open-source-culture]
roles: [tech-lead, code-craftsperson]
source_tier: 1
project: null
source_count: 1
status: active
---

# Preventing Territoriality

A healthy project keeps every area open to every contributor. Territoriality — one person
staking out exclusive ownership of a part of the codebase — is the failure mode that quietly
closes those areas off, and Fogel treats actively preventing it as a core management duty.

## Why exclusive ownership is destructive

Watch for "participants who try to stake out exclusive ownership of certain areas of the
project… to the extent of aggressively taking over work that others start." It can "even seem
healthy at first" — it looks like someone shouldering more responsibility. "But in the long
run, it is destructive. When people sense a 'no trespassing' sign, they stay away." The
consequences compound: "reduced review in that area, and greater fragility, because the lone
developer becomes a single point of failure." Worse, "it fractures the cooperative,
egalitarian spirit of the project"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=152), p. 139).

## Authority is granted, never seized

The principle is that "any developer is welcome to help out on any task at any time." In
practice people do have areas of greater influence, and non-experts defer to experts — "but
the key is that this is all voluntary." Informal authority "is granted based on competence and
proven judgement, but it should never be actively taken." Even a genuinely competent person
must hold authority "informally, through the consensus of the group," with boundaries that
"remain fuzzy and subjective," and that authority "never cause her to exclude others from
working in that area"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=152), p. 139).

Rejecting or editing work *for technical reasons* is entirely different: "the decisive factor
is the content of the work, not who happened to act as gatekeeper." One person doing most of
the reviewing in an area "is probably okay" — "as long as he never tries to prevent someone
else from doing that work too"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=152), p. 139).

## Cookie licking

The vivid name (Fogel credits Sumana Harihareswara) for claiming a task in front of the group
"but then [doing] nothing with it." As Harihareswara puts it, "Nobody in their right mind
would pick up and eat the licked cookie or finish the [task]." The remedy is light: "simply
pointing it out may be enough to de-territorialize the task in question and make others
consider picking it up"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=152), p. 139).

## Banning author tags from source files

To "combat incipient territorialism… many projects have taken the step of banning the
inclusion of author names or designated maintainer names in source files" — official or
near-official policy in Subversion and at the Apache Software Foundation, where ASF member
Sander Striker "puts it this way"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=152), p. 139).
Striker's reasoning is that author tags have "no clear line for when to add or remove" them,
"tend to get out of date," and invite gaming "to make the virtual author tag quota." Two deeper
objections: they "raise the awkward question of how much work one must do to get one's own name
listed," and they "conflate the issue of credit with that of authority" — "having done work in
the past does not imply ownership of the area where the work was done." No information is lost,
because "credit information can already be obtained from the version control logs"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=153), p. 140).
The principle: "A software project's source code files are the core of its identity. They
should reflect the fact that the developer community as a whole is responsible for them, and
not be divided up into little fiefdoms"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=153), p. 140).
This is why [[version-control]] — where authorship lives in the log, retrievable without
implying ownership — is the right home for credit.

## The core-to-periphery continuum

Don't over-apply the ban. Many projects keep a `contrib/` area of small helper scripts written
by outsiders, and "it's fine for those files to contain author names, because they are not
really maintained by the project as a whole." If such a tool later "starts getting hacked on by
other people," you move it somewhere less isolated and (with the author's approval) drop the
name. The governing idea is "a continuum between the core and the periphery": main source files
are community-maintained, while companion tools may stay essentially one person's — "as long as
the principle that community-maintained resources are not allowed to become individual
territories is upheld"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=153), p. 140).

## Negative Space

- **The compromise author-tag header example** (`illustrative-scaffolding`): the
  "Original Author / Now Maintained By" snippet is a sample, captured as the principle
  (peripheral files may keep names) rather than transcribed.
- **The sage-devel counter-argument** (`supporting-argument`): a footnoted mailing-list
  thread arguing for author tags in academic-math communities is noted as the bounded
  exception (credit-at-source cultures), not paged.

## See also

- [[version-control]] — where authorship and credit actually live (the log), making source-file
  author tags redundant.
- [[code-review]] — the open review territoriality suppresses when it closes an area off.
- [[open-source-culture]] — the egalitarian, "influence ∝ contribution" spirit fiefdoms
  fracture.
- [[forkability]] — the deeper reason no one can truly own a part of an open project.
- [[contributor-motivation]] — credit and recognition, the legitimate need territoriality
  distorts.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 8 "Managing Participants" —
  §Prevent Territoriality, §Cookie Licking, and the author-tag discussion (printed
  pp. 139–140).
