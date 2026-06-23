# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project aims to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/paulomuzyczuk/llm-wiki-kit/commits/main
