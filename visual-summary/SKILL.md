---
name: visual-summary
description: >
  Draws Excalidraw visual summaries of a single LLM-wiki topic page: a page
  overview under `## Visual summary` that covers the whole page, plus optional
  drawings for individual sections. The agent never
  places coordinates: it picks a layout template (map, pipeline, hub, contrast, cycle,
  matrix, timeline, tree, funnel/pyramid, venn, spectrum, causal-map), writes a short JSON spec of
  labels, and the co-located visual_summary.py builds an Obsidian
  `.excalidraw.md` file with text bound in shapes, arrows bound to them and
  details grouped with their shape (editable by hand), checks word budgets,
  overlaps and arrow crossings, and renders a PNG for review. Use when the user
  asks for a "visual summary", "diagram", "drawing" or "Excalidraw" of a wiki
  page, or to "visualise" a topic. One invocation = one page. See MZY-315, MZY-347, MZY-348.
---

# Visual Summary

> **Status:** twelve templates, validated on real topic pages (MZY-315,
> MZY-347, MZY-348). Not wired into the template `CLAUDE.md` or scheduled operations: a human
> reviews every drawing.

A visual summary is **not a diagram of the page's text**: the shapes carry the meaning,
words only label them. A page gets two kinds of drawing:

- **Page overview** (one per page, required): the whole page's ideas in one picture,
  under a `## Visual summary` heading. On a page with several sections' worth of ideas
  this is a **`map`** (≤ 200 words): the page's stages or facets as lanes, each with up
  to three cards (a fact, a risk or a tip) that link to the section they come from. On a
  short page whose sections all serve one idea, a single-idea template is the overview.
- **Section drawings** (optional, any number): one concept from one section, embedded
  under that section's heading, drawn with a single-idea template (**≤ 100 words**):
  order (pipeline), composition (hub), tension (contrast), feedback (cycle),
  classification (matrix), time (timeline), hierarchy (tree), rank (funnel/pyramid),
  overlap (venn), scale (spectrum) or causation (causal-map). Draw one only where the section has its own shape worth seeing (a
  decision tree, a before/after, a set of model terms), not for every section.

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

### Step 2 — Read the page and plan the drawings

Read the whole page. Write down, for yourself, the sentence a reader should leave with
and the page's main stages or facets: these become the overview's verdict and lanes.
Then pick the overview's shape (a `map` unless one idea covers the whole page) and list
the sections, if any, that deserve their own drawing, picking each one's shape:

| The page or section is mainly about… | Template | Validated on |
|---|---|---|
| A whole page with several sections' worth of ideas (overview only) | `map` | release-engineering |
| A process or method someone carries out, step by step | `pipeline` | release-engineering |
| One concept and its unranked parts, criteria or facets | `hub` | project-governance-elements |
| Two positions whose differences are the point | `contrast` | long-run-maintenance-effects |
| A loop: the last stage feeds the first | `cycle` | code-review-process, experimentation-and-roadmap |
| Two binary dimensions crossing into four named cases | `matrix` | project-growth-strategies, build-versus-buy |
| Phases something passes through over time | `timeline` | project-life-cycle, open-source-adoption |
| A taxonomy or decision tree | `tree` | estimation-methods-taxonomy, choosing-a-license |
| Ranked stages that shrink, or levels that build up | `funnel` (`shape: pyramid`) | contributor-acquisition-funnel, contributor-motivation-pyramid |
| Two lenses whose common ground matters as much as their differences | `venn` | copyleft-vs-permissive-licenses, long-run-maintenance-effects |
| A few values on one scale, where the gaps between them are the point | `spectrum` | release-engineering (support-window benchmarks), license-permissiveness (permissiveness scale) |
| What drives an outcome and in which direction, or which variables cause which (a DAG) | `causal-map` | contributor-churn-factors, build-failure-causes (overview and the flaky-test DAG) |

Section drawings validated on release-engineering: `hub` (build tooling),
`contrast` (branching policy), `tree` (choosing a branching model), `spectrum`
(support-window benchmarks).

`visual_summary.py list` prints each template's *use when* and *not when*. Common
near-misses: a pipeline is steps someone **does**, a timeline is phases something
**goes through**; a contrast is for opposition, a venn when the page argues the two
**share** more than they differ (long-run-maintenance-effects reads better as a venn);
a causal-map is for arrows that mean *causes*, not *comes next* (pipeline) or *is part of*
(hub), and a loop belongs in a cycle (causal-map refuses one).

If none fits, stop and tell the user which shape the page needs. Do not force a
template. New templates are added to the script, not improvised.

### Step 3 — Write the spec

Get the fields and a worked example for the chosen template:

```sh
python3 <skills-dir>/visual-summary/visual_summary.py schema <template>
```

Write the spec JSON to a scratch location (never into the vault). Limits, enforced by
the script:

- **Labels ≤ 4 words**: the noun phrase that names the box. Tree edge labels ≤ 3 words.
- **Details / points ≤ 8 words**, **notes / verdict ≤ 12 words**.
- **Total words**: single-idea templates ≤ 100, `map` ≤ 200; the build fails above.
  These are ceilings, not targets: the per-label limits above keep each box short, and
  fewer words read faster. Cut words; never shrink fonts or pack sentences. Titles and
  subtitles are not counted.
- `map`: 2–7 lanes of 1–3 cards. A card is one idea from one section: a `fact`
  (default), a `risk` (where the method breaks) or a `tip` (what saves it). Give each
  card the `section` it comes from (the heading, or a unique prefix of it): the card
  links there, and the build warns when no heading, or more than one, matches. Use the
  `verdict` for the page's one sentence. `ordered: false` when the lanes are facets
  rather than a flow.
- A section drawing names its `section` too (same matching), so the drawing records
  which heading it summarises.
- Pipeline `note`s are for the 1–3 places where the method **breaks** (`risk`) or a
  rule of thumb that **saves** it (`tip`), and only those. The script prefixes them
  with "Risk:" / "Tip:".
- Use hub `group`s when the facets fall into classes (e.g. builds vs defends the brand):
  colour carries the grouping, so don't repeat it in words.
- Timeline `weight`s only when widths carry meaning (e.g. adopter shares); a `gap`
  marks a real break the page names (Moore's chasm); a `curve` only when the page
  draws one (the bell-shaped PLC).
- `causal-map`: give each edge a `sign` (`+` raises, `-` lowers, `mixed`) only when the
  page states the direction; the arrow shows it as a word in the sign's colour. Mark
  unobserved variables `hidden` (dashed, as in a DAG), or set `dashed: true` on an edge
  and say what dashed means in `dashed_means` (e.g. weak evidence). Columns follow
  causal depth; a chain more than three deep reads better with `direction: "down"`.
  Edge labels are fine on a node that four or more arrows converge on: the build moves
  each label to its source end. When sources each feed two such nodes, keep
  `direction: "right"`: in `down` their labels sit side by side and the drawing gets wide.
- Numbers only when they are the point (benchmarks, ratios, cell values), copied
  exactly from the page.
- Plain words over symbols: Excalifont lacks arrows and maths glyphs (→, ≈, Γ). The
  build warns when a label uses one.

Every claim must be on the page. The drawing summarises; it never adds.

### Step 4 — Build

```sh
python3 <skills-dir>/visual-summary/visual_summary.py build <spec.json> \
  <vault>/wiki/visuals/<slug>.excalidraw.md
```

Name section drawings `<slug>--<key>.excalidraw.md` (e.g.
`release-engineering--branching`). Fix every `error:`. Treat `warning: overlap`,
`warning: arrow … crosses` and `warning: section …` as errors (shorten the label, drop a
detail, fix the heading), and the word-count warning as a prompt to cut.

The build prints the embed line with the drawing's width (`embed: ![[<name>|<px>]]`).
The plugin's default embed width is 400px, which shrinks a wide drawing to unreadable
text, so always embed with that width: the page column caps it, and the drawing then
fills the column. Keep drawings under ~1,000px wide so text stays legible at column
width (trees grow left to right by default for this reason; `direction: "down"` draws
them top-down, and does the same for a deep causal-map).

The file stores the spec (`visual_summary.py spec <drawing>` prints it back, for a
refresh) and tags every generated element with `customData.visualSummary.specHash`,
so a later check can tell generated elements from hand-added ones.

### Step 5 — Render and look

```sh
python3 <skills-dir>/visual-summary/visual_summary.py render \
  <vault>/wiki/visuals/<slug>.excalidraw.md <scratch>/<slug>.png
python3 <skills-dir>/visual-summary/visual_summary.py render \
  <vault>/wiki/visuals/<slug>.excalidraw.md <scratch>/<slug>-shapes.png --no-text
```

The renderer is Excalidraw's own exporter running headless under Node
(`npx mcp-excalidraw-server`, MIT), with Excalifont, the font Obsidian shows. It needs
Node ≥ 20; the first run downloads the package. Override with `EXCALIDRAW_RENDER`.

Open both PNGs and check:

1. **Glance test** (full render): does it state the one idea from Step 2 in a few
   seconds? Is any text clipped, crowded or wrapped awkwardly? Do arrows land on
   their shapes?
2. **Isomorphism test** (`--no-text`): with every word removed, does the structure
   alone still say *lanes of cards / flow / hub / loop / 2×2 / phases / tree / funnel /
   overlap / points on a scale / arrows converging on an outcome*? If the
   bare shapes could be any diagram, the template is wrong for this page.

If either fails, revise the spec and rebuild. Do not hand-edit the generated JSON.

### Step 6 — Embed and record

1. Embed the overview in a `## Visual summary` section placed just before the page's
   first `##` heading (after the lead paragraphs):

   ```markdown
   ## Visual summary

   ![[<slug>.excalidraw|<px>]]
   ```

2. Embed each section drawing on its own line directly under its heading:
   `![[<slug>--<key>.excalidraw|<px>]]`.
3. Bump the page's `last_updated` to today, the same date the script stamps as
   `visual-summary-date`. vault-lint (check 6, Condition C) flags a drawing as stale
   once the page's `last_updated` moves past that date.
4. Append one line per drawing to `wiki/log.md`:
   `## [YYYY-MM-DD] visual-summary | <name> | <template>, <N> words, page overview`
   (or `…, section: <heading>`).
5. Commit per the vault's commit discipline (pathspec-scoped):
   `content: visual summary — <slug>`.

### Refreshing a drawing

The kit's plugin installer turns off the Excalidraw plugin's `compress` setting, so
drawings edited in Obsidian stay plain JSON. With it on, any edit, even a single drag,
re-saves the `## Drawing` block as `compressed-json` (LZString base64). `render` and
`spec` read both forms; `build` always writes plain JSON, so a rebuild undoes the
compression.

`visual_summary.py spec <drawing> > <scratch>/spec.json` recovers the spec; re-read
the page, edit the spec, then rebuild over the drawing and repeat Steps 5–6. A rebuild
discards hand edits to the drawing, so check first whether anyone edited it in
Obsidian.

## What this skill does not do

- It never edits the page's prose, only the `## Visual summary` section, the section
  embed lines and `last_updated`.
- It never runs headless or in scheduled operations. A human reviews every drawing.
- It never hand-places coordinates. A layout the templates can't express is a script change.

## Open items

- vault-lint already skips `*.excalidraw.md` in every page check, and flags stale,
  undated or orphaned drawings (check 6, Condition C).
- Planned: lint the drawings themselves (embeds resolve, word budget, overlaps,
  hand-edited since generated via `specHash`). (MZY-316)
