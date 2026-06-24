# Architecture — how a vault is built

This document describes the *structure* of an LLM-Wiki vault: the contract that
governs it, the fleet model it lives in, the shape of a page, and the mechanisms
(source tiers, roles, controlled vocabulary, negative space, sanctioned divergence)
that keep a growing collection consistent. For the *reasoning* behind these choices,
see [theory.md](theory.md); for how content actually flows into a vault, see
[pipeline.md](pipeline.md).

## The contract and the template

Every vault is governed by a single `CLAUDE.md` **contract** at its root,
instantiated from [`CLAUDE.template.md`](../CLAUDE.template.md). The template is the
source of truth; a vault's `CLAUDE.md` is produced from it by substituting a small set
of `{{PLACEHOLDER}}` tokens (domain name, file-naming prefix, the execution-handoff
record type, etc.) and filling in a few vault-specific regions. `new-vault.sh` does
this substitution and builds the folder tree; a freshly scaffolded vault passes
`check-conformance.py` with exit 0.

The contract is not documentation *about* the vault — it is the operating instruction
the LLM reads on every session. It defines the page schema, the citation format, the
role taxonomy, the negative-space vocabulary, the pipeline, and the commit discipline.
Putting all of this in one machine-read file is what lets the rules be *enforced*
rather than merely hoped for.

## One template, many vaults — the fleet

A single template backs a **fleet** of domain vaults (e.g. business-analytics, design,
software-craft). They all share the same contract and are kept consistent by tooling:

- **`check-conformance.py`** performs a mechanical template-vs-vault diff. Any
  difference *outside* the sanctioned regions (below) is a defect.
- **`vault-lint`** runs a per-vault health sweep (citations, orphans, cross-references,
  duplicates, stale claims, vocabulary, role-count drift).
- **`VAULTS.md`** is the fleet registry, mapping intake prefixes to vault paths.

The payoff of the fleet model is that improvements to the template and the tooling
propagate to every vault, and every vault is held to the same standard.

### Sanctioned divergence regions

A vault's `CLAUDE.md` is expected to be a byte-for-byte substitution of the template
*except* in a fixed, enumerated set of regions (the roles table, the optional
out-of-scope parenthetical, the notation/extension blocks, the lint config, and a
handful of others). The conformance checker knows these regions and ignores
differences inside them while flagging differences anywhere else. This inverts the
usual problem: instead of hoping a vault hasn't drifted, **any unsanctioned drift is a
detectable, mechanical failure.**

## Directory structure

A vault separates immutable source material from synthesized knowledge:

- **`raw-input/`** — the original sources (`books/`, `papers/`), treated as
  **immutable**. Nothing here is edited after ingest; it is the ground truth citations
  point back to.
- **`wiki/`** — the synthesized layer:
  - `topics/` — the knowledge pages.
  - `entities/` — pages for the works themselves (e.g. `…-book.md`), which serve as
    citation collocation points.
  - `digests/` — process/QA records (review verdicts, lint reports).
  - `index.md` — the retrieval surface (see Navigation below).
  - `log.md` — the running activity record.
  - `gaps.md` — knowledge gaps and not-yet-ingested sources, recorded explicitly.
  - `topics-authority.md` — the controlled-vocabulary source of truth.

## The page schema

Every wiki page opens with YAML frontmatter. The load-bearing fields:

| Field | Meaning |
|---|---|
| `type` | `topic` (knowledge page), `digest` (process/QA record), `authority` (governance/vocabulary), or an entity page. |
| `topics:` | What the page is *about* — subject tags, governed by the controlled vocabulary. |
| `roles:` | *Who* reaches for the page at work (see below). |
| `source_tier:` | The epistemic weight of the page's sources (see below). |
| `status:` | `active`, `stub`, or `archived`. |
| `aliases:`, `date`, `last_updated`, `source_count`, `project` | Identity and provenance metadata. |

Topic pages aim for **2,000–5,000 tokens**; pages over ~8,000 are candidates for
splitting or aggressive negative-space review (cross-source convergence pages may
legitimately exceed this if flagged).

### Source tiers

`source_tier` records how much epistemic weight a page's sources carry (tier 1 =
strongest, tier 3 = weakest). The rule that matters: **a page drawing on multiple
tiers takes the *lowest* tier present.** One tier-3 source among five tier-1 sources
makes the page tier 3. This deliberately makes the *weakest* source visible rather
than the strongest — the opposite of cherry-picking.

### Roles vs. topics

`topics:` and `roles:` are orthogonal axes. `topics:` answers *what is this about*;
`roles:` answers *who reaches for this page at work*. The assignment rule is purpose,
not incidental relevance: a role is assigned when the page's primary value is for
someone in that working context. Every topic page carries **at least one** role; a
page accumulating **four or more** roles is signalling a definition problem (it's
probably trying to be several pages). Role maps-of-content in the index turn this
field into a browsable, persona-scoped reading layer. (Digests and authority files are
process records, not pages reached for at work, so they carry no `roles:`.)

### Controlled vocabulary

`topics:` and `aliases:` are governed by a per-vault **controlled vocabulary** in
`wiki/topics-authority.md`, structured as a lightweight thesaurus — a preferred term
plus the "use-for" variants that must resolve to it — in two tiers: **subjects** (which
govern `topics:`) and **concept aliases**. The governing rule is **resolve before
minting**: before introducing a new `topics:` value or alias, resolve the candidate
against the authority file first and reuse an existing preferred term rather than
spawn a scattered variant. `vault-lint` resolves every `topics:`/`aliases:` value
against the authority file and suggests the nearest preferred term on a miss. A freshly
scaffolded vault ships an empty skeleton, seeded on first ingest (≤10 subjects, ≤30
aliases) and grown from there.

## Citations as surrogate records

Each claim carries a two-part citation — a `#page=N` anchor into the source PDF plus a
`p. M` printed-page tail — alongside a `**Source entities:** [[<slug>-book]]` link to
the work's own entity page. The two halves are grounded independently (one is the
*manifestation coordinate* in this particular file, the other the *edition-stable*
printed page), and the entity page is a location-independent name that survives files
moving or being reorganised. The full rationale — citations as catalogue **surrogate
records** serving *collocation* and stable *identity* — is in
[theory.md](theory.md#citations-are-surrogate-records-not-just-links).

## Negative space

Every page carries a `## Negative Space` section recording what was deliberately *not*
written up, each entry tagged from a fixed rejection vocabulary (`too-granular`,
`subsumed-by`, `out-of-scope`, `foil`, `source-underdeveloped`,
`illustrative-scaffolding`, …). Vault-wide gaps and not-yet-ingested sources live in
`gaps.md`. This converts an invisible editorial judgement into a reviewable one — the
archival discipline of **appraisal**, detailed in
[theory.md](theory.md#negative-space-is-recorded-not-silently-absent).

## Retention, not deletion

Pages are never deleted. A page that falls out of date is marked `status: archived`;
forward-referenced but undeveloped concepts are created as `status: stub` (a
one-sentence definition) and fleshed out when a source treats them fully. Combined with
the immutable `raw-input/`, this preserves the provenance trail — a reader can see not
only what the vault currently holds but how that belief changed. The reasoning (the
archival **records-continuum** model) is in
[theory.md](theory.md#nothing-is-deleted-stale-pages-are-archived).

## Navigation

`index.md` is the **retrieval surface**: pages grouped by *subject* (collocation), not
by the source or batch they arrived in. Above that flat list sits a **Navigation**
layer of curated role maps-of-content — one per role — that act as a browsable reading
list for a given working persona. This two-level structure (flat subject index +
curated role browse layer) is how a human or an LLM enters the vault and finds the
right pages without grepping blindly.
