# CREDITS — borrowed ideas & attributions (live ledger)

This is the **live** attribution ledger for third-party ideas borrowed into
llm-wiki-kit (which is MIT-licensed). It is seeded from the landscape-scan ledger
in `docs/CREDITS-run2.md` (the reference/analysis artifact) and is the artifact
kept in sync with the code: flip **Planned → Shipped** and fill the borrow-site
(`file:symbol`) as each borrow lands, in the same commit that lands it.

Obligation model (from each source's licence):
- **Permissive (MIT/BSD/ISC/Apache-2.0)** vendored as code → keep the licence
  notice in `NOTICE`/`THIRD-PARTY-NOTICES` + an inline comment at the borrow site.
  Apache-2.0 additionally requires **stating changes** when source is modified.
- **Idea/pattern reimplemented independently** → credit in a comment; add a `NOTICE`
  entry as a courtesy. No source copied.
- **Copyleft/source-available (AGPL, BSL, Elastic, etc.)** → **reimplement
  independently, credit in a comment, never copy source.**

| Borrow (idea/technique) | Source (owner/repo) | Licence | Reuse mode | Status | Borrow-site |
|---|---|---|---|---|---|
| JSON-Schema-driven frontmatter validation as a lint rule (schema = SOT, per-field errors) | JulianCataldo/remark-lint-frontmatter-schema | ISC | reimplemented (pattern; no code copied) | **Shipped** | `schema/base.schema.json`; `vault-lint/lint.py` → `check_9_frontmatter_schema` |
| Hierarchical-namespace schema-validation model (`schema.yml`) | dendronhq/dendron | Apache-2.0 | reimplemented (pattern; no code copied) | **Shipped** | `schema/vaults/*.json` overlay model; `schema/build_effective_schema.py` |
| Invalidate-not-delete bi-temporal edge model (archive-not-delete / no-silent-drift) | getzep/graphiti | Apache-2.0 | idea/design reference | Planned (design note only — BACKLOG "Archive-not-delete") | — |
| Perspective-guided question-asking before writing a page (surfaces negative space) | stanford-oval/storm | MIT | reimplement / formulas | Planned | — |
| Grounded source→passage citation tracking | stanford-oval/storm | MIT | reimplement | Planned | — |
| Citation normalisation/resolution (DOI/CSL/BibTeX) engine | citation-js/citation-js | MIT | code-dependency | Planned | — |
| Fixed-section wiki-layout + auto-overview/diagram drafting (draft stage feeding review) | AsyncFuncAI/deepwiki-open | MIT | reimplement | Planned | — |
| Orphan/placeholder detection precedent; review surfaces | foambubble/foam | MIT | reimplement / formulas | Planned | — |
| Optional static-site publish/export layer (reviewer surface) | jackyzha0/quartz | MIT | vendor / code-dependency | Planned | — |
| Human chunk-inspect/edit-before-use (review-gate ergonomics) | infiniflow/ragflow | Apache-2.0 | reimplement | Planned | — |
| Local-embedding similarity as a lint signal (duplicate / missing cross-ref) | basicmachines-co/basic-memory; reorproject/reor; logancyang/obsidian-copilot; brianpetro/obsidian-smart-connections | AGPL-3.0 / AGPL-3.0 / AGPL-3.0 / source-available | **idea-only** (never copy source) | Planned | — |
| MCP note/observation/relation write interface (agent-proposed edits) | basicmachines-co/basic-memory | AGPL-3.0 | **idea-only** (never copy source) | Planned | — |

**Convention.** At each borrow site, leave an inline comment naming the source +
licence, e.g. `# adapted-pattern from JulianCataldo/remark-lint-frontmatter-schema
(ISC) — see CREDITS.md`. Permissive-code reuse → add the notice to `NOTICE` in the
same commit that vendors the code. Idea-only sources → credit in a comment, never
copy source.
