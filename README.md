# LLM-Wiki Kit

A system of [Claude Code](https://claude.com/claude-code) skills and tools for building and maintaining **LLM-Wiki vaults** — durable, structured knowledge bases in [Obsidian](https://obsidian.md) that an LLM reads, writes, and keeps honest.

The idea is to treat a knowledge vault less like a pile of notes and more like a small encyclopedia with a contract: every page has a defined shape, every claim cites its source, gaps in knowledge are recorded explicitly, and a linter plus a conformance checker enforce all of it instead of relying on discipline. The name nods to [Andrej Karpathy's framing](https://karpathy.ai/) of building a personal "wiki" of distilled understanding rather than hoarding raw material.

> **Status:** working personal system, opened up. The skills and tooling are mature and in daily use. The example artifacts (`VAULTS.md`, `closeout-handoffs/`, `BACKLOG.md`) are sanitized illustrations of the workflow's record types — fictional vaults and decisions, present to show the format. See [What's here](#whats-here).

## The core idea

A vault is governed by a single `CLAUDE.md` contract instantiated from [`CLAUDE.template.md`](CLAUDE.template.md). The template defines:

- **Page schema** — frontmatter fields, citation format, role taxonomy, cross-reference rules.
- **Sanctioned divergence regions** — exactly which parts of a vault's `CLAUDE.md` are allowed to differ from the template (e.g. the per-domain roles table), so everything *else* drifting is a detectable defect.
- **A pipeline** — how source material (books, articles) is planned, ingested, reviewed, and evaluated into wiki pages.
- **Negative space** — knowledge gaps and out-of-scope topics are first-class, recorded rather than silently absent.

One template, many vaults. A "fleet" of domain vaults (software craft, finance, sports science, …) all share the contract and are kept conformant by tooling.

## What's here

### Skills (`~/.claude/skills/`)

| Skill | What it does |
|-------|--------------|
| [`book-planner`](book-planner/) | Produces and persists a batching/synthesis plan *before* a book is ingested; recovers the plan when resuming mid-book. |
| [`book-ingestion`](book-ingestion/) | Ingests one approved batch of chapters into the vault — synthesized topic pages, entity updates, index/log entries, negative-space records. One batch per invocation, never headless. |
| [`book-review`](book-review/) | Verifies a freshly ingested chapter against the vault's discipline rules. Reports only — never modifies wiki files. |
| [`vault-evaluator`](vault-evaluator/) | Benchmarks how much a vault actually helps: runs question sets across three conditions (no context / raw source / vault) and multiple model classes, then reports comparative performance. |
| [`article-extractor`](article-extractor/) | Extracts clean article text from a URL into a Markdown note with provenance frontmatter, ready to drop into a vault. |
| [`vault-lint`](vault-lint/) | Health-check sweep — citation-resolution failures, orphan pages, missing cross-references, duplicate concepts, stale claims, role-count drift, plus per-vault extension checks. |

### Tools

| Tool | What it does |
|------|--------------|
| [`new-vault.sh`](new-vault.sh) | Scaffolds a new vault from `CLAUDE.template.md` + a subs file: validates the token set, substitutes every `{{PLACEHOLDER}}`, writes `CLAUDE.md`, and creates the folder tree. A freshly scaffolded vault passes `check-conformance.py` with exit 0. |
| [`vault-lint/lint.py`](vault-lint/lint.py) | Reference implementation of the lint spec. `python3 lint.py <vault-path>` → writes a dated digest and appends to the vault log. |
| [`check-conformance/check-conformance.py`](check-conformance/check-conformance.py) | Mechanical template-vs-vault diff that respects the sanctioned-divergence regions. Has a pytest suite under `check-conformance/tests/`. |

### Contract & examples

- [`CLAUDE.template.md`](CLAUDE.template.md) — the per-vault contract these skills are written against. Start here to understand the system.
- [`VAULTS.md`](VAULTS.md) — example fleet registry (intake prefixes → vault paths). *Illustrative.*
- [`BACKLOG.md`](BACKLOG.md), [`closeout-handoffs/`](closeout-handoffs/) — sanitized examples of the fleet backlog and the `planning-handoff` closeout record type. *Illustrative — fictional vaults and dates.*
- [`check-conformance/subs/software-craft.json`](check-conformance/subs/software-craft.json) — example subs file (token substitutions) for the conformance checker.

## Install

These are Claude Code skills. Clone the repo, then symlink (or copy) each skill folder into your skills directory:

```sh
git clone https://github.com/paulomuzyczuk/llm-wiki-kit.git
cd llm-wiki-kit
for skill in article-extractor book-ingestion book-planner book-review vault-evaluator vault-lint; do
  ln -s "$PWD/$skill" "$HOME/.claude/skills/$skill"
done
```

Then create a vault with the scaffolder, reusing the same subs format the conformance checker consumes:

```sh
./new-vault.sh --subs check-conformance/subs/software-craft.json --dest ~/vaults/my-vault
```

It substitutes the tokens, writes `CLAUDE.md`, and builds the folder tree; it then prints the judgment calls it deliberately leaves to you (the roles table, the optional notation/extension blocks, the lint config). Prefer to do it by hand? Copy `CLAUDE.template.md` into your vault root as `CLAUDE.md` and substitute the `{{PLACEHOLDER}}` values yourself — the instantiation header at the top of the template walks through it.

The Python tools require Python 3 and no third-party dependencies; run their test suites with `pytest`.

## Requirements

- [Claude Code](https://claude.com/claude-code)
- [Obsidian](https://obsidian.md) (the vaults are plain Markdown, so any editor works, but the conventions assume Obsidian-style `[[wikilinks]]`)
- Python 3.10+ for the linter and conformance checker

## License

[MIT](LICENSE)
