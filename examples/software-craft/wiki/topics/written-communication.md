---
title: Written Communication in Open Source
aliases: [written-culture, you-are-what-you-write, recognizing-rudeness, online-face, screen-name]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [open-source-communication, open-source-culture]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Written Communication in Open Source

Because open-source collaboration is conducted almost entirely in text, the ability
to write clearly is one of the most important skills a participant can have — *in the
long run it may matter more than programming talent*. A great programmer with poor
communication skills can get only one thing done at a time and may struggle to get
attention; a mediocre programmer with good communication skills can coordinate and
persuade many people, and so have an outsized effect on a project's direction and
momentum ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=107), p. 94). There is little correlation
between writing good code and communicating well with humans, so communication is a
distinct competence to be cultivated, not a by-product of technical skill ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=107), p. 94).

The core sensibility is **empathy with the audience**: seeing your own posts as others
will see them, and — equally important — *noticing when a communications medium has
stopped working* because it no longer scales to the number or diversity of participants,
then taking the time to fix it ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=107), p. 94). Maintaining the
communications machinery is therefore everyone's job, not just the project lead's — a
theme that runs into [[facilitating-online-discussion]] and the tooling pages
[[message-forums]] and [[real-time-chat]].

## You Are What You Write

On the Internet, most of what others know about you comes from what you write. You may
be brilliant in person, but if your emails are rambling and unstructured, people assume
that is the real you; conversely, lucid posts let a disorganized person pass for a clear
thinker ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=107), p. 94). The canonical illustration is
Jim Blandy's story of a 1993 GNU Emacs beta-tester whose bug reports were always clear
and whose fixes were almost always right — and who turned out, when copyright-assignment
paperwork forced the question, to be thirteen years old. *Because the kid didn't write
like a thirteen-year-old, no one knew that's what he was* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=108), p. 95).
The lesson is operational, not vain: writing well is how you earn standing in a project
where no one can see your face or credentials.

## Structure and Formatting

Persistent writing — emails, documentation, bug reports — should use complete sentences,
capitalization, paragraph breaks, and standard grammar and spelling. The rules are not
arbitrary; they evolved because they make text readable, and readability signals *someone
worth paying attention to* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=108), p. 95). Ephemeral media
(chat rooms) tolerate compressed, uncapitalized forms, but those habits must not bleed
into permanent forums — a register distinction that maps onto the chat-vs-mail divide in
[[real-time-chat]] and [[message-forums]]. Good grammar also *minimizes ambiguity*, which
matters most in technical writing where cause and effect must stay distinct ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=108), p. 95).

For email specifically, experienced developers converge on a few conventions, captured
here as principles rather than mechanics ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=108), pp. 95–96):

- **Plain text, not HTML** — so archives and text-based readers don't mangle it; offset
  quoted code or screen output clearly enough that the structure is visible "from five
  meters away."
- **Stay under 80 columns** in preformatted blocks, leaving room for quoting characters
  in replies without forcing a rewrap.
- **Quote and trim** — interleave responses where they belong and cut the parts you
  didn't use; top-post only for a short response sensible on its own.
- **Construct Subject lines carefully** — the Subject is the most important line because
  it lets each reader decide whether to read on; adjust it when a thread drifts, and start
  a genuinely new topic with a fresh mail rather than a reply, so threading headers don't
  misfile it.

## Content

Well-formatted mail attracts readers; content keeps them ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=109), p. 96).
Three principles raise the odds of good content:

- **Make things easy for your readers.** Spend the extra two minutes to dig up the
  archive URL, or the extra ten to summarize a complex thread, so your readers don't have
  to. The economic logic is the **reader-to-writer ratio**: the more successful the
  project, the higher that ratio, so effort spent once by the writer to save N readers
  time scales in value with N — *the project prefers one person making the effort to N
  people making it* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=109), p. 96). Holding yourself to this
  standard visibly pulls others toward it.
- **Don't engage in hyperbole.** Exaggeration is a classic arms race — a reporter inflates
  a mild annoyance into a "showstopper"; a programmer calls a tasteful disagreement a
  "maintenance nightmare." A point phrased more moderately is usually *stronger*. Hyperbole
  is not globally damaging — it mostly costs the sender credibility — so err toward
  moderation, and your rare strong statements will be taken seriously ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=109), p. 96).
- **Edit twice.** Reread anything longer than a medium paragraph before sending. Online
  composition is highly discontinuous (you break off to check mail, run a command, open a
  page), so it is easy to lose the narrative thread; a final pass keeps posts coherent and
  therefore read ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=109), p. 96).

## Tone, and the Role of Feelings

Long-time hackers drift toward terseness, which is the norm in technical forums and
"nothing wrong with it per se" — a degree of terseness unacceptable in normal social
interaction is simply the default among free-software developers ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=109), p. 96).
But terseness must sometimes be *leavened*: when a person is likely feeling insecure (say,
they just admitted to a mistake), a compact, engineer's-eye analysis can still close with
a "Good luck" or an emoticlue so the brevity reads as efficiency, not coldness ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=110), p. 97).

The governing claim is utilitarian: **feelings affect productivity** — *unhappy people
write worse software and tackle fewer bugs* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=110), p. 97). Because most
media give no overt cue to a person's state, you guess from (a) how most people would feel
in that situation and (b) what you know of this person from past interactions. Fogel
rejects the "deal with everyone at face value" stance: public forums make people *more*
restrained about inwardly-directed emotions (insecurity, pride) than they would be in
private, yet most humans work better knowing others are aware of their state of mind. The
goal is not group therapy but a long-run sensitivity that lets you read individuals you
have never met and quietly influence how they feel — to the project's benefit ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=110), p. 97).

## Recognizing Rudeness

Open-source culture has *distinctive notions of what does and does not constitute
rudeness* — conventions shared with mathematics, the hard sciences, and engineering, but
especially likely to trip up newcomers given free software's porous boundaries and
constant influx ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=110), p. 97). The surprising half is what is
**not** rude:

- **Direct technical criticism is not rude** — it can be a form of flattery, since taking
  the time to critique a post (rather than ignore it) implies the recipient is worth
  taking seriously ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=110), p. 97).
- **Blunt, unadorned questions are not rude** — the "Is your computer plugged in?" support
  question is the archetype: stripped of polite padding, it just rules out the most common
  explanation as fast as possible. Recipients who take this broad-minded view win points;
  those who react badly *must not be reprimanded* either — it is a collision of cultures,
  not anyone's fault, and the fix is to explain amiably that no hidden meaning was intended
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=111), p. 98).

The mirror-image claim defines what *is* rude: by the same principle that makes criticism
flattery, **failure to provide quality criticism can be an insult**. Simply not reacting
is usually fine (people assume you were busy). But reacting half-heartedly — a dismissive
response that skips the real analysis without acknowledging the shortfall — signals that
the topic, and its participants, weren't worth your time. The norm is honored either by
meeting it or by openly admitting you fell short this once ("I think there's a ticket for
this but didn't have time to search, sorry"); either way the norm is strengthened. *Better
to show your time is valuable by being terse than by being lazy* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=111), p. 98).
Naming rudeness the first time and then moving on is the [[setting-the-tone]] discipline
("nip rudeness in the bud"); people whose problematic behavior goes *beyond* rudeness are
[[difficult-people]], handled differently.

## Face: Your Screen Name as an Online Identity

The human brain has dedicated hardware for recognizing faces (the "fusiform face area"),
which is why Internet collaboration is psychologically odd: tight cooperation between
people who never identify each other by face, voice, or posture ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=111), p. 98).
The compensating move is to use a **consistent screen name everywhere** — email local
part, chat handle, committer name, ticket-tracker username — as a short identifying string
that serves some of the purpose of a real face ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=111), p. 98).

Two further rules sharpen the identity:

- **Use your real name** (or a consistently-used pseudonym), as an intuitive permutation
  of it. Fantastical handles like "Wonder Hacker" never impress; they signal image over
  substance, or insecurity — *even if no one knows you're a dog, you're still a dog*
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=112), p. 99).
- **Don't flaunt titles.** Hacker culture reads title displays ("doctor", "director") as
  exclusionary and insecure; a title in a standard signature block is fine, but never as a
  lever in a discussion — the attempt backfires. You want respect for the person, not the
  title ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=112), p. 99).

Keep signature blocks small or nonexistent, and avoid large corporate legal disclaimers:
an auto-appended confidentiality boilerplate sends two destructive signals — that the
poster lacks control over their own tools, and that they have little organizational support
for their free-software work. If you can't get the policy changed, post from a personal
account instead ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=112), p. 99).

## Negative Space

- **Jim Blandy's full thirteen-year-old anecdote** (`illustrative-scaffolding`) — captured
  only as the "you are what you write" principle, not the verbatim dialogue.
- **Shane's terse mailing-list reply, quoted in full** (`illustrative-scaffolding`) — the
  example illustrating acceptable terseness; the principle is kept, the quote is not.
- **The Deloitte & Touche disclaimer, reproduced verbatim** (`illustrative-scaffolding`) —
  a long real-world signature block used as a specimen; the two-signals analysis is kept.
- **The Paul Steiner "nobody knows you're a dog" New Yorker cartoon** (`illustrative-scaffolding`)
  — a rhetorical hook for the real-name point.
- **Per-client mail-software mechanics** (`tool-specific/perishable`) — how to disable
  HTML mail, threading-header details, quoting key-bindings; out of scope as recipes.
- **Group Awareness in Distributed Software Development (Gutwin et al.) footnote**
  (`source-underdeveloped`) — cited as a pointer with an unstable URL, not developed.
- **Codes of Conduct mechanics** (`subsumed-by` [[setting-the-tone]]) — cross-referenced
  here but treated there.

## See also

- [[facilitating-online-discussion]] — the group-level companion: how the same written
  culture keeps multi-person threads productive.
- [[difficult-people]] — the pair to "Recognizing Rudeness": behavior that is *not* rude but
  manipulates process, handled differently.
- [[setting-the-tone]] — culture is transmitted by precedent; "nip rudeness in the bud" is
  the tone-setting side of recognizing rudeness here.
- [[message-forums]] — the persistent forum where these formatting conventions (plain text,
  80 columns, Subject discipline) apply.
- [[real-time-chat]] — the ephemeral register where compressed, uncapitalized writing is
  acceptable, contrasted with composed mail here.

## Sources

- Karl Fogel, *Producing Open Source Software* (2nd ed., v2.3300), Chapter 6
  "Communications" — §Written Culture (You Are What You Write, Structure and Formatting,
  Content, Tone, Recognizing Rudeness, Face), PDF pp. 107–112 (printed pp. 94–99).
- **Source entities:** [[producing-open-source-software-book]]
