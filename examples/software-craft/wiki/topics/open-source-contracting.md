---
title: Open-Source Contracting
aliases: [contracting, contractors, osqa, open-source-quality-assurance]
date: 2026-06-23
last_updated: 2026-06-23
type: topic
topics: [open-source-economics, open-source-participation]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Open-Source Contracting

Contracting is the sharpest version of [[open-source-economics]]'s lesson that money buys
credibility, not control: you can pay for *work*, but you cannot pay for the community's
*acceptance* of that work. "Contracted work needs to be handled carefully in free software
projects," because the gap between delivering a patch and getting it merged is real, variable,
and outside any contract's power to close
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=87), p. 74).

## You cannot contract for acceptance

Ideally a contractor's work "be accepted by the community and folded into the public
distribution." In theory the contractor's identity shouldn't matter "as long as her work is
good"; in practice "it's very hard to produce an acceptable patch for a non-trivial
enhancement or new feature as a complete stranger," because the design "must first [be]
discuss[ed]… with the rest of the project," and "the duration of that discussion cannot be
precisely predicted." That unpredictability is a financial risk: "if the contractor is paid by
the hour, you may end up paying more than you expected; if she is paid a flat sum, she may end
up doing more work than she can afford"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=87), p. 74).

Two coping techniques:

- **Estimate and pad** — "make an educated guess about the length of the discussion process,
  based on… past experience with that community, add in some padding for error," and price the
  contract accordingly.
- **Decompose** — "divide the problem into as many small, independent chunks as possible, to
  increase the predictability of each chunk"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=87), p. 74).

The structural fix is the **best-effort integration clause**: "contract for delivery of a
patch that meets the formal upstream guidelines and for a tightly budgeted 'best effort' at
getting the patch integrated." The contract "can never require that the patch be accepted by
the upstream project, because that would involve selling something that's not for sale" — but
it "can require a bona fide effort to get the change accepted… and that it be committed… if the
community agrees." Referencing the project's "written standards (e.g., about coding
conventions, documentation, writing regression tests…)" makes the deliverable concrete
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=88), p. 75).

## Hire from within, or deliberately from outside

Two opposite contractor-selection tactics, each fitting a different goal
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=88), p. 75):

- **From within the community** (preferably a committer) — "it's not as corrupt as it might
  seem," because "a developer's influence… is due mainly to the quality of her code," which the
  contract doesn't change. What you buy is "advice about what sorts of changes are likely to be
  accepted" plus "a slight shift in the project's priorities" — since prioritization "is just a
  matter of who has time to work on what," paying for time moves the work up the queue, and
  others "will devote attention… simply because it looks like it's going to get done." For
  these reasons "the contractor is best drawn from the ranks of those already involved."
- **From outside the community** — when "you have a long-term goal of increasing the project's
  stability and longevity," deliberately hire "a person or firm who is new to the project." It
  costs ramp-up time, but afterward "they will now be invested in the project and may continue
  to participate," seeding a new pool of expertise.

## Be transparent about contracts

"In general, it's best to be open about contracts when you can." Otherwise a contractor's
behavior "may seem strange" — suddenly prioritizing features she "never shown interest in"
before — and she "can't answer convincingly if she can't talk about" the contract. The
complementary discipline: neither party should "act as though others should treat your
arrangement as a big deal." Contractors who "waltz onto a development list" expecting their
posts to count more "because they're being paid" signal that they value "the fact of the
contract — as opposed to the code." From the community's view "only the code matters"; "the
focus of attention should be kept on technical issues, not on the details of who is paying
whom." Transparency has a bonus: when multiple funders sponsor work on the same project,
"knowing what the others are trying to do" lets them "pool their resources." And resentment is
rarely a problem — "no one expects contract work to be distributed equally," and "it's
perfectly natural to have a few go-to people in the community"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=88), p. 75); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=89), p. 76).

## Community review is a free design board, not an obstacle

"The project's community will always be important to the long-term success of contract work."
Their involvement in design and review for sizeable changes "cannot be an afterthought… [it]
must be considered part of the work, and fully embraced by the contractor." The reframe:
"don't think of community scrutiny as an obstacle to be overcome — think of it as a free
design board and QA department"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=89), p. 76).

Fogel's cautionary tale is the 1995 CVS password-authentication contract he and Jim Blandy
took. Inexperienced at protocol design, they "made a few gaffes that would have been obvious
to an expert" — mistakes that "would easily have been caught had we taken the time to write up
a proposal and run it by the other developers for review." The "root of the problem was not
lack of experience… The problem was our attitude": they "regarded acceptance of the changes as
a hurdle to get over, rather than as a process by which the quality of the changes could be
improved." The lesson for selecting contractors: beyond technical skill, choose "someone with a
track record of constructive interaction with the other developers," so you get "an agent who
will be able to draw on a network of expertise"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=89), p. 76).

## RFI / RFP / contract language

When hiring outside vendors to *build* software for you, "the language you put in your
Requests For Information (RFIs), Requests For Proposals (RFPs), and contracts becomes crucially
important." The key thing to understand: "the decision makers at most large-scale software
development vendors don't really want their work to be open source." Their preferred model is
"bespoke software that, under the hood, shares many components with the other bespoke software
they're producing for other customers" — letting them "sell mostly the same product at full
price many times." This is "especially true of vendors to government agencies"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=89), p. 76).

So the customer "must require behaviors and deliverables that will result in a truly open
source product" — one "that has the potential to be supported and customized by vendors other
than the one who originally developed it." Fogel's requirement list (not exhaustive — "every
project is different")
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=90), p. 77):

- Design and development done "in the open from the very start" (see [[developing-in-the-open]]).
- Code "explicitly licensed for open source distribution, from the start… through delivery."
- If the vendor also deploys, "deployed code must match the open source code" — no "proprietary
  tweaks… via the back door through deployment customizations."
- "No dependencies on proprietary software modules" without written permission.
- Documentation "sufficient to allow third parties to understand, configure, and deploy," in
  open formats (plaintext, Markdown, AsciiDoc, DocBook).
- The vendor's community-management overhead "anticipated and budgeted for."
- Clear expectations about the vendor's role "in publicity about the project."
- "You, the customer, should be the copyright owner of the code."
- "An unambiguous, non-restrictive patent grant not just to you but to everyone who receives
  the code."
- If the vendor lacks open source experience, "bring in a separate Open Source Quality
  Assurance (OSQA) vendor."

## Open Source Quality Assurance (OSQA)

The recurring failure: "when a vendor whose normal mode is proprietary development is hired to
do open source, the result is usually a product that is not truly open source and that no third
party can actually deploy." Often the vendor isn't resistant, they "simply don't know what they
don't know." Open-source clauses in a contract "are effectively void unless there is some kind
of external review process," because most customers "do not have the in-house technical
capability" to test compliance
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=90), p. 77).

OSQA is the fix: a separate, independent vendor "to play the role of third-party open source
participant." It adapts the long contracting tradition of **IV&V** ("Independent Verification
and Validation"), where "the independent reviewer reports to the customer, not to the primary
development contractor." During development the OSQA reviewer "participates the way any third
party would" — posting in public forums, using the install docs, "reporting bugs via the public
tracker, submitting pull requests" — and as the project nears alpha/beta "confirms that the
software can be deployed as documented, without reliance on proprietary dependencies." But
"the reviewer's job is not just to review… [it] is there to help the primary vendor meet these
expectations… and to report back to the customer." Done right it yields "at least two
independent commercial entities able to deploy and support the software," and makes the primary
vendor "more inherently capable of performing quality open source work in the future." The
decisive design constraint: "the reviewer is responsible to the customer, not to the primary
development vendor." Cost runs "on the order of 5% to 10%" of the main contract
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=90), p. 77); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=91), p. 78).

## Negative Space

- **CVS password-auth / Subversion contractor case specifics** (`case-study-specifics`): the
  1995 partnership, the investment-bank client, the export-control constraint — illustrative
  detail; the "scrutiny as design board" principle is captured.
- **IV&V external links** (`tool-specific/perishable`): the Wikipedia references for IV&V are a
  pointer, not content; the concept (independent reviewer reporting to the customer) is paged.
- **Microsoft Word / .docx footnote** (`illustrative-scaffolding`): a vivid aside on why
  proprietary doc formats don't suit open source; subsumed by the "open formats" requirement.
- **Verbatim RFP legalese** (`too-granular`): the exact contract wording is a per-project
  drafting detail; captured here as decision criteria, not boilerplate to reproduce.

## See also

- [[open-source-economics]] — the buy-credibility-not-control principle contracting makes
  concrete.
- [[corporate-open-source-participation]] — the same "earn acceptance" discipline for in-house
  funded developers rather than contractors.
- [[government-and-open-source]] — why RFP language and OSQA matter most for contractor-reliant
  public agencies.
- [[developing-in-the-open]] — "in the open from the start," the first and load-bearing RFP
  requirement.
- [[code-review]] — the public review process a best-effort clause commits the contractor to.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 5 "Organizations and Money" —
  "Contracting," "Hiring From Within / Outside the Community," "Contracting and Transparency,"
  "Review and Acceptance of Changes," "Update Your RFI, RFP and Contract Language," "Open
  Source Quality Assurance (OSQA)" (printed pp. 74–78).
