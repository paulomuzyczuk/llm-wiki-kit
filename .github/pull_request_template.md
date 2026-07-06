## What & why

<!-- One or two sentences. Link the issue this addresses (non-trivial changes
should have one first — see CONTRIBUTING.md). -->

## Checklist

- [ ] `ruff check . && ruff format --check .` passes (and `shellcheck` if shell scripts changed)
- [ ] Tests pass (`vault-lint/tests`, `check-conformance/tests`); new behavior has tests
- [ ] No personal or unsanitized vault content in examples or fixtures
- [ ] Docs updated if behavior changed (`docs/`, the relevant `SKILL.md`, or `CLAUDE.template.md`)
