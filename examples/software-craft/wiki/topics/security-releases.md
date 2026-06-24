---
title: Security Releases
aliases: [security-release, security-fix-release, security-only-release]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [release-engineering, software-security]
roles: [security-engineer, tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Security Releases

A **security release** is a release made *solely* to close a security vulnerability. It
is the release-engineering counterpart to [[security-vulnerability-disclosure]]: that
page covers the secrecy-constrained *disclosure* process; this one covers what makes the
*release itself* different from an ordinary one ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=145), p. 132).

## The constraint: a release that cannot be tested in public

The defining problem is that the fixing code **cannot be made public until the release is
available**. That means the fix cannot be committed to any public repository before
release day — and, critically, **the release cannot be publicly tested before it ships**.
Developers can examine the fix among themselves and test privately, but the
wide real-world testing that a normal release gets (see [[releasing-and-signing]] on
candidate releases) is impossible ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=145), p. 132).

## The rule that falls out of it: existing release + fix, nothing else

Because of that missing test exposure, a security release should **always consist of
some existing release plus the security fix, and no other changes** ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=145), p. 132).
The reasoning is direct: the more untested changes you ship, the likelier one of them
introduces a *new* bug — possibly a new security bug. Minimal change is also **friendly
to administrators** whose upgrade policy forbids deploying unrelated changes alongside a
security fix; a fix-only release is one they can deploy without violating that policy
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=146), p. 133).

This is the same minimal-delta principle that [[security-vulnerability-disclosure]]
states from the disclosure side ("differ from an existing release by exactly the
security patch") — here it is justified by the **testing gap**, not just by admin
convenience.

## The "minor deception" of an in-flight release

Holding a fix secret can force a project to publicly misrepresent its near-term plans.
Suppose `1.1.3` was already announced with certain non-security fixes when a security
report arrives. The developers cannot mention the security problem until the fix is
available, so they must keep talking publicly as though `1.1.3` will be what it was
always planned to be. But when `1.1.3` actually ships it differs from `1.1.2` **only in
the security fix** — all the previously-promised fixes are **deferred to `1.1.4`** (which
will of course also carry the security fix, as will every later release) ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=146), p. 133).

## Numbering a security release

There are two conventions for signaling that a release is security-only ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=146), p. 133):

- **Add an extra component** — e.g. `1.1.2.1`, readable as "a security release against
  `1.1.2`," with the implication that anything numerically higher (`1.1.3`, `1.2.0`, …)
  contains the same fix. For people following closely this conveys a lot; for everyone
  else, an occasional four-component number among three-component ones is confusing.
- **Just use the next scheduled number** (shifting other planned releases by one). This
  trades the embedded signal for **numbering consistency**, and is what most projects
  choose.

The trade-off is signal-for-the-informed versus consistency-for-everyone; consistency
usually wins. The compatibility-domain rules of [[release-numbering]] still apply.

## Negative Space

- **Disclosure-process mechanics** (`subsumed-by` [[security-vulnerability-disclosure]]):
  private intake, quiet fixing, CVE/CVSS naming, and pre-notification are the disclosure
  page's territory; this page is deliberately scoped to the *release* differences and
  cross-links rather than restating them.
- **The `1.1.2`/`1.1.3`/`1.1.4` worked numbers** (`illustrative-scaffolding`): a scenario
  illustrating the deferral and the "minor deception," not concepts in themselves.

## See also

- [[security-vulnerability-disclosure]] — the paired disclosure process (Ch.6); this
  page is the release-mechanics half, that one is the communications half.
- [[releasing-and-signing]] — the normal release's wide-testing-then-sign gate that a
  security release is structurally unable to use.
- [[release-numbering]] — the compatibility and component rules a security release's
  number must respect.
- [[maintaining-multiple-release-lines]] — a security fix typically must be cut across
  every still-supported line at once.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 7 "Packaging,
  Releasing, and Daily Development", §Security Releases, printed pp. 132–133.
