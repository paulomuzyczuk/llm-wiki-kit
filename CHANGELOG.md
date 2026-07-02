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
- Lint Check 3b English-word and formatting-fragment guardrails: common-English
  emphasis words and formatting fragments (trailing-punctuation labels, bold-wrapped
  wikilinks) no longer surface as un-paged concept candidates. (Shipped earlier in
  `4f35d44`; entry was missing here.)
- Repo-root `regenerate-clones.sh` replacing the six per-skill copies — regenerates
  every skill's project-context clone (or a named subset), with the stale-deployment
  warning generalized from vault-lint to all skills.
- Tests for the previously untested growth edge: `--sync-role-counts` (the one
  vault-mutating mode — drift rewrite, idempotency, no-op byte-identity, both index
  formats), Phase 2b role-MoC curation, and the Check 3b guardrails, plus regression
  tests for every fix below (19 new tests; suites now 105 + 15).
- CI: a `macos-latest` job exercising the shell scripts under macOS system bash 3.2
  (install idempotency in both modes, scaffolder round-trip, friendly missing-flag
  errors, `plutil -lint` on the plist templates) — previously the bash-3.2
  portability discipline was enforced by author vigilance only.

### Fixed

- `vault-lint/lint.py`: Check 7's open-question marker regex `\[?\?\]` made the `[`
  optional, so bare `?]` in prose false-positived — now matches `[?]` only.
- `vault-lint/lint.py`: index-**table** role matching used substring containment
  (role `beta` could claim a "beta-blocker studies" row, first match won); detector
  and patcher now share exact `role-<id>.md`-link / normalized-cell matching, and the
  READY-TO-APPLY / `--sync-role-counts` patch edits only the count cell instead of
  the first matching number anywhere in the row. The never-reported sentinel is now
  an explicit leave-row-unpatched fail-safe.
- `lint.py` and `check-conformance.py` now honor their documented exit-code
  contract on crash: unhandled exceptions exit **2** (previously Python's default 1,
  which callers read as "findings/diffs found"). `check-conformance.py` reports
  missing/unreadable template, vault, or subs files with a friendly error + exit 2
  instead of a traceback.
- Skill/template drift: `/book-ingest` → `/book-ingestion` (the command the skill
  actually registers) in the template, the example vault, book-planner, and
  book-ingestion; references to the git-ignored `*-skill.md` clones now point at the
  skills themselves; the template's phantom "Step 0a gate" reference corrected to
  vault-lint's Step 2 confirmation gate; template version stamp bumped.
- `book-review`: frontmatter now carries a real trigger `description:`; check count
  corrected to ten; Check 6 validates `type` against the vault's declared schema
  instead of a hardcoded 3-value list and accepts `last_updated` on/after ingestion
  date; Check 9 reads the synthesis strategy from `ingestion-plan.md` (present from
  batch 1) instead of the end-of-book ingest report, so it can actually fire
  mid-book; Phase 1 falls back to searching the whole `log.md` when the ingest entry
  is not in the last 50 lines.
- `vault-lint` skill Step 2 now greps for `vault_slug:` (it lives in the
  VAULT-LINT-EXTENSIONS block, not the first 20 lines of `CLAUDE.md`).
- `install.sh --copy` is now idempotent as the header claims (a previously-copied
  skill directory is refreshed; unrelated directories still refuse); `new-vault.sh`
  flags with a missing value fail with a friendly `ERROR` instead of a raw `set -u`
  crash; `--help` on both scripts prints the header comment block instead of
  hardcoded line ranges (which had already drifted).
- launchd plist templates: the claude binary path is a `{{CLAUDE_BIN}}` token with
  a `which claude` instantiation step (was hardcoded `/opt/homebrew/bin/claude`,
  Apple Silicon Homebrew only).

### Changed

- `vault-evaluator` redesigned from a methodology document into an executable
  protocol. Every question × condition × model cell is now an isolated
  `claude -p --model <id>` subprocess launched from a neutral temp cwd (so
  Condition A is genuinely context-free and the orchestrating session never
  answers or scores anything itself); scoring is blind — a fixed frontier-tier
  judge subprocess sees shuffled, unlabeled answers, with per-question permutations
  recorded for audit. Verdicts are **position-swapped pairwise** (two judge calls
  per question, reversed presentation; disagreement = tie) with per-pair win rates
  gated by a sign-test significance table as the headline metric — rubric scores
  remain as diagnostics. Every cell runs `--output-format json` and records
  tokens/cost/duration, feeding a report Efficiency section (vault lift per 1k
  context tokens, quality per dollar, measured cost substitution). Golden sets add
  Type 4 **abstention controls** drawn from `gaps.md`/negative-space records —
  Condition C must decline at the vault's coverage boundary rather than
  hallucinate. The 10-question minimal version is now the mandatory first
  gate and every run states its exact subprocess call count at a confirmation gate;
  eval digests carry vault frontmatter and each completed run appends an
  `eval | <vault-slug> | …` log entry; Condition C falls back to `index.md` + topic
  pages for vaults without role MoCs; model tiers updated to current names. The
  vault log operation enum in `CLAUDE.template.md` (and the example vault) gains
  `eval`.
- CI hardening: top-level read-only token `permissions`, `concurrency` cancellation
  of superseded runs, pytest pinned like ruff/bandit.
- `.gitignore` now covers `.ruff_cache/` and `.claude/settings.local.json` (both
  previously ignored only by author-machine luck).

- Role map-of-content curation cap raised from **10–15 to 10–25** highest-value pages
  per role, in `CLAUDE.template.md` (and the example vault). A soft guideline only —
  the lint never hard-enforced it — but it makes larger curated browse maps explicitly
  in-bounds for content-dense roles.
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
