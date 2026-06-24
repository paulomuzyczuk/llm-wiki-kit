---
title: Review — Producing Open Source Software Ch.9 (batch 16 [9a])
aliases: []
source_tier: 1
topics: [software-craft, book-review, producing-open-source-software]
date: 2026-06-24
last_updated: 2026-06-24
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software, Ch.9 "Legal Matters" (batch 16 [9a])

Batch 16 opens Chapter 9 with its first half (PDF pp. 171–178; printed pp. 158–165):
Terminology, Aspects of Licenses, The GPL and License Compatibility, Choosing a License, and
The GNU GPL (incl. AGPL, "or any later version", The Copyright Holder Is Special, Is the GPL
Free or Not Free?). Strategy: **principles + decision criteria** (reference-catalog chapter —
no per-license mechanics pages). Ch.9 remains ⏳ partial; batch 17 [9b] completes it.

## Aggregate score

**9/9 applicable PASS, 0 warn, 0 fail.** Check 8 diagnostic = good. Check 9 N/A (book in
progress — no ingest report yet). Check 10 PASS (no notation on any reviewed page). One WARN
was found during the reverse-omission sweep and **fixed before this digest** (the "not legal
advice" caveat — see below), so the final state carries 0 unresolved warns.

## Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density | PASS | Every H2/H3 with original claims carries a citation; all paths use the `wiki/topics/` `../../` depth; all anchors (171–178) + tails verified vs PDF footers (printed=PDF−13). |
| 2 — Wikilink integrity | PASS | All targets resolve; pair-and-split [[copyleft]]↔[[permissive-licensing]] reciprocal; every page has ## See also + the `[[producing-open-source-software-book]]` source-entity backlink. |
| 3 — Negative-space discipline | PASS | Per-page ## Negative Space + log entry, all labels from the CLAUDE.md table. |
| 4 — Stance preservation | PASS | The GPL "less free" argument framed as a holy war to avoid; proprietary/closed-source framed as the foil to free, not a peer. |
| 5 — Enrichment-not-replacement | PASS | [[open-source-licensing]] (Ch.2 anchors 32/33 intact) and [[free-software-vs-open-source]] (Ch.1 anchors 16–21 intact) gained new H2 sections; no prior citation removed. |
| 6 — Frontmatter completeness | PASS | All schema fields present on 3 new + 2 enriched pages; `last_updated: 2026-06-24`; `topics:` resolve to seeded subjects; `roles: [tech-lead]`. |
| 7 — Index & log consistency | PASS | 3 new index entries; book entity + meta.md annotated (Ch.9 ⏳ partial — completion deferred to batch 17 per multi-batch convention); exactly one book-ingest log entry. |
| 8 — Extraction quality | good (diagnostic) | 3/3 forward spot-checks Match; reverse sweep clean after 1 caveat folded in. |
| 9 — Synthesis-strategy declaration | N/A — SKIP | No ingest report yet (book in progress). |
| 10 — Notation hygiene | PASS | Vault opts into notation hygiene, but no reviewed page contains notation → all sub-checks N/A. |

## Warns and fails detail

- **WARN (found + fixed) — silent omission of a framework-qualifying caveat.** Fogel's
  chapter-opening disclaimer — "I am not a lawyer, and … nothing in this book should be
  construed as formal legal advice" (PDF 171, p.158) — was absent from the licensing pages and
  not logged as negative space. Because it qualifies *every* claim in a legal-matters chapter,
  it was added as a parenthetical caveat to [[open-source-licensing]]'s intro, cited at
  #page=171, p.158. Re-verified present; no remaining unresolved warns.

## Extraction quality (Check 8)

**Part A — forward spot-checks (3/3 Match):**

1. **[[copyleft]]** — "the GPL makes freedom contagious" + the two requirements. Source (PDF
   175, p.162): *"Through these two conditions, the GPL makes freedom contagious."* Wiki renders
   the two numbered requirements then this conclusion. **Match** (anchor 175/p.162 confirmed).
2. **[[permissive-licensing]]** — MIT's GPL-compatibility. Source (PDF 176, p.163): *"the MIT
   license is fully compatible with all versions of the GNU General Public License."* Wiki quotes
   it as MIT's third advantage. **Match** (anchor 176/p.163 confirmed).
3. **[[license-compatibility]]** — what DFSG certifies. Source (PDF 172, p.159): *"it guarantees
   all the important freedoms (such as forkability even against the original author's wishes)."*
   Wiki quotes it verbatim, linking [[forkability]]. **Match** (anchor 172/p.159 confirmed).

**Part B — reverse omission sweep:**

| Source heading / caveat | Disposition | Detail |
|---|---|---|
| Ch.9 intro — "not a lawyer / not legal advice" | In wiki (fixed during review) | Added to [[open-source-licensing]] intro (was the one WARN). |
| Terminology — free software | In wiki | [[open-source-licensing]] §terminology; [[free-software-vs-open-source]]. |
| Terminology — open source software | In wiki | [[free-software-vs-open-source]] (OSI as "marketing program"); cross-ref. |
| Terminology — FOSS / F/OSS / FLOSS | In wiki | [[open-source-licensing]] §terminology (all mean the same thing). |
| Terminology — DFSG-compliant | In wiki | [[license-compatibility]] §certification tests. |
| Terminology — OSI-approved | In wiki | [[license-compatibility]] §certification tests. |
| Terminology — proprietary / closed-source; commercial≠proprietary | In wiki | [[open-source-licensing]] §terminology. |
| Terminology — public domain | In wiki | [[open-source-licensing]] §terminology (public domain vs. a license). |
| Terminology — reciprocal / copyleft | In wiki | [[copyleft]]. |
| Terminology — non-reciprocal / permissive | In wiki | [[permissive-licensing]]. |
| "Free Software and Open Source Are the Same Licenses" (copyleft≠free-only myth) | Subsumed-by | [[open-source-licensing]] §same-set + both license-family pages framed as free/open. |
| Aspects — compatibility w/ proprietary | In wiki | [[open-source-licensing]] §aspects; [[copyleft]]/[[permissive-licensing]]. |
| Aspects — compatibility w/ other free licenses | In wiki | [[license-compatibility]]. |
| Aspects — attribution requirements | In wiki | [[open-source-licensing]] §aspects; [[permissive-licensing]]. |
| Aspects — protection of trademark | In wiki (flagged → 9b) | [[open-source-licensing]] §aspects ("a type of attribution"); full treatment batch 17. |
| Aspects — patent snapback | In wiki (flagged → 9b) | [[open-source-licensing]] §aspects; [[permissive-licensing]] (Apache 2.0); full treatment batch 17. |
| The GPL and License Compatibility | In wiki | [[copyleft]] (two requirements, contagious) + [[license-compatibility]]. |
| Choosing a License | In wiki | [[open-source-licensing]] §choosing (use an existing well-recognized license + the 8-license list). |
| The GNU GPL — when to choose; LGPL for libraries | In wiki | [[copyleft]] §tuning reciprocity; [[open-source-licensing]] §choosing. |
| "or any later version" option | In wiki | [[open-source-licensing]] §choosing; copyleft negative-spaces it (subsumed-by). |
| The GNU Affero GPL | In wiki | [[copyleft]] §AGPL; [[license-compatibility]] (AGPL/GPL-2.0 note). |
| The Copyright Holder Is Special | In wiki | [[copyleft]] §copyright holder special (→ forward ref to 9b relicensing). |
| Is the GPL Free or Not Free? | In wiki | [[copyleft]] §holy war. |

Nothing substantive omitted after the "not legal advice" caveat was folded in.

**Part C — overall rating: good.**

## Pages reviewed

- `wiki/topics/copyleft.md` (new)
- `wiki/topics/permissive-licensing.md` (new)
- `wiki/topics/license-compatibility.md` (new)
- `wiki/topics/open-source-licensing.md` (enriched)
- `wiki/topics/free-software-vs-open-source.md` (enriched — fidelity update)
- `wiki/entities/books/producing-open-source-software-book.md`
- `wiki/index.md`, `wiki/log.md`, `wiki/topics-authority.md`, `raw-input/books/producing-open-source-software/meta.md`
