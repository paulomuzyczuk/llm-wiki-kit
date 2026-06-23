---
title: Topics Authority — software craft
type: authority
status: active
date: 2026-06-23
last_updated: 2026-06-23
---

# Topics Authority — software craft

Controlled-vocabulary source of truth for this vault — a lightweight thesaurus
(a preferred term plus its use-for variants). `/vault-lint` Check 8 resolves
every `topics:` value against **Subjects** and validates `aliases:` against
**Concepts**. Report-only.

> Seeded 2026-06-23 from the vault's first content — *Producing Open Source
> Software* (2nd ed.) plus the two open-access papers queued for ingest. ≤10
> subjects / ≤30 aliases per the first-ingest seed rule; grows from here under
> resolve-before-minting.

## Subject categories

Governs `topics:`. A value must be a preferred term below (or a reserved tag).
List variant spellings/synonyms that should resolve to a preferred term in its
Use-for column.

| Preferred | Use-for (variants that resolve to it) |
|---|---|
| version-control | vcs, source-control, revision-control |
| code-review | peer-review, code-reviews |
| continuous-integration | ci, ci-cd, continuous-delivery |
| project-infrastructure | technical-infrastructure, tooling, dev-infrastructure |
| software-collaboration | collaboration, distributed-development |
| open-source-governance | governance, project-governance |
| open-source-participation | participation, contributors, contribution, community |
| bug-tracking | issue-tracking, bug-tracker, defect-tracking |
| release-engineering | releasing, packaging, release-management |
| code-quality | quality, software-quality |

## Concept aliases

Governs `aliases:` / page identity — each topic page is a preferred concept and
its frontmatter `aliases:` are its use-for variants. No alias may belong to two
pages or shadow another page's canonical title/slug.

| Preferred (page) | Use-for (aliases) |
|---|---|
| version-control | vcs, source-control, revision-control |
| code-review | peer-review, conspicuous-code-review |
| continuous-integration | ci, ci-cd |
| open-source-participation | contributor-base, who-contributes |

## Reserved non-subject tags

Tags legal in the topics field but not subject categories: `stub`.
