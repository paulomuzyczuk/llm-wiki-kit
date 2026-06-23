---
name: vault-lint
description: >
  Runs a health-check sweep of a Karpathy-style LLM Wiki vault. Checks for
  citation-resolution failures, orphan pages, concepts lacking a page, missing
  cross-references, duplicate concept pages, stale claims, and data gaps. Also
  checks for drift between role-page-counts in wiki/index.md and the ground
  truth from page frontmatter, and runs any vault-specific extensions declared
  in the VAULT-LINT-EXTENSIONS block of CLAUDE.md. Report-only — never modifies
  wiki pages. Emits a ready-to-apply patch block for any role-count drift found.
  Use this skill whenever the user invokes /vault-lint, asks for a vault health
  check, or when a `lint | pending | <vault-slug>` marker appears in log.md with
  no subsequent `lint | <vault-slug> |` entry. One invocation = one vault.
---

# Vault Lint

Run a comprehensive health check on an LLM-wiki Obsidian vault. The check covers citation resolution, orphan pages, dangling wikilinks, missing cross-references, duplicate pages, contradictions, role-count drift, and vault-specific extensions.

The implementation is a single Python script, `lint.py`, co-located with this skill — it sits in the same folder as this `SKILL.md`. When the skill is installed per the repo README (symlinked or copied into `~/.claude/skills/`), that path is `~/.claude/skills/vault-lint/lint.py`. This skill exists to invoke that script and present its output. The script is the canonical source of truth — this skill does NOT describe check logic, does NOT contain reference implementations, and does NOT reimplement anything.

## When to invoke

- The user explicitly runs `/vault-lint`.
- A `lint | pending | <vault-slug>` marker exists in the vault's `wiki/log.md` (signals that prior operations have accumulated and a health check is due — book ingests and threshold-N article ingests both write this marker).
- Periodic health checks (monthly is typical).

## Procedure

### Step 1 — Identify the vault

Resolve the vault path from the user's working context:

1. If the user's current working directory contains both `CLAUDE.md` and `wiki/`, that is the vault root.
2. Otherwise, ask the user which vault they want to lint. The active vaults live under `~/vaults/`.

### Step 2 — Confirmation gate

Before running the script (which writes a digest report and modifies `log.md`), confirm with the user:

1. Read just the first ~20 lines of `<vault>/CLAUDE.md` to extract the `vault_slug:` value. Do not read further; the script will read everything it needs itself.
2. Ask the user: "Lint the `<vault_slug>` vault? This writes a digest to `wiki/digests/lint-YYYY-MM-DD.md` and appends a log entry. (proceed / cancel)"
3. Wait for explicit confirmation. Anything other than an affirmative ("proceed", "yes", "go ahead") cancels.

If a `lint | pending | <vault-slug>` marker exists in `log.md`, mention it in the confirmation message ("There's a pending marker from prior operations — proceed?") but still wait for explicit confirmation.

### Step 3 — Invoke the script

Once confirmed, execute the `lint.py` co-located with this skill. With the README install that is:

  python3 ~/.claude/skills/vault-lint/lint.py <vault-path>

If the skill was installed somewhere else, run the `lint.py` that sits beside this `SKILL.md` instead of hardcoding a clone path.

Capture stdout (the script prints a short status summary). Capture the exit code:
- 0 = success (clean lint, or lint with patches)
- 1 = Phase 2.5 FATAL fired (counting inconsistency)
- 2 = script crashed or vault structure invalid

### Step 4 — Present the report

After the script exits, read the digest at `<vault>/wiki/digests/lint-YYYY-MM-DD.md` and present its full contents to the user. The report is already formatted in markdown — pass it through, do not summarise unless asked.

If exit code 1 (FATAL), surface clearly: "The lint detected a counting inconsistency. Phase 2.5 fired. No patches were emitted and no log entry was written. The digest contains the FATAL section only." Then present that digest.

If exit code 2 (crash), report the error from stdout and stop. Do NOT attempt to lint by hand — the script is the only authoritative implementation.

## What this skill does NOT do

- Does NOT describe check logic. That lives in `lint.py`.
- Does NOT contain reference implementations. Past attempts to embed reference Python in this skill produced inconsistent results across sessions; the script architecture eliminates this variance.
- Does NOT reimplement any check. If you find yourself writing inline Python here that does what the script already does, stop. Use the script.
- Does NOT modify the vault directly. Only the script writes to disk.

## Calibration notes

This skill evolved through 8 lint runs against software-craft, each surfacing a different category of runtime non-determinism: wikilink parser regression, Check 4 filter-skipping, Phase 2 role-counting drift, Phase 2.5 guard inconsistency, parser improvisation, structural-exclusion skipping. Declarative spec language, imperative "MUST" instructions, embedded reference implementations, and hard cross-check guards were each ignored by different sessions at different times.

The single-script architecture (this skill in its current form) eliminates this entire class of variance. The script's behaviour is determined by its code, not by spec interpretation. Bugs are findable and fixable by editing the script directly; sessions cannot drift because there is no interpretation step.

If a future session is tempted to "improve" this skill by re-embedding check logic or substituting its own implementation, the history above is the warning. The script wins. The skill is a thin wrapper by design.
