---
title: Source Packaging
aliases: [packaging, source-distribution, release-packaging, source-package]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [release-engineering]
roles: [tech-lead, code-craftsperson]
source_tier: 1
project: null
source_count: 1
status: active
---

# Source Packaging

## Source code is the canonical form

The canonical form for distributing free software is **source code** — and this holds
regardless of whether the software normally runs in source form (interpreted, like
Perl, Python, PHP) or is compiled first (C, C++, Java, Rust). Even when most users
install from pre-built binary packages, those binaries are still *derived from a
particular source distribution* ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=140), p. 127).

The reason this matters is definitional: **the point of the source package is to
unambiguously define the release.** When a project distributes "Scanley 2.5.0," what
that *means*, specifically, is "the tree of source-code files that, when compiled (if
necessary) and installed, produces Scanley 2.5.0" ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=140), p. 127).
A release name is therefore a pointer to an exact source tree (compare the tag cut
from a [[release-branches|release branch]], which records that same exact state).

## Follow the conventional standard

There is a fairly strict, widely-followed standard for how a source release should
look. Deviations exist but are the exception, not the rule — **unless there's a
compelling reason to do otherwise, follow the standard**, because conforming to shared
expectations is itself what makes a package legible to users and downstream packagers
([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=140), p. 127).

The two governing conventions a project must settle:

- **Format** — ship the source in the standard archive format for transporting
  directory trees on the target platform: compressed TAR for Unix-like systems, ZIP
  for Windows (and, for JavaScript projects, the minified files alongside the
  human-readable source) ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=140), p. 127).
- **Name** — the package name is the software's name plus the release number plus the
  archive suffix, so the artifact itself carries which release it is ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=140), p. 127).

## Conform to the standard build and install procedure

> **Added in batch 13** (Ch.7 §Compilation and Installation), capturing the governing
> principle the batch-12 negative space deferred.

For software that must be compiled or installed from source, **experienced users expect
a standard procedure** (historically `./configure && make && sudo make install` on
Unix-like systems, increasingly also a container recipe; other languages carry their own
conventions). You can safely assume *some* standard applies even if you don't yet know
it — ask an experienced developer rather than inventing one ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=142), p. 129).

**Don't deviate from the applicable standard unless you absolutely must.** Standard
invocations are "practically spinal reflexes" for system administrators: seeing familiar
commands in your `INSTALL` file instantly raises their faith that the project is aware of
conventions and likely got other things right too, and a standard build also pleases
prospective developers. Building and installing is an **entry point** — it's acceptable
for things to get harder *after* that, but a user's first interaction shouldn't require
unexpected steps ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=143), p. 130).

## Binary packages must derive from an official source release

The formal release is a source package, but most users install from **binary packages**
(OS distribution packages, or pre-built downloads) — where "binary" means "pre-configured
to install without the source build," not necessarily "compiled." Whoever assembles them,
**users treat binary packages as equivalent to the project's official releases** and file
bug reports based on their behavior ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=143), p. 130).

The load-bearing rule: **packagers should always base their binary packages on an
official source release** — never an unstable repository snapshot or a release plus
hand-picked post-release commits. The intent is kind (give users newer fixes) but the
effect is corrosive: the project is prepared to receive bug reports against *known*
releases and against deliberately-bleeding-edge mainline, but **not against unspecified
intermediate or hybrid versions**, whose bugs are hard to reproduce and may stem from
unexpected interactions between changes pulled from different stages ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=143), p. 130).

When a packager insists a modification is necessary, the remedy is **disclosure, not
prohibition**: encourage them to raise it with the developers, who may approve it or at
least be warned to watch for unusual reports, and who may ask that both sides post a
disclaimer so users know the package differs from the official release ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=144), p. 131).
The framing to keep: **the bonds of obligation run both ways.** The project does packagers
a favor by producing the software, but packagers do the project a favor by taking on an
unglamorous job that makes the software far more widely available. Disagree with packagers
when needed, but don't flame them — their goals (best out-of-the-box experience) and the
project's (knowing exactly which versions are deployed, for coherent bug reports and
compatibility guarantees) simply differ ([Fogel 2023](../../raw-input/books/producing-open-source-software/producing-open-source-software.pdf#page=144), p. 131).

## Negative Space

- **Per-file layout mechanics** (`too-granular`): the conventional `README` /
  `INSTALL` / `LICENSE` / `CHANGES` files, the unpacked directory-tree layout, and the
  "release must not be a working copy" rule are reference mechanics; captured only as
  the governing principle here.
- **Build-tool and platform specifics** (`tool-specific/perishable`): the exact
  `./configure`/`make` invocation, Docker/MinGW/Cygwin/Visual Studio specifics, and the
  RPM/APT package formats are perishable mechanics under the durable "conform to the
  relevant standard" principle now captured above.
- **Specific archive tools and suffixes** (`tool-specific/perishable`): `gzip` /
  `bzip2` / minification utilities are perishable specifics; the durable point is
  "use the platform's standard archive format."
- **Iceweasel/Debian rebranding footnote** (`illustrative-scaffolding`): a named example
  of a packager modification, not a concept.

## See also

- [[release-numbering]] — the release number a package name must carry.
- [[release-branches]] — the branch/tag a source package is cut from.
- [[releasing-and-signing]] — what happens to the package next: testing, signing, and
  shipping it.
- [[open-source-licensing]] — the license a distribution must declare.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 7 "Packaging,
  Releasing, and Daily Development", §Packaging (Format, Name) — governing principle,
  printed p. 127; §Compilation and Installation, §Binary Packages — governing
  principles (batch 13), printed pp. 129–131.
