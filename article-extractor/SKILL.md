---
name: article-extractor
description: Extract clean article/blog/tutorial content from a URL and save it as a Markdown note with YAML provenance frontmatter, ready to drop into an Obsidian (or other) knowledge vault. Use this whenever the user gives a web article URL and wants to download, extract, capture, archive, or "save to my vault/notes" the readable text without ads, navigation, or clutter. Trigger even if the user only says "grab this article" or "add this to my reading vault."
allowed-tools: Bash, Read, Write
---

# Article Extractor (vault-ready)

Extract the main text of a web article and write it as a clean Markdown file with
provenance frontmatter (source URL, author, dates, tags) into a knowledge-vault
inbox folder. This skill is built for a reference/wiki workflow: every note must
carry its source so it can be trusted and re-found later.

## Design principles (do not violate)

1. **Provenance is mandatory.** Every output file gets YAML frontmatter including
   `source_url`. A note without its source is useless in a reference vault.
2. **Markdown, not plain text.** Output is `.md` so headings/lists/links survive
   and Obsidian can render and link it.
3. **Never auto-install anything, never use sudo.** If a required tool is missing,
   STOP and give the user copy-paste install commands, then wait. The user approves
   all side effects on their machine.
4. **One extraction engine: trafilatura.** It is the most reliable open-source
   extractor and handles many languages. Do not fall back to ad-hoc HTML parsing —
   a half-broken extraction silently poisons the vault.

## Step 0 — Confirm the destination folder

Before extracting, determine where the note will be written (`VAULT_INBOX`).

- If the user named a folder/vault, use it.
- Else, if a default is configured (an env var like `$VAULT_INBOX`, or a path the
  user has used before in this conversation), use that and state it.
- Else, ask: "Which folder should I save this into?" Offer a sensible default such
  as `./inbox`. Do not invent a path silently.

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
UA="Mozilla/5.0 (compatible; vault-article-extractor/1.0)"
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

## Error handling

- **trafilatura missing** → stop, give install command, wait (Step 1).
- **Empty/auth-walled page** (`page.html` tiny, or the Python step prints
  `EXTRACTION_EMPTY`) → tell the user: "This page appears to need JavaScript or a
  login; I couldn't extract clean text." Offer: they paste the article text
  directly, or provide a reader-friendly/print URL. Do not save a broken note.
- **Non-200 / bad URL** → report the HTTP status from curl (`-w '%{http_code}'`).

## After extraction

Offer, but don't assume:
- "Want me to suggest tags from your vault and fill the empty
  `tags:` field?"
- "Extract another?"

## Maintainer notes (for iteration)

- Tested intent, not execution: verify the exact `trafilatura` flags against your
  installed version (`trafilatura --help`). `--markdown`, `--json`, `--no-comments`,
  and stdin input are documented for 2.x.
- The frontmatter schema (`title, source_url, author, date_published,
  date_captured, source_type, tags, status`) is a starting point — align it with
  whatever schema your vault standardizes on.
- Consider adding `--only-with-metadata` if you want to reject sources that lack a
  title/date/url, trading recall for cleaner provenance.
