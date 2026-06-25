---
name: article-ingestion
description: Fetch a web article from a URL into a clean Markdown note with provenance frontmatter, AND/OR ingest a pending article note into a Karpathy-style LLM Wiki vault — synthesising topic/entity pages, resolving vocabulary, updating index/log, and triggering lint. Use this whenever the user gives a web article URL to "grab", "download", "extract", "capture", "save to my vault", or asks to "ingest"/"process" a clipped article, and as the article branch of the vault's scheduled Ingest operation. Supports interactive and headless/scheduled runs.
allowed-tools: Bash, Read, Write, Edit
---

# Article Ingestion (fetch + vault synthesis)

This skill owns the full article path for an LLM-Wiki vault, in two phases:

- **Phase 1 — Fetch** turns a URL into a clean Markdown note with provenance
  frontmatter, dropped into the vault's intake inbox (`raw-input/_pending/`).
- **Phase 2 — Ingest** reads a pending article note and synthesises it into the
  wiki — topic/entity pages, vocabulary resolution, index/log updates, lint trigger.

The two phases are independent entry points:

- A user who only wants the readable text saved → run **Phase 1** and stop.
- An article already sitting in `_pending/` (from the Obsidian Web Clipper, or from
  a prior Phase 1) → run **Phase 2** directly.
- A scheduled/headless run or "ingest these articles" → Phase 1 (if a URL was given)
  then Phase 2.

Unlike `book-ingestion`, this skill **supports headless/scheduled runs** — articles
are straightforward, single-pass sources. The vault's Scheduled Operations invoke it
headlessly. When headless, never pause for confirmation and write a digest (see Phase 2).

Vault-specific configuration (frontmatter schema, citation format, negative-space
categories, vault slug, the `topics-authority.md` controlled vocabulary) is read from
the vault's `CLAUDE.md` at runtime. This skill is written against that contract.

---

# Phase 1 — Fetch (URL → vault-ready note)

Extract the main text of a web article and write it as a clean Markdown file with
provenance frontmatter (source URL, author, dates, tags) into the vault inbox. Every
note must carry its source so it can be trusted and re-found later.

## Design principles (do not violate)

1. **Provenance is mandatory.** Every output file gets YAML frontmatter including
   `source_url`. A note without its source is useless in a reference vault.
2. **Markdown, not plain text.** Output is `.md` so headings/lists/links survive
   and Obsidian can render and link it.
3. **Never auto-install anything, never use sudo.** If a required tool is missing,
   STOP and give the user copy-paste install commands, then wait. The user approves
   all side effects on their machine. (Headless: if a tool is missing, fail cleanly
   into the digest — never self-install.)
4. **One extraction engine: trafilatura.** It is the most reliable open-source
   extractor and handles many languages. Do not fall back to ad-hoc HTML parsing —
   a half-broken extraction silently poisons the vault.

## Step 0 — Confirm the destination folder

Before extracting, determine where the note will be written (`VAULT_INBOX`).

- If this is a vault ingest, the inbox is the vault's `raw-input/_pending/`.
- Else if the user named a folder/vault, use it.
- Else, if a default is configured (an env var like `$VAULT_INBOX`, or a path the
  user has used before in this conversation), use that and state it.
- Else, ask: "Which folder should I save this into?" Offer a sensible default such
  as `./inbox`. Do not invent a path silently. (Headless: use the vault's
  `raw-input/_pending/`; never prompt.)

```bash
VAULT_INBOX="${VAULT_INBOX:-./inbox}"
mkdir -p "$VAULT_INBOX"
```

## Step 1 — Check that trafilatura is installed

```bash
command -v trafilatura
```

If it is **not** found, STOP and tell the user (do not install it yourself):

> trafilatura isn't installed. Install it once with:
> `pip3 install --user trafilatura`  (or `pipx install trafilatura`)
> Then re-run this.

Do not proceed until it is available.

## Step 2 — Fetch the page once

Download the HTML a single time and reuse it, so the metadata pass and the body
pass see identical content and we make only one network request.

```bash
ARTICLE_URL="<the URL>"
UA="Mozilla/5.0 (compatible; vault-article-ingestion/1.0)"
curl -sL --compressed -A "$UA" "$ARTICLE_URL" -o page.html
```

If `page.html` is empty or tiny, the site likely requires JavaScript or login.
Tell the user extraction may fail and continue to Step 3 to confirm.

## Step 3 — Extract metadata and body from the saved HTML

trafilatura reads HTML from stdin. Run it twice on the same file:

```bash
# Metadata as JSON (title, author, date, etc.)
cat page.html | trafilatura --json > meta.json

# Clean article body as Markdown (no comment sections)
cat page.html | trafilatura --markdown --no-comments > body.md
```

Notes:
- `--markdown` preserves headings, lists, links, and inline formatting.
- If `body.md` is empty, retry once favoring recall:
  `cat page.html | trafilatura --markdown --no-comments --recall > body.md`
- If it is still empty, report a clean failure (see Error handling) rather than
  saving an empty or garbage note.

## Step 4 — Assemble the final Markdown note

Use this Python step to read `meta.json` + `body.md`, build safe YAML frontmatter,
and write the note. Passing each scalar through `json.dumps` guarantees valid YAML
(JSON strings are valid YAML), so titles containing colons or quotes won't corrupt
the frontmatter.

```bash
ARTICLE_URL="$ARTICLE_URL" VAULT_INBOX="$VAULT_INBOX" python3 - <<'PY'
import json, os, re, datetime, sys, pathlib

url = os.environ["ARTICLE_URL"]
inbox = pathlib.Path(os.environ["VAULT_INBOX"])

try:
    meta = json.load(open("meta.json"))
except Exception:
    meta = {}

body = open("body.md", encoding="utf-8").read().strip()
if not body:
    print("EXTRACTION_EMPTY")
    sys.exit(2)

title  = (meta.get("title")  or "Untitled article").strip()
author = (meta.get("author") or "").strip()
date_pub = (meta.get("date") or "").strip()        # trafilatura: published date
captured = datetime.date.today().isoformat()

def y(v):  # YAML-safe scalar
    return json.dumps(v if v is not None else "")

frontmatter = "\n".join([
    "---",
    f"title: {y(title)}",
    f"source_url: {y(url)}",
    f"author: {y(author)}",
    f"date_published: {y(date_pub)}",
    f"date_captured: {y(captured)}",
    "source_type: article",
    "tags: []",
    "status: inbox",
    "---",
    "",
])

# Filesystem-safe filename from title
fname = re.sub(r'[\\/:*?"<>|]', "-", title).strip()
fname = re.sub(r"\s+", " ", fname)[:100].rstrip(" .") or "article"
path = inbox / f"{fname}.md"
i = 2
while path.exists():
    path = inbox / f"{fname} ({i}).md"
    i += 1

path.write_text(frontmatter + body + "\n", encoding="utf-8")
print(str(path))
PY
```

## Step 5 — Confirm and preview

- Print the saved path.
- Show the frontmatter plus the first ~12 lines of the body so the user can sanity-check.
- Then clean up temp files: `rm -f page.html meta.json body.md`.

```bash
echo "Preview:"; head -n 20 "<saved path>"
```

If the user (or the scheduled run) wants this in the wiki, continue to **Phase 2**.
Otherwise stop here.

## Phase 1 error handling

- **trafilatura missing** → stop, give install command, wait (Step 1). Headless: fail
  cleanly into the digest.
- **Empty/auth-walled page** (`page.html` tiny, or the Python step prints
  `EXTRACTION_EMPTY`) → tell the user: "This page appears to need JavaScript or a
  login; I couldn't extract clean text." Offer: they paste the article text
  directly, or provide a reader-friendly/print URL. Do not save a broken note.
- **Non-200 / bad URL** → report the HTTP status from curl (`-w '%{http_code}'`).

---

# Phase 2 — Ingest (pending note → wiki synthesis)

Triggered by: the vault's Ingest operation (article branch), a scheduled/headless run,
or a human asking to ingest a clipped/saved article. Processes article notes only —
books, exec-handoffs, planning-handoffs and free-form notes are handled elsewhere
(see the vault's `### Ingest` operation).

Read the vault's `CLAUDE.md` first for the frontmatter schema, citation format,
negative-space categories, vault slug, and the `topics-authority.md` model. Do NOT
load the full wiki — load `wiki/index.md` and only the pages relevant to this article.

> **First-ingest vocabulary seed (one-time).** If `wiki/topics-authority.md` is still
> an unpopulated skeleton (`status: stub` + `SEED-ME` comment) and this article is the
> first content entering the vault, seed it per the vault's Conventions *First-ingest
> seed* rule (≤10 subject categories, ≤30 aliases drawn from this article + the domain),
> set `status: active`, and remove the `SEED-ME` comment — **before** synthesising pages,
> so the pages you write resolve against it. The 10/30 caps apply to this initial seed
> only.

For each pending article note (in `raw-input/_pending/`):

1. **File the source.** Move it from `_pending/` to `raw-input/articles/`.
2. **Synthesise.** Read it; write or update the relevant `wiki/topics/` and
   `wiki/entities/` pages with what the article contributes. Compression and
   cross-reference, **never displacing paraphrase** — do not paste the article body
   into a page. Cite the filed source via its relative path in the vault's citation
   format. Record genuine gaps in the page's `## Negative Space` section per the
   vault's categories.
3. **Resolve before minting.** Before creating any new page or assigning `topics:`/
   `aliases:`, resolve the intended terms against `wiki/topics-authority.md`: prefer
   an existing Subject/Concept's preferred term over minting a near-synonym. Only mint
   a new vocabulary entry when the concept is genuinely new; when you do, add it to the
   authority file under the resolve-before-minting rule. (If the vault has no
   `topics-authority.md`, skip this step.)
4. **Update `wiki/index.md`** — add new pages to the flat catalogue. (Do NOT hand-edit
   the role-count numbers in the role maps-of-content header here; those are refreshed
   once per run by the post-loop sync step below.)
5. **Update cross-references**; flag contradictions inline with
   `<!-- CONTRADICTS: [[page]] section X -->`.
6. **Append the log entry:** `## [YYYY-MM-DD] ingest | article | <source-title>`.
7. **Article lint trigger** (after writing the log entry). Let `<slug>` be the vault
   slug from `CLAUDE.md`:
   a. Find the most recent `## [YYYY-MM-DD] lint | <slug> |` entry in `log.md`. If
      none, treat the start of the file as the watermark.
   b. Count all `## [YYYY-MM-DD] ingest | article |` entries strictly after that
      watermark (do not count `lint | pending` lines).
   c. If count ≥ 4 and no `lint | pending | <slug>` entry exists after the most recent
      `lint | <slug> |` entry, append: `## [YYYY-MM-DD] lint | pending | <slug>`.

**After all pending article notes are processed (post-loop, once per run):**
**Sync the index role-counts.** The per-article `index.md` edits (step 4) add page
entries but do NOT refresh the role-count numbers in the role maps-of-content header,
so those counts drift. Refresh them once, after the loop, by running the lint script's
sync mode (the `lint.py` co-located with the vault-lint skill; with the README install
that is `~/.claude/skills/vault-lint/lint.py`):
```
python3 ~/.claude/skills/vault-lint/lint.py --sync-role-counts <vault-path>
```
This recomputes the counts from topic-page frontmatter using the SAME logic as
`/vault-lint` Phase 2 and rewrites only the count digits in `wiki/index.md`
(report-free, log-free, idempotent — safe to re-run, and a no-op when no new pages were
minted). The script is the single source of truth for these counts; never hand-edit
them. This applies to interactive and headless runs alike. Skip only if the run minted
no new pages and changed no `roles:` frontmatter (the sync would be a no-op anyway).

When headless (scheduled run), also write `wiki/digests/ingest-<YYYY-MM-DD>.md` listing
sources processed, pages created/updated, contradictions flagged, and any unclassified
files left in `_pending/`. Never pause for confirmation and never make speculative or
stylistic edits to existing pages during a headless run.

Commit discipline is the caller's responsibility (the vault's Scheduled Operations
commit run-touched files; an interactive session commits per the vault's commit
table). This skill does not commit.

---

## Maintainer notes (for iteration)

- Tested intent, not execution: verify the exact `trafilatura` flags against your
  installed version (`trafilatura --help`). `--markdown`, `--json`, `--no-comments`,
  and stdin input are documented for 2.x.
- The Phase 1 frontmatter schema (`title, source_url, author, date_published,
  date_captured, source_type, tags, status`) is a starting point — align it with
  whatever schema your vault standardizes on (Phase 2 reads the real schema from
  `CLAUDE.md`).
- Consider adding `--only-with-metadata` if you want to reject sources that lack a
  title/date/url, trading recall for cleaner provenance.
