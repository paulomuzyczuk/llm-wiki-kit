#!/usr/bin/env python3
r"""visual_summary.py — build and check template-driven Excalidraw visual summaries.

The agent never places coordinates. It writes a small JSON spec naming a
template and short labels; this script computes the layout and writes an
Obsidian Excalidraw file (`.excalidraw.md`). Text is bound inside its shape and
arrows are bound to the shapes they connect, so the drawing stays editable by
hand in Obsidian.

Usage:
  visual_summary.py build  <spec.json> <out.excalidraw.md>
  visual_summary.py render <file.excalidraw.md> <out.png>   (headless Chrome)

`build` also runs the checks (word budget, label lengths, overlaps) and exits 1
if any hard limit is broken. `render` is for the human-style visual review the
skill requires before committing.

Env:
  CHROME   Path to a Chrome/Chromium binary for `render`
           (default: /Applications/Google Chrome.app/Contents/MacOS/Google Chrome).

---------------------------------------------------------------------------
SPEC FORMAT (all templates share title / subtitle / page)
---------------------------------------------------------------------------
{
  "template": "pipeline" | "hub" | "contrast",
  "page": "marketing-mix-modeling",           # wikilink target of the summarised page
  "title": "Marketing-mix modeling",
  "subtitle": "optional one-liner",

  # pipeline — ordered stages, each with an optional pitfall/tip note
  "steps": [{"label": "Specify", "detail": "adstock, saturation, ARIMA errors",
             "note": {"text": "No carryover → inflated elasticity", "kind": "risk"}}],

  # hub — one central concept with surrounding facets
  "center": "Brand equity",
  "spokes": [{"label": "Awareness", "detail": "recall, recognition", "group": "build"}],
  # optional "group": spokes in the same group share a colour and get a legend entry

  # contrast — two positions and an optional verdict
  "left":  {"label": "Short-term", "points": ["activation", "..."]},
  "right": {"label": "Long-term",  "points": ["brand-building", "..."]},
  "verdict": "Both: 60/40 brand/activation"
}
note.kind: "risk" (red) | "tip" (green). Default "risk".
"""

from __future__ import annotations

import datetime
import json
import os
import random
import re
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

# ---- budgets (the definition of a *visual* summary) -----------------------
MAX_WORDS = 40  # words in the drawing, excluding title and subtitle (warning)
HARD_MAX_WORDS = 60  # build fails above this
MAX_LABEL_WORDS = 4
MAX_DETAIL_WORDS = 8
MAX_NOTE_WORDS = 12

FONT = 5  # Excalifont (hand-drawn)
LH = 1.25  # line height
CHAR_W = 0.6  # approx glyph width as a fraction of font size
PAD = 14

PALETTE = [  # (fill, stroke)
    ('#e7f5ff', '#1971c2'),
    ('#ebfbee', '#2f9e44'),
    ('#fff9db', '#f08c00'),
    ('#f3f0ff', '#7048e8'),
    ('#fff0f6', '#c2255c'),
    ('#e6fcf5', '#0c8599'),
    ('#fff4e6', '#e8590c'),
    ('#f8f9fa', '#495057'),
]
NOTE_COLORS = {'risk': ('#ffe3e3', '#e03131', '#a61e1e'), 'tip': ('#ebfbee', '#2f9e44', '#1b5e20')}
INK, MUTED = '#1e1e1e', '#666666'


class Scene:
    def __init__(self, seed: int = 7):
        self.rng = random.Random(seed)
        self.elements: list[dict] = []
        self.byid: dict[str, dict] = {}
        self.n = 0

    def _id(self, prefix: str) -> str:
        self.n += 1
        return f'{prefix}{self.n}'

    def _add(self, etype: str, x: float, y: float, w: float, h: float, **kw) -> dict:
        el = {
            'id': kw.pop('id', None) or self._id(etype[:2]),
            'type': etype,
            'x': round(x, 1),
            'y': round(y, 1),
            'width': round(w, 1),
            'height': round(h, 1),
            'angle': 0,
            'strokeColor': INK,
            'backgroundColor': 'transparent',
            'fillStyle': 'solid',
            'strokeWidth': 2,
            'strokeStyle': 'solid',
            'roughness': 1,
            'opacity': 100,
            'groupIds': [],
            'frameId': None,
            'roundness': None,
            'seed': self.rng.randint(1, 2**31),
            'version': 1,
            'versionNonce': self.rng.randint(1, 2**31),
            'isDeleted': False,
            'boundElements': [],
            'updated': 1,
            'link': None,
            'locked': False,
        }
        el.update(kw)
        self.elements.append(el)
        self.byid[el['id']] = el
        return el

    # -- primitives ---------------------------------------------------------
    def text(self, x, y, s, size=18, color=INK, align='left', width=None, container=None) -> dict:
        lines = s.split('\n')
        w = width or max(len(line) for line in lines) * size * CHAR_W
        h = len(lines) * size * LH
        return self._add(
            'text',
            x,
            y,
            w,
            h,
            strokeColor=color,
            text=s,
            originalText=s,
            fontSize=size,
            fontFamily=FONT,
            textAlign=align,
            verticalAlign='middle' if container else 'top',
            containerId=container,
            lineHeight=LH,
            autoResize=True,
        )

    def shape(
        self,
        kind,
        x,
        y,
        w,
        label,
        size=20,
        fill='#ffffff',
        stroke=INK,
        text_color=None,
        min_h=0,
        dashed=False,
    ) -> dict:
        """A rectangle/ellipse/diamond with its label bound inside; height fits the text."""
        inner = w - 2 * PAD - (0.3 * w if kind != 'rectangle' else 0)
        lines = wrap(label, max(4, int(inner / (size * CHAR_W))))
        th = len(lines) * size * LH
        h = max(min_h, th + 2 * PAD + (0.35 * th if kind != 'rectangle' else 0))
        box = self._add(
            kind,
            x,
            y,
            w,
            h,
            backgroundColor=fill,
            strokeColor=stroke,
            roundness={'type': 3} if kind == 'rectangle' else {'type': 2},
            strokeStyle='dashed' if dashed else 'solid',
        )
        tw = min(inner, max(len(line) for line in lines) * size * CHAR_W)
        t = self.text(
            x + (w - tw) / 2,
            y + (h - th) / 2,
            '\n'.join(lines),
            size=size,
            color=text_color or stroke,
            align='center',
            width=tw,
            container=box['id'],
        )
        box['boundElements'].append({'type': 'text', 'id': t['id']})
        return box

    def connect(self, a: dict, b: dict, color=INK, dashed=False, head=True, label=None) -> dict:
        """Arrow from the edge of a to the edge of b, bound to both."""
        (x1, y1), (x2, y2) = edge_point(a, centre(b)), edge_point(b, centre(a))
        arr = self._add(
            'arrow',
            x1,
            y1,
            x2 - x1,
            y2 - y1,
            strokeColor=color,
            points=[[0, 0], [round(x2 - x1, 1), round(y2 - y1, 1)]],
            lastCommittedPoint=None,
            startArrowhead=None,
            endArrowhead='arrow' if head else None,
            startBinding={'elementId': a['id'], 'focus': 0, 'gap': 6},
            endBinding={'elementId': b['id'], 'focus': 0, 'gap': 6},
            strokeStyle='dashed' if dashed else 'solid',
            roundness={'type': 2},
        )
        a['boundElements'].append({'type': 'arrow', 'id': arr['id']})
        b['boundElements'].append({'type': 'arrow', 'id': arr['id']})
        return arr

    def header(self, spec: dict) -> float:
        self.text(0, 0, spec['title'], size=34)
        y = 50
        if spec.get('subtitle'):
            self.text(0, y, spec['subtitle'], size=18, color=MUTED)
            y += 30
        return y + 40


def wrap(s: str, width: int) -> list[str]:
    out: list[str] = []
    for para in s.split('\n'):
        out += textwrap.wrap(para, width=width, break_long_words=False) or ['']
    return out


def centre(el: dict) -> tuple[float, float]:
    return el['x'] + el['width'] / 2, el['y'] + el['height'] / 2


def edge_point(el: dict, towards: tuple[float, float]) -> tuple[float, float]:
    """Point where the line from el's centre to `towards` leaves el's bounding box."""
    cx, cy = centre(el)
    dx, dy = towards[0] - cx, towards[1] - cy
    if dx == 0 and dy == 0:
        return cx, cy
    if el['type'] == 'ellipse':
        a, b = el['width'] / 2, el['height'] / 2
        s = 1 / ((dx / a) ** 2 + (dy / b) ** 2) ** 0.5
        return cx + dx * s, cy + dy * s
    sx = (el['width'] / 2) / abs(dx) if dx else float('inf')
    sy = (el['height'] / 2) / abs(dy) if dy else float('inf')
    s = min(sx, sy)
    return cx + dx * s, cy + dy * s


# ---- templates ------------------------------------------------------------
def tpl_pipeline(sc: Scene, spec: dict) -> None:
    """Stages left to right; pitfall/tip notes sit above their stage, details below."""
    steps = spec['steps']
    if not 2 <= len(steps) <= 6:
        raise SpecError('pipeline needs 2–6 steps')
    y = sc.header(spec)
    W, GAP = 230, 80
    notes = {}
    for i, st in enumerate(steps):
        note = st.get('note')
        if note:
            kind = note.get('kind', 'risk')
            fill, stroke, ink = NOTE_COLORS[kind]
            notes[i] = sc.shape(
                'rectangle',
                i * (W + GAP),
                y,
                W,
                ('⚠ ' if kind == 'risk' else '✓ ') + note['text'],
                size=17,
                fill=fill,
                stroke=stroke,
                text_color=ink,
                dashed=True,
            )
    if notes:
        y += max(n['height'] for n in notes.values()) + 70
    boxes = [
        sc.shape(
            'rectangle',
            i * (W + GAP),
            y,
            W,
            st['label'],
            size=24,
            fill=PALETTE[i % len(PALETTE)][0],
            stroke=PALETTE[i % len(PALETTE)][1],
            min_h=90,
        )
        for i, st in enumerate(steps)
    ]
    row_h = max(b['height'] for b in boxes)
    for b in boxes:  # equalise heights so the flow arrows run level
        grow = row_h - b['height']
        b['height'] = row_h
        sc.byid[b['boundElements'][0]['id']]['y'] += grow / 2
    for a, b in zip(boxes, boxes[1:], strict=False):
        sc.connect(a, b, color=a['strokeColor'])
    for i, n in notes.items():
        sc.connect(n, boxes[i], color=n['strokeColor'], dashed=True)
    for i, st in enumerate(steps):
        if st.get('detail'):
            lines = wrap(st['detail'], int(W / (16 * CHAR_W)))
            sc.text(
                i * (W + GAP),
                y + row_h + 14,
                '\n'.join(lines),
                size=16,
                color=MUTED,
                align='center',
                width=W,
            )


def tpl_hub(sc: Scene, spec: dict) -> None:
    import math

    spokes = spec['spokes']
    if not 3 <= len(spokes) <= 8:
        raise SpecError('hub needs 3–8 spokes')
    y0 = sc.header(spec)
    RX, RY, W = 440, 250, 220
    cx, cy = RX + W / 2, y0 + RY + 60
    hub = sc.shape(
        'ellipse',
        cx - 150,
        cy - 60,
        300,
        spec['center'],
        size=26,
        fill='#f8f9fa',
        stroke=INK,
        min_h=120,
    )
    groups = list(dict.fromkeys(sp['group'] for sp in spokes if sp.get('group')))
    for i, sp in enumerate(spokes):
        ang = -math.pi / 2 + 2 * math.pi * i / len(spokes)
        # spokes sharing a group share a colour; ungrouped spokes each get their own
        fill, stroke = PALETTE[groups.index(sp['group']) if sp.get('group') else i % len(PALETTE)]
        px, py = cx + RX * math.cos(ang), cy + RY * math.sin(ang)
        b = sc.shape(
            'rectangle',
            px - W / 2,
            py - 40,
            W,
            sp['label'],
            size=22,
            fill=fill,
            stroke=stroke,
            min_h=70,
        )
        sc.connect(hub, b, color=stroke, head=False)
        if sp.get('detail'):
            lines = wrap(sp['detail'], int(W / (16 * CHAR_W)))
            below = py >= cy - 1
            ty = b['y'] + b['height'] + 8 if below else b['y'] - 8 - len(lines) * 16 * LH
            sc.text(b['x'], ty, '\n'.join(lines), size=16, color=MUTED, align='center', width=W)
    for k, g in enumerate(groups):  # legend, bottom-left
        fill, stroke = PALETTE[k]
        ly = cy + RY + 110 + k * 40
        sc._add(
            'rectangle',
            0,
            ly,
            28,
            28,
            backgroundColor=fill,
            strokeColor=stroke,
            roundness={'type': 3},
        )
        sc.text(40, ly + 2, g, size=18, color=stroke)


def tpl_contrast(sc: Scene, spec: dict) -> None:
    y0 = sc.header(spec)
    W, GAP = 360, 140
    cols = []
    for j, side in enumerate([spec['left'], spec['right']]):
        fill, stroke = PALETTE[0] if j == 0 else PALETTE[4]
        x = j * (W + GAP)
        head = sc.shape(
            'rectangle', x, y0, W, side['label'], size=26, fill=fill, stroke=stroke, min_h=70
        )
        y = y0 + head['height'] + 24
        for p in side.get('points', []):
            b = sc.shape('rectangle', x + 20, y, W - 40, p, size=18, fill='#ffffff', stroke=stroke)
            y += b['height'] + 16
        cols.append(y)
    sc.text(W + GAP / 2 - 22, y0 + 18, 'vs', size=30, color=MUTED)
    if spec.get('verdict'):
        sc.shape(
            'rectangle',
            0,
            max(cols) + 30,
            2 * W + GAP,
            spec['verdict'],
            size=22,
            fill='#fff9db',
            stroke='#f08c00',
            text_color=INK,
        )


TEMPLATES = {'pipeline': tpl_pipeline, 'hub': tpl_hub, 'contrast': tpl_contrast}


class SpecError(Exception):
    pass


# ---- checks -------------------------------------------------------------
def words(s: str) -> int:
    return len(re.findall(r'\S+', s))


def check_spec(spec: dict) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    labels, details, notes = [], [], []
    t = spec.get('template')
    if t not in TEMPLATES:
        return [f'unknown template {t!r}; choose one of {sorted(TEMPLATES)}'], []
    for k in ('title', 'page'):
        if not spec.get(k):
            errors.append(f'missing {k!r}')
    if t == 'pipeline':
        for s in spec.get('steps', []):
            labels.append(s['label'])
            details.append(s.get('detail', ''))
            if s.get('note'):
                notes.append(s['note']['text'])
    elif t == 'hub':
        labels.append(spec.get('center', ''))
        for s in spec.get('spokes', []):
            labels.append(s['label'])
            details.append(s.get('detail', ''))
        labels += list(dict.fromkeys(s['group'] for s in spec.get('spokes', []) if s.get('group')))
    elif t == 'contrast':
        for side in (spec.get('left', {}), spec.get('right', {})):
            labels.append(side.get('label', ''))
            details += side.get('points', [])
        notes.append(spec.get('verdict', ''))
    for label in labels:
        if words(label) > MAX_LABEL_WORDS:
            errors.append(f'label over {MAX_LABEL_WORDS} words: {label!r}')
    for d in details:
        if words(d) > MAX_DETAIL_WORDS:
            errors.append(f'detail/point over {MAX_DETAIL_WORDS} words: {d!r}')
    for n in notes:
        if words(n) > MAX_NOTE_WORDS:
            errors.append(f'note/verdict over {MAX_NOTE_WORDS} words: {n!r}')
    total = sum(words(x) for x in labels + details + notes)
    if total > HARD_MAX_WORDS:
        errors.append(
            f"{total} words in the drawing (hard limit {HARD_MAX_WORDS}); cut, don't shrink fonts"
        )
    elif total > MAX_WORDS:
        warnings.append(f'{total} words in the drawing (target ≤ {MAX_WORDS})')
    return errors, warnings


def check_overlaps(elements: list[dict]) -> list[str]:
    """Pairs of visible, unbound elements whose boxes intersect."""
    solid = [e for e in elements if e['type'] != 'arrow' and not e.get('containerId')]

    def hit(a, b, m=4):
        return not (
            a['x'] + a['width'] + m <= b['x']
            or b['x'] + b['width'] + m <= a['x']
            or a['y'] + a['height'] + m <= b['y']
            or b['y'] + b['height'] + m <= a['y']
        )

    out = []
    for i, a in enumerate(solid):
        for b in solid[i + 1 :]:
            if hit(a, b):
                out.append(f'overlap: {a["type"]} {a["id"]} ↔ {b["type"]} {b["id"]}')
    return out


# ---- file format ---------------------------------------------------------
def to_markdown(spec: dict, elements: list[dict]) -> str:
    scene = {
        'type': 'excalidraw',
        'version': 2,
        'source': 'https://github.com/zsviczian/obsidian-excalidraw-plugin',
        'elements': elements,
        'appState': {'gridSize': None, 'viewBackgroundColor': '#ffffff'},
        'files': {},
    }
    texts = '\n\n'.join(f'{e["text"]} ^{e["id"]}' for e in elements if e['type'] == 'text')
    return f"""---
excalidraw-plugin: parsed
tags: [excalidraw, visual-summary]
visual-summary-of: "[[{spec['page']}]]"
visual-summary-template: {spec['template']}
visual-summary-date: {datetime.date.today().isoformat()}
---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==

Visual summary of [[{spec['page']}]] — generated by llm-wiki-kit/visual-summary.

# Excalidraw Data

## Text Elements
{texts}

%%
## Drawing
```json
{json.dumps(scene, indent=1, ensure_ascii=False)}
```
%%
"""


def read_scene(path: Path) -> dict:
    m = re.search(r'```json\n(.*?)\n```', path.read_text(encoding='utf-8'), re.S)
    if not m:
        raise SystemExit(f'error: no uncompressed ```json drawing block in {path}')
    return json.loads(m.group(1))


# ---- commands ------------------------------------------------------------
def cmd_build(spec_path: str, out_path: str) -> int:
    spec = json.loads(Path(spec_path).read_text(encoding='utf-8'))
    errors, warnings = check_spec(spec)
    for w in warnings:
        print(f'warning: {w}', file=sys.stderr)
    if errors:
        for e in errors:
            print(f'error: {e}', file=sys.stderr)
        return 1
    sc = Scene()
    try:
        TEMPLATES[spec['template']](sc, spec)
    except SpecError as e:
        print(f'error: {e}', file=sys.stderr)
        return 1
    overlaps = check_overlaps(sc.elements)
    for o in overlaps:
        print(f'warning: {o}', file=sys.stderr)
    Path(out_path).write_text(to_markdown(spec, sc.elements), encoding='utf-8')
    print(f'built: {out_path} ({len(sc.elements)} elements, template {spec["template"]})')
    return 0


RENDER_HTML = """<!doctype html><html><head><meta charset="utf-8">
<script>window.EXCALIDRAW_ASSET_PATH="https://unpkg.com/@excalidraw/excalidraw@0.17.6/dist/";</script>
<script src="https://unpkg.com/react@18.2.0/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
<script src="https://unpkg.com/@excalidraw/excalidraw@0.17.6/dist/excalidraw.production.min.js"></script>
<style>body{margin:0;background:#fff}</style></head><body><div id="o"></div><script>
const scene=__SCENE__;
// The 0.17 bundle predates Excalifont (5); preview with Virgil (1), which has similar metrics.
scene.elements.forEach(e=>{if(e.type==="text"&&e.fontFamily===5)e.fontFamily=1;});
ExcalidrawLib.exportToSvg({elements:scene.elements,appState:{exportBackground:true,viewBackgroundColor:"#fff",exportPadding:24},files:{}})
 .then(svg=>{document.getElementById("o").appendChild(svg);})
 .catch(e=>{document.getElementById("o").textContent="ERR "+e});
</script></body></html>"""


def cmd_render(in_path: str, out_png: str) -> int:
    scene = read_scene(Path(in_path))
    els = [e for e in scene['elements'] if not e.get('isDeleted')]
    w = max(e['x'] + e['width'] for e in els) - min(e['x'] for e in els) + 60
    h = max(e['y'] + e['height'] for e in els) - min(e['y'] for e in els) + 60
    chrome = os.environ.get(
        'CHROME', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    )
    with tempfile.TemporaryDirectory() as td:
        html = Path(td) / 'render.html'
        html.write_text(RENDER_HTML.replace('__SCENE__', json.dumps(scene)), encoding='utf-8')
        subprocess.run(
            [
                chrome,
                '--headless=new',
                '--disable-gpu',
                '--hide-scrollbars',
                '--virtual-time-budget=15000',
                f'--window-size={int(w)},{int(h)}',
                f'--screenshot={Path(out_png).resolve()}',
                html.as_uri(),
            ],
            check=True,
            capture_output=True,
        )
    print(f'rendered: {out_png}')
    return 0


def main(argv: list[str]) -> int:
    if len(argv) == 3 and argv[0] == 'build':
        return cmd_build(argv[1], argv[2])
    if len(argv) == 3 and argv[0] == 'render':
        return cmd_render(argv[1], argv[2])
    print(__doc__.split('---')[0].strip(), file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
