---
title: Committers
aliases: [committership, commit-access, partial-commit-access, revoking-commit-access, dormant-committers]
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

# Committers

A **committer** is "someone who has commit access: the right to make changes to the copy of
the code that will be used for the project's next official release." The definition is
deliberately about *authority*, not mechanics: anyone can set up a repository and commit to
it (the default mode of decentralized [[version-control]]), but "what matters for the
project's purposes is who has the ability to put changes into the authoritative copy"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=164), p. 151).
The term survives from centralized version control — where "commit access" literally meant
running the `commit` command — even though today the gating happens on `push`/`pull`. "The
authoritative repository is a social concept, not a technical concept," so the label persists
in its identifying sense regardless of the underlying command
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=164), p. 151).

## The only formally distinct class — necessary discrimination

Committers are "the only formally distinct class of people found in all open source projects,"
and Fogel frames them bluntly as "an unavoidable concession to discrimination in a system
which is otherwise as non-discriminatory as possible." This is not pejorative: "Quality
control requires, well, control." Many people feel qualified to change a program; fewer
actually are, so "the project cannot rely on people's own judgement; it must maintain
standards and grant commit access only to those who meet those standards"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=164), p. 151).
The cost is a built-in power dynamic — people who can commit working beside people who cannot —
"that dynamic must be managed so that it does not harm the project." Because committers "are
ultimately responsible for the project's code base, and for the quality of its public software
releases," the long-term health of the project depends on how they work — though this is about
committers specifically, not all maintainers (not all of whom are coders)
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=164), p. 151).

## Choosing committers: the Hippocratic Principle

The basis for granting access is "first, do no harm." The decisive criterion "is not technical
skill or even deep familiarity with the code, but simply that a person show good judgement" —
and "judgement includes knowing what not to take on." A contributor who posts only small
patches that "apply cleanly, do not contain bugs, and are mostly in accord with the project's
log message and coding conventions," in enough quantity "to show a clear pattern," has proven
the thing that matters: "he is capable of judging his own abilities." The mechanics are a
subset of choosing maintainers generally — an existing committer proposes, and "if at least
(say) three people say yes, and no one objects, then the offer is made"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=164), p. 151).

When a proposal *does* provoke discussion, "it is usually not about technical ability, but
rather about the person's behavior in the project's discussion forums." Someone skilled but
"consistently belligerent or uncooperative in public forums" is a serious concern: "social
skills, or the ability to 'play well in the sandbox', are as important as raw technical
ability." Because everything is under version control, the penalty for a wrong choice "is not
so much the problems it could cause in the code (review would spot those quickly anyway), but
that it might eventually force the project to revoke the person's commit access" — an act that
"can sometimes fragment the whole community"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=165), p. 152).
That [[code-review]] catches bad code is precisely why committer selection is a *social* gate,
not a code-quality one.

Guard against the opposite failure too — committership hardening into "a matter of membership
in an exclusive club." Demanding a quota of nontrivial patches "isn't always a bad policy,"
but the question to keep in mind "should be 'What will bring the best results for the code?'
not 'Will we devalue the social status associated with committership by admitting this
person?'" The point of commit access "is not to reinforce people's self-worth; it's to allow
good changes to enter the code with a minimum of fuss." Hence the arithmetic of inclusion:
"If you have 100 committers, 12 of whom make large changes on a regular basis, and the other
88 of whom just fix typos and small bugs a few times a year, that's still better than having
only the 12"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=165), p. 152).

## Revoking commit access

"The first thing to be said about revoking commit access is: try not to be in that situation
in the first place." Such discussions "can be very divisive" and are "a time-consuming
distraction from productive work" even when they aren't. When unavoidable, the discussion is
held "privately among the same people who would be in a position to vote for granting that
person whatever flavor of commit access they currently have. The person himself should not be
included." This is the one deliberate exception to the project's usual injunction against
secrecy, for two reasons: "no one would be able to speak freely otherwise," and if the motion
fails, knowledge that it was even considered "could open up questions… that lead to the worst
sort of factionalism." No participant may "on her own initiative, reveal information from a
discussion and ballot that others assumed were secret." Once access is revoked the fact is
"unavoidably public," so present it as tactfully as possible
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=165), p. 152).

## Partial commit access

Projects can offer "gradations of commit access" — free rein in documentation, translations,
language bindings, or packaging files, but not the core code, i.e. "places where a mistake
will not result in a problem for the core project." Because commit access often doubles as
membership in an electorate, partial access raises a voting question. Subversion's answer:
"a partial committer can vote on matters confined exclusively to that committer's domain, and
not on anything else," with a mechanism for **advisory votes** ("+0" or "+1 (non-binding)")
so non-binding voices aren't silenced. "Full committers can vote on anything… and only full
committers vote on adding new committers of any kind," though adding *partial* committers is
usually delegated — any full committer can "sponsor" one, and existing partial committers in a
domain can effectively choose new ones for that same domain
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=165), p. 152).
The general principle: "Each committer should be able to vote on matters that fall within the
scope of her commit access, and not on matters outside that," with procedural questions
defaulting to full committers. Voting should be rare regardless. And it is "often best not to
have the version control system enforce partial commit domains, even if it is capable of doing
so" — partition is a social agreement, not a technical wall
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=166), p. 153).

## Dormant committers: don't expire access

Auto-removing access after a period of inactivity is "usually unhelpful and even
counterproductive." It "may tempt some people into committing acceptable but unnecessary
changes" just to stay alive, and it serves no real purpose: "If the main criterion for
granting commit access is good judgement, then why assume someone's judgement would
deteriorate just because she's been away from the project for a while?" A returning committer
"will know how out of touch she is, and act accordingly." Fogel's maxim: "If high school
diplomas do not expire, then commit access certainly shouldn't." (If a committer *asks* to be
removed or marked dormant, the project should of course accede)
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=166), p. 153).

## Avoid mystery: publish the rules and the roster

While the discussion around any *particular* candidate must stay confidential, "the rules and
procedures themselves need not be secret. In fact, it's best to publish them, so people
realize that the committers are not some mysterious Star Chamber, closed off to mere mortals,
but that anyone can join simply by posting good patches and knowing how to handle herself in
the community." Publish the roster too — conventionally a `MAINTAINERS` or `COMMITTERS` file at
the top of the source tree, full committers first, then each partial-commit domain, "each
person… listed by name and identifying handle(s)." The list records only the formal full/partial
distinction; it "should not try to indicate the informal distinctions that inevitably arise in
a project, such as who is particularly influential and how. It is a public record, not an
acknowledgements file"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=166), p. 153).

## Negative Space

- **Mechanics of choosing maintainers / "Who Votes?"** (`subsumed-by` [[open-source-governance]]):
  Fogel explicitly defers the voting mechanics for selecting committers to the maintainer-voting
  treatment; this page captures the *standards* committers are judged by, not the ballot
  procedure.
- **Subversion's specific partial-commit arrangement** (`case-study-specifics`): the exact
  Subversion domains and "+0/+1 (non-binding)" notation illustrate the general principle —
  vote within your domain — which is captured instead.
- **Version-control authorization configuration** (`tool-specific/perishable`): the §Authorization
  cross-reference on whether/how a VCS can enforce commit domains is tooling detail, folded into
  the "don't enforce in the VCS" principle.

## See also

- [[open-source-governance]] — the maintainer-selection and voting machinery committership is a
  formal subset of.
- [[code-review]] — the safety net that makes granting commit access low-stakes for the code,
  shifting the committer question onto judgement and conduct.
- [[contributor-motivation]] — why commit access must not be treated as a status reward.
- [[preventing-territoriality]] — partial domains as responsibility without exclusive ownership.
- [[credit-and-attribution]] — the public record of contribution from which committers are
  typically drawn.
- [[forks]] — why committers keep their access even when they work on a fork.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 8 "Managing Participants" —
  §Committers (Defining "Committer", Committers vs Maintainers, Choosing Committers, Revoking
  Commit Access, Partial Commit Access, Dormant Committers, Avoid Mystery) (printed pp. 151–153).
