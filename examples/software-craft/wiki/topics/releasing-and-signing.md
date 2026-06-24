---
title: Releasing and Signing
aliases: [release-testing, digital-signatures, release-checksums, candidate-releases, release-approval]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [release-engineering]
roles: [tech-lead, security-engineer]
source_tier: 1
project: null
source_count: 1
status: active
---

# Releasing and Signing

Once a source distribution is cut from the stabilized release branch (see
[[stabilizing-a-release]], [[source-packaging]]), the **public** part of the release
process begins. Two gates stand between the packaged tree and the download area:
**developer approval through real testing**, and **cryptographic signing** that lets
strangers trust what they downloaded ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=144), p. 131).

## Approval is testing, not inspection

Before a distribution is made available to the world it should be tested and approved
by some **minimum number of developers, usually three or more** ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=144), p. 131).
The key discipline: approval is *not* a matter of eyeballing the release for obvious
flaws. Ideally each approving developer **downloads the package, builds and installs it
onto a clean system, runs the regression test suite, and does some manual testing** —
plus whatever else the project's release checklist demands — before signing off ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=144), p. 131).
Building from the shipped artifact on a clean machine is what catches the packaging
mistakes (missing files, broken build scripts) that never show up in a developer's
own working tree.

## Signing and hashing: trust over an untrusted channel

The approval, once given, must be **signaled to the world using digital signatures and
identifying hashes**. The purpose is to give users a way to verify that the copy they
received has not been maliciously tampered with — they are about to run this code on
their machines, and a tampered build hands an attacker a back door to all their data
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=144), p. 131).

Each approving developer digitally signs **each container** (the `.tar.gz`, `.zip`,
etc.) using GnuPG or another OpenPGP-compliant tool. Two conventions matter ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=144), p. 131):

- **Personal keys, not a shared project key.** Developers sign with their own personal
  signatures rather than one project key.
- **A minimum, but no maximum, number of signers.** As many developers as wish to may
  sign. More signatures is strictly better: each added signer means the release got
  more testing, *and* it raises the chance that a security-conscious user can find a
  **web-of-trust path** from herself to the release.

Once approved, every released artifact goes into the project's download area
**accompanied by its signatures and checksums**. The exact filing scheme is a matter of
taste — a per-package `.asc`/`.md5`/`.sha256` sidecar file, or one collected
`.sigs`/checksum file for the whole release. What matters is to keep the scheme simple,
describe it clearly, and stay **consistent from release to release** ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=144), p. 131).

> The mechanics of *generating* signatures and hashes are deliberately out of scope in
> the source; the durable point is the *policy* — approval-by-testing, personal-key
> signing, consistent publication — not the tooling.

## Candidate releases: exposure before the blessing

For important releases carrying many changes, projects often ship **release candidates**
first (e.g. `scanley-2.5.0-beta1` before `2.5.0`). A candidate's whole purpose is to
**subject the code to wide testing before it is blessed** as official. If problems
surface, they are fixed on the release branch and a new candidate (`-beta2`) rolls out;
the cycle repeats until no unacceptable bugs remain — at which point the last candidate
*becomes* the official release, the **only difference being the removal of the qualifier
from the version number** ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=144), p. 131).

The operative rule: in every other respect, **treat a candidate exactly like a real
release** — same care, same testing, same signing. The `alpha`/`beta`/`rc` qualifier
(see [[release-numbering]]) is itself enough to warn conservative users to wait, so
there is no reason to cut corners. You *want* people to use candidates, because exposure
is the best way to uncover bugs, and you never know which candidate will end up being
the one that ships ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=144), p. 131).

## Announcing a release

Announcing a release uses the same channels as any project event (see
[[open-source-publicity]]), with a few release-specific additions ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=145), p. 132):

- **Repeat checksums and signature pointers wherever the download URL appears.** Because
  the announcement goes out across multiple forums (mailing list, news page, …), users
  can cross-check the checksums from independent sources — extra assurance for the
  security-conscious that the *checksums themselves* weren't tampered with. Re-posting
  the signature-file link doesn't make the signatures more secure, but it signals that
  the project takes security seriously.
- **Include the relevant portion of the `CHANGES` file** so readers can see why
  upgrading is in their interest. This matters as much for candidate releases as for
  final ones — visible bugfixes and features are what tempt people into testing a
  candidate.
- **Thank the team, testers, and good bug-reporters — but don't single people out by
  name** except for someone individually responsible for a widely-recognized large
  piece of work. Naming names routinely starts a slide down the slippery slope of credit
  inflation (a topic developed under [[open-source-participation|Credit]] in Ch.8).

## Negative Space

- **GnuPG / OpenPGP signing mechanics and web-of-trust setup** (`too-granular`): the
  source explicitly declares the details of creating signatures and hashes beyond its
  scope; the page keeps the policy, not the key-management recipe.
- **Specific sidecar-file naming schemes** (`tool-specific/perishable`): the
  `.asc`/`.md5`/`.sha256` vs. collected-`.sigs` layouts are illustrative conventions;
  the durable rule is "simple, documented, consistent."
- **The Scanley `-beta1`/`-beta2` package-name examples** (`illustrative-scaffolding`):
  worked names demonstrating the qualifier-drop, not concepts.
- **Apache release-signing URL and "web of trust" search suggestion**
  (`tool-specific/perishable`): external further-reading pointers.

## See also

- [[stabilizing-a-release]] — produces the branch this process releases *from*; the
  release manager typically drives the build/sign/upload logistics here.
- [[source-packaging]] — the source distribution that gets tested, signed, and shipped.
- [[release-numbering]] — where the `alpha`/`beta`/`rc` candidate qualifiers come from.
- [[security-releases]] — the special case where the "wide pre-release testing" gate
  above is impossible and conservatism substitutes for it.
- [[open-source-publicity]] — the general announcement machinery a release announcement
  rides on.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 7 "Packaging,
  Releasing, and Daily Development", §Testing and Releasing (incl. Candidate Releases,
  Announcing Releases), printed pp. 131–132.
