---
title: Review — Producing Open Source Software Ch.6 (batch 10)
aliases: []
source_tier: 1
topics: [software-craft, book-review, producing-open-source-software]
date: 2026-06-24
last_updated: 2026-06-24
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software Ch.6 (batch 10 [6a])

Chapter 6 "Communications" first half (§Written Culture, §Avoiding Common Pitfalls,
§Difficult People), PDF pp. 107–118 (printed pp. 94–105). Full synthesis. Three new pages:
[[written-communication]], [[facilitating-online-discussion]], [[difficult-people]].
Ch.6 continues in batch 11 (6b), so the chapter remains intermediate `[ ]` in meta.md and
`◐ batch 10 (6a)` in the entity index — the same mid-chapter state used for Ch.5 across
batches 7–8.

## 1. Aggregate score

**8/8 applicable PASS, 0 WARN, 0 FAIL.** Check 5 N/A (no enrichment — all three pages new);
Check 9 N/A (book in progress, no ingest report yet); Check 10 PASS (no notation on any page).

## 2. Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density | PASS | Every H2/H3 with original claims carries a PDF-page + printed-page citation; all 12 distinct `#page` anchors verified against the source via distinctive-word grep; tails follow the documented PDF−13 offset; paths use the correct `../../raw-input/` topics-depth prefix. |
| 2 — Wikilink integrity | PASS | All 10 wikilink targets resolve; each page has a `## See also`; reciprocal links bridge the three pages; each carries the `**Source entities:** [[producing-open-source-software-book]]` backlink. |
| 3 — Negative-space discipline | PASS | Each page has a `## Negative Space`; log entry lists 12 rejections, all with valid CLAUDE.md categories. |
| 4 — Stance preservation | PASS | Anti-patterns (holy wars, bikeshedding, noisy-minority, hyperbole, fantastical handles, obstructionism) all framed as foils/pitfalls, not peer options. |
| 5 — Enrichment-not-replacement | N/A | No pre-existing page was enriched this batch. |
| 6 — Frontmatter completeness | PASS | All declared fields present on all three pages; `topics:` resolve to authority subjects; `roles: [tech-lead]`; `last_updated: 2026-06-24`. |
| 7 — Index/log consistency | PASS | Three index entries added under "Open-source communication & conflict"; one `book-ingest` log entry; entity + meta reflect batch-10 (6a) progress (partial, per the multi-batch precedent). |
| 8 — Extraction quality | good | 3 forward spot-checks all Match; reverse sweep covers every source heading; no silent omissions after two thread caveats were folded in. |
| 9 — Synthesis-strategy declaration | N/A | No ingest report yet (book in progress). |
| 10 — Notation hygiene | PASS | No page contains notation (no math markers, no formal logic, no pseudocode). |

## 3. WARNs and FAILs detail

None.

## 4. Extraction quality (Check 8)

### Part A — Forward spot-checks

| # | Wiki claim | Source sentence (PDF p.) | Verdict |
|---|---|---|---|
| 1 | "writing clearly… in the long run it may matter more than programming talent" ([[written-communication]]) | "The ability to write clearly is one of the most important skills… In the long run it may matter more than programming talent." (PDF 107 / p. 94) | Match |
| 2 | Bikeshed Effect = Parkinson's Law; board approves an atomic plant near-instantly but argues endlessly over a bike shed ([[facilitating-online-discussion]]) | "…get approval for building a multi-million or even billion dollar atomic power plant, but if you want to build a bike shed you will be tangled up in endless discussions." (PDF 115 / p. 102) | Match |
| 3 | Difficult behavior "is usually not conscious" ([[difficult-people]]) | "People generally do not do it consciously. No one wakes up in the morning and says…" (PDF 117 / p. 104) | Match |

Anchors for all three spot-checked claims confirmed (`#page` and printed tail). No ASCII
figures reproduced (the chapter has none).

### Part B — Reverse omission sweep

| Source heading / caveat | Disposition | Detail |
|---|---|---|
| Ch.6 intro (communications revolve around the written word) | In wiki | [[written-communication]] intro |
| Written Culture (intro: clarity, empathy, notice when a medium stops scaling) | In wiki | [[written-communication]] intro |
| You Are What You Write | In wiki | [[written-communication]] §You Are What You Write |
| Structure and Formatting | In wiki | §Structure and Formatting (email conventions as principles) |
| Content | In wiki | §Content (reader-to-writer ratio, hyperbole, edit twice) |
| Tone | In wiki | §Tone, and the Role of Feelings |
| Recognizing Rudeness | In wiki | §Recognizing Rudeness |
| Face | In wiki | §Face: Your Screen Name as an Online Identity |
| Avoiding Common Pitfalls (intro) | In wiki | [[facilitating-online-discussion]] intro |
| Don't Post Without a Purpose | In wiki | §Don't Post Without a Purpose |
| Productive vs Unproductive Threads | In wiki | §Productive vs. Unproductive Threads (both caveats folded in) |
| The Smaller the Topic, the Longer the Debate | In wiki | §The Bikeshed Effect |
| Avoid Holy Wars | In wiki | §Avoid Holy Wars |
| The "Noisy Minority" Effect | In wiki | §The "Noisy Minority" Effect |
| Don't Bash Competing Open Source Products | In wiki | §Don't Bash Competing Open Source Products |
| Difficult People | In wiki | [[difficult-people]] intro + §The Pattern |
| Handling Difficult People | In wiki | §Understanding the Mentality + §The Handling Strategy |
| Case study (Subversion "Energy Sink") | Negative-space | `case-study-specifics` — method captured, specifics rejected |
| Caveat: "unproductive thread ≠ waste of time" | In wiki | folded into §Productive vs. Unproductive Threads |
| Caveat: "be wary of quashing threads prematurely" | In wiki | folded into §Productive vs. Unproductive Threads |
| Caveat: "not group therapist" (Tone) | In wiki | captured in §Tone |
| Aside: "never a right side in a holy war? sometimes there is" (humor) | Negative-space (implicit) | `illustrative-scaffolding` — authorial aside, not load-bearing |

Nothing substantive omitted.

### Part C — Overall rating

**good** — no mismatches, no unsourced derivations, no silent omissions.

## 5. Compression-ratio diagnostic

Omitted — no ingest report exists yet (book in progress).

## 6. Pages reviewed

- `wiki/topics/written-communication.md` (new)
- `wiki/topics/facilitating-online-discussion.md` (new)
- `wiki/topics/difficult-people.md` (new)
- `wiki/entities/books/producing-open-source-software-book.md`
- `wiki/index.md`
- `wiki/log.md`
- `raw-input/books/producing-open-source-software/meta.md`
- `raw-input/books/producing-open-source-software/producing-open-source-software.pdf` (pp. 107–118, spot-checks + reverse sweep)
