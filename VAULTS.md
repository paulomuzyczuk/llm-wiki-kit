<!--
EXAMPLE REGISTRY — illustrative only.

This file shows the shape of the fleet registry: the lookup table that routes an
incoming document to the right vault's intake folder by filename prefix. The rows
below are illustrative. Replace them with your own vaults when you adopt the
convention; the `software-craft` row is the example vault referenced elsewhere in
this repo (see check-conformance/subs/software-craft.json).
-->
# Fleet Vault Registry

All active LLM-Wiki vaults, their intake prefixes, and their vault paths.
Use this table when routing a document to the correct vault's `raw-input/_pending/` folder.

| Prefix | Vault path | Domain | Example filename |
|--------|-----------|--------|-----------------|
| `sc-` | `vaults/software-craft` | Software Craft | `sc-planning-handoff-vault-buildout-2026-01-05.md` |
| `<prefix>-` | `vaults/<vault-slug>` | `<Domain>` | `<prefix>-<subtype>-<topic>-<date>.md` |

## Notes

- Each prefix is declared as `Vault prefix: <prefix>-` in the vault's `CLAUDE.md`.
- The intake filter keeps only `.md` files whose name starts with that vault's prefix (case-insensitive).
- `planning-handoffs` use the same prefix as all other documents; the subtype segment distinguishes them.
- One row per vault. The second row above is a format placeholder — replace or remove it.
