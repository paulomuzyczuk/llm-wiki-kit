# LLM-Wiki Kit

A system of [Claude Code](https://claude.com/claude-code) skills and tools for building and maintaining **LLM-Wiki vaults** — durable, structured knowledge bases in [Obsidian](https://obsidian.md) that an LLM reads, writes, and keeps honest.

The idea is to treat a knowledge vault less like a pile of notes and more like a small encyclopedia with a contract: every page has a defined shape, every claim cites its source, gaps in knowledge are recorded explicitly, and a linter plus a conformance checker enforce all of it instead of relying on discipline. The name nods to [Andrej Karpathy's framing]([https://karpathy.ai/](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)) of building a personal "wiki" of distilled understanding rather than hoarding raw material.

> **Status:** working personal system, opened up. The skills and tooling are mature and in daily use. The example artifacts (`VAULTS.md`, `closeout-handoffs/`, `BACKLOG.md`) are sanitized illustrations of the workflow's record types — fictional vaults and decisions, present to show the format. See [What's here](#whats-here).

## The core idea

A vault is governed by a single `CLAUDE.md` contract instantiated from [`CLAUDE.template.md`](CLAUDE.template.md). The template defines:

- **Page schema** — frontmatter fields, citation format, role taxonomy, cross-reference rules.
- **Sanctioned divergence regions** — exactly which parts of a vault's `CLAUDE.md` are allowed to differ from the template (e.g. the per-domain roles table), so everything *else* drifting is a detectable defect.
- **A pipeline** — how source material (books, articles) is planned, ingested, reviewed, and evaluated into wiki pages.
- **Negative space** — knowledge gaps and out-of-scope topics are first-class, recorded rather than silently absent.

One template, many vaults. A "fleet" of domain vaults (e.g. business-analytics, design, software-craft) all share the contract and are kept conformant by tooling.

## Why it's shaped this way

The contract's more opinionated rules aren't arbitrary — several are deliberate borrowings from library, archival, and information science, disciplines that have spent over a century on keeping a *growing* collection findable, trustworthy, and honest about its own limits:

- **Negative space is recorded, not silently absent** — documenting what was deliberately left out, and why, is **appraisal** in the archival sense: a selection judgement made accountable rather than invisible (Foscarini, *Currents of Archival Thinking*, 2017).
- **Citations are surrogate records, not just links** — the two-part page reference plus the `[[<slug>-book]]` entity backlink give each claim a stable, location-independent identity instead of a fragile file path that rots when things move (Svenonius 2000; Joudrey & Taylor 2018; "cool URIs don't change").
- **A human reviews what the machine describes** — judging what a source is *about* is the task automated describers fail at, so `book-review` is mandatory and independent: the LLM proposes, a reviewer and the human dispose (Svenonius 2000; Joudrey & Taylor 2018).
- **Nothing is deleted; stale pages are archived** — for a digital collection, retention beats pruning, and the **records-continuum** model treats disposition as a transition, not an endpoint (Upward via Oliver, *Currents of Archival Thinking*, 2017).

Underneath all four is Glushko's tradeoff (*The Discipline of Organizing*, 2013): effort spent organizing "on the way in" is repaid as trust and findability "on the way out" — and the bet here is that an LLM can afford that upfront effort where a human maintaining notes by hand often can't.

One honest caveat: this is a **reference base, not a thinking tool**. In the Zettelkasten tradition (Ahrens, *How to Take Smart Notes*, 2017) the value comes from *you* doing the writing — elaboration is how you learn. Here the LLM writes, so the vault is optimised for retrieval; it sharpens your exchanges with Claude but doesn't teach you the material the way writing your own notes would. It's Karpathy's "distilled wiki" — a store of understanding to draw on, not a substitute for thinking.

→ The full rationale, with the supporting theory and sources, is in **[docs/theory.md](docs/theory.md)** — part of the **[docs/](docs/)** set (theory, architecture, and pipeline).

## What's here

### Skills (`~/.claude/skills/`)

| Skill | What it does |
|-------|--------------|
| [`book-planner`](book-planner/) | Produces and persists a batching/synthesis plan *before* a book is ingested; recovers the plan when resuming mid-book. |
| [`book-ingestion`](book-ingestion/) | Ingests one approved batch of chapters into the vault — synthesized topic pages, entity updates, index/log entries, negative-space records. One batch per invocation, never headless. |
| [`book-review`](book-review/) | Verifies a freshly ingested chapter against the vault's discipline rules. Reports only — never modifies wiki files. |
| [`vault-evaluator`](vault-evaluator/) | Benchmarks how much a vault actually helps: runs question sets across three conditions (no context / raw source / vault) and multiple model classes, then reports comparative performance. |
| [`article-ingestion`](article-ingestion/) | Owns the article path: **fetches** a URL into a provenance-stamped Markdown note, and **ingests** a pending article into the wiki (topic/entity synthesis, vocabulary resolution, index/log, lint trigger). Interactive or headless. |
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
- [`examples/software-craft/`](examples/software-craft/) — a **populated example vault** built by running the real pipeline. It shows actual synthesized output, not just templates: topic pages with frontmatter and [two-part citations](examples/software-craft/wiki/topics/version-control.md), `## Negative Space` sections, a subject-grouped [`index.md`](examples/software-craft/wiki/index.md), a role map-of-content, the `book-planner` → `book-ingestion` → `book-review` artifacts (plan, meta, [review digest](examples/software-craft/wiki/digests/)), and cross-source enrichment where a peer-reviewed paper extends a book-derived page. CI runs `vault-lint` against it on every push to keep it clean.

### Example sources (all openly licensed, committed under `examples/software-craft/raw-input/`)

- *Producing Open Source Software* (2nd ed.) — Karl Fogel — **CC BY-SA 4.0** — https://producingoss.com/
- *Studying the Impact of CI on Pull Request Delivery Time in Open Source Projects* — Guo & Leitner, *PeerJ CS* 5:e245 (2019) — **CC BY 4.0** — [doi:10.7717/peerj-cs.245](https://doi.org/10.7717/peerj-cs.245)
- *Who Makes Open Source Code?* — Mehler, Otto & Sapienza, *EPJ Data Science* 13:35 (2024) — **CC BY 4.0** — [doi:10.1140/epjds/s13688-024-00475-0](https://doi.org/10.1140/epjds/s13688-024-00475-0)

The example synthesizes and cites these sources (attribution as required by their licenses); it does not reproduce them in full.

## Install

These are Claude Code skills — there's nothing to compile. "Installing" just symlinks each skill folder into `~/.claude/skills/` so Claude Code can discover it. Clone the repo and run `install.sh`:

```sh
git clone https://github.com/paulomuzyczuk/llm-wiki-kit.git
cd llm-wiki-kit
./install.sh
```

The installer auto-discovers every skill (any folder with a `SKILL.md`), creates the skills directory if needed, and is safe to re-run — it replaces existing links instead of duplicating them. Useful flags:

```sh
./install.sh --dir ~/some/other/skills   # install into a non-default location
./install.sh --copy                      # copy the folders instead of symlinking
./install.sh --uninstall                 # remove only the links pointing back at this repo
```

(`--uninstall` is conservative: it removes a skill link only if it resolves into this clone, and never touches a real directory or a link you pointed elsewhere. You can also override the target with the `CLAUDE_SKILLS_DIR` environment variable.)

Prefer to do it by hand? It's just a symlink loop:

```sh
mkdir -p "$HOME/.claude/skills"
for skill in article-ingestion book-ingestion book-planner book-review vault-evaluator vault-lint; do
  ln -sfn "$PWD/$skill" "$HOME/.claude/skills/$skill"
done
```

Then create a vault with the scaffolder, reusing the same subs format the conformance checker consumes:

```sh
./new-vault.sh --subs check-conformance/subs/software-craft.json --dest ~/vaults/my-vault
```

It substitutes the tokens, writes `CLAUDE.md`, and builds the folder tree; it then prints the judgment calls it deliberately leaves to you (the roles table, the optional notation/extension blocks, the lint config). Prefer to do it by hand? Copy `CLAUDE.template.md` into your vault root as `CLAUDE.md` and substitute the `{{PLACEHOLDER}}` values yourself — the instantiation header at the top of the template walks through it.

The Python tools require Python 3 and no third-party dependencies; run their test suites with `pytest`.

**Want to see real output before building your own?** Browse [`examples/software-craft/`](examples/software-craft/) — start at its [`wiki/index.md`](examples/software-craft/wiki/index.md), open [`version-control`](examples/software-craft/wiki/topics/version-control.md) to see the citation and negative-space conventions in practice, then run the linter against it to confirm it's clean:

```sh
python3 vault-lint/lint.py examples/software-craft   # Phase 1 findings: 0
```

Once you have a vault, see [Using the vault](#using-the-vault) for how to prompt an LLM against it efficiently.

## Using the vault

The build pipeline is the hard part; *reading* a vault is deliberately plain — it's Markdown, so any LLM with file access works. In practice you point Claude Code (or any agent) at the vault directory and ask. The vault's shape is what makes that exchange efficient: the LLM should **enter through [`index.md`](examples/software-craft/wiki/index.md), pull only the pages it needs, and answer from their citations** rather than re-deriving the material. A few prompt patterns get you most of the value:

**Scope the agent to the vault, entering through the index.** The index is the retrieval surface — subject-grouped, with role maps-of-content as a browse layer above it. Tell the agent to start there instead of grepping blindly:

> Use `~/vaults/software-craft` as your only knowledge source. Start from `wiki/index.md`, follow the `[[wikilinks]]` to the relevant topic pages, and answer: *what does this vault say about choosing a version control system?*

**Demand citations, and answer only from what's paged.** Every claim in a topic page carries a two-part citation (a `[[<slug>-book]]` entity backlink plus a source page anchor). Make the agent carry those through so you can verify, and forbid it from filling gaps with its own training data:

> Answer using only the cited claims in the vault. Quote each supporting line and include its citation (e.g. `Fogel 2023, p. 43`). If the vault doesn't cover something, say so — do not supplement from general knowledge.

**Ask what the vault deliberately leaves out.** Negative space is first-class here: each page has a `## Negative Space` section, and [`gaps.md`](examples/software-craft/wiki/gaps.md) records knowledge gaps and books not yet ingested. This is the question most knowledge bases can't answer:

> Based on the `## Negative Space` sections and `wiki/gaps.md`, what does this vault explicitly *not* cover on continuous integration, and why was it left out?

**Read through a role.** Role maps-of-content (under **Navigation** in the index) and the `roles:` frontmatter field let you scope to a persona's reading list rather than the whole fleet:

> Using the `role-code-craftsperson` map-of-content, give me the three pages most worth reading before my first open-source contribution, and summarize each in two sentences with citations.

**Follow the cross-references.** Pages link to each other with `[[wikilinks]]`; let the agent traverse them to assemble a synthesis no single page holds:

> Starting from `[[version-control]]`, follow its cross-references and synthesize how version control, code review, and continuous integration reinforce each other. Cite each page you draw from.

The throughline: tell the agent to treat the vault as authoritative and bounded — **enter through the index, cite every claim, and surface gaps instead of papering over them.** That's the behavior the contract was built to reward.

## Requirements

- [Claude Code](https://claude.com/claude-code)
- [Obsidian](https://obsidian.md) (the vaults are plain Markdown, so any editor works, but the conventions assume Obsidian-style `[[wikilinks]]`)
- Python 3.10+ for the linter and conformance checker
- [Calibre](https://calibre-ebook.com/) (its `ebook-convert` CLI) — only if you ingest non-PDF books; `book-planner` uses it to convert `.epub`/`.mobi`/`.azw` sources to PDF. Not needed for PDF sources or article ingestion.

### Scheduling (optional, macOS only)

The "Scheduled Operations" pipeline (`scheduled-job.plist.template`, `freshness-job.plist.template`) is **macOS-only** — it uses [launchd](https://www.launchd.info/). On Linux use `cron` or a systemd timer; on Windows use Task Scheduler. The job just invokes Claude Code against the vault on a cadence, so any scheduler that can run a command works — the plist files are a convenience for macOS, not a requirement. Everything else (skills, linter, conformance checker, scaffolder) is cross-platform.

## License

[MIT](LICENSE)
