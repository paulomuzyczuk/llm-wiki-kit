---
title: Review — Producing Open Source Software Ch.3 (batch 5)
aliases: []
source_tier: 1
topics: [project-infrastructure, book-review, producing-open-source-software]
date: 2026-06-23
last_updated: 2026-06-23
type: digest
source_count: 0
status: active
---

# Review — Producing Open Source Software Ch.3 (batch 5)

Reviews the batch-5 slice of Chapter 3 "Technical Infrastructure" (PDF pp. 43–54 /
printed pp. 30–41), synthesised as **principles + decision criteria**. Chapter 3 is
intentionally partial (`[~]`): batch 1 covered §Version Control; batch 6 will cover
the Ch.3b remainder (bug tracker, real-time chat, wikis, translation, social
networking) and complete the chapter.

## Aggregate score

**8/8 applicable checks PASS, 0 WARN, 0 FAIL.** Check 9 N/A (no ingest-report yet —
book in progress); Check 5 N/A (no pages enriched this batch — all three created);
Check 10 PASS (no notation on any page); Check 8 diagnostic rating: **good**.

## Results table

| Check | Verdict | Note |
|---|---|---|
| 1 — Citation density | PASS | Every claim-bearing H2/H3 carries ≥1 inline citation; all 27 citations resolve at correct depth (`../../`), and every `#page` anchor + printed-page tail verified against the source. |
| 2 — Wikilink integrity | PASS | Links resolve or are deliberate dead links ([[bug-tracking]], [[real-time-chat]] — batch 6); each page has `## See Also` + a `[[producing-open-source-software-book]]` source-entity backlink. No concept pair conflated. |
| 3 — Negative-space discipline | PASS | Each page has a `## Negative Space` section; log entry lists 11 rejections, all using valid CLAUDE.md categories. |
| 4 — Stance preservation | PASS | Reply-to munging, over-requiring registration, and over-automation all framed as cautions/failure modes, not neutral peers. |
| 5 — Enrichment-not-replacement | N/A | All three pages are new; no pre-existing page was enriched. |
| 6 — Frontmatter completeness | PASS | All 11 schema fields present on each page; `roles: [tech-lead]`; `last_updated` = today; `type: topic`. |
| 7 — Index & log consistency | PASS | All 3 pages in `index.md` (new "Project infrastructure & tooling" group); entity + meta show Ch.3 ◑ batch 1,5; exactly one batch-5 `book-ingest` log entry. Ch.3 not marked complete — correct, chapter is mid-ingest. |
| 8 — Extraction quality | good | Diagnostic; see below. |
| 9 — Synthesis-strategy declaration | N/A | No `ingest-report-*` exists yet (book in progress). |
| 10 — Notation hygiene | PASS | CLAUDE.md opts in, but no page contains notation (Brooks'-Law "square of participants" is prose) → all sub-checks N/A. |

## Warns and fails detail

None.

## Extraction quality (Check 8)

**Forward spot-checks (4):**

1. *project-infrastructure* — "complexity of communications … increases as the
   square of the number of participants." Source PDF 43: "the complexity of
   communications in a project increases as the square of the number of
   participants." **Match** (#page=43, p. 30 confirmed).
2. *project-hosting* — "if you are not sure whether to use canned hosting, you
   should probably use canned hosting." Source PDF 46: "If you're not sure whether
   to use canned hosting, then you should probably use canned hosting." **Match**
   (#page=46, p. 33 confirmed).
3. *project-hosting* — "no evidence that the software-freedom of the hosting
   platform meaningfully affects a project's success." Source PDF 47: "I cannot say
   I've seen any evidence that the degree of software-freedom of the hosting
   platform has much effect on a project's success." **Match** (#page=47, p. 34
   confirmed).
4. *message-forums* — "Spam prevention is mandatory … submerged in junk." Source
   PDF 49: "A mailing list that takes no spam prevention measures at all will
   quickly be submerged in junk emails … Spam prevention is mandatory." **Match**
   (#page=49, p. 36 confirmed).

No ASCII figures reproduced.

**Reverse omission sweep (PDF pp. 43–54):**

| Source heading / caveat | Disposition | Detail |
|---|---|---|
| Ch.3 intro (info management, Brooks' Law) | In wiki | [[project-infrastructure]] §Information Management as the Antidote to Brooks' Law |
| Beware over-automation (closing caveat) | In wiki | [[project-infrastructure]] §Beware Over-Automation |
| What a Project Needs | In wiki | [[project-infrastructure]] §What a Project Needs |
| Web Site | In wiki | [[project-infrastructure]] §The Web Site |
| Canned Hosting | In wiki | [[project-hosting]] §The Trade-off |
| Choosing a Canned Hosting Site | In wiki | [[project-hosting]] §The Default Decision |
| Hosting on Fully Open Source Infrastructure | In wiki | [[project-hosting]] §Hosting on Fully Open-Source Infrastructure |
| Anonymity and Involvement | In wiki | [[project-hosting]] §Anonymity and the Involvement Bar |
| Message Forums / Mailing Lists | In wiki | [[message-forums]] (intro + §When a Project Needs Dedicated Forums) |
| Choosing the Right Forum Management Software | In wiki | [[message-forums]] §Choosing Forum Software |
| Spam Prevention (incl. Filtering posts) | In wiki | [[message-forums]] §Spam Prevention Is Mandatory |
| Use the Moderation Channel Only for Moderation | In wiki | [[message-forums]] §Spam Prevention (moderation-only paragraph) |
| Identification and Header Management | Negative-space | header-management mechanics (`too-granular`) |
| The Great Reply-to Debate | In wiki | [[message-forums]] §A Governance Lesson (captured as principle; mechanics rejected) |
| Two Fantasies | Negative-space | Reply-to mechanics & speculative features (`too-granular`) |
| Archiving | In wiki | [[message-forums]] §Archiving: Criteria for an Archiver |
| Mailing List / Message Forum Software | Negative-space | named software (`tool-specific/perishable`) |

Nothing substantive omitted: every source heading is either captured in a wiki page
or dispositioned as negative space with a valid category.

## Compression-ratio diagnostic

Omitted — no protocol report exists yet (book in progress).

## Pages reviewed

- `wiki/topics/project-infrastructure.md` (created)
- `wiki/topics/project-hosting.md` (created)
- `wiki/topics/message-forums.md` (created)
- `wiki/entities/books/producing-open-source-software-book.md`
- `wiki/index.md`
- `wiki/log.md`
- `raw-input/books/producing-open-source-software/meta.md`
