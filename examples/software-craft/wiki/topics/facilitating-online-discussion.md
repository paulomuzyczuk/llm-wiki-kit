---
title: Facilitating Online Discussion
aliases: [avoiding-common-pitfalls, productive-threads, bikeshed-effect, bikeshedding, holy-wars, noisy-minority]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-communication, software-collaboration]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Facilitating Online Discussion

Where [[written-communication]] covers how an individual writes, this page covers the
group-level skill: keeping threaded discussion productive when many people, of varying
investment and expertise, are talking at once. Certain anti-patterns *appear again and
again* in project forums, and a facilitator's job is to recognize them and steer around
them without seeming to dictate conduct ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=113), p. 100). The recurring
theme: you cannot command a volunteer forum, so influence is exercised by *offering a
better path*, framed so people feel invited rather than restricted.

## Don't Post Without a Purpose

A common newcomer error is feeling obligated to respond to everything. You aren't: an
active project has more threads than anyone can track, and within a thread, most messages
need no reply ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=113), p. 100). Development forums are dominated
by four message types — questions, non-trivial proposals, expressions of support or
opposition, and summing-up messages — none of which *inherently* demands your voice,
especially when someone else is likely to say what you would have ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=113), p. 100).

A post should serve a **definite purpose**. Two reliable reasons to speak: you see a flaw
in a proposal and suspect you're the only one who does, or you can fix an emerging
miscommunication with a clarifying post. Short "thank you" or "Me too!" posts are fine —
a reader can tell instantly they need no further action, so the mental effort ends at the
last line — but even then, think twice: *it's always better to leave people wishing you'd
post more than wishing you'd post less* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=113), p. 100).

## Productive vs. Unproductive Threads

On a busy list you have two imperatives: figure out what to attend to vs. ignore, and
behave so as to *avoid causing noise* — making your own posts high signal-to-noise and
the kind that prompt others to do likewise or stay quiet ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=113), p. 100). The
hallmarks of an **unproductive thread** ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=113), pp. 100–101):

- Already-made arguments being repeated, as though no one heard them the first time.
- Rising hyperbole and intensity *as the stakes get smaller*.
- A majority of comments from people who do little in the project, while the doers stay
  silent.
- Many ideas discussed without any clear proposal ever crystallizing.

The art is to guide a thread toward usefulness **without being pushy**. Admonishing people
to stop wasting time is offensive and ineffective; instead, *suggest conditions for
further progress* — a concrete path to the result you want. The distinction is one of
tone. Fogel contrasts a bad intervention ("This discussion is going nowhere... Code speaks
louder than words, folks") with a good one that (a) speaks in terms of *"we"*, reminding
even silent readers they have a stake, (b) dispassionately states *why* the thread is
stuck, without pejoratives, and (c) offers a positive next action — e.g. "further posts
should contain either a complete specification or a patch." People feel offered a way up
rather than shut down, and most productive people will want to meet that standard
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=114), p. 101).

Two cautions temper this. First, an unproductive thread is not automatically a waste of
time — it may be about an important topic, in which case its *failure* to make headway is
all the more troublesome, not less ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=113), p. 100). Second, be wary of
quashing threads prematurely: some speculative chatter is productive depending on the
topic, and pushing for resolution too fast stifles the creative process and makes you look
impatient ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=114), p. 101).

Often you'll be equally happy if the thread either levels up or dies; your post is
designed to force one or the other. Don't expect a thread to *stop on a dime* — a few
trailing posts are normal (crossed mails, last-word impulses) and need no further reply.
You can't have complete control, but you can expect a statistically significant effect
*across many threads* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=114), p. 101).

## The Bikeshed Effect: The Smaller the Topic, the Longer the Debate

The probability that discussion meanders goes *up* as the technical difficulty of the
topic goes *down*. The harder the problem, the fewer people can follow it — and those who
can are usually experienced developers who already know what leads to a workable
consensus. So consensus is *hardest* on questions that are simple to understand and easy
to have an opinion about, and on "soft" topics (organization, publicity, funding) where no
qualification is needed to participate, no clear way exists to decide who was right, and
*outwaiting or outposting others is sometimes a winning tactic* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=114), p. 101).

This inverse relationship between discussion volume and topic complexity is known as the
**Bikeshed Effect**, from Poul-Henning Kamp's famous post to BSD developers, itself drawn
from C. Northcote Parkinson's *Parkinson's Law* (early 1960s). Parkinson's parable: a board
will approve a multi-million-dollar atomic power plant almost without debate — it's too
vast and complex to grasp, so everyone assumes someone else checked the details — but a
proposal to build a bike shed gets tangled in endless argument, because *anyone* can
picture a bike shed and so everyone weighs in to "set their fingerprint," to point and say
"There! I did that" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=115), p. 102). You usually can't stop people
from painting bikesheds, but you can name the phenomenon when it happens and persuade the
*senior* developers — whose posts carry the most weight — to drop their paintbrushes
early, and you can shrink these episodes by spreading awareness of the effect through the
project's culture ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=115), p. 102). The effect is a recurring stress
on [[open-source-governance]]'s consensus-by-default model: trivial questions, not hard
ones, are where consensus breaks down.

## Avoid Holy Wars

A **holy war** is a dispute — often over a minor issue — that *cannot be resolved on the
merits* but about which people feel passionate enough to keep arguing in hope their side
prevails. It differs from bikeshedding: bikeshed-painters jump in with opinions but don't
necessarily feel strongly and may even argue multiple sides; in a holy war, understanding
the other side is treated as weakness, and everyone *knows* there is One Right Answer —
they just disagree on what it is ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=115), p. 102).

Two reasons the usual exit ("we've spent more time on this than it's worth, can we drop
it?") fails: the spent time is a sunk cost and irrelevant to whether a little *more* effort
would resolve it; and dropping the matter often lets the **status quo win by inaction** —
unacceptable when everyone agrees *some* decision must be made ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=116), p. 103).

Handling, in order ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=116), p. 103):

- **Prevent.** Anticipate the standard holy wars — programming languages, licenses (see
  [[open-source-licensing]]), reply-to munging — and head them off. Even when sure you're
  right, express genuine sympathy for the other side's points: a holy war hardens because
  surrender means admitting you were *certain and still wrong*, so showing some uncertainty
  yourself makes the other side's retreat psychologically bearable. *Make a gesture that
  provides space for a reciprocal gesture.*
- **Exit gracefully.** When a holy war can't be avoided, decide early how much you care,
  then be willing to *publicly give up* — without bitterness and without a parting shot.
  Giving up is effective only when done gracefully.
- **Special case — language wars.** Highly technical yet everyone feels qualified, and the
  stakes are high (which language the codebase uses). Choose the language early with buy-in
  from influential initial developers, and defend it on the grounds that it's what the team
  is comfortable writing — never as objectively "better." An academic comparison of
  languages is a *death topic* to refuse outright.

## The "Noisy Minority" Effect

A small minority can manufacture the impression of widespread dissent by flooding a list
with numerous lengthy emails — like a filibuster, but more potent, because the volume is
split across many discrete posts and most readers won't track who said what. They come away
with a vague sense that the topic is "very controversial" and wait for the fuss to subside
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=116), p. 103). The counter is **quantitative**: point out plainly how
small the actual number of dissenters is versus those in agreement, optionally privately
polling mostly-silent people you expect agree, then show the numbers side by side. Don't
allege the minority *meant* to inflate their presence — there's no strategic gain in it;
just let the real count correct people's impression. This generalizes beyond for/against
issues: when a fuss has failed to gain traction despite many mails, simply observing
publicly that it isn't gaining traction *reshapes* how everyone understands what happened
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=116), p. 103).

## Don't Bash Competing Open Source Products

Refrain from *negative opinions* about competing open-source software, while **negative
facts** — easily confirmable assertions of the kind found in honest comparison charts —
remain fair game. Two reasons ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=116), pp. 103–104): unrigorous
characterizations start flame wars that derail real work; and, more importantly,
**developer crossover** is more common than it looks — competing projects share a domain,
expertise travels to wherever it applies, and even without direct overlap your developers
likely know developers on the rival project. Overly negative marketing can poison those
constructive personal ties. Bashing *closed-source* competitors is more widely tolerated,
but Fogel deplores it too — partly as rude, but mainly because a project that believes its
own hype stops seeing where proprietary competition may be *technically superior*
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=117), p. 104). This is the community-discussion sibling of the
marketing-side rule in [[open-source-marketing]] ("Don't Bash Competing Vendors' Efforts"):
watch the effect your own marketing has on your developers' objectivity, who may even *poke
fun* at the marketing message to keep the community grounded.

## Negative Space

- **The bad/good intervention email pair** (`illustrative-scaffolding`) — verbatim
  specimens of pushy vs. constructive thread-steering; the tone principle is kept, the
  quotes are not.
- **Kamp's full bikeshed post and the bikeshed.com link** (`illustrative-scaffolding`) —
  the parable's substance (Parkinson, atomic plant vs. bike shed, "setting fingerprints")
  is captured; the quoted block and external link are not reproduced.
- **Jargon-file and Danny Cohen IEN-137 holy-war references** (`source-underdeveloped`) —
  pointers offered for historical background, not developed.
- **Sealioning / Help-Vampire detail** (`subsumed-by` [[difficult-people]]) — named in a
  Ch.6 footnote; the obstructionist subspecies is treated on the difficult-people page.
- **The Subversion "Energy Sink" case study** (`case-study-specifics`) — the J. Random
  mailing-list-volume case; its *method* (build a case on neutral quantitative data) is
  captured in [[difficult-people]], the specific archive figures are not.

## See also

- [[written-communication]] — the individual-level companion: how one person writes well,
  prerequisite to facilitating a forum of them.
- [[difficult-people]] — when unproductive discussion is *deliberate* process manipulation
  rather than ordinary thread drift.
- [[open-source-governance]] — the consensus-and-voting machinery that bikeshedding and holy
  wars stress, and that thread-steering protects.
- [[open-source-marketing]] — "Don't Bash Competing Vendors' Efforts" is the marketing-side
  sibling of not bashing competing open-source products.

## Sources

- Karl Fogel, *Producing Open Source Software* (2nd ed., v2.3300), Chapter 6
  "Communications" — §Avoiding Common Pitfalls (Don't Post Without a Purpose, Productive
  vs Unproductive Threads, The Smaller the Topic the Longer the Debate, Avoid Holy Wars,
  The "Noisy Minority" Effect, Don't Bash Competing Open Source Products), PDF pp. 113–117
  (printed pp. 100–104).
- **Source entities:** [[producing-open-source-software-book]]
