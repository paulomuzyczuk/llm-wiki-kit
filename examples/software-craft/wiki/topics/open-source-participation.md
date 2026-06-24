---
title: Open-Source Participation
aliases: [contributor-base, who-contributes]
date: 2026-06-23
last_updated: 2026-06-24
type: topic
topics: [open-source-participation, open-source-governance]
roles: [tech-lead, product-engineer]
source_tier: 1
project: null
source_count: 2
status: active
---

# Open-Source Participation

Who actually *makes* open-source code is far less evenly distributed than the
"anyone-can-contribute" framing suggests. Modelling the GitHub dependency graph, Mehler,
Otto & Sapienza find that "a small core of repositories… delivers the majority of
dependencies," so "the majority of GitHub projects… rely on a small subset of the overall
ecosystem" — in short, "not all F/OSS repositories on GitHub are equal in terms of
influence" ([Mehler et al. 2024](../../raw-input/papers/who-makes-open-source-code.pdf#page=15), p. 15).

## A "GitHub-elite," weighted toward organizations

This influential core is best read as a "GitHub-elite": more **specialized** (by
programming language) and more **organizationally owned** than the ecosystem at large
([Mehler et al. 2024](../../raw-input/papers/who-makes-open-source-code.pdf#page=15), p. 15).
The finding nuances the folk image of the lone critical maintainer — the "Nebraska
developer" — as "probably more than just a 'random guy'": critical dependencies sit with
identifiable, structurally central actors ([Mehler et al. 2024](../../raw-input/papers/who-makes-open-source-code.pdf#page=16), p. 16).

## Hybridisation: commercial actors in the open-source core

Open-source organizations and individuals supply the most *direct* dependencies, but large
private companies (e.g. Microsoft, Google) are "generally better connected to other
influential nodes" and "seemingly successfully insert themselves as large owners within
the communities comprising the core" — the **hybridisation** of commodified and
open-source code ([Mehler et al. 2024](../../raw-input/papers/who-makes-open-source-code.pdf#page=14), p. 14).
One visible mechanism is sponsorship: the most influential developers and organizations
tend to offer direct funding channels (GitHub Sponsors, Tidelift, Open Collective),
signalling "a level for more professional organization surrounding their coding practices"
([Mehler et al. 2024](../../raw-input/papers/who-makes-open-source-code.pdf#page=14), p. 14).

## The formal counterpart: the committer class

The paper's structural elite has an *institutional* counterpart inside each project. Fogel
identifies **committers** — those with the right to put changes into the authoritative release
copy — as "the only formally distinct class of people found in all open source projects," an
"unavoidable concession to discrimination in a system which is otherwise as non-discriminatory
as possible," justified because "quality control requires, well, control"
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=164), p. 151).
The two views are complementary: Mehler et al. measure stratification *across* the ecosystem
(which repositories carry the dependency weight), while Fogel describes stratification *within*
a project (who is trusted to commit). Both cut against the flat "anyone-can-contribute" image —
participation is real and open at the edges, but influence concentrates, by structure in the
one case and by formal grant in the other. The craft of administering that inner gate — choosing,
revoking, and publishing commit access without letting it become an exclusive club — is the
subject of [[committers]].

## Negative Space

- **Network-centrality methodology** (`supporting-argument`): the out-degree, eigenvector,
  betweenness, and PageRank measures are how the core is identified, not concepts in their
  own right.
- **Specific company rankings** (`case-study-specifics`): the exact placements (Microsoft
  2nd, Google 8th by eigenvector centrality) are illustrative of the pattern, not durable
  facts to page.

## See also

- [[code-review]] — the day-to-day peer-review practice this contributor base performs.
- [[continuous-integration]] — the automated pipeline the ecosystem's core projects run on.
- [[contributor-motivation]] — why individuals join and stay in that contributor base
  (Fogel's complement to this paper's structural view of *who* contributes).
- [[delegation-in-open-source]] — how maintainers draw new contributors deeper into a project.
- [[treating-users-as-participants]] — the recruitment funnel that converts users into the
  contributors counted here.
- [[committers]] — the formal trusted class within a project; the institutional complement to
  this page's empirical view of who contributes.

## Sources

**Source entities:** [[who-makes-open-source-code-paper]], [[producing-open-source-software-book]]

- Peter Mehler, Eva Iris Otto & Anna Sapienza, "Who Makes Open Source Code? The
  Hybridisation of Commercial and Open Source Practices," *EPJ Data Science* (2024) 13:35,
  CC BY 4.0.
- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 8 "Managing Participants" —
  §Committers (the committer as the only formally distinct class) (printed p. 151).
