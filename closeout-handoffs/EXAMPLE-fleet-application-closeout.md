<!--
EXAMPLE RECORD — illustrative only.

This file demonstrates the shape of a `planning-handoff` closeout record, the
session-bridging document type the LLM-Wiki workflow produces at the end of a
fleet-maintenance cycle. The vaults, dates, books, and decisions below are
fictional and exist solely to show the format. Replace wholesale when you adopt
the convention; nothing here describes a real vault.
-->
---
title: EXAMPLE — fleet application closeout
date: 2026-01-15
last_updated: 2026-01-15
type: planning-handoff
topics: [vault-ops, conformance, template, fleet-management]
source_tier: 3
source_count: 0
status: example
---

## Scope

This cycle ran from 2026-01-11 through 2026-01-15. At cycle entry, `demo-alpha`
had been audited against an earlier template version and `demo-beta` was
unaudited. At cycle close, both vaults carry template version 2026-01-13, both
subs files are ratified, and every fleet propagation item tracked in the BACKLOG
at cycle entry is marked ALL VAULTS PROPAGATED.

## Template version 2026-01-13 changes

Two edits distinguish template version 2026-01-13 from its predecessor:

1. **Calendar version header at line 1.** `<!-- Template version: 2026-01-13 -->`
   was added as the first line of `CLAUDE.template.md`, enabling mechanical
   version identification without parsing change history.
2. **`aliases` field promoted to YAML schema.** The `aliases:` field (form
   `aliases: [<alternate names>]`) was added to the frontmatter schema block,
   establishing it as a universal field across all vault instantiations.

## Per-vault application summary

| Vault        | Status at cycle start | Applied    | Edits | Conformance                          |
|--------------|-----------------------|------------|-------|--------------------------------------|
| `demo-alpha` | audited (older)       | 2026-01-13 | 2     | exit 1, 4 PASS, 2 DIFF, 0 EXEMPT     |
| `demo-beta`  | first-contact         | 2026-01-14 | 3     | exit 1, 5 PASS, 1 DIFF, 1 EXEMPT     |

**`demo-alpha`.** Re-audited 2026-01-13 against template version 2026-01-13. The
`aliases` convention note was added (the field itself was already present); the
roles heading was already canonical. The two remaining DIFFs are deliberate
domain-specific content, re-ratified under the prior audit's closeout.

**`demo-beta`.** First-contact audit 2026-01-14. Subs were constructed and all
tokens ratified. Three edits applied: the `aliases` field and convention note,
plus a Boundary-section rewrite ratified as a permanent vault-specific exception
(the vault declares no external working artifacts, so the condensed phrasing is
more accurate than the substituted template paragraph). The single DIFF is that
Boundary rewrite under inline ratification; the roles-table swap accounts for the
EXEMPT-CONTAINED region.

## Propagations applied across the fleet

**`aliases` field and convention note.** Originated from the observation that
`demo-alpha` used the field on production pages while the template did not declare
it. Promoted to the template 2026-01-13 and propagated to both vaults the same
cycle. ALL VAULTS PROPAGATED.

## BACKLOG resolutions this cycle

1. **`aliases` field promotion to template** (RESOLVED 2026-01-13) — promoted to
   the schema and propagated fleet-wide.

## BACKLOG additions opened this cycle (still Active)

1. **Enrichment-rules block — template-promotion candidate** (target: next cycle)
   — confirmed present in `demo-alpha`; evaluate the other vault before promoting.

## Notable patterns and discoveries

### Explicit READ-ONLY framing prevents autonomous-action drift

A first-contact session framed as "audit and we'll apply fixes if appropriate"
produced several STOP-and-surface violations: fixes were applied autonomously
where the workflow specified surfacing for human approval first. A later session
framed as strictly READ-ONLY, with no "apply if appropriate" hedging, closed with
zero violations. Learning: ambiguous permission language gets resolved toward
action; explicit READ-ONLY framing eliminates the drift.

## Next initiatives

1. **Skill extraction.** Move the dominant byte-consumer section out of each
   `CLAUDE.md` into a shared skill file, cutting per-vault size. Parked as the
   first initiative of the next cycle.
2. **Template version 2026-01-14 candidates.** Enrichment-rules block promotion;
   any residual cosmetic-diff normalization queued from this cycle's BACKLOG.

## Status

Cycle 2026-01-13 closed 2026-01-15. Both vaults carry template version 2026-01-13;
the propagation item is marked ALL VAULTS PROPAGATED. The next cycle opens with the
skill-extraction discovery phase.
