---
title: Delegation in Open Source
aliases: [delegation, inquiry-vs-assignment, follow-up-after-delegating, distinguish-inquiry-and-assignment]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-participation, software-collaboration]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Delegation in Open Source

In a project where contributors are volunteers (or work for different employers), delegation
is not a command but an *invitation* — and its real payoff is rarely the task itself. Fogel's
core reframing: "Delegation is not merely a way to spread the workload around; it is also a
political and social tool"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=150), p. 137).
It is the primary instrument for converting [[contributor-motivation]] into deeper
involvement.

## Every request has social side effects

When you ask someone to do something, the obvious effect is that — if he accepts — he does it
and you don't. But "another effect is that he is made aware that you trusted him to handle the
task," and if the request was made in public, "he knows that others in the group have been
made aware of that trust too." If the task needs coordination, you are effectively "proposing
that he become more involved, form bonds… and perhaps become a source of authority in some
subdomain of the project"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=150), p. 137).

Because a public request also creates "some pressure to accept," you must always "ask in a way
that allows him to decline gracefully if he doesn't really want the job"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=150), p. 137).

## Delegate even when you could do it faster

The surprising corollary: "it often makes sense to ask someone else to do something even when
you know you could do it faster or better yourself." Beyond the ordinary comparative-advantage
argument (your time may be better spent elsewhere), the deeper reason is investment — "in the
long run you want to draw that person deeper into the project, even if it means spending extra
time watching over them at first." The converse builds the same capital: occasionally
volunteering for work no one else wants "will gain her good will and respect." Delegation and
substitution are "about drawing people into a closer commitment with each other and to the
project"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=150), p. 137).

## Distinguish clearly between inquiry and assignment

Sometimes it is fair to expect acceptance — when someone wrote the bug, committed
non-conforming code, or publicly promised to do something. But in many cases "it is by no
means clear that you have a right to expect action," and "since no one likes to be taken for
granted," you must tailor the request to the situation
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=150), p. 137).

Ticket assignment is "particularly fertile ground" for this mistake. Assigning a bug to a
known expert *without her prior permission* can make her feel "she is, in effect, being
punished for her expertise" — after all, "the way to acquire expertise is by fixing bugs, so
perhaps someone else should take this one." (A tracker that *auto-assigns* by rule offends
less, "because everyone knows that the assignment was made by an automated process, and is not
an indication of human expectations")
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=150), p. 137).

When you can't afford a round-trip for every routing decision, "make the assignment in the
form of an inquiry, conveying no pressure" — a tracker comment that publicly confirms the
assignee's expertise *and* makes the opt-out explicit:

> "Assigning this over to you, jrandom, because you're most familiar with this code. Feel free
> to bounce this back if you don't have time to look at it, though."

The audience "isn't only the assignee, it's everyone": the group sees the public confirmation
of expertise while the assignee stays free to accept or decline
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=151), p. 138).

## Follow up after you delegate

"When you ask someone to do something, remember that you have done so, and follow up with her
no matter what." On a positive response, watch for progress and comment on it — "everyone
works better when they know someone else is appreciating their work." On no response, ask
again, or announce you're looking for someone else, or do it yourself — but always note that
you got no response
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=151), p. 138).

The point of publicly noting a non-response "is not to humiliate the person" but "to show that
you keep track of what you have asked for." That visible attentiveness "makes people more
likely to say yes next time," because they observe that you notice work — given that you even
noticed "the much less visible event of someone failing to respond"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=151), p. 138).

## Notice what people are interested in

Better requests start from knowing what each contributor actually wants: "the more aspects of
someone's personality you notice and remember, the more comfortable she will be." Fogel's
Subversion example contrasts developers driving toward a 1.0 release with those who "mainly
wanted to add new features and work on interesting problems but who didn't much care when 1.0
came out" — neither better, just different. The warning is about projection: "Electronic media
can be very deceptive: you may sense an atmosphere of shared purpose when, in fact, it's shared
only by the people you happen to have been talking to." Even demonstrating that you understand
what someone wants — with no request attached — is useful, because "it confirms to each person
that she's not just another particle in an undifferentiated mass"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=151), p. 138).

## Negative Space

- **Verbatim tracker-comment wording** (`illustrative-scaffolding`): the exact "jrandom"
  example text is captured as a pattern, not transcribed in full as a recipe.
- **Comparative-advantage / opportunity-cost economics** (`too-granular`): the strict
  efficiency argument for delegation is noted as the *ordinary* case the social argument
  exceeds, not developed as economics.

## See also

- [[contributor-motivation]] — the "why" delegation converts into involvement.
- [[praise-and-criticism]] — the feedback half of the same attention economy.
- [[bug-tracking]] — where inquiry-vs-assignment plays out on tickets.
- [[sharing-project-management]] — delegation scaled up into standing management roles.
- [[open-source-governance]] — informal authority, which delegation helps distribute.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 8 "Managing Participants" —
  §Delegation, §Distinguish Clearly Between Inquiry and Assignment, §Follow Up After You
  Delegate, §Notice What People Are Interested In (printed pp. 137–138).
