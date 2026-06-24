---
title: Software Patents
aliases: [patents, defensive-patents, patent-trolls, patent-non-aggression]
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

# Software Patents

Software patents are, in Fogel's framing, **"the only real threat against which the free
software community cannot defend itself."** They have "long been a lightning rod issue in free
software" precisely because, unlike the other legal regimes, a project cannot simply route
around them
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=182), p. 169).

## Why a patent is uniquely dangerous

Copyright and trademark problems "can always be gotten around": infringing code can be
rewritten while keeping the same algorithm, and an infringing project name can be changed (a
temporary inconvenience — "the code itself would still do what it always did"). But "a patent
is a blanket injunction against implementing a certain idea. It doesn't matter who writes the
code, nor even what programming language is used"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=182), p. 169).

Once accused of infringement, a project "must either stop implementing that particular feature,
or expose the project and its users to expensive and time-consuming lawsuits." Because the
instigators are usually "corporations with deep pockets," most projects "cannot afford either
to defend themselves nor to indemnify their users, and must capitulate immediately" — even when
they believe the patent would not survive court. The defensive consequence is that projects
sometimes **code defensively**, "avoiding patented algorithms in advance even when they are the
best or only available solution." The community sentiment is near-unanimous: surveys show "the
vast majority … think that software patents should be abolished entirely," and open source
developers "may refuse to work on projects that are too closely associated with the collection
or enforcement of software patents."

## The defensive-patenting arms race and its collateral damage

Fogel concedes the grim logic: "collecting patents purely for defensive purposes is rational."
The U.S. patent system "is by its nature an arms race" — if competitors hold patents, your best
defense is to hold your own, so that a suit can be answered with a counter-threat, after which
"the two parties usually sit down and work out a cross-licensing deal"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=183), p. 170).

The more insidious harm is **secrecy**. Patents "encourage an atmosphere of secrecy among
firmware designers," who fear that publishing interface details makes it easier for competitors
to find infringement. Fogel's worked example is the video-card industry: manufacturers withhold
the programming specs needed for "high-performance open source drivers," not because they oppose
broader OS support, but because "behind the design room door, these shops are all violating one
another's patents," and full specs would expose that. The patents "are so unpredictable and so
potentially broad that no card manufacturer can ever be certain it's safe."

## Three partial defenses (decision criteria)

Fogel names what *can* be done, while stressing none is a full cure
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=183), p. 170):

- **License-level patent clauses.** "Modern free software licenses generally have clauses to
  combat, or at least mitigate" patent danger — typically by "automatically revoking the overall
  open source license for any party who makes a patent infringement claim based on either the
  work as a whole or on the claimant's contributions." (This is the "patent snapback" aspect on
  [[open-source-licensing]]; GPL-3.0, Apache-2.0, and MPL-2.0 carry it.) Useful "legally and
  politically," but "not enough to dispel the chilling effect."
- **Public non-enforcement pledges.** If your organization collects software patents, "make it
  clear, in a public and legally enforceable way, that the patents would never be enforced when
  the infringement comes from open source code," reserving them purely for defense. Fogel calls
  this "not only the right thing to do" but "good open source public relations" (citing RedHat's
  patent promise as the model)
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=182), p. 169).
- **Join a patent non-aggression community (OIN).** Since 2005 the **Open Invention Network**
  has provided a "patent non-aggression community" for open source: members "agree to provide
  royalty-free cross-licensing for a broad set of patents that read on widely-used open source
  software." Joining is "essentially a way to say 'Our company doesn't want to enforce software
  patents on anyone … and we don't want anyone enforcing them on us either.'" Membership is free
  and open to anyone; Fogel recommends it
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=183), p. 170).

Ultimately, Fogel argues, "only changes in the substance or interpretation of international
patent law" can truly fix the problem. He notes the 2014 *Alice Corp. v. CLS Bank* decision
(against the patentability of abstract ideas) made software patents' future "unpredictable," but
remains pessimistic that "patent trolls" and large portfolio-holders will relent soon, "because
there is so much money to be extracted via infringement claims."

## Negative Space

- **General patent-law doctrine and the Alice/troll legal history** (`out-of-scope`): the
  chapter is explicitly an introduction; deep patent law is left to specialist resources.
- **Video-card-industry case** (`illustrative-scaffolding`): cited to demonstrate
  patent-induced secrecy; the industry specifics are not the concept.
- **Specific pledges/orgs (RedHat patent promise, OIN membership terms)**
  (`tool-specific/perishable`): named as live exemplars of the defensive options; the option
  *type* is retained, not the changeable program details.
- **"read on" patent jargon footnote** (`too-granular`): the definitional aside (a patent may
  cover code the owner never wrote) supports the threat argument; folded in, not paged.

## See also

- [[open-source-licensing]] — "patent snapback" appears there as a license aspect; this page is
  the standalone regime and the non-license defenses (pledges, OIN).
- [[copyleft]] — modern copyleft licenses carry the auto-revoke patent clause as part of their
  reciprocity machinery.
- [[trademarks-in-open-source]] — the paired Ch. 9b regime; a trademark threat (rename) or
  copyright threat (rewrite) is escapable, a patent is not.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 9 "Legal Matters" —
  "Patents" (why patents are the undefendable threat, defensive coding, the arms race and
  secrecy harm, license patent clauses, public non-enforcement pledges, the Open Invention
  Network, and Alice Corp. v. CLS Bank) (printed pp. 169–170).
