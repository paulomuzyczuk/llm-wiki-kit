# Vault Schema — software craft Knowledge Wiki

This vault is a Karpathy-style LLM-maintained knowledge base for the software craft domain. You (Claude Code) are the maintainer. The human is the curator and questioner.

---

## Purpose

This vault exists for documentation only. Its job is to enrich the human's exchanges with Claude Code in the software craft domain by accumulating synthesised knowledge over time.

---

## Directory structure

> **Naming convention:** Top-level folder names are hyphenated — `raw-input/` rather than a space-separated form — because spaces in folder names create encoding friction in bash, markdown links, and launchd. The template commits to hyphenated folder names throughout.

- `raw-input/` — immutable source materials. Read-only for existing content; add new files only via intake/ingest. Never modify, never delete existing files.
  - `_pending/` — staging area. Intake and Obsidian Web Clipper write here; ingest empties it.
  - `articles/` — web-clipped articles (Obsidian Web Clipper).
  - `books/` — one subfolder per book, each containing the source PDF and a `meta.md` (title, author, edition/identifier, chapter->page map, ingest status). No per-chapter subfolders.
  - `coding-handoffs/` — raw outputs of coding sessions.
  - `notes/` — research, references, misc material the human writes.
  - `planning-handoffs/` — raw outputs (e.g. chat exports) of thinking/sparring sessions.

- `wiki/` — your domain.
  - `index.md` — catalogue of every wiki page with one-line summaries, organised by category.
  - `topics-authority.md` — controlled-vocabulary source of truth: the preferred `topics:` subject terms and the registered `aliases:`, each with their accepted variants (a lightweight thesaurus). `/vault-lint` resolves every `topics:`/`aliases:` value against it. Scaffolded as an unpopulated skeleton and seeded by the first ingest (see Conventions → *First-ingest seed*).
  - `log.md` — append-only chronological log of operations.
  - `gaps.md` — field-level open questions and missing source coverage tracker; two sections: §1 explicit knowledge gaps found in ingested content, §2 books not yet in the vault.
  - `handoffs/`
    - `coding-handoffs/` — one page per coding session (cross-referenced summary, not a copy of the raw handoff).
    - `planning-handoffs/` — one distillation page per thinking/sparring session.
  - `entities/` — pages about specific things, in two families. Subdirs are listed only when they exist; add a new subdir when a type is first created, not speculatively.
    - **Source entities** — one page per ingested source, one subdir per source type. Each page's filename carries a **type suffix** so its wikilink is self-describing and never collides with a concept page (and gives the source-entity-backlink lint check a deterministic source→entity mapping):
      - `books/` → `<slug>-book.md` — one overview page per book (chapter index, ingest progress, and the edition/identifier it was ingested from).
      - `papers/` → `<slug>-paper.md` — one page per scientific article.
      - `blog-posts/` → `<slug>-blog-post.md` — one page per blog post.
      - `whitepapers/` → `<slug>-whitepaper.md` — one page per whitepaper.
    - **Output entities** — subjects the vault produces from its own knowledge; no source suffix.
      - `projects/` — one page per item; the living synthesis of its state.
  - `topics/` — cross-source synthesis pages (concepts live here, including book concepts).
  - `digests/` — point-in-time summary artifacts for human review: scheduled-run
       outcomes (intake, ingest) and interactive review/completion reports
       (book-review verdicts, end-of-book ingest reports).
  - `quality-debt.md` — process-failure / quality-debt tracker — items the vault got wrong, distinct from `gaps.md`'s knowledge gaps.

- `claude/` — ops docs (scheduler setup and other operational references). Not read at runtime during normal operation.

---

## Boundary

This schema governs knowledge work only. It does not govern the domain's external working artifacts, which live at `~/projects/<name>/` and are the domain's source of truth. You may read from there to inform a wiki page; you never write to it from a vault session. (If the domain has no external working artifacts, this vault is simply documentation-only and nothing external is ever written.)

---

## Entity pages are living syntheses

A `projects` entity page reflects CURRENT state and trajectory. When a new coding-handoff arrives you REVISE the entity page to reflect the new state; you do not append the full handoff. This keeps it bounded. The per-session trail lives as discrete pages in `wiki/handoffs/coding-handoffs/`, plus the immutable raw records and `log.md`.

---

## File naming standard

Vault prefix: `sc-`. Every file the human drops into Downloads for intake must be named:

`sc-<subtype>-<descriptor>.md`

| Subtype | Pattern | Raw destination |
|---|---|---|
| coding-handoff | `sc-coding-handoff-<project>-<YYYY-MM-DD>.md` | `coding-handoffs/` |
| planning-handoff | `sc-planning-handoff-<topic>-<YYYY-MM-DD>.md` | `planning-handoffs/` |
| notes | `sc-notes-<topic>.md` | `notes/` |

Exempt from the prefix rule:
- Articles arrive via Obsidian Web Clipper into `raw-input/_pending/`, named by article title, tagged `clippings`.
- Books are added manually into `raw-input/books/<book-name>/` and ingested via the dedicated book-ingest operation, not through Downloads intake.

---

## Conventions

All wiki pages start with YAML frontmatter:

~~~yaml
---
title: <human-readable>
aliases: [<alternate names>]
date: <YYYY-MM-DD created>
last_updated: <YYYY-MM-DD>
type: entity | topic | coding-handoff | planning-handoff | book | paper | blog-post | whitepaper | digest | authority
topics: [<list of topic tags>]
roles: [<one or more role labels defined for this vault>]
source_tier: 1 | 2 | 3
project: <name or null>
source_count: <integer>
status: active | stub | archived
---
~~~

The `aliases:` field is an optional list of alternate names a page may be searched by. Use `[]` if none.

The `roles:` field is required on every topic page. It is orthogonal to `topics:` — `topics:` answers *what is this about*, `roles:` answers *who reaches for this page at work*. Assignment rule: assign a role when a page's primary value is for someone in that working context, not merely when the page is incidentally relevant. Every page gets at least one role; pages with 4+ roles signal a definition problem.

The `roles:` field is required on topic pages only; on `type: digest` artifacts it is optional, since digests are process/QA records, not knowledge pages reached for at work. `type: authority` files — controlled-vocabulary source-of-truth artifacts such as `topics-authority.md` — likewise carry **no** `roles:`, `source_tier:`, or `topics:`: they are governance records, not knowledge pages reached for at work, and the topic-page checks do not apply to them.

**Roles for this vault:**

| Role | Definition | Assign when… |
|---|---|---|
| `code-craftsperson` | Writing, reviewing, or improving code at module/class/function level | Page's primary value is a code-granularity decision: module structure, encapsulation, API surface, naming, comments, refactoring, or testing |
| `system-designer` | Structural decisions spanning components: architecture styles, coupling, topology | Page governs choices spanning multiple components or services: coupling metrics, architecture styles, fitness functions, distributed topology |
| `data-engineer` | Storage, replication, consistency, transactions, batch/stream processing | Page is primarily about data-system internals: storage mechanics, replication protocols, consistency/isolation models, partitioning, encoding |
| `security-engineer` | Threat modelling, authentication, cryptographic controls | Page's primary value is adversarial thinking, security control design, or security-specific system aspects (auth, crypto, identity) |
| `tech-lead` | Team practices, technical direction, stakeholder alignment, career | Page's primary value is for someone with organisational scope: team structure, negotiation, technical culture, professional growth |
| `product-engineer` | System behaviour from the user's perspective: reliability, scalability, end-to-end correctness, ethics | Page primarily concerns what users depend on the system to do correctly, or the ethical consequences of technical decisions |

The `source_tier:` field is required on every topic page. Source tiers define the epistemic weight of the sources a page draws from:
- tier-1: edited, peer-reviewed, or otherwise citable sources with stable page references (books, academic papers, official specifications, RFCs). Claims from these sources are treated as authoritative within the domain.
- tier-2: long-form articles, edited blog posts, conference talks with published slides. Claims are treated as well-reasoned but not peer-reviewed; prefer corroboration with a tier-1 source when available.
- tier-3: unedited spoken sources (podcast and YouTube transcripts), forum posts, informal notes. Claims require corroboration before being treated as authoritative; cite as "per [source], unverified" when no tier-1/2 corroboration exists.

A page drawing from multiple tiers carries the LOWEST tier present. A page with one tier-3 source and five tier-1 sources is source_tier: 3. This makes the weakest source visible, not the strongest.

Existing pages (synthesized from books only) are all source_tier: 1. The field is required on new pages; backfill existing pages lazily when they are next updated, not as a bulk pass.

**Source-identity fields (source-entity pages only).** Pages of `type: book | paper | blog-post | whitepaper` additionally record the bibliographic identity of the specific manifestation they describe, so every citation resolves against a known edition:
- `edition:` — the printing/edition actually ingested (e.g. `2nd ed., 2018`), or `null` for a single-version work with no edition statement.
- `isbn:` (books) / `doi:` (papers) — a stable external identifier when one exists; `null` otherwise.

This is what protects each `#page=N` anchor over time: if a different printing is ever ingested, the discriminator makes the manifestation explicit instead of letting page anchors silently drift from the `p. M` tail. These fields are optional and backfilled lazily on existing source entities when they are next updated, not as a bulk pass.

**Controlled vocabulary — `wiki/topics-authority.md`.** The `topics:` and `aliases:` fields are governed by a per-vault controlled vocabulary, structured as a lightweight thesaurus (a preferred term plus its "use-for" variants) in two tiers:
- **Subjects** (governs `topics:`) — the canonical broad subject categories, each listing the variant spellings/synonyms that must resolve to it. A `topics:` value must be a preferred subject, or a reserved non-subject tag such as `stub`.
- **Concepts** (governs `aliases:` / page identity) — each topic page is a preferred concept and its `aliases:` are use-for variants. No alias may belong to two pages, and no alias may shadow another page's canonical title/slug (those are the uniqueness guarantees the de-alias handling depends on).

`aliases:` are still authored in page frontmatter; `topics-authority.md` is the source of truth, and `/vault-lint`'s vocabulary check resolves every `topics:`/`aliases:` value against it (report-only, suggesting the nearest preferred term on a miss). **Resolve before minting:** before introducing a new `topics:` value or a new alias, resolve the candidate against `topics-authority.md` first — if it already resolves to a preferred term, reuse that term rather than create a scattered variant; only register a genuinely new term.

**First-ingest seed.** A freshly scaffolded vault ships an unpopulated skeleton `topics-authority.md` (marked `status: stub` with a `SEED-ME` comment). The **first ingest** into the vault — `book-planner` Phase 0 if a book is added first, otherwise the first article/notes ingest — seeds it with **up to 10 subject categories and up to 30 aliases** drawn from that first content and the domain, then sets `status: active` and removes the `SEED-ME` comment. The 10/30 caps apply to the **initial seed only**; the vocabulary grows from there under the resolve-before-minting rule, and `/vault-lint` reconciles scatter. A vault with no `topics-authority.md` at all skips the vocabulary check entirely.

Other conventions:

- Cross-references use Obsidian `[[wikilink]]` syntax.
- Citations to raw sources use relative paths. The source folder is `raw-input/` (no spaces, no `%20` encoding needed). Depth depends on the citing file's location: `wiki/topics/*.md` → `../../raw-input/`; `wiki/entities/books/*.md` → `../../../raw-input/`; `wiki/handoffs/**/*.md` → `../../raw-input/`.
- Book citations are **two-part**: a PDF-page anchor and a printed-page tail, each grounded independently in the source. Format: `([<Author> <YYYY>](../../raw-input/books/<slug>/<file>.pdf#page=N), p. N)` — en dash `–` for page ranges (`pp. N–M`). Every H2, H3, and H4 section containing original claims must carry its own inline citation; citation density is never deferred. Multiple sources for one claim: `([A 2010](…), p. N); ([B 2015](…), p. M)`.
  - From `wiki/topics/` (two levels up): `([<Author> <YYYY>](../../raw-input/books/<slug>/<file>.pdf#page=N), p. N)`
  - From `wiki/entities/books/` (three levels up): `([<Author> <YYYY>](../../../raw-input/books/<slug>/<file>.pdf#page=N), p. N)`
- **Two-part grounding.** The two halves of a citation are derived from the source independently — never computed from each other:
  - `#page=N` — the PDF page on which the cited sentence actually appears.
  - `, p. N` — the printed page **containing** the sentence (the block holding it), not the printed page that merely begins on PDF page N.
  Because a printed page overflows onto the next PDF page, the two values may legitimately differ. Do not infer the tail from a PDF→printed offset: the offset drifts within a chapter, and the tail must reflect the printed page of the block holding the sentence.
  - **Canonical locator.** `, p. M` (the printed page) is the canonical, edition-stable reference — it resolves in any copy of the same edition. `#page=N` is a resolver hint into one specific digitised manifestation (this PDF); across a different printing or edition it may drift while `p. M` does not. If the two ever conflict, trust `p. M` and re-derive `#page=N`. This is why the source entity records the edition it was ingested from (see Source-identity fields below).
- **Ground-truth precedence for the printed-page tail.** Derive the tail from, in order:
  1. The PDF's own printed page numbers, when the digitisation preserves them.
  2. Otherwise, for an EPUB-derived PDF that strips them, the EPUB `page0NNN` page-div containing the sentence (one div = one printed page). Maintain `raw-input/books/<slug>/printed-page-map.md` — a div → printed → PDF mapping — and derive every tail from it.
  3. If neither is available, record the tail as **unverifiable** rather than guessing.
- **Same author, same year.** When two cited works share an author and year, disambiguate them with a letter suffix on the year — `[Author 2004a]`, `[Author 2004b]` — assigned in order of first appearance on the page and used identically in the inline citation and the `## Sources` block. Each suffix maps to a distinct `[[<slug>-book]]` source entity.
- Page filenames in `kebab-case.md`.
- Topic page size: aim for 2,000–5,000 tokens per page. Pages exceeding 8,000 tokens are candidates for splitting or for aggressive negative-space review. Cross-book convergence pages may legitimately exceed this — flag them explicitly in frontmatter with a note explaining why.
- `log.md` entries use the format:
  `## [YYYY-MM-DD] <operation> | <topic-or-project> | <one-line summary>`
  where `<operation>` is one of: `intake`, `ingest`, `book-ingest`, `query`, `distil`, `lint`, `lint-fix`, `digest`.
- Never delete; flag stale pages with `status: archived` in frontmatter.
- `status: stub` — for pages created with a one-sentence definition when a concept is forward-referenced but not yet developed. Add `stub` to `topics:` tags. Flesh out when the concept is fully treated by a source.

<!-- NOTATION-BLOCK-START -->
- **Notation is preserved verbatim where it appears.** This vault may handle a mix of operational/process content and formally notated material (equations, statistical models, causal frameworks, formal logic, type systems, algorithm pseudocode). When notation appears, reproduce it precisely, define symbols where introduced, and have the human verify the summary captures the result correctly before treating it as settled.
- **Silent corrections require visible footnotes.** When the printed source contains a typo, OCR artifact, or non-standard convention and the corrected form is recorded in a wiki page, add an inline footnote or parenthetical naming the discrepancy. Pattern: "Source prints `<as-printed>`; this page uses `<corrected>` (`<name of correct form>`)." Never silently fix the source; the fix must be visible to anyone reading the page later.
- **Multi-line printed formulas or formal derivations require a self-consistency check before ingestion.** For any printed formula containing nested fractions, sums of exponentials, multi-factor coefficients in numerator or denominator, solution formulas for differential equations, or any multi-step derivation: (a) verify the boundary or base condition; (b) verify the result satisfies its parent equation or constraint by direct differentiation, substitution, or analogous algebraic check; (c) if either check fails, do not commit the page — flag the formula as "transcription uncertain, awaiting human verification" at the top of the page and stop. Textual eyeball checking alone has been demonstrated to miss subtle coefficient errors.
- **Form-variant cross-references must be disambiguated.** When the source uses different equation or section numbers for the same fundamental relation in different presentational forms (e.g. a general expectation form vs. a substituted PDE form, discrete-time vs. continuous-time, matrix vs. summation), record which variant a cross-reference points to. Verify by re-reading the cited equation or passage, not by trusting the reference number alone.
<!-- NOTATION-BLOCK-END -->

**Concept graining:**

- **Anchor page** — create when the source devotes a section (or more) to a concept and it connects to ≥ 2 other concepts. This is the default for load-bearing ideas.
- **Stub-with-intent** — create when the source explicitly forward-references a concept but does not develop it yet. Body = one sentence definition + `stub` in topics. Flesh out when the concept is fully treated by a source.
- **Dead wikilink** — use `[[concept name]]` inline for concepts named but not yet paged. Do not create an empty page; let the link dangle until that concept is ingested.
- **Do not page** — operational details, named examples used only as illustration, book-structural elements (chapters, intros), author biographical facts.

**Negative-space categories** (use exactly these labels in `## Negative Space` sections and log entries):

| Label | Meaning |
|---|---|
| `too-granular` | Sub-concept that belongs as a bullet under a parent page |
| `subsumed-by` | Fully covered by an existing page; no marginal content |
| `out-of-scope` | Outside software craft |
| `illustrative-scaffolding` | Example/anecdote used to explain a concept, not a concept itself |
| `foil` | Presented as what NOT to do; anti-pattern not worth a dedicated page |
| `conceptual-tool-not-concept` | A rhetorical device the author uses to argue, not a domain concept |
| `supporting-argument` | Evidence or sub-argument for a claim, not a standalone concept |
| `foreshadowing` | Named but not developed — use dead wikilink instead |
| `source-underdeveloped` | Source raises the concept but provides only a citation, caveat, or gesture rather than a developed treatment; or frames it as open/missing or pre-production research with insufficient grounding to support a page |
| `book-metadata` | Prefaces, acknowledgements, chapter summaries, self-referential content |
| `case-study-specifics` | Particular to one institution or historical case; not generalizable |
| `tool-specific/perishable` | Software names, version-specific workflows, vendor-specific advice |

> **Figures are captured, not rejected — `figures-as-prose` is not a label.** Never
> reproduce a source figure as ASCII art: capture its underlying insight as prose or a
> structured list and cite the figure by name (e.g. "see Figure 4.2"). Handling a figure
> this way is a *capture*, recorded where useful as a capture note (the ingest log line
> or the page's figure citation) — **not** with a negative-space label. A figure enters
> `## Negative Space` only when its content is deliberately *not* captured: use
> `subsumed-by` if surrounding prose already covers it, or `illustrative-scaffolding` if
> it is purely decorative.

---

## Shell commands

The source folder is `raw-input/` (hyphenated, no spaces). No special quoting or
`%20` encoding is needed for that path segment.

- Citation paths in wiki pages use `raw-input/` directly.
- The vault root is always the current working directory; derive all paths relative
  to `$(pwd)`, never hardcode `~/vaults/<vault-name>` or any old vault name.

---

## One-record-per-session rule

Each coding session produces one coding-handoff. A thinking/sparring session produces a planning-handoff. One session yields one record — never both. Exception: if the coding session surfaces a cross-cutting insight, that specific insight may additionally earn a `topics/` page. Deliberate and rare.

---

## Startup Protocol

At the start of every interactive session, before responding to the human's first request:

1. Read `wiki/log.md`, `wiki/index.md`, and `wiki/gaps.md`.
2. Wait for the human's first message.
3. Infer the most likely topic(s) from it.
4. Scan `log.md` for the last 2 entries matching the inferred topic — prioritise `planning-handoff`, `coding-handoff`, and `ingest` entries. If fewer than 2 exist, supplement with the single most recent planning-handoff of any topic.
5. Read the matched pages in full.
6. If any entry in `wiki/gaps.md` §1 is directly relevant to the session topic, surface it in the acknowledgement line.
7. Scan `log.md` for any `lint | pending | <slug>` entry that has no later `lint | <slug> |` entry. If one exists, note it for the acknowledgement line.
8. Acknowledge what you loaded in one short line: *"Loaded on <topic>: <page-1>, <page-2>."* If a gap was surfaced (step 6), append: *"Open gap: <one-line summary>."* If a pending lint was found (step 7), append: *"Lint pending: <slug> — vault-wide lint due, run in a fresh session."*
9. If the topic was ambiguous, say so once and offer to load a different set if corrected.
10. Then proceed.

---

## Commit discipline

Vault state is committed to git after each completed operation. Commits are
human-triggered or human-authorised; no operation commits on its own.

Scheduled operations remain report-only — outputs accumulate in the working
tree until the next interactive session bundles them.

One commit per completed unit of work. Bundle by operation:

| Operation completed | Commit bundles |
|---|---|
| Book-ingest batch (all chapters reviewed-clean) | Book entity page, new topic pages, enriched topic pages, log/index/gaps updates, chapter review digests, ingest report |
| Article ingest (one article OR one scheduled multi-article run) | Page updates, log entries, any digest |
| Lint run | Lint digest, log entry, any quality-debt updates surfaced |
| Distil | Handoff page, log entry, any entity/topic page updates |
| CLAUDE.md edit (vault-schema change) | CLAUDE.md only — never bundled with content |

Commit message prefix matches the unit of work:

- `content: book-ingest <book-slug> batch <N>`
- `content: article ingest — <source-title>`
- `content: <YYYY-MM-DD> scheduled intake/ingest`
- `content: <YYYY-MM-DD> lint outputs`
- `content: distil — <topic>`
- `docs(claude-md): <change>` — any edit to this file
- Other prefixes as new operation types emerge.

When unrelated WIP exists in the working tree, scope the commit with pathspec
(`git commit ... -- <paths>`) rather than letting unrelated changes ride along.

Never bundle content WIP into a CLAUDE.md commit, or vice versa.

---

## Operations

### Intake (Downloads -> `raw-input/_pending/`)

Triggered by: scheduled job (5-day cadence) OR human request.

1. Enumerate files in `~/Downloads/` modified within the last 5 days.
2. Keep only files where extension is `.md` AND filename (case-insensitive) starts with `sc-`.
3. For each kept file: move (not copy) to `raw-input/_pending/`, then append
   `## [YYYY-MM-DD] intake | scheduled | <filename>` to `log.md`.
4. If interactive: list moved files. If headless: write `wiki/digests/intake-<YYYY-MM-DD>.md`.

> Web Clipper writes articles directly into `_pending/`; they bypass this Downloads filter and are picked up at ingest (article synthesis is delegated to `/article-ingestion` — see `### Article-ingest`). Books are NOT handled here — see book-ingest.

---

### Ingest (`raw-input/_pending/` -> wiki updates)

Triggered by: scheduled job (after intake) OR human request. Processes ALL `_pending/` types.

> **First-ingest vocabulary seed (one-time).** If `wiki/topics-authority.md` is still an unpopulated skeleton (`status: stub` + `SEED-ME` comment) and this notes/handoff content is the first to enter the vault, seed it per the Conventions *First-ingest seed* rule (≤10 subjects, ≤30 aliases from this content + the domain) before synthesising pages, so the pages you write resolve against it. (When an article is the first content, `/article-ingestion` performs this seed — see `### Article-ingest`.)

For each file in `_pending/`:

1. **Classify** (two-tier): parse filename prefix first (`sc-coding-handoff-`, `sc-planning-handoff-`, `sc-notes-`, or `clippings`-tagged frontmatter -> article). If absent/unrecognised, read the document and classify by content.
2. **File** the source: move from `_pending/` to the matching `raw-input/` subfolder.
3. **Synthesise** per type:

   - **coding-handoff** -> write a cross-referenced summary page at `wiki/handoffs/coding-handoffs/<YYYY-MM-DD>-<project>.md` (summary + wikilinks, not a copy of the raw). Then REVISE `wiki/entities/projects/<name>.md` to reflect new current state (living synthesis, bounded). Link the entity page to the new handoff page.
   - **planning-handoff** -> write or update `wiki/handoffs/planning-handoffs/<YYYY-MM-DD>-<topic>.md` in distillation format: decisions, rationale, open questions. Cross-reference entities/topics mentioned.
   - **article** -> invoke `/article-ingestion` (Phase 2) to synthesise it into the wiki. The skill owns the article path end to end — synthesis, resolve-before-minting, index/log updates, the article lint trigger, and the headless digest. See `### Article-ingest`. (Do the steps below — index, cross-refs, log, lint trigger — only for the non-article types in this loop.)
   - **notes** -> identify topic(s); write or update `wiki/topics/` or `wiki/entities/` pages.

4. Update `wiki/index.md`.
5. Update cross-references; flag contradictions inline with `<!-- CONTRADICTS: [[page]] section X -->`.
6. Append to `log.md`: `## [YYYY-MM-DD] ingest | <topic-or-project> | <source-title>`. (The article branch logs its own `ingest | article |` entry and runs the article lint trigger inside `/article-ingestion`.)

When headless, also write `wiki/digests/ingest-<YYYY-MM-DD>.md` listing sources processed, pages created/updated, contradictions flagged, and any unclassified files left in `_pending/`.

---

### Article-ingest (URL or pending clipping -> wiki updates)

Triggered by: the Ingest operation's article branch, a human giving an article URL or asking to ingest a clipped article, OR a scheduled/headless run. Supports headless — articles are straightforward, single-pass sources.

Invoke: `/article-ingestion`. The skill has two entry points: **Phase 1 (Fetch)** turns a URL into a provenance-stamped Markdown note in `raw-input/_pending/`; **Phase 2 (Ingest)** synthesises a pending article note into the wiki — page writes, resolve-before-minting against `topics-authority.md`, the first-ingest vocabulary seed when an article is the vault's first content, `index.md`/cross-reference updates, the `ingest | article |` log entry, the article lint trigger, and the headless `wiki/digests/ingest-<date>.md`.

The full procedure lives in `article-ingestion-skill.md`. This contract delegates the article path to it the same way the book path is delegated to `book-ingestion-skill.md`. Articles still arrive in `_pending/` via the Obsidian Web Clipper as well as via the skill's fetch phase.

---

### Book-ingest (`raw-input/books/<book>/` -> wiki updates)

Triggered by: human request only. Always interactive. Never headless. Each human request authorizes exactly one batch. Within that batch, chapters are ingested autonomously without pausing for confirmation. When the final chapter of the batch is reviewed and clean, stop — report the batch outcome and wait. Do not begin the next batch without a new explicit human request in a fresh context window.

> **Hard rule — plan-first:** Before ingesting any chapter of a book, `/book-planner` must have run and produced an approved ingestion plan at `raw-input/books/<slug>/ingestion-plan.md`. Do not begin any batch until that file exists and the human has explicitly approved it.

> **Resume rule:** When starting a session for a partially-ingested book, read `raw-input/books/<slug>/ingestion-plan.md` (for synthesis strategy and batch boundaries) and `raw-input/books/<slug>/meta.md` (for chapter progress) before doing anything else. State in one line: *"Resuming \<book\>: next batch is batch-\<N\> — chapters \<X\>–\<Y\>."*

Book onboarding (first add of a new book — creating meta.md and the book entity page) is the responsibility of `book-planner-skill.md` Phase 0. Invoke `/book-planner` for any new book; ingestion cannot begin until the plan + meta.md + book entity all exist.

The full ingest procedure — chapter state machine, per-chapter synthesis steps, mark-reviewed-clean transitions, on-book-completion guard and ingest report schema — lives in `book-ingestion-skill.md`. Invoke `/book-ingest` to run a batch.

Reviewer is mandatory. See `### Book-review` below for the reviewer-failure hard rule (full DO NOT list).

<!-- VAULT-SPECIFIC-EXTENSIONS-START -->
> **Vault-specific extensions** (ratified YYYY-MM-DD, see `_provenance`):
>
> - <topic 1>
> - <topic 2>  (add or omit bullets as needed; one bullet per distinct topic)
<!-- VAULT-SPECIFIC-EXTENSIONS-END -->

---

### Book-review (chapter verification)

Triggered by: the final step of every book-ingest chapter, or an explicit human request to re-review a chapter.

Invoke: `/book-review <book-slug> <chapter-number>`

> **Hard rule — reviewer failure:** `/book-review` is the ONLY acceptable source of a review verdict. If the skill fails to execute for ANY reason — path error, permission block, skill not found, load failure, or anything else — STOP immediately and report the failure to the human in plain terms: state that the reviewer did not run and why. Do NOT: (a) perform the review manually or "by hand," (b) run the ten checks yourself from memory, (c) report any PASS/WARN/FAIL score, or (d) write a review digest. A self-performed review is never a substitute for the independent reviewer and must never be presented as one. A chapter whose `/book-review` did not successfully run is **"ingested, NOT reviewed"** — do not tick it as reviewed in `meta.md`, the log, or the book entity. Treat a reviewer that cannot run exactly as you would treat a FAIL: halt and surface it.

The skill runs ten checks — citation density, wikilink integrity, negative-space discipline, stance preservation, enrichment-not-replacement, frontmatter completeness, index/log consistency, extraction quality (diagnostic only — no FAIL), synthesis-strategy declaration, and notation hygiene application (conditional — applies only when the vault opts into notation hygiene) — and writes a verdict digest to `wiki/digests/review-<book>-ch<n>-<YYYY-MM-DD>.md`. Checks 1–7, 9, and 10 are scored; the aggregate is X/9 when notation hygiene applies and X/8 when it does not.

Source tier and reviewer scrutiny: the reviewer's Check 8 forward spot-checks and reverse omission sweep apply standard scrutiny to tier-1 sources. For any page drawing from tier-2 or tier-3 sources, the reviewer must additionally:
- Flag any claim from a tier-2/3 source that is not corroborated by a tier-1 source — mark as WARN: unverified claim, suggest corroboration.
- Flag any claim from a tier-3 source presented as authoritative (without a "per [source], unverified" qualifier) — mark as FAIL: unqualified tier-3 claim.
- Check that the page's source_tier value matches the lowest tier of any source cited — mismatch is a WARN.
This prevents tier-3 claims from being laundered into the vault as if they were peer-reviewed.

On FAIL: fix the flagged issue and re-run `/book-review` before proceeding to the next chapter.
On WARN: fix all WARNs immediately and re-run `/book-review`; batch only when the human explicitly defers.

---

### Query

1. Use the index loaded at startup to find relevant pages.
2. Read them.
3. Answer with citations to specific wiki pages and raw sources.
4. If substantive, propose filing the answer back as a page.
5. Append: `## [YYYY-MM-DD] query | <topic> | <one-line summary>`

---

### Distil (end of a live sparring session in the vault)

Triggered by: human asking to wrap an in-vault session (exported sessions arrive as `sc-planning-handoff-*.md` via ingest instead).

1. Identify substantive outputs.
2. Write `wiki/handoffs/planning-handoffs/<YYYY-MM-DD>-<topic>.md`: decisions, rationale, open questions. Frame for a future human who forgot the conversation.
3. Update `index.md` and affected entity/topic pages.
4. Append: `## [YYYY-MM-DD] distil | <topic> | <title>`

---

### Lint (health check)

Triggered by: human request OR a `lint | pending | software-craft` marker in `log.md`. Invoke the shared skill: `/vault-lint`. The skill handles all checks (universal sweep, role-count drift, vault-specific extensions declared in the VAULT-LINT-EXTENSIONS block below). Report-only by default; the role-count drift check emits a ready-to-apply patch block at the bottom of the report. Apply patches in a follow-up turn after human review.

Report path: `wiki/digests/lint-<YYYY-MM-DD>.md`.

<!-- VAULT-LINT-EXTENSIONS-BEGIN -->

vault_slug: software-craft

# CHOOSE ONE — keep the active line, delete or comment out the other.
freshness_model: structural    # default — staleness detected only by last_updated age (Phase 1 Check 6); use for slow-changing or static content.
# freshness_model: calendar    # pages carry volatility: live|fast|slow|static and next_review: <date>; requires a calendar staleness sweep job in Scheduled Operations (see sanctioned region 6).

depth_table:
  "wiki/topics/": "../../"
  "wiki/entities/*/": "../../../"

# OPTIONAL — uncomment and populate only if your vault has project-segmented content (see sanctioned region 4).
# projects:
#   - <project-code-1>
#   - <project-code-2>

extension_checks: []    # TBD — confirm vault-specific checks with human before first lint run.
# Example entries — uncomment and adapt:
#   - id: <kebab-case-id>
#     description: <one-line description of the check>
#     applies_to_projects: true   # optional; only meaningful when projects: is set

<!-- VAULT-LINT-EXTENSIONS-END -->

#### Manual-review failure modes

Failure modes this vault is susceptible to that have no automated
check in `extension_checks` above. Watch for these during ingest,
distil, and periodic sweeps — not only during /vault-lint. Items
here may graduate into `extension_checks` once a handler exists.

Format: one bullet per item, kebab-case name + brief description of
how the failure manifests. State "None currently identified." if the
vault has none. Example:

- **<failure-mode-name>** — One-line description of how this failure
  manifests in vault content.

---

## Scheduled Operations

Cron/launchd invokes Claude Code headless and runs:

1. **Guard.** Read `log.md`; find the last `intake | scheduled` or `ingest | scheduled` entry. If fewer than 5 days elapsed since the most recent, exit.
2. If 5+ days elapsed: first snapshot the pre-run dirty set in scoped paths (`log.md`, `wiki/`, `raw-input/`) using `git status --porcelain` and retain the list for step 3. Then run Intake, then Ingest (all `_pending/` types), then write `wiki/digests/scheduled-<YYYY-MM-DD>.md`.
3. **Commit (run-touched files only).** Compute the run-touched set: the dirty paths in scope after step 2 minus the pre-run snapshot from step 2. Pre-existing WIP — files already dirty before the run started — is intentionally excluded even if the run further modified them; the user resolves any such files manually on the next interactive session in this vault. If the run-touched set is empty, skip the commit (no empty commits). Otherwise commit ONLY the run-touched paths using pathspec commit: `git commit -m "content: scheduled run <YYYY-MM-DD> | <one-line summary>" -- <each-run-touched-path>`, where the summary is built from the digest (e.g., "no-op (0 candidates)" or "3 articles ingested, 5 pages updated"). For any newly-created (untracked) files in the run-touched set, `git add <file>` them before the pathspec commit since pathspec commit doesn't capture untracked files on its own. Never commit `CLAUDE.md` or any path outside scope.
4. Exit.

The Ingest step delegates each `_pending/` article to `/article-ingestion` (Phase 2), which is headless-capable and runs in this scheduled context; book-ingest is never run headless. To change cadence, edit the day count in step 1.
launchd label for this vault: `com.user.vault-sc-scheduled`.
Scheduled to fire daily at `08:02`.
vault-lint is never invoked from scheduled operations; it requires interactive human authorisation via the skill's Step 0a gate.

---

## What you don't do

- Don't write to `raw-input/` except as part of intake (adding to `_pending/`), ingest (moving from `_pending/`), and book setup (`meta.md` only).
- Don't write to the domain's external working artifacts from a vault session.
- Don't make up sources. If information isn't in the wiki or `raw-input/`, ask the human or use web search and cite the result.
<!-- NOTATION-BLOCK-DONT-START -->
- Don't degrade notation — reproduce it precisely and define symbols. Apply the notation hygiene rules from the Conventions section to every page that records notation.
<!-- NOTATION-BLOCK-DONT-END -->
- Don't produce long displacive summaries — compress and cross-reference.
- Don't let an entity page become an append-only log; keep it a bounded living synthesis.
- Don't duplicate concept pages; enrich the existing page when a concept recurs across sources.
- Don't auto-apply fixes during lint; only report.
- During headless runs, don't make speculative or stylistic edits to existing pages.
- Don't produce both coding-handoff and planning-handoff records for the same session.
- Don't run book-ingest headless or one-shot a whole book.
- Don't chain book-ingest batches: a human request scopes exactly one batch. When the batch is clean and complete, stop. The next batch requires a new explicit request in a fresh session.
