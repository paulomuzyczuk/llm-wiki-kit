---
name: visual-summary
description: >
  Draws a one-glance Excalidraw visual summary of a single LLM-wiki topic page,
  so a reader can grasp the page's core idea without reading it. The agent never
  places coordinates: it picks a layout template (pipeline, hub, contrast),
  writes a short JSON spec of labels, and the co-located visual_summary.py
  builds an Obsidian `.excalidraw.md` file with text bound in shapes and arrows
  bound to them (editable by hand), checks word budgets and overlaps, and
  renders a PNG for review. Use when the user asks for a "visual summary",
  "diagram", "drawing" or "Excalidraw" of a wiki page, or to "visualise" a
  topic. One invocation = one page. Draft: templates and limits may change.
---

# Visual Summary

> **Status: draft.** Templates: `pipeline`, `hub`, `contrast`.
> Not yet wired into vault-lint, the template `CLAUDE.md`, or scheduled operations.

A visual summary is **not a diagram of the page's text**. It is the page's core idea
in one picture: **≤ ~40 words, and the shapes carry the meaning**: order (pipeline),
composition (hub) or tension (contrast). If you are summarising every section, you
are doing it wrong; a reader who wants the sections reads the page.

The implementation is `visual_summary.py`, co-located with this file
(`<skills-dir>/visual-summary/visual_summary.py` once installed). The script owns
layout, file format and checks. This skill owns **choosing what to say and which
shape says it**.

## When to invoke

- The user asks for a visual summary, diagram, drawing or Excalidraw of a topic page.
- The user asks to refresh a visual summary after the page changed substantially.

Do not invoke for entity pages, digests, logs or handoffs: they are records, not concepts.

## Procedure

### Step 1 — Identify the page and vault

The vault root contains `CLAUDE.md` and `wiki/`. The page is
`wiki/topics/<slug>.md`. If either is ambiguous, ask.

### Step 2 — Read the page and find its one idea

Read the whole page. Write down, for yourself, the single sentence a reader should
leave with. Everything in the drawing must serve that sentence. Typical page shapes:

| The page is mainly about… | Template | Example |
|---|---|---|
| A process, method or causal chain (do A, then B…) | `pipeline` | marketing-mix-modeling: collect → specify → estimate → check → allocate |
| One concept and its parts, criteria or facets | `hub` | brand-elements: six criteria around "brand element" |
| Two schools, options or trade-offs | `contrast` | long-run-advertising-effects: Sharp vs Binet & Field |

If none fits, stop and tell the user which shape the page needs. Do not force a
template. New templates are added to the script, not improvised.

### Step 3 — Write the spec

Write the spec JSON to a scratch location (never into the vault). The spec format is
documented at the top of `visual_summary.py`. Limits, enforced by the script:

- **Labels ≤ 4 words**: the noun phrase that names the box.
- **Details / points ≤ 8 words**, **notes / verdict ≤ 12 words**.
- **≤ 40 words total** (warning), **60 hard limit** (build fails). Cut words; never
  shrink fonts or pack sentences.
- Pipeline `note`s are for the 1–3 places where the method **breaks** (`risk`) or a
  rule of thumb that **saves** it (`tip`), and only those.
- Use hub `group`s when the facets fall into classes (e.g. builds vs defends the brand):
  colour carries the grouping, so don't repeat it in words.
- Numbers only when they are the point (benchmarks, ratios), copied exactly from the page.

Every claim must be on the page. The drawing summarises; it never adds.

### Step 4 — Build

```sh
python3 <skills-dir>/visual-summary/visual_summary.py build <spec.json> \
  <vault>/wiki/visuals/<slug>.excalidraw.md
```

Fix every `error:`. Treat `warning: overlap` as an error, and the word-count warning as
a prompt to cut.

### Step 5 — Render and look

```sh
python3 <skills-dir>/visual-summary/visual_summary.py render \
  <vault>/wiki/visuals/<slug>.excalidraw.md <scratch>/<slug>.png
```

Open the PNG and check: does it state the one idea from Step 2 at a glance? Is any
text clipped or wrapped awkwardly? Do arrows land on their shapes? If not, revise the
spec and rebuild. Do not hand-edit the generated JSON. (The preview uses the Virgil
font; Obsidian shows Excalifont, which has similar metrics.)

### Step 6 — Embed and record

1. Embed the drawing directly under the page's H1: `![[<slug>.excalidraw]]`.
2. Bump the page's `last_updated` to today, the same date the script stamps as
   `visual-summary-date`. vault-lint (check 6, Condition C) flags the drawing as stale
   once the page's `last_updated` moves past that date.
3. Append to `wiki/log.md`: `## [YYYY-MM-DD] visual-summary | <slug> | <template>, <N> words`.
4. Commit per the vault's commit discipline (pathspec-scoped):
   `content: visual summary — <slug>`.

## What this skill does not do

- It never edits the page's prose, only the embed line and `last_updated`.
- It never runs headless or in scheduled operations. A human reviews every drawing.
- It never hand-places coordinates. A layout the templates can't express is a script change.

## Open items

- vault-lint already skips `*.excalidraw.md` in every page check, and flags stale,
  undated or orphaned drawings (check 6, Condition C).
- Planned: lint the drawings themselves (embeds resolve, word budget, overlaps).
- More layouts (cycle, 2×2 matrix, timeline, tree, funnel…), each validated on real
  pages before it joins the script.
