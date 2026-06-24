---
title: Launching an Open Source Project
aliases: [project-presentation, hacktivation-energy, scaled-presentation, getting-started]
date: 2026-06-23
last_updated: 2026-06-24
type: topic
topics: [open-source-participation, project-infrastructure]
roles: [tech-lead]
source_tier: 1
project: null
source_count: 1
status: active
---

# Launching an Open Source Project

Starting a free software project is "a twofold task": the software must "acquire users,
and … acquire developers," and the interaction between those two audiences "adds some
complexity to a project's initial presentation"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=22), p. 9).
The hardest part is not technical: it is "transforming a private vision into a public
one." The founders may "know perfectly well what [they] want, but expressing that goal
comprehensibly to the world is a fair amount of work" — and most of that work is "pure
drudgery," the unglamorous job of "organizing and documenting things everyone already
knows" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=23), p. 10).

## Scaled presentation

The governing principle for all launch material is **scaled presentation**: "the degree
of detail presented at each stage should correspond to the amount of time and effort put
in by the reader at that stage. More effort should always result in more reward." The
failure mode is decoupling the two — "when effort and reward do not correlate reliably,
people lose faith and stop investing effort"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=22), p. 9).
The same principle reappears in the small: a video link that states its own duration
("Watch our 3 minute video") lets a visitor commit the right amount of attention before
clicking, "removing as much risk as possible"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=31), p. 18).

## Appearances matter — form is substance

Programmers' "love of substance over form is almost a point of professional pride," but
project presentation is precisely a case "where form is substance." A visitor forms an
immediate first impression of the home page "before any of the text has been read or
links clicked on," and "humans have extremely sensitive antennae for detecting the
investment of care"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=22), p. 9).
Running a project is therefore "partly about supplying information, but it's also about
supplying comfort": the mere presence of standard offerings "in expected places"
reassures newcomers that "your time will not be wasted if you get involved"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=22), p. 9).

## Hacktivation energy

The bootstrapping goal is to lower the project's **hacktivation energy** — "the amount of
energy a newcomer must put in before she starts getting something back." Investment in
presentation exists "to bring the project to a kind of minimum activation energy"; the
lower that threshold, "the better"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=23), p. 10).
This is why the boring finishing work pays off: "boring work with a high payoff should
always be done early," and the highest-leverage example is packaging that lets a newcomer
build and run the code at all
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=27), p. 14).

## But first, look around

Before founding anything, "always look around to see if there's an existing project that
does what you want." Reinventing a solved problem wastes effort; even an imperfect match
may make it "more sense to join that project and add functionality to it than to start
from scratch." The exceptions are narrow — an educational exercise, or a problem so
specialized no one could have done it — so "there's no point not looking, and the payoff
can be huge"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=23), p. 10).

## The newcomer checklist — what a launch needs

The launch material is "presented roughly in the order that a new visitor would encounter
them" and can be treated "as a checklist." Each item is captured here by *what it signals*
and the principle behind it, not its mechanics (tooling specifics belong to
[[project-infrastructure]] and are developed in Ch.3):

- **A good name** — gives "some idea what the project does," is easy to remember without
  depending on English fluency or puns, does not collide with another project or
  trademark, and is ideally available as a domain and as a username in the namespaces
  that matter
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=24), p. 11).
  Owning "the project's name in as many of the relevant namespaces" keeps it "right where
  a potential contributor would expect it to be."
- **A clear mission statement** — "concrete, limiting, and above all, short," placed
  "right under the project's name" so a visitor can decide "within 30 seconds" whether to
  read on; it may freely "assume a minimally informed reader"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=25), p. 12).
- **An explicit statement that the project is free** — "the front page must make it
  unambiguously clear that the project is open source," with the exact license named near
  the mission statement; burying it "can lose many potential developers and users." See
  [[open-source-licensing]]
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=25), p. 12).
- **A features and requirements list** — "a logical expansion of the mission statement"
  that lets readers gauge fit; unfinished features are listed but marked "planned" or "in
  progress"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=26), p. 13).
- **Development status** — answers two questions at once: the formal "where does the
  project stand in relation to its stated goals," and the informal but often more
  important "how active is this project?" Both are best shown, via a status page and/or
  automatically-updated activity indicators
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=26), p. 13).
- **Downloadable source in standard formats** — "as convenient, standard, and
  low-overhead as possible," with a unique version number per release so people can tell
  which supersedes which. Deviating from standard build/install methods silently sheds
  contributors who "give up and go away confused"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=27), p. 14).
- **Version control and bug tracker access** — a public, real-time repository and an
  accessible bug database are signals "to both users and developers — that this project is
  making an effort to give people what they need to participate." A well-maintained bug
  database "makes a much better impression than … no bug database," and a high bug count
  reflects engagement, not poor quality. See [[version-control]] and [[bug-tracking]]
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=27), p. 14); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=28), p. 15).
- **Communications channels** — visibly listed forums (mailing lists, chat) that the
  maintainers are seen to be subscribed to. Early on, "there's usually no need to have
  separate user and developer forums"; one shared room is better while the developer-user
  distinction is fuzzy
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=28), p. 15).
- **Developer guidelines** — "not so much technical as social": how developers interact,
  how to report bugs and submit patches, and "how decisions are made." Crucially the
  project should "come right out and say so" — a stated [[open-source-governance|benevolent
  dictatorship]] does fine, but "a tyranny pretending to be a democracy will turn people
  off"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=28), p. 15); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=29), p. 16).
- **Documentation, written for users first** — "essential," never finished, and "the
  first area where a new open source project falls down" because its utility "to those
  writing it is the inverse of its utility to those reading it." Bound the scope to make
  it finishable: state assumed expertise, cover setup with a confirming diagnostic, give
  one walked-through tutorial task, and "label the areas where the documentation is known
  to be incomplete." If time allows only one audience, "write it for users"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=29), p. 16); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=30), p. 17); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=31), p. 18).
- **Demos, screenshots, videos** — for graphical or distinctive output, "a single
  screenshot or video can be more convincing than paragraphs of descriptive text," because
  it is "proof that the software works"
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=31), p. 18).
- **Hosting** — early on the user-facing and developer-facing sites need not be separate;
  most new projects "just use one of the 'canned hosting' sites." See [[project-hosting]]
  ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=32), p. 19).

## Honest status beats hype

A recurring discipline cuts across the whole checklist: **development status should always
reflect reality.** "Never give in to the temptation to inflate or hype" — "there's no
shame" in labelling software alpha, and "one of the worst things a project can do is
attract users before the software is ready for them," because "a reputation for
instability … is very hard to shake." Conservatism pays: better that software "be more
stable than the user expected rather than less"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=27), p. 14).
The same scrupulous honesty about "known deficiencies … is the norm in the open source
world" and applies to documentation, the bug tracker, and mailing lists alike
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=30), p. 17).

## Announcing — the capstone of the launch

The launch is finished by announcing the project, and the bar is lower than founders
expect: "Once the project is presentable — not perfect, just presentable — you're ready to
announce it to the world." Announcements go in "two kinds of forums": **generic** forums
that carry many project announcements, and **topic-specific** forums where the project is
on-topic news. Topic-specific forums are "probably where you'll get the most interest"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=40), p. 27); ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=41), p. 28).

The discipline of the announcement itself
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=41), p. 28):

- **Be findable.** Include "key words and phrases that will help people find your project in
  search engines"; the test is that a search for your project's actual domain ("open source
  foo bar baz") should put a credible offering "on the first page of results."
- **Post once per forum, and redirect follow-up.** "Be careful to make exactly one post per
  forum," directing replies to the project's own discussion areas (by setting the `Reply-to`
  header when posting by email). The announcement "should be short and get right to the
  point," with a Subject line that flags it plainly as a new-project announcement
  (`[ANNOUNCE]`).
- **Don't join the marketing arms race.** General venues like Hacker News or the relevant
  subreddits work by upvote/word-of-mouth; getting featured is good, but Fogel pointedly
  declines to suggest tactics for engineering it — "use your judgement and try not to spam."

### Running code is no longer a precondition

Fogel revises his own earlier view that "running code" was "what separated successful
projects from toys." Subversion launched "with a design document, a core of interested and
well-connected developers, a lot of fanfare, and no running code at all" and acquired active
participants immediately; Mozilla was likewise "launched without running code." So he backs
away from the absolute claim — running code "is still the best foundation for success," and
the rule of thumb is to "wait until you have it before announcing," but "there may be
circumstances where announcing earlier makes sense." What *is* required is "at least a
well-developed design document, or else some sort of code framework" — "something concrete …
for people to sink their teeth into." (Announcement timing is independent of open-sourcing:
the code should be public from day one regardless of when you announce — see
[[developing-in-the-open]])
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=42), p. 29).

### Announcement is planting a seed

Calibrate expectations: "don't expect a horde of participants to join the project
immediately afterward." The usual result is "a few casual inquiries, a few more people join
your mailing lists," and otherwise business as usual — "but over time, you will notice a
gradual increase in participation." Announcement "is merely the planting of a seed"; if the
project "consistently rewards those who get involved, the news will spread, … because people
want to share when they've found something good"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=42), p. 29).

## Negative Space

- **Per-item tooling mechanics** (`tool-specific/perishable`): screen-recording key
  combos, specific TLD/Twitter/GitHub registration steps, ReadTheDocs/Pandoc/OpenShot
  recommendations — captured as "use standard, low-overhead tooling," not paged.
- **Alpha vs. beta definitions** (`too-granular`): the exact API-freeze semantics of each
  release stage are a sidebar; the durable point is "label status honestly." Release
  staging proper belongs to [[release-numbering]] (the Alpha/Beta/RC qualifiers) and
  [[stabilizing-a-release]] (Ch.7).
- **FAQ maintenance** (`too-granular`): "good FAQs are not written, they are grown" — a
  practice bullet under documentation, not a standalone concept.
- **Developer documentation vs. developer guidelines distinction** (`subsumed-by`):
  captured inline (guidelines = social, documentation = code-level); not worth its own
  page.
- **Scanley / Hadoop / Gnome examples** (`illustrative-scaffolding`): named only to
  illustrate mission statements and namespace ownership.
- **Bug-count-as-good-news essay** (`supporting-argument`): the linked rants.org argument
  that bug reports signal engagement rather than technical debt supports the "high bug
  count looks good" claim; not paged.
- **Verbatim Scanley `[ANNOUNCE]` email** (`illustrative-scaffolding`): the sample
  announcement (features list, requirements, the "long-distance mind-reading" joke) models
  format; the durable rules (short, one-post-per-forum, set `Reply-to`) are captured instead.
- **Specific announcement venues** (`tool-specific/perishable`): Hacker News, the named
  subreddits, and the FSF Free Software Directory are named as of early 2022; captured as the
  generic-vs-topic-specific distinction, not the venue list.

## See also

- [[open-source-licensing]] — the "state that the project is free" item, developed: which
  license to pick and how to apply it.
- [[free-software-vs-open-source]] — why "free" and "open source" name the same thing the
  launch page must declare.
- [[version-control]] — the public repository that the checklist treats as a seriousness
  signal as well as a collaboration tool.
- [[open-source-governance]] — the decision-making model developer guidelines must state
  plainly.
- [[forkability]] — why a stated "dictatorship" is benign in open source.
- [[setting-the-tone]] — the dynamic, behavioral culture-setting that complements this
  static presentation checklist.
- [[developing-in-the-open]] — why the launch artifacts must be public from Day One, and why
  announcement timing is independent of open-sourcing.
- [[installation-surface]] — the modern, practitioner extension of "appearances matter":
  low-friction multi-path install as the top readiness signal, and leading the README with
  the use case ("nobody cares about your stack") rather than the dependency list.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 2 "Getting Started" —
  chapter intro (scaled presentation, appearances matter), "But First, Look Around,"
  "Starting From What You Have," and the launch checklist subsections through "Hosting"
  (printed pp. 9–18); "Announcing" (printed pp. 28–29, added batch 4).
