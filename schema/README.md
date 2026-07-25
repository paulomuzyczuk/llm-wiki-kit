# Frontmatter schema — single source of truth

This directory is the machine-readable SOT for wiki-page YAML frontmatter across
the fleet. Before this existed, the "schema" lived only as a prose YAML example in
each vault's `CLAUDE.md` `## Conventions` section — which meant per-vault
customizations drifted silently and every legitimate variation forced a
`check-conformance` `Conventions` DIFF requiring manual ratification.

## Layout

```
schema/
  base.schema.json            # universal fields (the SOT)
  vaults/<slug>.json          # per-vault overlay — legitimate variance only
  build_effective_schema.py   # base ⊕ overlay → effective schema (+ subs cross-check)
```

**Effective schema = base + overlay.** The base is a valid JSON Schema
(Draft 2020-12) for the universal fields. An overlay declares only what a vault
legitimately varies:

| Overlay key | Meaning | Example |
|---|---|---|
| `entity_field` | the vault's entity-subject field, or `null` (documentation-only) | `project`, `null` |
| `handoff_type` | the vault's exec-handoff `type` value, or `null` | `coding-handoff`, `null` |
| `roles` | the vault's role enum | `[code-craftsperson, …]` |
| `status_add` | status-enum additions beyond `active\|stub\|archived` | `[needs-review]` |
| `extra_fields` | vault-specific fields | `volatility`, `next_review` |
| `topics_prefix` | required first `topics` tag, or `null` | `my-domain`, `null` |

`entity_field` and `handoff_type` are **cross-checked** against the vault's
existing substitution map (`check-conformance/subs/<slug>.json`) at build time, so
the schema and the subs map cannot silently disagree.

The overlay-key examples above (`entity_field`, freshness fields, `topics_prefix`)
illustrate the format a vault may vary. This example kit ships a single
example overlay, `vaults/software-craft.json`, paired with the example
`check-conformance/subs/software-craft.json`; add one overlay per vault as you
adopt the convention.

## Who consumes it

- **`vault-lint` `check_9_frontmatter_schema`** validates every wiki page's parsed
  frontmatter against the effective schema (stdlib-only checker — no `jsonschema`
  runtime dependency, matching `lint.py`'s zero-dependency design).
- **`check-conformance`** masks the `CLAUDE.md` frontmatter YAML block, because
  this schema — not the prose — is now authoritative for frontmatter.

## Attribution

The "frontmatter validated against a schema, per-field errors, schema-as-SOT"
pattern is adapted (no code copied) from:
- `JulianCataldo/remark-lint-frontmatter-schema` (ISC)
- `dendronhq/dendron` `schema.yml` hierarchical namespaces (Apache-2.0)

See root `CREDITS.md` / `NOTICE`.

## Usage

```
python3 schema/build_effective_schema.py software-craft   # print effective schema + any drift warnings
```
