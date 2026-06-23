---
title: Review — Producing Open Source Software Ch.3 (batch 6)
aliases: []
source_tier: 1
topics: [project-infrastructure, book-review, producing-open-source-software]
date: 2026-06-23
last_updated: 2026-06-23
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software Ch.3 (batch 6)

Reviews the batch-6 contribution to Chapter 3 "Technical Infrastructure"
(PDF pp. 63–71 / printed pp. 50–58): the §Bug Tracker, §Real-Time Chat, §Wikis,
§Translation Infrastructure, and §Social Networking Services sections, synthesised
as principles + decision criteria. Batch 6 completes Chapter 3.

## 1. Aggregate score

**8/8 applicable checks PASS, 0 WARN, 0 FAIL.** Check 9 N/A (no ingest-report yet —
book in progress); Check 10 PASS (no notation on any reviewed page). Check 8 is
diagnostic (unscored): rating **good**.

## 2. Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density | PASS | Every claim-bearing H2/H3 carries a PDF-page + printed-page citation; all 9 distinct anchors (pp.63–71) verified against the source; depth `../../` correct for `wiki/topics/`. |
| 2 — Wikilink integrity | PASS | All wikilinks resolve (the prior [[bug-tracking]]/[[real-time-chat]] dead links are now live); every page has a See Also and a `**Source entities:**` backlink. i18n/l10n pair handled — see detail. |
| 3 — Negative-space discipline | PASS | Each page has a `## Negative Space`; the log entry lists 14 rejections, all using labels from the CLAUDE.md table. |
| 4 — Stance preservation | PASS | Foils framed as foils: no-anonymous-wiki-editing, avoid-Slack, the collaborative-editing-auto-quality fallacy, MediaWiki-not-recommended, short-tempered-ticket-closing tendency. |
| 5 — Enrichment-not-replacement | PASS | [[project-infrastructure]] gained a new H2 (Social Networking Services); all prior content and citations intact; a resolved forward-reference note updated, none removed. |
| 6 — Frontmatter completeness | PASS | All 11 schema fields present on the 4 new pages; `topics:` values all resolve to preferred subjects; `last_updated` = today; type = topic. |
| 7 — Index & log consistency | PASS | 4 new index entries; Ch.3 ticked in meta.md and marked ✓ in the book entity; exactly one batch-6 `book-ingest` log line. |
| 8 — Extraction quality | good (diagnostic) | 4/4 forward spot-checks Match; reverse sweep shows no silent omissions. |
| 9 — Synthesis-strategy declaration | N/A — SKIP | No `ingest-report-producing-open-source-software-*.md` yet; book in progress. |
| 10 — Notation hygiene | PASS | Vault opts into notation hygiene, but no reviewed page contains notation (i18n/l10n are abbreviations, not formal symbols). |

## 3. WARNs and FAILs detail

None.

**Note on Check 2 (i18n/l10n pair).** The §i18n/l10n source sidebar presents a
contrasting pair. They were captured as two clearly-separated, individually-defined
bullets on a single [[translation-infrastructure]] page rather than split into two
pages, and both terms are registered as page aliases (so each is independently
retrievable). Judged PASS, not a pair-and-split WARN: neither term is an
independently load-bearing concept in this reference-catalog chapter — they are
supporting terminology for the page's actual concept (when to adopt a translation
platform), and the i18n→l10n dependency is bridged in-page. Splitting a definitional
sidebar into two micro-pages would over-granulate against the chapter's declared
principles + decision-criteria strategy.

## 4. Extraction quality (Check 8)

### Part A — Forward spot-checks

1. **[[bug-tracking]] — reproduction as validation.** Source (PDF p.64): "the fact
   that someone besides the original filer was able to make it happen proves that it
   is genuine, and … confirms to the original filer that they've contributed."
   Wiki: "proves the bug is genuine and confirms to the original filer that their
   report mattered." **Match.** Anchor #page=64 / p.51 confirmed.
2. **[[real-time-chat]] — Slack.** Source (PDF p.67): "Slack hasn't been widely
   adopted by open source projects and I wouldn't recommend it for them." Wiki:
   "Fogel recommends against it for them." **Match.** Anchor #page=67 / p.54 confirmed.
3. **[[wikis]] — open-wiki spam.** Source (PDF p.69): "any open wiki other than
   Wikipedia will be covered completely with spam in approximately 3 milliseconds."
   Wiki quotes this verbatim. **Match.** Anchor #page=69 / p.56 confirmed.
4. **[[translation-infrastructure]] — i18n etymology.** Source (PDF p.70): "The '18'
   refers to the number of letters between the initial 'i' and … final 'n'." Wiki:
   "('18' = the letters between the initial *i* and final *n*)." **Match.** Anchor
   #page=70 / p.57 confirmed.

No ASCII figure reproductions.

### Part B — Reverse omission sweep

| Source heading / caveat (pp.63–71) | Disposition | Detail |
|---|---|---|
| Commit Notifications / Commit Emails (tail, p.63) | Negative-space | `subsumed-by` [[version-control]]/[[code-review]]; outside batch named scope |
| Bug Tracker | In wiki | [[bug-tracking]] |
| (ticket vs. behavior distinction) | In wiki | [[bug-tracking]] §Holds "Tickets" |
| (ticket life cycle + variations) | In wiki | [[bug-tracking]] §Life Cycle, §Handling the Common Variations |
| (tracker as public face / acknowledge) | In wiki | [[bug-tracking]] §Acknowledge Every Ticket |
| (technical features: email, identity, APIs) | In wiki | [[bug-tracking]] §Decision Criteria for Tracker Features |
| Interaction with Email | In wiki | [[bug-tracking]] §A Tracker Is Not the Development List |
| Pre-Filtering the Bug Tracker | In wiki | [[bug-tracking]] §Pre-Filtering |
| Real-Time Chat Systems | In wiki | [[real-time-chat]] intro |
| Chat Rooms and Growth | In wiki | [[real-time-chat]] §Rooms and Growth |
| Nick-Flagging and Notifications | In wiki | [[real-time-chat]] §Nick-Flagging |
| Paste Rooms and Paste Sites | In wiki | [[real-time-chat]] §Pastes Belong Out of Band |
| Chat Bots | In wiki | [[real-time-chat]] §Bots |
| Commit Notifications in Chat | In wiki | [[real-time-chat]] §Commit Notifications in Chat |
| Wikis | In wiki | [[wikis]] intro, §Collaborative Editing |
| Wikis and Spam | In wiki | [[wikis]] §Never Allow Anonymous Editing |
| Choosing a Wiki | In wiki | [[wikis]] §Choosing a Wiki |
| Translation Infrastructure | In wiki | [[translation-infrastructure]] §When to Use, §Choosing |
| i18n / l10n sidebar | In wiki | [[translation-infrastructure]] §i18n vs. l10n |
| Social Networking Services | In wiki | [[project-infrastructure]] §Social Networking Services |

Nothing substantive omitted.

### Part C — Overall rating

**good** — no mismatches, no unsourced derivations, no silent omissions.

## 5. Compression-ratio diagnostic

Omitted — no ingest-report exists yet (book in progress).

## 6. Pages reviewed

- `wiki/topics/bug-tracking.md` (created)
- `wiki/topics/real-time-chat.md` (created)
- `wiki/topics/wikis.md` (created)
- `wiki/topics/translation-infrastructure.md` (created)
- `wiki/topics/project-infrastructure.md` (enriched)
- `wiki/entities/books/producing-open-source-software-book.md`
- `wiki/index.md`, `wiki/log.md`, `raw-input/books/producing-open-source-software/meta.md`
- Source: `raw-input/books/producing-open-source-software/producing-open-source-software.pdf` pp. 63–71
