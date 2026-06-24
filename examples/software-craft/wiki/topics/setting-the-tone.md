---
title: Setting the Tone
aliases: [project-culture, setting-precedents, codes-of-conduct, in-group-behaviors]
date: 2026-06-23
last_updated: 2026-06-24
type: topic
topics: [open-source-culture, software-collaboration]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Setting the Tone

Picking a license and standing up a web site are "one-time tasks you do during project
setup," but "the most important aspects of starting a new project are dynamic." Choosing
a mailing-list address is easy; "ensuring that the list's conversations remain on-topic
and productive is another matter entirely"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=34), p. 21).
The companion to the static launch checklist in [[launching-an-open-source-project]] is
this: the founders set the project's working culture, on purpose, through their own early
conduct.

## Culture is transmitted, not legislated

"The first steps are the hardest, because precedents and expectations for future conduct
have not yet been set." Stability "does not come from formal policies, but from a shared,
hard-to-pin-down collective wisdom that develops over time." Written rules exist, but they
"tend to be essentially a distillation of the intangible, ever-evolving agreements that
really guide the project" — the policies "do not define the project's culture so much as
describe it, and even then only approximately"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=34), p. 21).

Because culture is carried by transmission, "growth and high turnover are not as damaging
to the accumulation of social norms as one might think." As long as change "does not happen
too quickly," new arrivals have time to learn how things are done, "and after they learn,
they will help reinforce those ways themselves" — Fogel's analogy is children's songs that
survive for centuries despite complete turnover of the singers, because they are
"transmitted regularly and repeatedly." The faster turnover of a software project "must be
compensated for by a more active and deliberate transmission effort"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=34), p. 21).

## Set precedents early; make useful behaviors the "in-group" ones

The transmission dynamic is exploitable. "People generally show up expecting and looking
for social norms" — in any group "unified by a common endeavor, people who join
instinctively search for behaviors that will mark them as part of the group." So "the goal
of setting precedents early is to make those 'in-group' behaviors be ones that are useful
to the project; once established, they will be largely self-perpetuating"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=34), p. 21).
The practical leverage: physically every developer "may be working separately, but you can
do a lot to make them feel like they're all working together in the same room. The more
they feel this way, the more time they'll want to spend on the project." The sections below
are the load-bearing precedents to set.

## Public by default — avoid private discussions

Founders are repeatedly tempted to "settle difficult questions by private communications
among an inner circle," especially early on when there are many decisions and few people
qualified to make them. Fogel's instruction is blunt: "Don't do it." Making important
decisions in private "is like spraying contributor repellent on your project. No serious
contributor would stick around for long in an environment where a secret council makes all
the big decisions behind closed doors"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=35), p. 22).

Public discussion carries beneficial side effects beyond resolving the immediate question
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=35), p. 22):

- It **trains new developers** — silent lurkers glean how the software works even when they
  never post.
- It **trains you** to explain technical issues to people less familiar with the code than
  you — "a skill that requires practice, and you can't get that practice by talking to
  people who already know what you know."
- It leaves a **permanent public archive**, so future discussions "avoid retracing the same
  steps."

There is also the chance that a listener makes a real contribution — and Fogel argues this
is "more likely than you might expect," citing Subversion's founders, who doubted anyone on
the new list could help with their "deep and complex" problems, took conversations private,
were nudged back to the public list, and "were stunned by the number of insightful comments
and suggestions that quickly resulted." Without claiming "the group is always smarter than
the individual," he notes groups excel at two things: "massive peer review" and "generating
large numbers of ideas quickly"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=35), p. 22).

The governing rule: **"If there's no reason for it to be private, it should be public."**
Making this real "requires action" — it is not enough to route your own posts to the public
list; you must "nudge other people's unnecessarily private conversations to the list too."
When someone opens a private thread without cause, "open the appropriate meta-discussion
immediately" and don't even engage the topic until the conversation is public or privacy is
confirmed genuinely necessary. Done consistently, "people will catch on pretty quickly and
start to use the public forums by default"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=35), p. 22).
This is the discussion-level expression of the broader transparency norm developed in
[[developing-in-the-open]].

## Nip rudeness in the bud

From the project's first public moment, "maintain a zero-tolerance policy toward rude or
insulting behavior." Critically, "zero-tolerance does not mean technical enforcement per
se" — not removing people from the list or revoking commit access — it "simply means never
letting bad behavior slide by unnoticed." When a post mixes a technical comment with an ad
hominem attack, "it is imperative that your response address the ad hominem attack as a
separate issue unto itself, separate from the technical content"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=35), p. 22).

The mechanism is a light touch, because in technical debate "it's often hard to tell where
technical debate leaves off and character attack begins, which is one reason why drastic
responses or punishments are not a good idea." A "Nice Police" post stresses keeping the
discussion friendly "without accusing anyone of being deliberately poisonous." Three rules
make it work ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=36), p. 23):

- **Keep the meta-discussion an aside**, never the main topic — "a brief preface to the main
  portion of your response," then move on to real content so people have something on-topic
  to answer.
- **Never demand an apology or acknowledgement.** Calling out the behavior while not
  demanding contrition "leave[s] people free to cool down and show their better side …
  next time — and they will." Demanding it "will only cause resentment."
- **Refuse to be drawn into an argument** about whether the rebuke was deserved.

The aim is to make "good etiquette be seen as one of the 'in-group' behaviors." This is a
"long-term survival strategy": flame wars silently drive away contributors — "someone might
lurk on the mailing list, see that it takes a thick skin to participate … and decide
against getting involved at all." It is "easier to do when the project is still small,"
and once it is part of the culture, "it will be maintained by everyone"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=36), p. 23).
Fuller treatment of recurring conflict and disruptive individuals is developed in
[[difficult-people]] (Ch.6).

## Codes of conduct

Since the book's 2006 first edition it "has become somewhat more common for open source
projects, especially the larger ones, to adopt an explicit code of conduct" — a trend Fogel
endorses. As projects "become … more diverse," a code of conduct reminds participants "that
the maintenance of a respectful and welcoming environment is everyone's responsibility." The
most popular template is the **Contributor Covenant**, and adopting it carries a positive
feedback dynamic: more developers are already familiar with it and its translations come
for free ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=36), p. 23).

Two cautions temper the endorsement
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=36), p. 23); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=37), p. 24):

- A code "will not solve all the interpersonal problems," and if misused "has the potential
  to create new problems" — some people "specialize in manipulating social norms and rules
  to harm a community rather than help it." Enforcement therefore falls to "the project
  leadership, by which I mean those whom others in the project tend to listen to the most,"
  who must "see to it that a code of conduct is used wisely." This ties code-of-conduct
  authority to the de-facto influence structure described in [[open-source-governance]].
- **Disagreeing with the need for a code of conduct is not itself a violation of one.** If
  participants argue in good faith that a code could do more harm than good, "it is
  imperative that you help make sure they're able to state their view without being attacked
  for it." Conflating the two is a recurring confusion that "need[s] to be reminded of."

A separate **Commercial / Corporate Code of Conduct (CCoC)** or **Organizational Code of
Conduct (OCoC)** may be warranted when organizational actors participate "in ways that might
not be conducive to the project's long-term health"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=37), p. 24).
This anticipates the corporate-participation tensions developed in Ch.5
([[open-source-governance]] covers the power dimension).

## Negative Space

- **Children's-songs analogy** (`illustrative-scaffolding`): the centuries-of-transmission
  image explains *why* norms survive turnover; the transferable claim (norms persist by
  active, repeated transmission) is captured, the analogy is not paged.
- **Subversion / Behlendorf private-discussion anecdote** (`illustrative-scaffolding`): the
  founders' eye-rolling move back to the public list dramatizes the "public is more
  productive" claim; the claim is captured, the story is not.
- **The verbatim "Nice Police" example post** (`illustrative-scaffolding`): the sample
  rebuke about a "naive and ignorant" security design illustrates tone; the three operating
  rules are captured instead of the script.
- **Specific code-of-conduct documents** (`tool-specific/perishable`): the Contributor
  Covenant URL, the Arches Commercial guidelines, and the Bytecode Alliance draft OCoC are
  named only as examples; the decision criteria (when a CCoC/OCoC is warranted, who
  enforces) are captured, the documents are not.
- **Recurring-conflict and difficult-people mechanics**: zero-tolerance here is the
  *early-precedent* form; the scaling treatment of conflict, "Difficult People," and
  "Recognizing Rudeness" (Ch.6) is developed in [[difficult-people]], [[written-communication]],
  and [[scaling-project-communication]].

## See also

- [[developing-in-the-open]] — the artifact-level transparency norm; "avoid private
  discussions" is its discussion-level twin.
- [[launching-an-open-source-project]] — the static presentation checklist this page's
  dynamic, behavioral culture-setting completes.
- [[open-source-governance]] — the influence structure that must enforce a code of conduct
  and that developer guidelines should state plainly.
- [[code-review]] — "Practice Conspicuous Code Review" is itself one of the tone-setting
  precedents from this same section, developed on its own page.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 2 "Getting Started",
  §Setting the Tone — "Avoid Private Discussions," "Nip Rudeness in the Bud," and "Codes of
  Conduct" (printed pp. 21–24).
