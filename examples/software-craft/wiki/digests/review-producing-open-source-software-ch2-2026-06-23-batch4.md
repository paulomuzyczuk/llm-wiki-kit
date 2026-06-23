---
title: Review — Producing Open Source Software Ch.2 (batch 4)
aliases: []
source_tier: 1
topics: [open-source-culture, book-review, producing-open-source-software]
date: 2026-06-23
last_updated: 2026-06-23
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software, Ch.2 "Getting Started" (batch 4)

Reviews the batch-4 slice of Chapter 2 (§Setting the Tone, §Be Open From Day One,
§Opening a Formerly Closed Project, §Announcing; PDF pp. 34–42, printed pp. 21–29).
Earlier Ch.2 slices (§Code Review, batch 1; §Starting From What You Have + §Choosing a
License, batch 3) were reviewed in their own batches; this review covers only the
batch-4 pages.

## 1. Aggregate score

**8/8 applicable checks PASS, 0 WARN, 0 FAIL.** Check 9 N/A (no ingest-report yet — book
in progress). Check 10 fires (vault opts into notation hygiene) but is PASS — no page in
this batch contains notation. Check 8 is diagnostic (unscored): **good**.

## 2. Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density | PASS | Every H2/H3 with original claims cited; all anchors PDF-verified; 6 anchors were corrected at pre-commit (off-by-one page-overflow) before review. |
| 2 — Wikilink integrity | PASS | All links resolve or are deliberate dead links ([[communications]] = Ch.6). Pair-and-split honoured (setting-the-tone ↔ developing-in-the-open). Source-entity backlink present on all three pages. |
| 3 — Negative-space discipline | PASS | 11 rejection items logged, all with valid CLAUDE.md categories. |
| 4 — Stance preservation | PASS | Private decisions, flame wars, siege mentality, CoC misuse all framed as foils/dangers, not peer options. |
| 5 — Enrichment-not-replacement | PASS | launching-an-open-source-project: prior content + citations intact; Announcing added as new H2. |
| 6 — Frontmatter completeness | PASS | All schema fields present on both new pages; roles on topic pages; last_updated = 2026-06-23. |
| 7 — Index & log consistency | PASS | Both new pages in index.md; Ch.2 ticked in meta.md and book entity; exactly one batch-4 ch.2 log entry. |
| 8 — Extraction quality | good (diagnostic) | 4/4 forward spot-checks Match; reverse sweep finds no silent omissions. |
| 9 — Synthesis-strategy declaration | N/A | No ingest-report-*.md yet (book in progress). |
| 10 — Notation hygiene | PASS | Vault opts in; no notation on any batch-4 page → all sub-checks N/A. |

## 3. WARNs and FAILs detail

None.

## 4. Extraction quality (Check 8)

**Part A — forward spot-checks (4):**

| # | Wiki claim | Source (PDF p.) | Verdict |
|---|---|---|---|
| 1 | "You open source your code, not your time" (developing-in-the-open) | p.39: "You open source your code, not your time." | Match |
| 2 | Mozilla launched without running code (launching) | p.42: "the Mozilla project was also launched without running code" | Match |
| 3 | Private decisions = "spraying contributor repellent" (setting-the-tone) | p.35: "like spraying contributor repellent on your project" | Match |
| 4 | Contributor Covenant is the most popular CoC (setting-the-tone) | p.36: "The most popular one is probably the one at …contributor-covenant.org" | Match |

Each spot-check's `#page` anchor and `, p. N` tail were re-confirmed at the source (Check 1
method). No figures reproduced as ASCII (chapter contains none).

**Part B — reverse omission sweep (PDF pp. 34–42):**

| Source heading / caveat | Disposition | Detail |
|---|---|---|
| Setting the Tone (intro) | In wiki | [[setting-the-tone]] — culture transmitted, set precedents early |
| Avoid Private Discussions | In wiki | [[setting-the-tone]] — public-by-default norm |
| Nip Rudeness in the Bud | In wiki | [[setting-the-tone]] — zero-tolerance ≠ technical enforcement; Nice Police |
| Codes of Conduct | In wiki | [[setting-the-tone]] — Contributor Covenant, leadership enforces, CCoC/OCoC |
| Practice Conspicuous Code Review | In wiki | [[code-review]] (ingested batch 1 from these same pages) — logged as convergence-miss |
| Be Open From Day One | In wiki | [[developing-in-the-open]] — incompatible-choice accumulation |
| Waiting Just Creates an Exposure Event | In wiki | [[developing-in-the-open]] — exposure event vs. continuous low-rate |
| Opening a Formerly Closed Project | In wiki | [[developing-in-the-open]] — siege mentality, prevention |
| Announcing | In wiki | [[launching-an-open-source-project]] (enriched) — forums, running-code, seed |
| Caveat: "open your code, not your time" | In wiki | developing-in-the-open §Openness is about artifacts |
| Caveat: running code no longer a precondition | In wiki | launching §Running code is no longer a precondition |
| Caveat: disagreeing with a CoC ≠ violating it | In wiki | setting-the-tone §Codes of conduct |

Nothing substantive omitted.

**Part C — overall rating:** good (no mismatches, no unsourced derivations, no silent
omissions).

## 5. Compression-ratio diagnostic

Omitted — no ingest-report exists yet (book in progress).

## 6. Pages reviewed

- `wiki/topics/setting-the-tone.md` (new)
- `wiki/topics/developing-in-the-open.md` (new)
- `wiki/topics/launching-an-open-source-project.md` (enriched — Announcing)
- `wiki/entities/books/producing-open-source-software-book.md`
- `wiki/index.md`, `wiki/log.md`, `raw-input/books/producing-open-source-software/meta.md`
- Source: `producing-open-source-software.pdf` pp. 34–42 (spot-checks + omission sweep)
