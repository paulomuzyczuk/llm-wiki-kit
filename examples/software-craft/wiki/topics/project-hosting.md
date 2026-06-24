---
title: Project Hosting (Canned Hosting)
aliases: [canned-hosting, project-hosting-site, code-hosting]
date: 2026-06-23
last_updated: 2026-06-24
type: topic
topics: [project-infrastructure]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Project Hosting (Canned Hosting)

A "canned hosting" site is an online service offering some or all of the
collaboration tools needed to run a free-software project — at minimum public
version-control repositories and bug tracking, usually wiki space, often mailing
lists, sometimes continuous-integration testing and more. For many projects it is
a perfectly adequate developer-facing entry point, removing the need to stand up a
separate site ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=45), p. 32).
This page is the **build-vs-buy decision framework** for project infrastructure;
the assembled-yourself alternative and the full toolset are covered in
[[project-infrastructure]].

## The Trade-off: Convenience vs. Control

Two advantages drive the buy decision ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=46), p. 33):

- **Server maintenance is someone else's problem** — uptime monitoring, OS
  upgrades, backups for all tool data.
- **Simplicity** — the provider has already chosen and configured a bug tracker,
  a version-control system, discussion software, single-sign-on, and so on. You
  fill in a registration form, press a button, and have a project site.

The cost is the mirror image: you must accept their choices and configurations
even where something else would suit your project better. Canned sites are
adjustable only within narrow parameters; you never get the fine-grained control
of a server you administer yourself ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=46), p. 33).

## The Default Decision

Fogel's decision heuristic is deliberately blunt: **if you are not sure whether to
use canned hosting, you should probably use canned hosting.** These sites have
integrated their services in ways that would be laborious to reproduce (for
example, auto-linking a commit to a bug ticket it mentions), the same set of
choices has faced everyone running a project, and there are settled solutions now.
Unless you have specific reason to believe you can do better, the project will
likely run best on one of these sites ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=46), p. 33).

**Default platform:** if you do not know what to choose, choose GitHub — by far
the most popular, with a good feature/integration set, a developer base already
familiar with it, and programmatic APIs. If GitHub does not fit (e.g. the project
uses Mercurial rather than Git), Wikipedia's comparison of hosting facilities is
the first place to look for current, comprehensive options ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=46), p. 33).

**Keep the exit open.** Address the project's development home at a *custom domain*
that forwards to the canned site, so that switching providers later does not force
the project's main address to change ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=46), p. 33).

## Hosting on Fully Open-Source Infrastructure

A project may prefer a host whose own stack is entirely free software — to signal
a commitment to software freedom, or for the utilitarian reason that a
politically sensitive project worried about deplatforming wants to know it can
reproduce its hosting independently if necessary. Free-software hosts exist
(examples Fogel names: GitLab's Community Edition, Sourcehut, and Codeberg, which
runs the community-forked Forgejo platform) ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=47), p. 34).

**Decision criterion — freedom of the platform is a values choice, not a success
factor.** Fogel reports no evidence that the software-freedom of the hosting
platform meaningfully affects a project's success; most free-software developers
will happily participate through a non-free platform when that is what the project
uses. So this decision should be made on the project's philosophical position,
not on expected adoption ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=47), p. 34).

### The Durable Criterion: No Lock-In

Whatever you choose, the criterion that actually protects the project is the
ability to **interact with project data programmatically and to export it out of
the platform.** A host meeting those two conditions can never truly lock you in
and is even somewhat extensible via its interface. Independently of the host, the
project itself should *never require participants to run proprietary software on
their own machines* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=47), p. 34).

## Anonymity and the Involvement Bar

A failure mode most common on (but not exclusive to) canned sites is
over-requiring user registration. Registration genuinely helps — it deters spam,
and you do not want anonymous strangers pushing changes — but requiring a login
for tasks that should be open, especially filing or commenting on bug tickets,
raises the involvement bar for what should be quick actions. It also *biases the
data*: people willing to create an account are not a random sample even of users
willing to file bugs, and a newcomer who must complete a signup form before
reporting a bug may simply not file it ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=47), p. 34).

**Decision criterion:** where you control it, permit *all read-only actions*
anonymously, and ideally allow data-entry portals that carry information from
users to developers (the bug tracker above all) to be used anonymously too — with
anti-spam measures such as captchas where needed. A simple optional email field
covers the need to contact a reporter without forcing an account ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=47), p. 34).

## Negative Space

- **Specific provider directory** (`tool-specific/perishable`): named resellers
  and instances (GitLabHost BV, 2nd Watch, librehq, partner-search URLs) are
  perishable specifics; the durable point is the no-lock-in criterion, retained
  above.
- **Generated-files / FAQ-regeneration example** (`illustrative-scaffolding`): the
  difficulty of setting a custom regeneration hook on someone else's server is an
  illustration of the "accept their configuration" cost, not a separate concept.
- **The Forgejo fork backstory** (`illustrative-scaffolding`): the corporate-move
  origin of the Codeberg/Forgejo fork is context for one named example.
- **The sandboxed-proprietary-JavaScript footnote** (`out-of-scope`): a
  philosophical aside on whether browser-confined code counts as client or server
  software; not an infrastructure decision.

## Sources

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch.3 "Technical
  Infrastructure" — "Canned Hosting," "Choosing a Canned Hosting Site," "Hosting
  on Fully Open Source Infrastructure," and "Anonymity and Involvement"
  (PDF pp. 45–47 / printed pp. 32–34).
- **Source entities:** [[producing-open-source-software-book]]

## See also

- [[project-infrastructure]] — the full minimum toolset hosting provisions in one place.
- [[version-control]] — the repository hosting exists first to serve.
- [[bug-tracking]] — the tracker a canned-hosting site bundles alongside the repo.
- [[continuous-integration]] — the build/test automation increasingly bundled with hosting.
