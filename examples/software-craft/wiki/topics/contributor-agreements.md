---
title: Contributor Agreements
aliases: [cla, contributor-license-agreement, copyright-assignment, developer-certificate-of-origin, dco]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-licensing]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Contributor Agreements

A **contributor agreement** is the paper trail establishing that the people who wrote a
project's code and documentation actually granted the project the right to distribute their
work under its open source license. Fogel frames it as a choice among three ways to handle
copyright ownership "for free code and documentation that were contributed to by many
people"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=178), p. 165).
The decision is about *evidence and risk*, not about the freedom of the code — which the
license already guarantees.

## The three options (decision criteria)

Fogel lays out three approaches, in increasing order of burden, and recommends the middle one
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=178), p. 165):

1. **Do nothing — ignore copyright entirely.** *Not recommended.* The project accepts code
   "whenever it seems reasonably clear that the contributor intended it to be incorporated."
   This "can seem to work for a long time, as long as the project has no enemies," but leaves
   the project with no documentation that a contributor formally granted the right to use the
   code. If someone later sues for copyright infringement — as the SCO Group did to Linux —
   "some legal defenses" become "more difficult."
2. **Collect a Contributor License Agreement (CLA).** *Recommended for most projects.* Each
   contributor signs (often electronically) an agreement "explicitly granting the project the
   right to use that person's contributions." This is "usually enough for most projects."
3. **Require actual copyright assignment (CA).** The project (a legal entity, usually a
   nonprofit) becomes "the copyright owner for everything." This is "the most burdensome for
   contributors, and some contributors simply refuse to do it"; only a few projects still ask,
   and Fogel does not recommend requiring it "these days." (Copyright transferal is also
   "subject to national law" — licenses designed for the U.S. "may encounter problems
   elsewhere," e.g. Germany, where full transfer is apparently not possible.)

The governing principle: **collect enough evidence to defend the project's right to the code,
without imposing more burden than that purpose requires.** A CLA hits the tradeoff "between
safety and convenience."

## Central ownership does not endanger the code's freedom

A key reassurance against the fear that copyright assignment "proprietizes" a project: even
under centralized copyright ownership, "the code remains free, because open source licenses do
not give the copyright holder the right to retroactively proprietize all copies of the code."
If the owning entity suddenly relicensed everything restrictively, the community "could start a
fork based on the latest free copy of the code and continue as if nothing had happened"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=178), p. 165).
This is [[forkability]] acting as the backstop: ownership of the copyright is not ownership of
the community's right to the already-published code.

## What a CLA actually grants

The mechanism a CLA establishes is a **license, not a transfer**. Its core language grants the
project a "perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright
license to reproduce, prepare derivative works of, publicly display, publicly perform,
sublicense, and distribute [the] Contributions and such derivative works." Many CLAs open by
reminding the contributor of exactly this distinction — "This is a license agreement only; it
does not transfer copyright ownership and does not change your rights to use your own
Contributions for any other purpose"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=179), p. 166).
Some projects keep two variants — one for individuals, one for corporate contributors — but
the core grant is the same. (Fogel's recurring caveat applies: have a lawyer approve any CLA.)

## The DCO: the minimal CLA

The **Developer Certificate of Origin (DCO)** is "a particularly convenient style of simple
CLA" that many projects now use. It is "an attestation that the contributor intends to
contribute the enclosed code under the project's license, and that the contributor has the
right to do so." The contributor acknowledges the DCO text once, then adds a `Signed-Off-By:`
line to each patch or commit using the same identity, certifying that contribution under the
DCO
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=179), p. 166).

The simplification that makes the DCO work is that it **sets the inbound license of the
contribution equal to the outbound license of the project.** This deliberately avoids the
"sticky issues" of a more complex CLA — chiefly, that the CLA's recipient "might reserve the
right to relicense the project (and thus all the past contributions) under some different
license in the future, possibly even a proprietary license." A DCO grants no such reservation,
so it cannot become the lever for [[proprietary-relicensing]]. Fogel's bottom line: a DCO is
"probably the minimum amount of CLA a free software project should adopt," though some
circumstances still call for a fuller CLA. (The DCO relies on the project's own license for any
trademark or patent provisions, "which in most cases is fine.")

## Negative Space

- **Verbatim CLA / DCO legal text** (`too-granular`): the load-bearing grant language is quoted
  to fix the license-not-transfer distinction; the full forms live at the project's own CLA and
  at developercertificate.org, not transcribed here.
- **Electronic-submission mechanics and per-jurisdiction validity** (`tool-specific/perishable`):
  whether email or a web checkbox suffices "in many jurisdictions" is a lawyer question the
  source explicitly defers; no recipe captured.
- **The SCO v. Linux litigation history** (`illustrative-scaffolding`): cited only to show why
  "doing nothing" is risky; the case particulars are not the concept.
- **Two-CLA (individual vs. corporate) split** (`too-granular`): noted as a practice, folded
  into the CLA option rather than paged.

## See also

- [[proprietary-relicensing]] — the asymmetric scheme a broad CLA's relicensing reservation
  enables, and which a DCO's inbound=outbound rule forecloses.
- [[copyleft]] — why even a relicensing owner cannot un-free already-published code; the
  sole-copyright-holder exemption that makes relicensing legally possible.
- [[forkability]] — the community's backstop if a copyright-owning entity ever relicenses
  restrictively.
- [[open-source-licensing]] — the project-level license the DCO points inbound contributions at.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 9 "Legal Matters" —
  "Contributor Agreements" (the three ways: doing nothing, CLA, copyright assignment),
  "Doing Nothing" (the SCO risk), "Contributor License Agreements" (the core grant language),
  and "Developer Certificate of Origin (DCO): An Easier Style of CLA" (printed pp. 165–166).
