---
title: Topics Authority — software craft
type: authority
status: stub
date: 2026-06-23
last_updated: 2026-06-23
---

# Topics Authority — software craft

Controlled-vocabulary source of truth for this vault — a lightweight thesaurus
(a preferred term plus its use-for variants). `/vault-lint` Check 8 resolves
every `topics:` value against **Subjects** and validates `aliases:` against
**Concepts**. Report-only.

<!-- SEED-ME: unpopulated skeleton. The FIRST ingest into this vault — book-planner
     Phase 0 if a book is added first, otherwise the first article/notes ingest —
     seeds this file with up to 10 subject categories and up to 30 aliases drawn
     from that first content and the domain. The 10/30 caps apply to the INITIAL
     SEED ONLY: afterwards, resolve every new term against this file before minting
     it, grow the vocabulary as the vault grows, and let /vault-lint reconcile any
     scatter. Set status: active and delete this comment once seeded. -->

## Subject categories

Governs `topics:`. A value must be a preferred term below (or a reserved tag).
List variant spellings/synonyms that should resolve to a preferred term in its
Use-for column.

| Preferred | Use-for (variants that resolve to it) |
|---|---|

## Concept aliases

Governs `aliases:` / page identity — each topic page is a preferred concept and
its frontmatter `aliases:` are its use-for variants. No alias may belong to two
pages or shadow another page's canonical title/slug.

| Preferred (page) | Use-for (aliases) |
|---|---|

## Reserved non-subject tags

Tags legal in the topics field but not subject categories: `stub`.
