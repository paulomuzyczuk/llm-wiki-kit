---
title: Review — Producing Open Source Software Ch.4
aliases: []
source_tier: 1
topics: [software-craft, book-review, producing-open-source-software]
date: 2026-06-23
last_updated: 2026-06-23
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software, Ch.4 "Social and Political Infrastructure"

## 1. Aggregate score

**8/8 scored checks PASS** — 0 WARN, 0 FAIL. Check 9 N/A (no protocol report yet — book
in progress). Synthesis strategy: full synthesis.

> Re-review after fixing the one WARN found on the first pass (silent omission of "Polls
> Versus Votes"): the subsection is now captured in `open-source-governance` (Electorate
> section, `#page=77`, p.64). Sweep below is clean.

## 2. Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density | PASS | Every H2/H3/H4 with claims cited; `../../raw-input/` depth correct; all `#page`/`p.N` anchors machine-verified (offset −13), incl. the new polls sentence. |
| 2 — Wikilink integrity | PASS | Live links resolve; `[[forks]]` deliberate dead link; all pages have `## See also` + source-entity backlink. BD-vs-consensus kept as continuum sub-sections (see detail). |
| 3 — Negative-space discipline | PASS | Labels (tool-specific/perishable, too-granular ×3, illustrative-scaffolding) all valid. |
| 4 — Stance preservation | PASS | Voting-as-last-resort, veto abuse, "don't be comprehensive" framed as cautions/foils. |
| 5 — Enrichment-not-replacement | PASS | `version-control` gained a new H2 only; all prior Ch.3 citations + Sources line intact. |
| 6 — Frontmatter completeness | PASS | All schema fields present; `last_updated: 2026-06-23`; valid topics/roles. |
| 7 — Index & log consistency | PASS | Both new pages indexed, vc entry enriched; entity + meta ticked; one `book-ingest` log entry. |
| 8 — Extraction quality | good | 3/3 forward spot-checks Match; reverse sweep clean after fix. Diagnostic — not scored. |
| 9 — Synthesis-strategy declaration | N/A SKIP | No `ingest-report-*` exists yet (book in progress). |
| 10 — Notation hygiene | PASS | No notation on any page; sub-checks N/A. |

## 3. WARNs and FAILs detail

None remaining. (First-pass WARN — silent omission of "Polls Versus Votes" — resolved by
capturing it in `open-source-governance.md`'s Electorate section with citation `#page=77`,
p.64.)

### Note on Check 2 (pair-and-split)

Ch.4 presents *benevolent dictator* vs *consensus-based democracy*. These are kept as two
H3 sub-sections of a single `open-source-governance` page rather than split into separate
pages, because the source frames them explicitly as "two idealized extremes" on "a
continuum between them" — two ends of one governance axis, not two independently
load-bearing concepts. This mirrors the established vault precedent where
`version-control` holds "centralized vs. decentralized" as one section. Both models remain
independently retrievable via the page's registered aliases (`benevolent-dictator`,
`consensus-democracy`). Scored PASS, not a pair-and-split WARN.

## 4. Extraction quality (Check 8)

**Pages:** `open-source-governance.md`, `forkability.md`, `version-control.md` (enriched).

### Part A — Forward spot-checks

1. **"Replicability implies forkability, and forkability implies consensus."** Source
   (PDF p.72 / printed 59): verbatim. Wiki quotes it in `forkability`. **Match.** Anchor
   `#page=72`, p.59 confirmed.
2. **"approval voting… comprehensibility is an important factor."** Source (PDF p.75 /
   printed 62): *"A good choice in most cases is approval voting"* … *"comprehensibility
   is an important factor when choosing a voting method."* Wiki quotes both. **Match.**
   Anchor `#page=75`, p.62 confirmed.
3. **"-1 … comes from the Apache Software Foundation."** Source (PDF p.77 / printed 64):
   *"This usage originally comes from the Apache Software Foundation."* Wiki renders it.
   **Match.** Anchor `#page=77`, p.64 confirmed.

### Part B — Reverse omission sweep

| Source heading / caveat | Disposition | Detail |
|---|---|---|
| Forkability | In wiki | `forkability` |
| Benevolent Dictators | In wiki | `open-source-governance` (BD sub-section) |
| Who Can Be a Good Benevolent Dictator? | In wiki | `open-source-governance` (qualifications) |
| Consensus-based Democracy | In wiki | `open-source-governance` (evolutionarily-stable shift) |
| Version Control Means You Can Relax | In wiki | `version-control` (enriched H2) + `open-source-governance` |
| When Consensus Cannot Be Reached, Vote | In wiki | `open-source-governance` (voting mechanics) |
| Voting Systems (sidebar: Arrow's theorem) | Negative-space | `too-granular` (voting-system taxonomy) |
| When To Vote | In wiki | `open-source-governance` (voting as last resort) |
| Who Votes? | In wiki | `open-source-governance` (electorate / commit access) |
| Not All Maintainers Are Coders | In wiki | `open-source-governance` (maintainer ≠ coder) |
| Adding New Maintainers | In wiki | `open-source-governance` (secrecy appropriate) |
| Polls Versus Votes | In wiki | `open-source-governance` (Electorate section, #page=77 p.64) — captured on fix |
| Vetoes | In wiki | `open-source-governance` (veto / -1 / veto abuse) |
| Writing It All Down | In wiki | `open-source-governance` (describes-not-creates; CONTRIBUTING.md) |
| Linking To Emails (sidebar) | Negative-space | `too-granular` |
| Joining or Creating a Non-Profit Organization | In wiki | `open-source-governance` (umbrella org; legal/technical separation) |

Nothing substantive omitted.

### Part C — Overall rating

**good** — no mismatches, no unsourced derivations, no silent omissions (after fix).

## 5. Compression-ratio diagnostic

Omitted — no protocol report exists yet (book in progress).

## 6. Pages reviewed

- `wiki/topics/open-source-governance.md`
- `wiki/topics/forkability.md`
- `wiki/topics/version-control.md`
- `wiki/entities/books/producing-open-source-software-book.md`
- `wiki/index.md`
- `wiki/log.md`
- Source: `raw-input/books/producing-open-source-software/producing-open-source-software.pdf` (PDF pp. 72–79)
