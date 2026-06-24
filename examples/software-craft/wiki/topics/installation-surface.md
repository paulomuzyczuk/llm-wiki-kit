---
title: Installation Surface
aliases: [install-surface, multi-path-install, compile-once-repackage-many, low-friction-install, binary-distribution]
date: 2026-06-24
last_updated: 2026-06-24
type: topic
topics: [release-engineering]
roles: [product-engineer, tech-lead]
source_tier: 2
project: null
source_count: 1
status: active
---

# Installation Surface

The **installation surface** is the set of ways a stranger can install and try a
tool. Akita's strongly-stated ordering puts it first among the three things a project
needs before publishing (ahead of tests/CI and documentation): the new user must be
able to install and try the tool with the least friction possible — one command,
ideally. A project whose only documented install is "clone the repo and run
`cargo build --release`" forces the curious user to have the toolchain installed, wait
through a long compile, and hope no system library is missing — losing, in his
estimate, ~90% of potential users
([Akita 2026](../../raw-input/articles/oss-best-practices-llm-bare-minimum-2026-05-30.md)).
This is a tier-2 practitioner claim; it corroborates and modernizes the tier-1
[[launching-an-open-source-project]] guidance that "appearances matter" and that
getting-started friction is where new projects fall down.

## Offer several paths, let the user pick

The discipline is to publish **multiple install paths** and let each user pick the one
that fits their environment, rather than mandating one. A representative header offers
Homebrew (macOS/Linux), AUR (Arch), `cargo install` (any Rust platform), mise, and a
direct binary tarball download. The Arch user runs `yay`, the macOS user `brew`, the
Rust dev `cargo install`, and whoever just wants the binary grabs the tarball — nobody
is forced to install a whole toolchain just to evaluate the tool
([Akita 2026](../../raw-input/articles/oss-best-practices-llm-bare-minimum-2026-05-30.md)).

## Compile once, repackage many

The mechanic that makes a broad install surface cheap to maintain: **compile the binary
once per architecture, then repackage that same binary into every format.** The build
job produces a tarball plus its `sha256`; the downstream packaging steps (Docker, AUR,
Homebrew, …) *download that already-compiled artifact* instead of recompiling. Three
payoffs: it cuts CI time, it guarantees the byte shipped to one package manager is
identical to the byte shipped to another, and it eliminates the "works in one format,
breaks in the other" class of bug
([Akita 2026](../../raw-input/articles/oss-best-practices-llm-bare-minimum-2026-05-30.md)).
This is the binary-distribution corollary to the tier-1 [[source-packaging]] principle
that binary packages must derive from a single official source release: here the single
*build artifact*, not just the source, is the shared root of every package.

## The menu of formats is a decision space

Each platform is its own world; the choice is which formats to offer against how much
work each costs
([Akita 2026](../../raw-input/articles/oss-best-practices-llm-bare-minimum-2026-05-30.md)):

- **Linux** is the most fragmented. A plain **tarball** is the lowest common denominator
  and should always be offered. **AUR** ships a prebuilt `-bin` package (installs in
  seconds) and a source package; the `-bin` is what most people use. **AppImage** bundles
  all dependencies into one executable, good for desktop apps. **RPM/DEB** for
  Fedora/Debian families are generated from a single declarative spec rather than learning
  each packager's internals.
- **macOS** has Apple-Silicon and Intel targets (or a universal binary), and its defining
  cost is **signing and notarization** — without it Gatekeeper refuses to open the app,
  and it requires a paid developer account.
- **Windows** is the easiest to build and the thorniest to sign: a code-signing
  certificate is expensive and bureaucratic, so for a personal project the pragmatic call
  is to skip it and document that the OS will warn on first run.
- **Language registries** (e.g. `cargo publish` to crates.io) give a first-class install
  path almost for free; make the publish step idempotent so re-running on an
  already-published version doesn't fail the release.

A structural detail ties it together: several of these channels (AUR, Homebrew, mise,
direct download) **all consume the same release tarball**, which is why "compile once,
repackage many" is the organizing rule rather than a per-format afterthought
([Akita 2026](../../raw-input/articles/oss-best-practices-llm-bare-minimum-2026-05-30.md)).

## Signing is a per-platform tax, paid where it matters

Code-signing and notarization friction is unavoidable but unevenly distributed: mandatory
and account-gated on macOS, expensive on Windows, absent for a bare Linux tarball. The
transferable decision is to pay the signing cost where the platform actually blocks the
user (macOS) and accept a documented warning where the cost outweighs the benefit for a
small project (Windows)
([Akita 2026](../../raw-input/articles/oss-best-practices-llm-bare-minimum-2026-05-30.md)).
Project-internal release signing for tamper-verification is a separate concern, covered in
[[releasing-and-signing]].

## Negative Space

- **Named packaging tools and CI actions** (nfpm, `appimagetool`, `lipo`, `codesign`,
  `notarytool`, the AUR-deploy and Rust-cache GitHub Actions) (`tool-specific/perishable`):
  named as current mechanics; the transferable claims (compile-once-repackage-many, offer
  multiple paths, signing-as-per-platform-tax) are captured, the specific tools are not
  load-bearing.
- **Akita's own projects as install examples** (ai-jail, ai-memory, ai-usagebar)
  (`illustrative-scaffolding`): used to illustrate the multi-path header and the
  build-once-reuse flow; the principles are captured, the projects are not paged.
- **The `release.yml` YAML excerpts** (`too-granular`): pipeline configuration detail
  showing how the artifact is reused, not a standalone concept.

## See also

- [[source-packaging]] — the tier-1 principle this extends: a release is defined by its
  canonical source, and binary packages must derive from one official build.
- [[releasing-and-signing]] — the release-approval gate and OpenPGP signing that the
  packaged artifacts pass through before shipping.
- [[launching-an-open-source-project]] — install surface as the top launch-readiness
  signal; the user-facing "appearances matter" side of getting started.
- [[the-automation-ratio]] — why a single uniform packaging pipeline pays back: the common
  task is automated once and the saving is multiplied across every release and format.
- [[llm-assisted-maintenance]] — the standardized, predictable release pipeline an agent
  can be told to run end to end.

## Sources

- Fabio Akita, "Open Source Best Practices with LLMs — The Bare Minimum" (2026),
  [oss-best-practices-llm-bare-minimum-2026-05-30](../../raw-input/articles/oss-best-practices-llm-bare-minimum-2026-05-30.md).
  Tier-2 — long-form practitioner blog post; install-surface and packaging claims are this
  author's experience-based practice, corroborated where noted against the tier-1
  [[producing-open-source-software-book]].
