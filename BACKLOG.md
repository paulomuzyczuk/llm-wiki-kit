<!--
EXAMPLE BACKLOG — illustrative only.

This file shows the shape of the fleet-level backlog the LLM-Wiki workflow keeps:
items that require a cross-vault or template-level decision, parked here when a
single audit session shouldn't resolve them alone. The entries below are
fictional and exist solely to demonstrate the format and the kinds of items that
land here. Replace wholesale when you adopt the convention.
-->
# llm-wiki-kit backlog

Items requiring fleet-level decisions or template evolution.
Vault-internal handoffs can point here when deferring items
that touch multiple vaults or the template itself.

## Active

### ✓ RESOLVED 2026-01-13: aliases field promotion to template
Discovered during a first-contact audit. The `aliases:` frontmatter field was in
use on production pages in some vaults but not declared in the template's schema.
Decision needed: promote to the template with a canonical form
(`aliases: [<alternate names>]`), then backfill the vaults whose schema lacked the
declaration. RESOLVED 2026-01-13: promoted to the template schema with the
convention note; propagated to all vaults the same cycle. ALL VAULTS PROPAGATED.

### ✓ RESOLVED 2026-01-13: roles-heading canonical form
Customized vaults failed the conformance tool's roles-heading anchor because the
heading text had drifted. Decision needed: normalize per-vault, loosen the tool's
anchor regex, or fix the heading fleet-wide. RESOLVED 2026-01-13: normalized all
vaults to the literal `**Roles for this vault:**` heading the tool anchors on.

### Enrichment-rules block — template-promotion candidate
A positive "enrich the existing page rather than create a duplicate" guidance
block appears inline in some vaults but only as a thin negative rule in the
template. Confirmed present in one vault; verify the others before promoting the
expanded form to the template. Lower urgency — functional coverage already exists
via the template's negative rule plus the book-review duplicate-concept check.

### Template filled-examples row missing for a domain
The template's filled-examples table documents several domains but not every one
in the active fleet. Add the missing row(s) so manual subs construction has a
worked reference for each domain. Target: next template version.

### Lint-section extraction — next similar-pattern candidate
The Lint procedure currently lives inline in each vault's `CLAUDE.md`, parallel to
the book-ingest procedure before it was extracted into a shared skill. A
lint-skill + stub split would save comparable per-vault space. Verify the Lint
content is template-identical across vaults before scoping the extraction.

### Citation grounding convention — design review
Open design question: the citation schema requires two-part grounding (a stable
anchor plus a human-page tail), and the human-page tail carries measurable rework
cost at review when it's derived rather than verified. Worth a deliberate
conversation about whether the second part earns its cost or should become
optional. Not blocking any current work.

## Closed

(empty)
