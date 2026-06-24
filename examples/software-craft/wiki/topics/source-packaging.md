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

## Negative Space

- **Per-file layout mechanics** (`too-granular`): the conventional `README` /
  `INSTALL` / `LICENSE` / `CHANGES` files, the unpacked directory-tree layout, and the
  "release must not be a working copy" rule are reference mechanics that fall on
  printed p. 128+ (outside this batch's pp. 119–127 scope); captured only as the
  governing principle here, to be detailed if a later batch warrants it.
- **Compilation/installation and binary-package details** (`too-granular`): the book's
  later sub-sections (§Compilation and Installation, §Binary Packages) are
  build-tooling mechanics, not durable concepts.
- **Specific archive tools and suffixes** (`tool-specific/perishable`): `gzip` /
  `bzip2` / minification utilities are perishable specifics; the durable point is
  "use the platform's standard archive format."

## See also

- [[release-numbering]] — the release number a package name must carry.
- [[release-branches]] — the branch/tag a source package is cut from.
- [[open-source-licensing]] — the license a distribution must declare.

## Sources

**Source entities:** [[producing-open-source-software-book]]

- Karl Fogel, *Producing Open Source Software* (2nd ed.), Ch. 7 "Packaging,
  Releasing, and Daily Development", §Packaging (Format, Name) — governing principle
  only, printed p. 127.
