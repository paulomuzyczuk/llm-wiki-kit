---
title: Open-Source Marketing
aliases: [oss-marketing, freedom-from-vendor-lock-in, cost-of-total-ownership]
date: 2026-06-23
last_updated: 2026-06-23
type: topic
topics: [open-source-economics]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Open-Source Marketing

"Although most open source developers would probably hate to admit it, marketing works." Good
marketing "can create buzz around an open source product, even to the point where hardheaded
coders find themselves having vaguely positive thoughts about the software for reasons they can't
quite put their finger on." The inevitability is the point: "any corporation involved in free
software will eventually find itself considering how to market themselves, the software, or their
relationship to the software"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=95), p. 82).
What makes open-source marketing distinct is that it operates under the same scrutiny as the code
(see [[open-source-economics]]): claims are publicly verifiable, so the discipline is mostly about
leveraging one structural advantage and avoiding a handful of self-inflicted wounds.

## The structural advantage: product and vendor are not the same

The advantage "open source businesses should promote as often as possible" is the lack of vendor
lock-in. Lock-in "is what happens when a vendor sells a service or product to a customer, perhaps
at a cheap up-front price, but the customer has to make certain further investments in order to
use the product — e.g., infrastructure changes, workflow and other process changes, data
reformatting, retraining." The accumulated cost of switching away "is… the degree to which the
vendor has the customer locked in." Fogel is careful to separate this from sunk cost: switching
costs "are different from sunk costs… and it is the latter that are the real issue here," because
even an unhappy customer faces a switching cost "separate from whatever licensing or service fees
the vendor charges"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=95), p. 82); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=96), p. 83).

"The great commercial strength of open source is that product and vendor are not the same." A
customer "can switch to another vendor, or to a combination of vendors, or even a combination of
vendor and in-house support, all while continuing to use the same product." The selling tactic
follows directly — make customers "clear on this point, and give them as many concrete examples
as you can." Counter-intuitively, it can help "to point out the existence of some of your
competitors, because their presence paradoxically reassures the customer that choosing you is a
safe decision — if things don't work out, there are other options"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=96), p. 83).

## "Cost of total ownership"

Proprietary vendors compete by invoking "total cost of ownership" — arguing that beyond
open source's "up-front cost of zero… in practice software integration involves organizational and
technical costs that can be quite significant." Fogel concedes this "is quite true, as far as it
goes, but that argument works the other way too: to the extent that there are such costs… the
danger to the customer of vendor lock-in is directly proportional to them." Over time "the costs
of proprietary software tend to outstrip the costs of open source," because "one pays a premium
for decreasingly competitive vendor selection, both in money and in loss of flexibility and
options." His counter-coinage inverts the slogan: the **"cost of total ownership"** — "how much
does it cost a company to be totally owned by its software vendors? With open source, customers
are not owned — they are the owners, to exactly the degree that they want to be," outsourcing "as
much of that responsibility… as they want," in relationships "based on mutual satisfaction and
mutual benefit, not on an asymmetrical pseudo-monopoly"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=96), p. 83).

## Remember that you are being watched

The governing constraint on every claim: "it is very important not to say anything that isn't
demonstrably true. Audit all claims carefully before making them, and give the public the means to
check your claims on their own. Independent fact checking is a major part of open source, and it
applies to more than just the code." Open source carries "an unusually high quantity of people
with the expertise to verify claims" — people with "the right social contacts to publicize their
findings in a damaging way." Fogel's contrast: when "Global Megacorp Industries pollutes a stream,
that's verifiable, but only by trained scientists, who can then be refuted by Global Megacorp's
scientists," whereas open-source behavior "is not only visible and recorded, it is also easy for
many people to check it independently." The blunt summary: "refutation is difficult when what
people are saying is true"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=96), p. 83).

The practical line falls on precise crediting: it is "okay to refer to your organization as having
'founded project X' if you really did," but not "the 'makers of X' if most of the code was written
by outsiders"; and do not "claim to have a deeply involved, broad-based developer community if
anyone can look at your repository and see that there are few or no code changes coming from
outside your organization"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=96), p. 83).

## Don't bash competing vendors

Selling services around shared open-source software means having competitors who sell around the
same software. Comparison "is expected, and in many ways healthy. However, be careful to avoid
straying into public criticism of the other development teams or of their development priorities."
The reason is that the commercial and development realms overlap: "your own developers have to
work directly with those competitors' developers in the open source project," often with "friendly
relations," and "you may find yourself hiring developers from your competitors; if you burn up
available goodwill in advance, you may not get the best candidates." Marketing statements in the
commercial realm are "also visible and had effects in the development community"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=97), p. 84).

## "Commercial" vs "Proprietary": terminology integrity

A common structure is **open core** — marketing "a fully open source version of their product
alongside, and in direct comparison to, an enhanced proprietary version." Because reproducing the
proprietary enhancements and "maintain[ing] a divergent fork" costs each would-be collaborator
more "than the cost of just paying for the proprietary version," it "rarely happens." Open core is
"a core set of functionality that is available as open source software, with a more featureful
application wrapped around it as proprietary software," usually depending "on the open source core
having a non-copyleft license" — its licensing mechanics are developed in Ch.9 (see
[[open-source-licensing]]). It "has been successful strictly from a business point of view"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=97), p. 84).

The marketing-integrity rule is to "use the words 'open source' and 'proprietary'… respectively,"
not "Community Edition" vs. "Commercial Edition" / "Enterprise Edition." The terms smuggle in two
falsehoods. "Commercial Edition" implies open source "is not commercial," but open source "is
commercial by definition: the license guarantees the freedom to use the software for any
commercial purpose." "Enterprise Edition" implies it "is not suitable for enterprise-level use,"
also untrue. This "particularly hurts efforts… to get their software accepted by governments and
by other buyers who have sophisticated procurement requirements," whose regulations "often include
stipulations that purchased software must be 'commercial', 'commercial off-the-shelf', or
'commercially available' — definitions that all open source software meets." Portraying open source
as non-commercial "gives purchasing officers a misimpression" and "hurts open source software as a
whole" — the procurement link to [[government-and-open-source]]
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=97), p. 84); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=98), p. 85).

## Negative Space

- **"You Can't Fake It" case study (Singer 5)** (`illustrative-scaffolding`): the anecdote of a
  company announcing "rigorous testing" while its repo sat at three revisions; the captured
  principle is "audit your claims and link to tangible evidence," not the story.
- **Global Megacorp stream-pollution analogy** (`conceptual-tool-not-concept`): a rhetorical
  device contrasting verifiability, not a domain concept.
- **Arms-race dynamics of marketing in general** (`out-of-scope`): Fogel explicitly declines to
  "dissect the arms-race dynamics of marketing in general"; outside software-craft scope.
- **"Publicity" and "Don't Bash Competing Open Source Products" cross-references**
  (`foreshadowing`): the broader publicity and competitor-relations treatment lives in Ch.6
  (Communications), not yet ingested — left as dead references.
- **Open-core / proprietary-relicensing licensing mechanics** (`foreshadowing`): captured here
  only as a marketing pattern; the license-compatibility detail is deferred to Ch.9 and will
  enrich [[open-source-licensing]].

## See also

- [[open-source-economics]] — why claims are publicly verifiable; marketing under scrutiny is a
  special case of money buying credibility, not control.
- [[corporate-open-source-participation]] — the honest-broker behavior that "you are being
  watched" extends from the development list to the marketing department.
- [[open-source-licensing]] — the non-copyleft licensing that open core depends on; Ch.9 deepens
  proprietary relicensing.
- [[government-and-open-source]] — why "commercial off-the-shelf" procurement language makes the
  Commercial/Enterprise-Edition mislabeling actively harmful.
- [[funding-non-programming-activities]] — the other half of corporate engagement: spending on the
  project rather than positioning around it.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 5 "Organizations and Money" —
  "Marketing," "Open Source and Freedom from Vendor Lock-In," "Remember That You Are Being
  Watched," "Don't Bash Competing Vendors' Efforts," "'Commercial' vs 'Proprietary'" (printed
  pp. 82–85).
