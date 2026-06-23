# Security Policy

## Reporting a vulnerability

Please report security issues **privately** through GitHub's private vulnerability
reporting: go to the repository's **Security** tab → **Report a vulnerability**
(or the **"Report a vulnerability"** button under *Security advisories*). This keeps
the report confidential until a fix is available.

Please do **not** open a public issue for a suspected vulnerability.

This is a personal, best-effort project maintained by one person — there is no SLA,
but I aim to acknowledge a report within a week and will keep you updated on any fix.
Reports that include a clear reproduction and the affected file/skill are easiest to
act on.

## Supported versions

This project is pre-1.0 and ships from a single line of development. Only the current
`main` branch is supported; fixes land there and are not backported.

## What this project is (and what's in scope)

This repo is a set of **Claude Code skills** (Markdown instructions an LLM agent
follows) plus dependency-free **Python/shell tooling** (`lint.py`,
`check-conformance.py`, `new-vault.sh`, `install.sh`). In scope for this policy:

- The Python and shell scripts in this repo.
- The skill instructions themselves (e.g. an instruction that could cause unsafe
  behavior).
- The install/scaffolding scripts and the scheduling templates.

**Out of scope** (report these to their respective projects): Claude Code itself, the
Anthropic API, Obsidian, Calibre, and any vault *content* you generate.

## Security model — what to know before you run this

These skills drive an AI agent that reads and writes files and can run shell commands.
A few properties are worth understanding:

- **The skills run with the permissions of your Claude Code session.** A skill can do
  anything the agent is allowed to do in your environment — read, write, and delete
  files, and run commands. Run them against vaults and directories you're comfortable
  granting that access to.
- **`article-ingestion` fetches remote URLs.** Fetched web content is **untrusted
  input** and a potential prompt-injection vector: a malicious page could contain text
  designed to steer the agent. Treat ingestion of arbitrary URLs with the same caution
  you'd apply to running untrusted input through any automated pipeline, and review
  what gets written to your vault.
- **The scheduling templates run the agent autonomously on a cadence.** The optional
  `scheduled-job.plist.template` / `freshness-job.plist.template` invoke Claude Code
  against a vault unattended. Understand what the scheduled job is allowed to do before
  enabling it.
- **Don't put secrets in a vault.** Vaults are plain Markdown intended to be readable
  (and often committed). The repo's `.gitignore` defensively blocks common credential
  files (`.env`, `*.pem`, `*.key`, `credentials.json`, …), and CI runs a secret scan,
  but the durable rule is simply: keep credentials out of vault content.

## Good practice

- Review skill changes before installing or updating, the same as any code you run.
- Prefer scoping the agent to a specific vault directory rather than broad filesystem
  access.
- Keep your Claude Code and Python toolchain up to date.
