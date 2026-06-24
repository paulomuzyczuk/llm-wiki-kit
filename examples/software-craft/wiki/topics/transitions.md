---
title: Transitions
aliases: [role-transitions, asking-someone-to-step-down, succession, replacing-a-role-holder]
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

# Transitions

Every standing role — patch manager, translation manager, release manager — eventually
outlives its holder's ability or willingness to do it. "From time to time, a person in a
position of ongoing responsibility… will become unable to perform the duties of the position,"
whether because the job "turned out to be more work than he anticipated" or because of "a
change in employment, a new baby, whatever." Managing that handoff gracefully is its own craft,
and it is the remedy of last resort when [[praise-and-criticism|criticism]] of someone failing
in a role hasn't worked
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=162), p. 149).

## The slow fade — and why you have to notice it

People rarely resign cleanly. "When a person gets swamped like this, he usually doesn't notice
it right away. It happens by slow degrees." The visible signature is a rhythm, not an
announcement: "the rest of the project just doesn't hear much from him for a while," then "a
flurry of activity, as he feels guilty," then silence again. "There's rarely an unsolicited
formal resignation," because to resign "would mean openly acknowledging… that his ability to
fulfill a commitment has been permanently reduced," which people are reluctant to admit
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=162), p. 149).

So the burden falls on everyone else "to notice what's happening — or rather, not happening —
and to ask the person what's going on." The inquiry must be "friendly and 100% guilt-free":
its "purpose is to find out a piece of information, not to make the person feel bad." Make it
visible to the project by default, "so that if the person responds by saying that he won't be
able to do the job anymore, there's a context established for your next public post: a request
for a new person to fill that role"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=162), p. 149).

## Asking someone to step aside: a multistep process

When someone "just isn't working out in the role… even after everyone else has given all the
help and suggestions they can," and doesn't see it himself, "he'll need to be told." Fogel's
sequence, each step load-bearing
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=162), p. 149):

1. **Check your own perception first.** "Privately talk to others in the project to see if they
   agree that the problem is as serious as you think it is." Even if you're certain, this signals
   that you're considering acting — and usually others "will just be happy you're taking on the
   awkward task, so they don't have to."
2. **Contact the person privately, kindly but directly.** Be specific, "giving as many examples
   as possible," and note that people had tried to help but the problems persisted. "You should
   expect this email to take a long time to write," and the rule is "if you don't back up what
   you're saying, you shouldn't say it at all." Offer that there are "many other ways to
   contribute." Crucially, at this stage "don't say that you've talked to others about it;
   nobody likes to be told that people were conspiring behind his back."

The reactions, in descending order of ease
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=163), p. 150):

- **He agrees / won't argue.** Suggest "he make the announcement himself," then follow up
  seeking a replacement.
- **He asks for one more chance.** A judgement call — but "don't agree to it just because you
  feel like you can't refuse such a reasonable request." Often there's a good reason to decline:
  "there have already been plenty of chances and that's how things got to where they are now."
  ("Eventually, one of the tries has to be the last one.")
- **He disagrees outright.** "Accept that things are going to be awkward and plow ahead anyway."
  *Now* is the time to say you talked to others — "but still don't say who until you have their
  permission." Be "insistent, but never threatening."

## The transition happens when the new person starts

A liberating reframe: "with most roles, the transition really happens the moment someone new
starts doing the job, not the moment the old person stops doing it." You and other influential
people "can solicit for a new issue manager" without first extracting a resignation — "it's not
actually necessary that the person who was previously doing it stop doing it, as long as he does
not sabotage… the efforts of the new person"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=163), p. 150).

## Don't dodge it by adding a "helper"

The tempting evasion — "instead of asking the person to resign, why not just frame it as a
matter of getting him some help?… have two issue managers" — is "generally not a good idea."
What makes manager roles useful "is their centralization. Those things that can be done in a
decentralized fashion are usually already being done that way." Splitting one role adds
"communications overhead" and "the potential for slippery displacement of responsibility ('I
thought you brought the first aid kit!')." There are exceptions where two people genuinely mesh,
"but these are not likely to be applicable when you see someone flailing in a role he is not
suited for"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=163), p. 150).

## Privacy is the most important factor

The overriding rule is "giving him the space to make a decision without feeling like others are
watching and waiting." Fogel's own cautionary tale: to save time he once emailed the Subversion
release manager *and* the two people ready to replace him in a single message. "I was wrong. The
current release manager was very offended, and rightly so. It's one thing to be asked to hand
off the job; it's another thing to be asked that in front of the people you'll hand it off to."
He apologized; the manager stepped aside gracefully and stayed involved, "but his feelings were
hurt" — and it was a poor start for the new managers too
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=163), p. 150).

## Negative Space

- **Verbatim "one more try" email exchange** (`illustrative-scaffolding`): the quoted mail to the
  release manager illustrates how to decline a request for another chance; the transferable
  rule — there's a point past which "one more try" only prolongs the agony — is captured above.
- **The three-party-email mistake as narrative** (`illustrative-scaffolding`): retained only as
  the source of the durable principle (privacy: never ask someone to step down in front of their
  successors), not as a paged case study.

## See also

- [[praise-and-criticism]] — the feedback discipline whose failure makes a transition necessary;
  "the solution is for the group to remove that person from the position… minimizing hurt
  feelings."
- [[sharing-project-management]] — the standing management roles that these transitions hand off,
  and the "document the process so someone else can pick it up" duty that eases them.
- [[difficult-people]] — the related but distinct case of someone obstructing rather than merely
  underperforming.
- [[committers]] — the parallel, harder transition of revoking commit access.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 8 "Managing Participants" —
  §Transitions (printed pp. 149–150).
