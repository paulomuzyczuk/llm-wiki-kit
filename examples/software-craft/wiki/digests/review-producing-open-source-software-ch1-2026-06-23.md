---
title: Review — Producing Open Source Software Ch.1
aliases: []
source_tier: 1
topics: [software-craft, book-review, producing-open-source-software]
date: 2026-06-23
last_updated: 2026-06-23
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software, Ch.1 "Introduction"

## 1. Aggregate score

**8/8 scored checks PASS** — 0 WARN, 0 FAIL. Check 9 N/A (no protocol report yet — book
in progress). Synthesis strategy: full synthesis (foundational chapter).

## 2. Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density | PASS | Every H2/H3 with claims cited; `../../raw-input/` depth correct; all `#page` anchors + `p.N` tails machine-verified (offset −13). |
| 2 — Wikilink integrity | PASS | Live links resolve; `[[copyleft]]`, `[[open-source-licensing]]`, `[[organizations-and-money]]` are deliberate dead links; both pages have `## See also` + source-entity backlink. |
| 3 — Negative-space discipline | PASS | Labels used (foreshadowing, illustrative-scaffolding, conceptual-tool-not-concept) all in CLAUDE.md table; in log + page sections. |
| 4 — Stance preservation | PASS | "Not a panacea," packaging-skimping, "free" confusion all framed as mistakes/fallacies, not peer options. |
| 5 — Enrichment-not-replacement | PASS | Ch.1 created new pages only; no enrichment to verify. |
| 6 — Frontmatter completeness | PASS | All schema fields present; `last_updated: 2026-06-23`; valid topics/roles; `type: topic`. |
| 7 — Index & log consistency | PASS | Both pages in index; entity + meta ticked (✓ batch 2 / [x]); one `book-ingest` log entry. |
| 8 — Extraction quality | good | 3/3 forward spot-checks Match; reverse sweep clean (no silent omissions). Diagnostic — not scored. |
| 9 — Synthesis-strategy declaration | N/A SKIP | No `ingest-report-*` exists yet (book in progress). |
| 10 — Notation hygiene | PASS | No notation on either page; sub-checks N/A. |

## 3. WARNs and FAILs detail

None.

## 4. Extraction quality (Check 8)

**Pages:** `free-software-vs-open-source.md`, `open-source-culture.md`.

### Part A — Forward spot-checks

1. **"open source coined by Christine Peterson in 1998."**
   Source (PDF p.20 / printed 7): *"In 1998, the term open source was coined by Christine
   Peterson as an alternative to 'free'."* Wiki renders identically. **Match.** Anchor
   `#page=20`, p.7 confirmed.
2. **"governments are less suited… than for-profit corporations are, with non-profits
   somewhere in between."** Source (PDF p.15 / printed 2): near-verbatim. Wiki quotes it as
   a direct quotation. **Match.** Anchor `#page=15`, p.2 confirmed.
3. **GPL "a clever piece of legal judo."** Source (PDF p.17 / printed 4): *"The GNU General
   Public License (GPL) is a clever piece of legal judo."* Wiki quotes it. **Match.** Anchor
   `#page=17`, p.4 confirmed.

### Part B — Reverse omission sweep

| Source heading / caveat | Disposition | Detail |
|---|---|---|
| Intro (not-a-panacea, packaging, management, cultural navigation) | In wiki | `open-source-culture` — all four threads captured |
| History | In wiki | `free-software-vs-open-source` — compressed "why history matters" |
| The Rise of Proprietary Software and Free Software | In wiki | `free-software-vs-open-source` — "proprietary enclosure" bullet |
| Conscious Resistance (Stallman/GNU/GPL) | In wiki | `free-software-vs-open-source` — "conscious resistance" bullet |
| Accidental Resistance (BSD/X/TeX) | In wiki | `free-software-vs-open-source` — "accidental resistance" bullet |
| "Free" Versus "Open Source" | In wiki | `free-software-vs-open-source` — two-camps + ambiguity sections |
| The Situation Today | In wiki | `open-source-culture` (cohesion principle) + `free-vs-open-source` |
| GPL/copyleft license mechanics | Negative-space | `foreshadowing` → deferred to Ch.9 (dead wikilinks) |
| Zawinski "magic pixie dust" anecdote | Negative-space | `illustrative-scaffolding` |

Nothing substantive omitted.

### Part C — Overall rating

**good** — no mismatches, no unsourced derivations, no silent omissions.

## 5. Compression-ratio diagnostic

Omitted — no protocol report exists yet (book in progress).

## 6. Pages reviewed

- `wiki/topics/free-software-vs-open-source.md`
- `wiki/topics/open-source-culture.md`
- `wiki/entities/books/producing-open-source-software-book.md`
- `wiki/index.md`
- `wiki/log.md`
- Source: `raw-input/books/producing-open-source-software/producing-open-source-software.pdf` (PDF pp. 14–21)
