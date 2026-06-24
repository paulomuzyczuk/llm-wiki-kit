---
title: Review — Producing Open Source Software Ch.6 (batch 11)
aliases: []
source_tier: 1
topics: [software-craft, book-review, producing-open-source-software]
date: 2026-06-24
last_updated: 2026-06-24
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software Ch.6 (batch 11 [6b])

Review of the second half of Chapter 6 "Communications" (§Handling Growth, §Choose the
Right Forum, §Cross-Link Between Forums, §Publicity, §Announcing Security Vulnerabilities),
PDF pp. 119–131 / printed pp. 106–118. Batch 11 completes Chapter 6.

## 1. Aggregate score

**8/8 applicable checks PASS — 0 WARN, 0 FAIL.** Check 8 is diagnostic-only (rated `good`);
Check 9 is N/A (book still in progress, no ingest report yet); Check 10 fires PASS
(no notation on any page).

## 2. Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density & anchor accuracy | PASS | Every H2/H3 with original claims cited; all 12 distinct `#page` anchors + printed-page tails verified against source (offset PDF − 13 confirmed by footers). |
| 2 — Wikilink integrity | PASS | All links resolve except `[[release-engineering]]` (deliberate dead link, Ch.7 pending). Pair-and-split reciprocal links present (`choosing-the-right-forum` ↔ `facilitating-online-discussion`). Source-entity backlink on all 4 pages. |
| 3 — Negative-space discipline | PASS | 14 items logged with valid CLAUDE.md categories; per-page `## Negative Space` on all 4 pages. |
| 4 — Stance preservation | PASS | Security "don't"s and forum anti-patterns framed as warnings, not peer options. |
| 5 — Enrichment-not-replacement | PASS | `facilitating-online-discussion` gained one reciprocal See-also link; all prior content/citations intact. |
| 6 — Frontmatter completeness | PASS | All schema fields present on 4 new pages; `last_updated` = today; topics resolve to authority subjects (`open-source-communication`, `software-security`). |
| 7 — Index & log consistency | PASS | 4 index entries added; Ch.6 ticked in meta.md + book entity; exactly one batch-11 book-ingest log entry. |
| 8 — Extraction quality | good | 3/3 forward spot-checks Match; reverse omission sweep clean (table below). |
| 9 — Synthesis-strategy declaration | N/A | No ingest-report yet (book in progress). |
| 10 — Notation hygiene | PASS | No notation on any batch-11 page (CVSS vector-string negative-spaced, not rendered). |

## 3. WARNs and FAILs detail

None.

## 4. Extraction quality (Check 8)

### Part A — Forward spot-checks

| # | Wiki claim | Source (PDF p.) | Source quote | Verdict |
|---|---|---|---|---|
| 1 | Subversion cut bogus filings by reformatting the tracker front page in "huge bold red letters" | p.123 | "would stand out in huge, bold red letters, on a bright yellow background … a noticeable drop in the rate of bogus ticket filings" | Match |
| 2 | Pre-notify each recipient individually, never the whole list and not via BCC | p.129 | "send them individually (one at a time) … Do not send to the entire list … Sending it to them all via blind CC (BCC) isn't a good solution either" | Match |
| 3 | Formal guidelines are statutory law; the archives are common law | p.121 | "If a project's formal guidelines are its statutory law, the archives are its common law" | Match |

### Part B — Reverse omission sweep

| Source heading / caveat | Disposition | Detail |
|---|---|---|
| Handling Growth | In wiki | [[scaling-project-communication]] §The Scalability Problem, §Strategy 1, §Strategy 2 |
| Conspicuous Use of Archives | In wiki | [[scaling-project-communication]] §Strategy 2 → Conspicuous Use of Archives |
| Treat All Resources Like Archives | In wiki | [[scaling-project-communication]] (five resource properties) |
| Codifying Tradition | In wiki | [[scaling-project-communication]] (acculturation burden, advertising space, canonical referral) |
| Choose the Right Forum | In wiki | [[choosing-the-right-forum]] §Match the Forum, §Convergent-vs-Divergent |
| Cross-Link Between Forums | In wiki | [[choosing-the-right-forum]] §Cross-Link, §Writer-Responsible Culture |
| Publicity | In wiki | [[open-source-publicity]] (internal-to-PR continuum) |
| Announcing Releases and Other Major Events | In wiki | [[open-source-publicity]] (channels, simultaneity, meant-to-be-quoted) |
| Announcing Security Vulnerabilities | In wiki | [[security-vulnerability-disclosure]] (openness-vs-secrecy, two guidelines) |
| Receive the Report | In wiki | [[security-vulnerability-disclosure]] §Receive the Report |
| Develop the Fix Quietly | In wiki | [[security-vulnerability-disclosure]] §Develop the Fix Quietly |
| CVE Numbers | In wiki | [[security-vulnerability-disclosure]] §Name and Score |
| CVSS Scores | In wiki | [[security-vulnerability-disclosure]] §Name and Score |
| Pre-Notification | In wiki | [[security-vulnerability-disclosure]] §Pre-Notification |
| Distribute the Fix Publicly | In wiki | [[security-vulnerability-disclosure]] §Distribute the Fix Publicly |
| Further Reading on Handling Security Vulnerabilities | Negative-space entry | `source-underdeveloped` (link list) |
| J. Random "Energy Sink" conclusion (top of p.119) | Negative-space entry | `case-study-specifics` (logged batch 10) |

Nothing substantive omitted.

### Part C — Overall rating

**good** — no mismatches, no unsourced derivations, no silent omissions.

## 5. Compression-ratio diagnostic

Omitted — no ingest-report exists yet (book in progress).

## 6. Pages reviewed

- `wiki/topics/scaling-project-communication.md` (created)
- `wiki/topics/choosing-the-right-forum.md` (created)
- `wiki/topics/open-source-publicity.md` (created)
- `wiki/topics/security-vulnerability-disclosure.md` (created)
- `wiki/topics/facilitating-online-discussion.md` (enriched — reciprocal pair-link)
- `wiki/entities/books/producing-open-source-software-book.md`
- `wiki/index.md`, `wiki/log.md`, `wiki/topics-authority.md`, `raw-input/books/producing-open-source-software/meta.md`
