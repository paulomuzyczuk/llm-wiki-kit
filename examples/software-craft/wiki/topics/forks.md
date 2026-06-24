---
title: Forks
aliases: [hard-forks, forking, development-forks, handling-a-fork, initiating-a-fork]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-governance, open-source-culture]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Forks

Where [[forkability]] is the *latent* right — the ever-present possibility of copying the code
that caps everyone's power — this page is about what happens when an actual fork occurs. "At
its most basic, a fork is when one copy of a project diverges from another copy: think 'fork in
the road'." What the divergence *means* "depends on the intentions behind the fork"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=168), p. 155).

## Development forks versus hard forks

The word now spans two very different things
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=168), p. 155):

- **Development forks** are "the normal way development is done in most projects today": a
  developer makes a public copy, changes it, and submits the changes back. They are "really
  just an extension of the concept of development branches" and "have no negative effect on the
  social cohesiveness of the project." (This benign sense comes from GitHub's choice to label
  personal copies "forks" rather than "clones.")
- **Hard forks** (or "social forks") are "much less common, and… much more significant." A
  hard fork is "when a group of developers disagrees with the direction of the project and
  decides to create a divergent version more in line with their own vision" — "a potentially
  permanent divergence" that "is a completely different beast from a cooperative development
  fork."

A hard fork comes "with long discussions and rationales." Knowing how to initiate or react to
one constructively is "useful even if a fork never happens, since understanding what leads to
hard forks, and signaling clearly how you will behave in such an event, can sometimes prevent
the fork from happening in the first place"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=168), p. 155).
Below, "fork" means hard fork.

## Which side is "the fork"? Perception is the reality

When a fork happens, "there is no definitive answer to the question of which fork is the 'true'
or 'original' project." Because "'the project' is ultimately a social concept in the first
place," the perceptions aren't an imperfect read of some underlying truth — "the perceptions
*are* the objective truth, since ultimately a project — or a fork — is an entity that exists
only in people's minds anyway." If the initiators feel they're "sprouting a new branch," it
resolves itself: a new name, site, and philosophy. It gets messy "when both sides feel they are
the legitimate guardians of the original project" and both claim the name — a dispute that
trademark or domain control "usually resolves… by fiat… in a public relations showdown"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=168), p. 155).

In practice there's usually little doubt, "because a fork is, in essence, a vote of
confidence." If "more than half of the developers are in favor of whatever course the fork
proposes," there's usually no need to fork — "the project can simply go that way itself, unless
it is run as a dictatorship with a particularly stubborn dictator." If fewer than half favor
it, "the fork is a clearly minority rebellion," and it "should think of itself as the divergent
branch." Non-copyable assets (trademarks, money, hardware, a conference banner) follow their
formal owners; genuinely disputed ones could in principle reach a "court of law," though that
"is extremely rare" in free software — usually no one's best alternative is worse than just
conceding
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=169), p. 156).

## Handling a fork of your project: don't be vindictive

"If someone threatens a fork in your project, keep calm and remember your long-term goals. The
mere existence of a fork isn't what hurts a project; rather, it's the loss of developers and
users. Your real aim, therefore, is not to squelch the fork, but to minimize these harmful
effects." Venting that the fork is unjust "can only alienate undecided developers." The
counterintuitive playbook is generosity
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=169), p. 156):

- **Don't revoke commit access** just because someone works on the fork — "committers before
  should remain committers afterward" (an application of the [[committers|dormant-committer]]
  logic: working elsewhere doesn't void their judgement).
- **Offer to stay compatible**, encourage porting changes both ways, and "publicly offer the
  forkers infrastructure help at startup time" — e.g. "a complete export of the bug database."
- **"Bend over backward to show that you are not standing in the way."**

The reason "is not to actually help the fork, but to persuade developers that your side is a
safe bet, by appearing as non-vindictive as possible." Developers who work on both sides "keep
the lines of communication open," let you "benefit from interesting new features in the fork,"
and "increase the chances of a merger down the road"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=169), p. 156).

A fork can even win: the **GCC/EGCS** fork began as a non-adversarial Cygnus fork that "did
not, at any point, try to portray their version… as a new official version" but simply
incorporated patches faster, until distributors shipped EGCS by default and the GCC maintainers
"adopted the EGCS codebase" — "a single GCC, but greatly improved because of the fork." So
"you cannot always regard a fork as an unadulteratedly bad thing"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=169), p. 156).
Keep an eye on it, absorb features, and "in the most extreme case… even join the fork if it
gains the bulk of the project's mindshare." Read the fork's prospects by *who joins*: "the
project's biggest complainer" plus a few disgruntled developers has "essentially solved a
problem for you," but "influential and respected developers supporting the fork" is a signal to
ask why — perhaps to "avoid the fork by becoming it"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=170), p. 157).

## Initiating a fork: a last resort

"All the advice below assumes that you are forking as a last resort. Exhaust all other
possibilities before starting a fork." Forking "almost always means losing developers, with
only an uncertain promise of gaining new ones later," and it forces a question on every user:
"do I want that one or the other one?" The ecosystem-level "natural selection" defense of forks
("the fittest will survive") "may be true from the ecosystem's point of view, but it's not true
from the point of view of any individual project. Most forks do not succeed"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=170), p. 157).

Two cautions follow. First, "you should not use the threat of a fork as an extremist debating
technique" — everyone knows a fork that fails to attract developers "is unlikely to survive
long," so the bluff is weak; "appear extremely reluctant to fork, so that if you finally do it,
you can credibly claim it was the only route left." Second, "do not neglect to take all factors
into account" — notably employer alignment: developers paid by one entity "are unlikely to say
so out loud if they know that their employer is against it." The license guarantees freedom "in
an ultimate sense," but single-funder reality still matters
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=170), p. 157).

If you must proceed: "line up support privately first, then announce the fork in a non-hostile
tone." Don't air anger; "dispassionately state what led you to the decision." "Emphasize that
you're forking the code and not the name, and choose a name that does not conflict." And start
on the right foot by "automatically granting all committers of the original project commit
access to the fork, including even those who openly disagreed with the need for a fork" — the
message being "there are disagreements here, but no enemies"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=170), p. 157).

## Negative Space

- **GitHub's "fork"-vs-"clone" naming history** (`tool-specific/perishable`): the footnote on
  why GitHub repurposed "fork" for personal copies explains the term's drift but isn't a durable
  concept.
- **GCC/EGCS as a narrative** (`illustrative-scaffolding`): kept only as the carrier of the
  transferable claim — a non-adversarial fork can supplant the original and be re-absorbed — not
  as a paged case history.
- **BATNA / "court of law" asset disputes** (`too-granular`): the legal-last-resort and
  negotiation-theory aside is a gloss on why disputes rarely escalate, folded into the
  perception-and-assets section.

## See also

- [[forkability]] — the latent right-to-fork that this page's actual-fork mechanics are the
  realization of; the two are a pair (the ceiling on power vs. what happens when it's invoked).
- [[committers]] — why forkers keep their commit access, and the grant-everyone-access opening
  move of a well-run fork.
- [[open-source-governance]] — the "vote of confidence" framing: a fork is the escape valve when
  the decision machinery can't reconcile a direction.
- [[evaluating-open-source-projects]] — reading the two sides of a fork from the outside.
- [[open-source-culture]] — "the project is a social concept," the premise that makes perception
  the deciding reality in a fork.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 8 "Managing Participants" —
  §Forks (Development vs Hard Forks, Figuring Out Whether You're the Fork, Handling a Fork,
  Initiating a Fork) (printed pp. 155–157).
