---
title: Funding Non-Programming Activities
aliases: [non-code-funding, funding-non-programming-work, professional-testing]
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

# Funding Non-Programming Activities

Programming "is only part of the work that goes on in an open source project" — and "the most
visible and glamorous part," which is exactly why testing, documentation, and the rest "can
sometimes be neglected." Organizations "are sometimes in the best position to make up this gap,
by devoting some of their own staff time"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=92), p. 79).
This page is the catalogue of *where* a funder's money does the most good once it accepts
[[open-source-economics]]'s lesson that money buys credibility, not control: every item below is
a way to convert resources into community standing by doing visible, useful, non-code work.

## The bridging principle

The single discipline underlying all funded non-code work is translation between two worlds:
"the key to doing this successfully is to translate between the company's internal processes and
those of the public development community. Such translation is not effortless: often the two are
not a close match, and the differences can only be bridged via human intervention." Even with
identical tracker software, "the data stored in it will be very different, because the
bug-tracking needs of a company are very different from those of a free software community" — a
fact that "may need to be reflected in the other, with confidential portions removed or… added."
The target outcome states the constraint precisely: the project "runs more smoothly, the
community recognizes the company's investment of resources, and yet does not feel that the
company is inappropriately steering things toward its own goals"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=92), p. 79).

## Professional testing (Technical Quality Assurance)

Dedicated QA teams are "normal" in proprietary development but "not pursued as vigorously" by
free-software communities, for three structural reasons: it is "hard to get highly-motivated
labor for unglamorous work like testing" (committers "have their names inscribed for all time…
but there are fewer mechanisms for remembering the tester who found the bug"); developers "assume
that having a large user community gives the project good testing coverage"; and not all
developers "have access to the requisite hardware resources"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=93), p. 80).

The many-users-equals-many-testers assumption "is not entirely baseless" — basic-functionality
bugs in common environments "will quickly be found by users in the natural course of things." But
users "are just trying to get work done," so they "do not consciously set out to explore
uncharted edge cases," often "silently implement the workaround without bothering to report the
bug," and — "most insidiously" — the "usage patterns of your customers… may differ in
statistically significant ways from the usage patterns of the Average User In The Street." A
professional team probes exactly these gaps, so a bug report from it "is in some ways more
valuable than one received from users at large"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=93), p. 80).

The bridging problem is that internal reports carry "company-specific jargon," confidential
metadata, and priority annotations "inappropriate for the public bug tracker." The solution is a
**dual-ticket pattern**: either the QA department "file[s] tickets directly in the public ticket
tracker" (preferred — it gives the public "a direct appreciation of your company's involvement,"
adds organizational credibility "just as any technical contribution would," and opens "a direct
line of communication to the testing team"), or "an intermediary (usually one of the developers)
can 'translate' the testing department's internal reports into new tickets." Once a public ticket
exists, "the original internal ticket should simply reference the public ticket for technical
content." Expect overhead: "maintaining two tickets for one bug is, naturally, more work," repaid
because "many more coders will see the report"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=93), p. 80).

## Legal advice — and engaging counsel early

Corporations "are almost the only entities that ever pay attention to complex legal issues in
free software"; individual developers "do not have the time or resources to competently handle
legal issues themselves." A legal department can assist "with trademark issues, copyright license
ownership and compatibility questions, defense against patent trolls," and — if the project
organizes formally or joins an umbrella org — "issues of corporate law, asset transfer, reviewing
agreements, and other due diligence." The governing caution mirrors the bridging principle:
communications between legal and the development community must "happen with a mutual appreciation
of the very different universes the parties are coming from," often needing "a liaison (usually a
developer, or else a lawyer with technical expertise)… to translate"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=93), p. 80); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=94), p. 81).

The timing rule is **"don't surprise your lawyers."** Corporate lawyers "sometimes have an uneasy
relationship with free software" because "they have often spent their careers diligently seeking
to maximize the control and exclusivity their clients have." The ideal "is to make sure your
lawyers first understand why you are running an open source project, and give them a chance to
familiarize themselves with open source in general, before you bring the particulars… to them."
Critically: "do not assume that open source is part of a standard legal education. It is not, at
least as of this writing in 2022." Consulting legal only "after development is already under way"
forces them "to scramble and make under-researched decisions hastily"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=92), p. 79).
The deeper licensing, trademark, and patent material is forward-referenced to Ch.9 and will
enrich [[open-source-licensing]].

## Documentation and usability

Both are "famous weak spots." Fogel thinks the documentation gap is "frequently exaggerated," yet
concedes it is "empirically true that much open source software lacks first-class documentation
and usability research." The counter-intuitive staffing rule: "hire people who are not regular
developers on the project." Two reasons — you "don't take development time away from the project,"
and "those closest to the software are usually the wrong people to write documentation or
investigate usability anyway, because they have trouble seeing the software from an outsider's
point of view." The hire must still "be technical enough to talk to the coding team, but not so
expert in the software that they can't empathize with regular users." The crisp heuristic:
"a medium-level user is probably the right person to write good documentation" — recent enough to
the system "to remember the problems," but "past them" enough to describe the way through
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=94), p. 81).

## User-experience (UX) work

The recurring error is to treat UX as a deliverable: "user experience design is not a checkbox.
It is an attitude taken by a team throughout development." So the primary qualification "to look
for in UX contractors is their ability to gain long-term credibility with the developers, and to
help developers pay attention to user experience goals." Effective UX requires that results
"be presented to the development team in a way that makes it easy for the developers to take the
results seriously," which "can only happen through a sustained, two-way interaction, in which UX
experts are subscribed to the appropriate project forums and take the attitude that they are a
kind of specialized developer on the project, rather than an outside expert providing advice."
Prefer "UX experts who have worked with open source projects before"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=94), p. 81); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=95), p. 82).

## Infrastructure: build farms and development servers

Some project needs "cost more money than any individual developer has at their disposal" —
notably "continuous integration (CI) testing, a.k.a. build farms." A funder can "donate the
server space and bandwidth and the technical expertise to set up the continuous integration and
automated testing," or, lacking the expertise on staff, "hire someone from the project to do it,
or at the very least give some of the project's developers administrative access to the CI
servers so they can set things up themselves." See [[continuous-integration]]
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=95), p. 82).

## Security audits

If a company "has a good internal security department, or can afford to hire specialists,
providing in-depth security review… can do the project a tremendous amount of good." Findings
must be returned "using the precautions" of responsible disclosure (the report-handling
procedure is developed later, in Ch.6). One asymmetry worth noting: while the *findings* follow
disclosure discipline, "it is fine to be public about the fact that you are conducting the audit;
there your organization should get credit for a substantial contribution like that"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=95), p. 82).

## Sponsoring in-person meetings

"A very effective use of funds is to sponsor in-person contact between developers who might not
otherwise meet." "From a corporate sponsorship point of view, nothing creates good will like a
plane ticket and a hotel room," and project-centric meetups are "the perfect neutral ground" when
peers work at other companies. Conference attendance also signals commitment in a way that
compounds: meeting your developers once signals "a real investment," but when they "show up again
at the same conference the next year, still working on the same project, that's a very powerful
signal that your organizational commitment… is long-term and strategic" — which buys both
influence (they are "seen as people who will be around for the long term") and "a recruiting
advantage." Even without travelers you can sponsor expenses: "everyone remembers fondly the
company that sponsors the pizza, or lunch, or drinks or dinner"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=95), p. 82).

## Negative Space

- **Dirk Reiners documentation email** (`illustrative-scaffolding`): a reader's anecdote
  confirming the "medium-level user writes the best tutorial" point; the principle is captured,
  the quoted email is not paged.
- **Responsible-disclosure report-handling mechanics** (`foreshadowing`): the "Receive the
  Report" procedure for routing security findings is named but developed in Ch.6 (Communications),
  not yet ingested — left as a dead reference.
- **Build-farm / automated-testing mechanics** (`foreshadowing`): the operational detail of CI
  and automated testing is forward-referenced to Ch.7 ("Automated testing") and will enrich
  [[continuous-integration]]; captured here only as a funding target.
- **Conference/hackfest logistics** (`foreshadowing`): the mechanics of running in-person
  meetings are deferred to the later "Meeting In Person" section; captured here only as a use of
  funds.
- **The New Developer Test** (captured, not rejected): the concrete OSQA technique that sits at
  this page's boundary is recorded under [[open-source-contracting]], where the rest of OSQA
  lives.

## See also

- [[open-source-economics]] — the buy-credibility-not-control premise that makes every item here
  a credibility investment rather than a purchase of influence.
- [[corporate-open-source-participation]] — the behavioral playbook for *how* funded staff
  conduct themselves; this page is *what* the money can usefully buy.
- [[open-source-contracting]] — funded *code* work and OSQA, including the New Developer Test; the
  same translate-between-worlds discipline.
- [[bug-tracking]] — the public tracker the dual-ticket pattern bridges into.
- [[continuous-integration]] — the build-farm infrastructure a funder can donate.
- [[open-source-marketing]] — converting the same investment into market positioning.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 5 "Organizations and Money" —
  "Don't Surprise Your Lawyers," "Funding Non-Programming Activities," "Technical Quality
  Assurance," "Legal Advice and Protection," "Documentation and Usability," "Funding User
  Experience (UX) Work," "Providing Build Farms and Development Servers," "Running Security
  Audits," "Sponsoring Conferences, Hackathons, and other Developer Meetings" (printed pp. 79–82).
