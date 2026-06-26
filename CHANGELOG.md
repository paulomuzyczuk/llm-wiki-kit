# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project aims to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `vault-lint/lint.py --sync-role-counts <vault-path>` — a deterministic,
  report-free, log-free, idempotent mode that recomputes the role-page counts in
  `wiki/index.md` from topic-page frontmatter and rewrites them in place. It reuses
  the Phase 2 counter (`phase_2_role_drift`) and a newly extracted
  `_rewrite_role_section` helper now shared with the lint report's READY-TO-APPLY
  patch block, so the counting/rewriting logic has a single implementation. Errors
  (exit 2) when a vault declares no role-counts surface.
- Lint **Phase 2b — role-MoC curation candidates** (advisory). Per role, surfaces the
  top-K-central role-bearing topic pages that the role MoC (`role-<role>.md`) omits,
  where K is the MoC's current curated size and centrality is vault-wide inbound
  wikilink count. Bounded by K to stay low-noise; also flags `stale` MoC entries that
  bear a different canonical role. Each candidate shows its current placement — other
  role MoCs that already curate it (or a ⚠ orphan flag when none) and its full role
  tags — so a reviewer can tell a page already reachable elsewhere from one orphaned out
  of the browse layer entirely. Report-only — no gating, no writes. Renders a
  `## Phase 2b` report section plus summary/stdout lines.

### Changed

- `book-ingestion` and `article-ingestion` skills now call `--sync-role-counts` at
  their existing index-update points (book: Phase 5 batch-end; article: post-loop,
  once per run, interactive and headless). This keeps `wiki/index.md` role counts
  in step with frontmatter so `/vault-lint` Phase 2 reverts to a pure detector —
  any future non-zero drift signals a skill that skipped its sync rather than
  expected accumulation.

## [0.1.0] - 2026-06-24

First tagged release. Establishes the public baseline of the kit: the skills,
the Python tooling, the per-vault contract, and the example vault.

### Added

- `install.sh` — one-command install/uninstall of the skills into
  `~/.claude/skills/` (replaces the manual symlink loop). Supports `--uninstall`,
  `--dir <path>`, `--copy`, and `CLAUDE_SKILLS_DIR`; idempotent, and refuses to
  clobber or unlink anything that isn't a symlink back into this repo.
- CI: `lint` job (Ruff lint + Ruff format check + ShellCheck) and `security`
  job (Bandit Python SAST gated at medium+ severity, plus Gitleaks secret scan).
- `ruff.toml` — Ruff configuration (single-quote formatter, `E`/`F`/`W`/`I`/`UP`/`B`
  rule sets; `E501` left to the formatter).
- `SECURITY.md` — security policy (private vulnerability reporting, scope, and the
  project's security model).
- `CONTRIBUTING.md` — contributor guide (setup, local check commands, the skill-clone
  and template-contract rules, commit/PR conventions).
- This changelog.

### Changed

- Reformatted the Python tooling (`check-conformance/`, `vault-lint/`) with Ruff
  and removed dead code flagged by the linter. No behavior change; all test
  suites still pass.
- Moved `THEORY.md` into a `docs/` set and expanded it: `docs/theory.md` (the why),
  `docs/architecture.md` (the structure), `docs/pipeline.md` (the workflow), and a
  `docs/README.md` index. README and CONTRIBUTING links updated accordingly.

[Unreleased]: https://github.com/paulomuzyczuk/llm-wiki-kit/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/paulomuzyczuk/llm-wiki-kit/releases/tag/v0.1.0
