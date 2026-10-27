#!/usr/bin/env python3
r"""visual_summary.py — build and check template-driven Excalidraw visual summaries.

The agent never places coordinates. It writes a small JSON spec naming a
template and short labels; this script computes the layout and writes an
Obsidian Excalidraw file (`.excalidraw.md`). Text is bound inside its shape,
arrows are bound to the shapes they connect, and free-standing labels are
grouped with their backdrop, so the drawing stays editable by hand in Obsidian.

Usage:
  visual_summary.py list                                   templates and when to use each
  visual_summary.py schema <template>                      fields and a worked example
  visual_summary.py build  <spec.json> <out.excalidraw.md>
  visual_summary.py render <file.excalidraw.md> <out.png> [--no-text]
  visual_summary.py spec   <file.excalidraw.md>            print the spec a drawing was built from

`build` runs the checks (word budget, label lengths, overlaps, arrows crossing
other elements) and exits 1 if any hard limit is broken. It stores the spec in
the drawing and tags every generated element with
`customData.visualSummary.specHash`, so later tools can tell generated
elements from hand-added ones. `render` draws a PNG for the visual review;
`--no-text` drops all text, for the isomorphism test (does the structure alone
still say it?).

Env:
  EXCALIDRAW_RENDER  Command prefix for `render`
                     (default: npx -y mcp-excalidraw-server@2.1.2 render).
                     The renderer is Excalidraw's own SVG exporter running headless
                     under Node (MIT, github.com/yctimlin/mcp_excalidraw); it needs
                     Node >= 20 and, on first use, network access to fetch the package.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import math
import os
import random
import re
import shlex
import subprocess
import sys
import tempfile
import textwrap
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

# ---- budgets (the definition of a *visual* summary) -----------------------
MAX_WORDS = 100  # words in a single-idea drawing, excluding title and subtitle; build fails above
MAP_MAX_WORDS = 200  # the same for a page-overview map
MAX_LABEL_WORDS = 4
MAX_EDGE_WORDS = 3  # tree edge labels sit on an arrow
MAX_DETAIL_WORDS = 8
MAX_NOTE_WORDS = 12

FONT = 5  # Excalifont (hand-drawn)
LH = 1.25  # line height
CHAR_W = 0.6  # approx glyph width as a fraction of font size
PAD = 14
DETAIL = 16  # font size of details; nothing in a drawing is smaller

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
VERDICT = ('#fff9db', '#f08c00')
INK, MUTED = '#1e1e1e', '#666666'
RENDER_DEFAULT = 'npx -y mcp-excalidraw-server@2.1.2 render'
SPEC_BLOCK = re.compile(r'## Visual summary spec\n```json\n(.*?)\n```', re.S)


class SpecError(Exception):
    pass


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
    def text(
        self, x, y, s, size=18, color=INK, align='left', width=None, container=None, **kw
    ) -> dict:
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
            **kw,
        )

    def para(self, x, y, s, width, size=DETAIL, color=MUTED, align='center', **kw) -> dict:
        """Free-standing text wrapped to `width` and aligned within it.

        Excalidraw shrinks an auto-sized text box to its widest line and keeps x,
        so the box is placed by its estimated width rather than relying on
        textAlign over the full width.
        """
        lines = wrap(s, max(4, int(width / (size * CHAR_W))))
        est = min(width, max(len(line) for line in lines) * size * CHAR_W)
        shift = {'center': (width - est) / 2, 'right': width - est}.get(align, 0)
        return self.text(
            x + shift, y, '\n'.join(lines), size=size, color=color, align=align, width=est, **kw
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

    def set_height(self, box: dict, h: float) -> None:
        """Grow a shape to height h, keeping its bound label centred."""
        grow = h - box['height']
        box['height'] = h
        for b in box['boundElements']:
            if b['type'] == 'text':
                self.byid[b['id']]['y'] += grow / 2

    def connect(
        self,
        a: dict,
        b: dict,
        color=INK,
        dashed=False,
        head=True,
        bulge=None,
        label=None,
        sideways=False,
        ends=None,
        via=None,
        label_size=DETAIL,
    ) -> dict:
        """Arrow from the edge of a to the edge of b, bound to both.

        `bulge` = (cx, cy, d) curves the arrow by pushing its midpoint d px away
        from the point (cx, cy); `label` binds a short text to the arrow;
        `sideways` runs it from a's right side to b's left side; `ends` = ((x1, y1),
        (x2, y2)) fixes both end points; `via` lists waypoints it passes through.
        """
        if ends:
            (x1, y1), (x2, y2) = ends
        elif sideways:
            x1, y1 = a['x'] + a['width'], centre(a)[1]
            x2, y2 = b['x'], centre(b)[1]
        else:
            (x1, y1), (x2, y2) = edge_point(a, centre(b)), edge_point(b, centre(a))
        pts = [[0, 0], [round(x2 - x1, 1), round(y2 - y1, 1)]]
        if bulge:
            cx, cy, d = bulge
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            k = d / (math.hypot(mx - cx, my - cy) or 1)
            pts.insert(1, [round(mx + (mx - cx) * k - x1, 1), round(my + (my - cy) * k - y1, 1)])
        for i, (vx, vy) in enumerate(via or []):
            pts.insert(1 + i, [round(vx - x1, 1), round(vy - y1, 1)])
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        arr = self._add(
            'arrow',
            x1,
            y1,
            max(xs) - min(xs),
            max(ys) - min(ys),
            strokeColor=color,
            points=pts,
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
        if label:
            size = label_size
            tw = len(label) * size * CHAR_W
            # where Excalidraw puts a bound label: the middle point, or the middle segment's midpoint
            n = len(pts)
            (px, py), (qx, qy) = (
                (pts[n // 2], pts[n // 2]) if n % 2 else (pts[n // 2 - 1], pts[n // 2])
            )
            mx, my = x1 + (px + qx) / 2, y1 + (py + qy) / 2
            t = self.text(
                mx - tw / 2,
                my - size * LH / 2,
                label,
                size=size,
                color=color,
                align='center',
                width=tw,
                container=arr['id'],
            )
            arr['boundElements'].append({'type': 'text', 'id': t['id']})
        return arr

    def header(self, spec: dict) -> float:
        self.text(0, 0, spec['title'], size=34)
        y = 50
        if spec.get('subtitle'):
            self.text(0, y, spec['subtitle'], size=18, color=MUTED)
            y += 30
        return y + 40

    def verdict(self, x: float, y: float, w: float, s: str) -> dict:
        return self.shape(
            'rectangle', x, y, w, s, size=22, fill=VERDICT[0], stroke=VERDICT[1], text_color=INK
        )

    def group(self, *els: dict) -> None:
        """Group elements (and their bound labels) so they move together."""
        gid = self._id('g')
        for e in els:
            e['groupIds'].append(gid)
            for b in e['boundElements']:
                if b['type'] == 'text':
                    self.byid[b['id']]['groupIds'].append(gid)


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


def backdrop(el: dict) -> dict:
    """Mark a shape as a deliberate background: free text may sit on it."""
    el['_role'] = 'backdrop'
    return el


def extent(el: dict) -> tuple[float, float, float, float]:
    """(x0, y0, x1, y1) actually covered: an arrow's points may run up or left of x, y."""
    if el.get('points'):
        xs, ys = [el['x'] + p[0] for p in el['points']], [el['y'] + p[1] for p in el['points']]
        return min(xs), min(ys), max(xs), max(ys)
    return el['x'], el['y'], el['x'] + el['width'], el['y'] + el['height']


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
                ('Risk: ' if kind == 'risk' else 'Tip: ') + note['text'],
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
        sc.set_height(b, row_h)
    for a, b in zip(boxes, boxes[1:], strict=False):
        sc.connect(a, b, color=a['strokeColor'])
    for i, n in notes.items():
        sc.connect(n, boxes[i], color=n['strokeColor'], dashed=True)
    for i, st in enumerate(steps):
        if st.get('detail'):
            sc.group(boxes[i], sc.para(i * (W + GAP), y + row_h + 14, st['detail'], W))


def tpl_hub(sc: Scene, spec: dict) -> None:
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
            lines = wrap(sp['detail'], int(W / (DETAIL * CHAR_W)))
            below = py >= cy - 1
            ty = b['y'] + b['height'] + 8 if below else b['y'] - 8 - len(lines) * DETAIL * LH
            sc.group(b, sc.para(b['x'], ty, sp['detail'], W))
    for k, g in enumerate(groups):  # legend, bottom-left
        fill, stroke = PALETTE[k]
        ly = cy + RY + 110 + k * 40
        sw = sc._add(
            'rectangle',
            0,
            ly,
            28,
            28,
            backgroundColor=fill,
            strokeColor=stroke,
            roundness={'type': 3},
        )
        sc.group(sw, sc.text(40, ly + 2, g, size=18, color=stroke))


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
        sc.verdict(0, max(cols) + 30, 2 * W + GAP, spec['verdict'])


def tpl_cycle(sc: Scene, spec: dict) -> None:
    """Stages round an ellipse, clockwise from the top, each arrow curving outward."""
    stages = spec['stages']
    if not 3 <= len(stages) <= 6:
        raise SpecError('cycle needs 3–6 stages')
    y0 = sc.header(spec)
    RX, RY, W, SIDE = 230, 220, 200, 160  # SIDE: width of details beside the ring
    cx, cy = RX + W / 2 + SIDE + 14, y0 + RY + 90
    boxes = []
    for i, st in enumerate(stages):
        ang = -math.pi / 2 + 2 * math.pi * i / len(stages)
        fill, stroke = PALETTE[i % len(PALETTE)]
        px, py = cx + RX * math.cos(ang), cy + RY * math.sin(ang)
        b = sc.shape(
            'rectangle', px - W / 2, py - 36, W, st['label'], size=22, fill=fill, stroke=stroke
        )
        boxes.append((b, st, py))
    h = max(b['height'] for b, _, _ in boxes)
    for b, _, _ in boxes:
        sc.set_height(b, max(h, 72))
    for i, (b, _, _) in enumerate(boxes):
        nxt = boxes[(i + 1) % len(boxes)][0]
        sc.connect(b, nxt, color=b['strokeColor'], bulge=(cx, cy, 34))
    for b, st, _ in boxes:
        if not st.get('detail'):
            continue
        bx, by = centre(b)
        lines = wrap(st['detail'], int(W / (DETAIL * CHAR_W)))
        th = len(lines) * DETAIL * LH
        if abs(bx - cx) < W / 2:  # top or bottom of the ring
            ty = b['y'] + b['height'] + 8 if by > cy else b['y'] - 8 - th
            sc.group(b, sc.para(b['x'], ty, st['detail'], W))
        elif bx > cx:  # right side: detail to the right
            lines = wrap(st['detail'], int(SIDE / (DETAIL * CHAR_W)))
            th = len(lines) * DETAIL * LH
            sc.group(b, sc.para(b['x'] + W + 14, by - th / 2, st['detail'], SIDE, align='left'))
        else:
            lines = wrap(st['detail'], int(SIDE / (DETAIL * CHAR_W)))
            th = len(lines) * DETAIL * LH
            sc.group(b, sc.para(b['x'] - SIDE - 14, by - th / 2, st['detail'], SIDE, align='right'))
    if spec.get('center'):
        sc.para(cx - 130, cy - 24, spec['center'], 260, size=22, color=INK)


def tpl_matrix(sc: Scene, spec: dict) -> None:
    """A 2×2: two labelled axes (low → high) and four labelled quadrants."""
    q = spec['quadrants']
    keys = ('top_left', 'top_right', 'bottom_left', 'bottom_right')
    missing = [k for k in keys if k not in q]
    if missing:
        raise SpecError(f'matrix needs quadrants {", ".join(missing)}')
    y0 = sc.header(spec)
    CW, CH, G, X0 = 320, 170, 10, 190
    for k, key in enumerate(keys):
        r, c = divmod(k, 2)
        x, y = X0 + c * (CW + G), y0 + r * (CH + G)
        fill, stroke = PALETTE[k]
        cell = backdrop(
            sc._add(
                'rectangle',
                x,
                y,
                CW,
                CH,
                backgroundColor=fill,
                strokeColor=stroke,
                roundness={'type': 3},
            )
        )
        quad = q[key]
        has_detail = bool(quad.get('detail'))
        lab = sc.para(
            x + 16,
            y + (24 if has_detail else CH / 2 - 16),
            quad['label'],
            CW - 32,
            size=24,
            color=stroke,
        )
        parts = [cell, lab]
        if has_detail:
            parts.append(sc.para(x + 16, lab['y'] + lab['height'] + 14, quad['detail'], CW - 32))
        sc.group(*parts)
    xa, ya = spec['x_axis'], spec['y_axis']
    gx1, gy1 = X0 + 2 * CW + G, y0 + 2 * CH + G  # grid's right / bottom edge
    ax_y = gy1 + 20
    sc._add(
        'arrow',
        X0,
        ax_y,
        gx1 - X0,
        0,
        points=[[0, 0], [gx1 - X0, 0]],
        strokeColor=MUTED,
        endArrowhead='arrow',
        startArrowhead=None,
        lastCommittedPoint=None,
        startBinding=None,
        endBinding=None,
    )
    for c, tick in enumerate((xa['low'], xa['high'])):
        sc.para(X0 + c * (CW + G), ax_y + 10, tick, CW, size=18)
    sc.para(X0, ax_y + 44, xa['label'], 2 * CW + G, size=22, color=INK)
    ax_x = X0 - 20
    sc._add(
        'arrow',
        ax_x,
        gy1,
        0,
        gy1 - y0,
        points=[[0, 0], [0, -(gy1 - y0)]],
        strokeColor=MUTED,
        endArrowhead='arrow',
        startArrowhead=None,
        lastCommittedPoint=None,
        startBinding=None,
        endBinding=None,
    )
    for r, tick in enumerate((ya['high'], ya['low'])):
        sc.para(0, y0 + r * (CH + G) + CH / 2 - 12, tick, ax_x - 12, size=18, align='right')
    lw = len(ya['label']) * 22 * CHAR_W
    sc.text(
        0,
        y0 - 40,
        ya['label'],
        size=22,
        width=lw,
    )
    if spec.get('note'):
        sc.verdict(X0, ax_y + 90, 2 * CW + G, spec['note'])


def tpl_timeline(sc: Scene, spec: dict) -> None:
    """Phases as a band along a time axis; optional proportional widths, gaps and a curve."""
    phases = spec['phases']
    if not 3 <= len(phases) <= 7:
        raise SpecError('timeline needs 3–7 phases')
    y0 = sc.header(spec)
    TW, MINW, GAPW, SEP = 760, 150, 90, 6  # TW keeps the band within a page column
    weights = [float(p.get('weight', 1)) for p in phases]
    widths = [max(MINW, TW * w / sum(weights)) for w in weights]
    gaps = {g['after']: g for g in spec.get('gaps', [])}
    curve = spec.get('curve')
    band_y = y0 + (200 if curve else 40 if gaps else 0)
    xs, x = [], 0.0
    for i, w in enumerate(widths):
        xs.append(x)
        x += w + SEP + (GAPW if i in gaps else 0)
    end_x = x - SEP
    boxes = []
    for i, (p, px, w) in enumerate(zip(phases, xs, widths, strict=True)):
        fill, stroke = PALETTE[i % len(PALETTE)]
        boxes.append(
            sc.shape('rectangle', px, band_y, w, p['label'], size=20, fill=fill, stroke=stroke)
        )
    bh = max(max(b['height'] for b in boxes), 72)
    for b in boxes:
        sc.set_height(b, bh)
    ax_y = band_y + bh + 22
    sc._add(
        'arrow',
        0,
        ax_y,
        end_x + 40,
        0,
        points=[[0, 0], [end_x + 40, 0]],
        strokeColor=MUTED,
        endArrowhead='arrow',
        startArrowhead=None,
        lastCommittedPoint=None,
        startBinding=None,
        endBinding=None,
    )
    sc.text(end_x + 56, ax_y - 12, spec.get('axis', 'time'), size=18, color=MUTED)
    for i, g in gaps.items():
        gx = xs[i] + widths[i] + SEP / 2 + GAPW / 2
        sc._add(
            'line',
            gx,
            band_y - 10,
            0,
            bh + 20,
            points=[[0, 0], [0, bh + 20]],
            strokeColor=NOTE_COLORS['risk'][1],
            strokeStyle='dashed',
            lastCommittedPoint=None,
            startArrowhead=None,
            endArrowhead=None,
        )
        sc.para(gx - 90, band_y - 46, g['label'], 180, size=18, color=NOTE_COLORS['risk'][1])
    for p, px, w, b in zip(phases, xs, widths, boxes, strict=True):
        if p.get('detail'):
            sc.group(b, sc.para(px, ax_y + 16, p['detail'], w))
    if curve:
        vals = curve['values']
        if len(vals) != len(phases):
            raise SpecError('timeline curve needs one value per phase')
        top, height, vmax = y0 + 30, 140, max(vals) or 1
        pts = [(0, top + height)]
        pts += [
            (px + w / 2, top + height * (1 - v / vmax))
            for px, w, v in zip(xs, widths, vals, strict=True)
        ]
        pts.append((end_x, top + height * (1 - vals[-1] / vmax / 2)))
        x0, y_0 = pts[0]
        rel = [[round(px - x0, 1), round(py - y_0, 1)] for px, py in pts]
        sc._add(
            'line',
            x0,
            y_0,
            end_x,
            height,
            points=rel,
            strokeColor=INK,
            strokeWidth=3,
            roundness={'type': 2},
            lastCommittedPoint=None,
            startArrowhead=None,
            endArrowhead=None,
            _role='backdrop',
        )
        peak = max(range(len(vals)), key=lambda k: vals[k])
        sc.para(xs[peak], top - 32, curve['label'], widths[peak], size=20, color=INK)


def tpl_tree(sc: Scene, spec: dict) -> None:
    """A top-down tree (taxonomy or decision tree); `edge` labels the branch into a node."""
    root = spec['root']
    nodes = list(walk(root))
    leaves = [n for n, _ in nodes if not n.get('children')]
    if max(d for _, d in nodes) > 3:
        raise SpecError('tree is at most 3 levels below the root')
    if len(leaves) > 6 or len(nodes) > 12:
        raise SpecError('tree has at most 6 leaves and 12 nodes')
    y0 = sc.header(spec)
    if spec.get('direction', 'right') == 'right':
        tree_right(sc, root, y0)
        return
    edge_w = max((len(n.get('edge', '')) * DETAIL * CHAR_W for n, _ in nodes), default=0)
    W, SLOT, LV = 210, min(320, max(250, 2 * (edge_w + 24))), 170

    def place(node: dict, depth: int, x_left: float) -> tuple[dict, float]:
        kids = node.get('children', [])
        if kids:
            boxes, cur = [], x_left
            for kid in kids:
                b, cur = place(kid, depth + 1, cur)
                boxes.append((b, kid))
            mid = (boxes[0][0]['x'] + boxes[-1][0]['x'] + W) / 2
            nxt = cur
        else:
            mid, nxt, boxes = x_left + SLOT / 2, x_left + SLOT, []
        fill, stroke = PALETTE[min(depth, len(PALETTE) - 1)] if depth else ('#f8f9fa', INK)
        me = sc.shape(
            'rectangle',
            mid - W / 2,
            y0 + depth * LV,
            W,
            node['label'],
            size=24 if depth == 0 else 20,
            fill=fill,
            stroke=stroke,
            min_h=64,
        )
        for b, kid in boxes:
            sc.connect(me, b, color=stroke, label=kid.get('edge'))
        if not kids and node.get('detail'):
            sc.group(
                me,
                sc.para(
                    me['x'] - (SLOT - W) / 2, me['y'] + me['height'] + 10, node['detail'], SLOT - 10
                ),
            )
        return me, nxt

    place(root, 0, 0)


def tree_right(sc: Scene, root: dict, y0: float) -> None:
    """Left-to-right tree: depth runs across, leaves stack down, so width grows with depth
    rather than with the number of leaves and the drawing fits a page column.

    A branch's `edge` label sits above the node it leads to, grouped with it.
    """
    W, COL, ROWGAP = 200, 90, 22
    edge_h = DETAIL * LH + 4

    def leaf_h(node: dict) -> float:
        lines = len(wrap(node['detail'], int(W / (DETAIL * CHAR_W)))) if node.get('detail') else 0
        return 64 + lines * DETAIL * LH + (10 if lines else 0)

    def place(node: dict, depth: int, y_top: float) -> tuple[dict, float]:
        """Lay out node's subtree from y_top; returns its box and the next free y."""
        kids = node.get('children', [])
        x = depth * (W + COL)
        top = y_top + (edge_h if node.get('edge') else 0)
        if kids:
            boxes, cur = [], y_top
            for kid in kids:
                b, cur = place(kid, depth + 1, cur)
                boxes.append(b)
            mid = (centre(boxes[0])[1] + centre(boxes[-1])[1]) / 2
            nxt = cur
        else:
            mid, nxt, boxes = top + 32, top + leaf_h(node) + ROWGAP, []
        fill, stroke = PALETTE[min(depth, len(PALETTE) - 1)] if depth else ('#f8f9fa', INK)
        me = sc.shape(
            'rectangle',
            x,
            mid - 32,
            W,
            node['label'],
            size=24 if depth == 0 else 20,
            fill=fill,
            stroke=stroke,
            min_h=64,
        )
        if me['height'] > 64:  # a wrapped label: keep the box centred on its row
            me['y'] -= (me['height'] - 64) / 2
            for b in me['boundElements']:
                sc.byid[b['id']]['y'] -= (me['height'] - 64) / 2
        for b in boxes:
            sc.connect(me, b, color=stroke, sideways=True)
        parts = [me]
        if node.get('edge'):
            parts.append(sc.text(x + 4, me['y'] - edge_h, node['edge'], size=DETAIL, color=MUTED))
        if not kids and node.get('detail'):
            parts.append(sc.para(x, me['y'] + me['height'] + 10, node['detail'], W))
        if len(parts) > 1:
            sc.group(*parts)
        return me, nxt

    place(root, 0, y0)


def walk(node: dict, depth: int = 0):
    yield node, depth
    for kid in node.get('children', []):
        yield from walk(kid, depth + 1)


def tpl_funnel(sc: Scene, spec: dict) -> None:
    """Stacked bars that narrow downward (funnel) or upward (pyramid); details on the right."""
    stages = spec['stages']
    if not 3 <= len(stages) <= 6:
        raise SpecError('funnel needs 3–6 stages')
    pyramid = spec.get('shape', 'funnel') == 'pyramid'
    y = sc.header(spec)
    WMAX, WMIN, GAP = 680, 240, 8
    n = len(stages)
    for i, st in enumerate(stages):
        k = (n - 1 - i) if pyramid else i
        w = WMAX - (WMAX - WMIN) * k / (n - 1)
        fill, stroke = PALETTE[i % len(PALETTE)]
        b = sc.shape(
            'rectangle',
            (WMAX - w) / 2,
            y,
            w,
            st['label'],
            size=22,
            fill=fill,
            stroke=stroke,
            min_h=64,
        )
        if st.get('detail'):
            lines = wrap(st['detail'], int(300 / (DETAIL * CHAR_W)))
            sc.group(
                b,
                sc.para(
                    WMAX + 40,
                    y + b['height'] / 2 - len(lines) * DETAIL * LH / 2,
                    st['detail'],
                    300,
                    align='left',
                ),
            )
        y += b['height'] + GAP
    if spec.get('note'):
        sc.verdict(0, y + 24, WMAX, spec['note'])


def tpl_spectrum(sc: Scene, spec: dict) -> None:
    """Values on one axis: each mark is a card above or below the axis, arrowed to its point.

    Cards alternate above and below; a card that would overlap a neighbour moves out a
    row. Optional bands shade ranges of the axis (e.g. inelastic vs elastic).
    """
    axis, marks = spec['axis'], spec['marks']
    if not 2 <= len(marks) <= 8:
        raise SpecError('spectrum needs 2–8 marks')
    lo, hi, log = float(axis['min']), float(axis['max']), axis.get('scale') == 'log'
    if lo >= hi or (log and lo <= 0):
        raise SpecError('spectrum axis needs min < max (and min > 0 on a log scale)')
    for m in marks:
        if not lo <= float(m['value']) <= hi:
            raise SpecError(f'mark {m["label"]!r} lies outside the axis')
    L, CW, GAP = 860, 170, 12  # axis length, card width, horizontal gap between cards

    def pos(v: float) -> float:
        if log:
            return L * (math.log(v) - math.log(lo)) / (math.log(hi) - math.log(lo))
        return L * (v - lo) / (hi - lo)

    def card_text(m: dict) -> str:
        """The card's label with its value on a second line (`show` overrides the number)."""
        shown = m.get('show') or f'{float(m["value"]):g}'
        return f'{m["label"]}\n{shown}'

    def card_h(m: dict) -> tuple[float, float]:
        box = len(wrap(card_text(m), int((CW - 2 * PAD) / (18 * CHAR_W)))) * 18 * LH + 2 * PAD
        det = (
            len(wrap(m['detail'], int(CW / (DETAIL * CHAR_W)))) * DETAIL * LH
            if m.get('detail')
            else 0
        )
        return max(box, 50), det

    # assign each mark (left to right) the first slot where its card fits
    slots: dict[tuple[int, int], list[tuple[float, float]]] = {}
    placed = []
    for m in sorted(marks, key=lambda m: float(m['value'])):
        x = min(max(pos(float(m['value'])) - CW / 2, 0), L - CW)
        for row in range(1, 4):
            for side in (-1, 1):
                taken = slots.setdefault((side, row), [])
                if all(x + CW + GAP <= a or b + GAP <= x for a, b in taken):
                    taken.append((x, x + CW))
                    placed.append((m, x, side, row))
                    break
            else:
                continue
            break
        else:
            raise SpecError('spectrum marks are too crowded; merge or drop some')
    row_h = {k: max(sum(card_h(m)) + 8 for m, _, s, r in placed if (s, r) == k) + 18 for k in slots}
    y0 = sc.header(spec)
    above = sum(row_h.get((-1, r), 0) for r in range(1, 4))
    axis_y = y0 + above + 46
    band_h = 26
    for i, band in enumerate(spec.get('bands', [])):  # shaded ranges, behind everything else
        fill, stroke = PALETTE[(5 + i) % len(PALETTE)]
        bx0, bx1 = pos(float(band['from'])), pos(float(band['to']))
        strip = backdrop(
            sc._add(
                'rectangle',
                bx0,
                axis_y - band_h / 2,
                bx1 - bx0,
                band_h,
                backgroundColor=fill,
                strokeColor=fill,
                roundness={'type': 3},
            )
        )
        # the label goes where in its band it is furthest from the arrows into the dots
        lw = min(bx1 - bx0, len(band['label']) * DETAIL * CHAR_W + 8)
        dots = [pos(float(m['value'])) for m in marks]
        lx = max(
            (bx0, (bx0 + bx1 - lw) / 2, bx1 - lw),
            key=lambda c: min((abs(d - min(max(d, c), c + lw)) for d in dots), default=0),
        )
        sc.group(strip, sc.para(lx, axis_y + band_h / 2 + 4, band['label'], lw, color=stroke))
    sc._add(
        'arrow',
        0,
        axis_y,
        L + 30,
        0,
        points=[[0, 0], [L + 30, 0]],
        strokeColor=MUTED,
        endArrowhead='arrow',
        startArrowhead=None,
        lastCommittedPoint=None,
        startBinding=None,
        endBinding=None,
    )
    sc.text(L + 44, axis_y - 12, axis.get('label', ''), size=18, color=MUTED)
    below0 = axis_y + band_h / 2 + (30 if spec.get('bands') else 10) + 24
    for i, (m, x, side, row) in enumerate(placed):
        kind = m.get('kind', 'fact')
        if kind not in MAP_KINDS:
            raise SpecError(f'mark kind must be one of {MAP_KINDS}, not {kind!r}')
        fill, stroke = PALETTE[i % len(PALETTE)] if kind == 'fact' else NOTE_COLORS[kind][:2]
        bh, dh = card_h(m)
        if side < 0:  # above: detail on top, box nearest the axis
            bottom = axis_y - 34 - sum(row_h[(-1, r)] for r in range(1, row))
            box_y, det_y = bottom - bh, bottom - bh - 8 - dh
        else:  # below: box nearest the axis, detail underneath
            box_y = below0 + sum(row_h[(1, r)] for r in range(1, row))
            det_y = box_y + bh + 8
        box = sc.shape(
            'rectangle',
            x,
            box_y,
            CW,
            card_text(m),
            size=18,
            fill=fill,
            stroke=stroke,
            dashed=kind != 'fact',
            min_h=bh,
        )
        vx = pos(float(m['value']))
        dot = backdrop(  # sits on the axis by design
            sc._add(
                'ellipse', vx - 7, axis_y - 7, 14, 14, backgroundColor=stroke, strokeColor=stroke
            )
        )
        sc.connect(box, dot, color=stroke)
        parts = [box, dot]
        if m.get('detail'):
            parts.append(sc.para(x, det_y, m['detail'], CW, color=INK))
        sc.group(*parts)
    if spec.get('verdict'):
        bottom = max(e['y'] + e['height'] for e in sc.elements)
        sc.verdict(0, bottom + 30, L, spec['verdict'])


def tpl_venn(sc: Scene, spec: dict) -> None:
    """Two overlapping sets: what is only left, only right, and shared."""
    y0 = sc.header(spec)
    W, H, OFF = 560, 400, 330
    sides = []
    for j, side in enumerate((spec['left'], spec['right'])):
        fill, stroke = PALETTE[0] if j == 0 else PALETTE[4]
        x = j * OFF
        e = backdrop(
            sc._add(
                'ellipse',
                x,
                y0 + 50,
                W,
                H,
                backgroundColor=fill,
                strokeColor=stroke,
                opacity=70,
                roundness={'type': 2},
            )
        )
        sides.append((e, side, stroke))
    regions = [(40, OFF - 30), (OFF + 25, W - 25), (W + 30, OFF + W - 40)]  # x spans
    cy = y0 + 50 + H / 2
    for (e, side, stroke), (rx0, rx1) in zip(sides, (regions[0], regions[2]), strict=True):
        parts = [e, sc.para(rx0 - 20, y0, side['label'], rx1 - rx0 + 40, size=26, color=stroke)]
        parts += stack(sc, side.get('points', []), rx0, rx1, cy, ink=INK)
        sc.group(*parts)
    both = spec.get('both', {})
    rx0, rx1 = regions[1]
    parts = []
    if both.get('label'):
        parts.append(sc.para(rx0, y0 + 50 + 95, both['label'], rx1 - rx0, size=20, color=INK))
    parts += stack(sc, both.get('points', []), rx0, rx1, cy + 10, ink=INK)
    if len(parts) > 1:
        sc.group(*parts)
    if spec.get('verdict'):
        sc.verdict(0, y0 + 50 + H + 30, OFF + W, spec['verdict'])


CAUSAL_SIGNS = {
    '+': ('raises', '#1971c2'),
    '-': ('lowers', '#e8590c'),
    'mixed': ('mixed', '#7048e8'),
}
CAUSAL_ROLES = {  # role: (fill, stroke)
    'factor': ('#ffffff', INK),
    'cause': ('#e6fcf5', '#0c8599'),
    'outcome': ('#fff0f6', '#c2255c'),
}


def causal_layers(nodes: list[dict], edges: list[dict]) -> dict[str, int]:
    """Column of each node: the length of the longest path that reaches it."""
    layer = {n['id']: 0 for n in nodes}
    for _ in nodes:  # a DAG settles within len(nodes) passes; a loop never does
        changed = False
        for e in edges:
            if layer[e['to']] < layer[e['from']] + 1:
                layer[e['to']] = layer[e['from']] + 1
                changed = True
        if not changed:
            return layer
    raise SpecError('causal-map edges form a loop; draw feedback with `cycle`')


def tpl_causal(sc: Scene, spec: dict) -> None:
    """Causes and effects: nodes in layers by causal depth, arrows coloured by sign.

    A node's layer is the longest path reaching it, so every arrow runs one way: left
    to right, or top to bottom with `direction: "down"` (for chains too deep to fit
    across). An arrow that skips layers is routed around the layers it passes. Where four
    or more labelled arrows converge on one node, each carries its label just past its
    source, so the labels do not bunch at the node. Dashed nodes and their arrows are
    unobserved (or whatever `dashed_means` says).
    """
    nodes, edges = spec['nodes'], spec['edges']
    if not 2 <= len(nodes) <= 9:
        raise SpecError('causal-map needs 2–9 nodes')
    if not 1 <= len(edges) <= 14:
        raise SpecError('causal-map needs 1–14 edges')
    byid = {n['id']: n for n in nodes}
    if len(byid) != len(nodes):
        raise SpecError('causal-map node ids must be unique')
    for n in nodes:
        if n.get('role', 'factor') not in CAUSAL_ROLES:
            raise SpecError(f'node role must be one of {tuple(CAUSAL_ROLES)}, not {n["role"]!r}')
    for e in edges:
        for k in ('from', 'to'):
            if e[k] not in byid:
                raise SpecError(f'edge {k} {e[k]!r} is not a node id')
        if e.get('sign') is not None and e['sign'] not in CAUSAL_SIGNS:
            raise SpecError(f'edge sign must be one of {tuple(CAUSAL_SIGNS)}, not {e["sign"]!r}')
    down = spec.get('direction', 'right') == 'down'
    layer = causal_layers(nodes, edges)
    nlayers = max(layer.values()) + 1
    y0 = sc.header(spec)
    W, DW, SEP, LEVEL = 180, 150, 30, 30  # box, side detail (down), between nodes, route clearance

    def arrow_label(e):
        shown = CAUSAL_SIGNS[e['sign']][0] if e.get('sign') else ''
        return ' '.join(x for x in (shown, e.get('label', '')) if x) or None

    longest = max((len(arrow_label(e) or '') * 20 * CHAR_W for e in edges), default=0)
    GAP = 90 if down else max(90, longest + 40)  # between layers: room for the labels
    # FAN_IN or more labelled arrows into one node would bunch their labels at the
    # midpoints; those arrows (between adjacent layers) carry their label on a straight
    # run at the source end instead, and converge on the node past every label
    FAN_IN, STUB = 4, 14
    CONVERGE = 130 if down else 100  # room for the arrows to bend in
    into = {n['id']: sum(e['to'] == n['id'] and bool(arrow_label(e)) for e in edges) for n in nodes}
    early = {
        i
        for i, e in enumerate(edges)
        if into[e['to']] >= FAN_IN and arrow_label(e) and layer[e['to']] == layer[e['from']] + 1
    }
    run = {}  # source layer -> length of its label runs
    label_w = {}  # source node -> its widest such label (down: they sit side by side)
    for i in early:
        c = layer[edges[i]['from']]
        f = edges[i]['from']
        label_w[f] = max(label_w.get(f, 0), len(arrow_label(edges[i])) * 20 * CHAR_W)
        need = 20 * LH + 40 if down else len(arrow_label(edges[i])) * 20 * CHAR_W + 20
        run[c] = max(run.get(c, 0), need)
    layer_end = {}  # layer -> where it ends along the flow
    outs = {n['id']: sum(e['from'] == n['id'] for e in edges) for n in nodes}
    # a source with several such arrows spreads their ports a label apart: a taller
    # box (right), or a wider one (down), where the labels sit side by side
    multi = {f for f in label_w if sum(edges[i]['from'] == f for i in early) > 1}
    degree = {
        n['id']: max(
            sum(e['from'] == n['id'] for e in edges), sum(e['to'] == n['id'] for e in edges)
        )
        for n in nodes
    }
    start = len(sc.elements)
    boxes, units = {}, {}  # node id -> its shape; node id -> (x0, y0, x1, y1) with its detail
    pos = 0.0  # where the next layer starts along the flow
    for c in range(nlayers):
        layer_start, made = len(sc.elements), []
        across, label_right = 0.0, -math.inf
        for n in (n for n in nodes if layer[n['id']] == c):
            role = n.get('role', 'factor')
            fill, stroke = CAUSAL_ROLES[role]
            x, y = (across, pos) if down else (pos, across)
            lw = label_w.get(n['id'], 0) if down else 0
            k = outs[n['id']] if n['id'] in multi else 1
            bw = max(W, k * (lw + 20)) if down and k > 1 else W
            if lw:  # its labels, below the row, clear the previous node's
                span = bw * (k - 1) / k + lw
                x = max(x, label_right + 20 + (span - bw) / 2)
                label_right = x + (bw + span) / 2
            b = sc.shape(
                'rectangle',
                x,
                y,
                bw,
                n['label'],
                size=20 if role == 'factor' else 22,
                fill='#f8f9fa' if n.get('hidden') else fill,
                stroke=stroke,
                dashed=bool(n.get('hidden')),
                min_h=max(  # room to spread its arrows
                    56, 36 * degree[n['id']], 36 * (outs[n['id']] + 1) * (n['id'] in multi)
                ),
            )
            members, ux1, uy1 = [b], x + bw, y + b['height']
            if n.get('detail'):
                if down:  # beside the box, so arrows leave its bottom edge freely
                    d = sc.para(x + bw + 10, y, n['detail'], DW, align='left')
                    d['y'] = round(y + (b['height'] - d['height']) / 2, 1)
                    ux1 = x + bw + 10 + DW
                else:
                    d = sc.para(x, uy1 + 6, n['detail'], W)
                    uy1 = d['y'] + d['height']
                members.append(d)
                sc.group(*members)
            boxes[n['id']] = b
            units[n['id']] = [x, y, ux1, max(uy1, y + b['height'])]
            made.append(n['id'])
            across = (ux1 if down else uy1) + (SEP + 10 if down else SEP)
        span = across - (SEP + 10 if down else SEP)
        depth = max((units[i][3] - units[i][1]) if down else W for i in made)
        if down:  # vertically centre each node in its row
            for i in made:
                off = (depth - (units[i][3] - units[i][1])) / 2
                for el in sc.elements[layer_start:]:
                    if (
                        el is boxes[i]
                        or set(el['groupIds']) & set(boxes[i]['groupIds'])
                        or (el.get('containerId') == boxes[i]['id'])
                    ):
                        el['y'] = round(el['y'] + off, 1)
                units[i][1] += off
                units[i][3] += off
        for el in sc.elements[layer_start:]:  # centre each layer on the axis
            k = 'x' if down else 'y'
            el[k] = round(el[k] - span / 2, 1)
        for i in made:
            if down:
                units[i][0] -= span / 2
                units[i][2] -= span / 2
            else:
                units[i][1] -= span / 2
                units[i][3] -= span / 2
        layer_end[c] = pos + depth
        pos += depth + (max(GAP, STUB + run[c] + CONVERGE) if c in run else GAP)

    # route: straight, unless the arrow would cross a node of a layer it skips
    def ends(e):
        a, b = boxes[e['from']], boxes[e['to']]
        if down:
            return (centre(a)[0], a['y'] + a['height']), (centre(b)[0], b['y'])
        return (a['x'] + W, centre(a)[1]), (b['x'], centre(b)[1])

    route, used = {}, {'low': 0, 'high': 0}  # low = above (right) or left (down)
    for i, e in enumerate(edges):
        mid = [m for m in byid if layer[e['from']] < layer[m] < layer[e['to']]]
        p, q = ends(e)
        clear = [(u[0] - 14, u[1] - 14, u[2] + 14, u[3] + 14) for u in (units[m] for m in mid)]
        if not any(segment_hits_box(p, q, u) for u in clear):
            continue
        k = 0 if down else 1
        lo, hi = min(units[m][k] for m in mid), max(units[m][k + 2] for m in mid)
        here = (p[k] + q[k]) / 2
        # the emptier side, then the nearer one, so routed arrows do not pile up
        side = min(
            ('low', 'high'), key=lambda sd: (used[sd], abs((lo if sd == 'low' else hi) - here))
        )
        n_side = used[side]
        used[side] += 1
        route[i] = (n_side, lo - LEVEL - 26 * n_side if side == 'low' else hi + LEVEL + 26 * n_side)

    # ports: a node's arrows are spread along its edge, ordered by where the other end,
    # or the route, lies, so they do not cross at the node
    def far(i, end):
        if i in route:
            return route[i][1]
        return centre(boxes[edges[i][end]])[0 if down else 1]

    port = {}
    for nid, b in boxes.items():
        for end, other in (('from', 'to'), ('to', 'from')):
            mine = sorted(
                (i for i, e in enumerate(edges) if e[end] == nid), key=lambda i: far(i, other)
            )
            lo, size = (b['x'], b['width']) if down else (b['y'], b['height'])
            for j, i in enumerate(mine):
                if down and end == 'from' and nid in multi:  # a label width apart
                    port[i, end] = lo + size * (j + 0.5) / len(mine)
                else:
                    port[i, end] = lo + size * (j + 1) / (len(mine) + 1)
    for i, e in enumerate(edges):
        a, b = boxes[e['from']], boxes[e['to']]
        (px, py), (qx, qy) = ends(e)
        if down:
            px, qx = port[i, 'from'], port[i, 'to']
        else:
            py, qy = port[i, 'from'], port[i, 'to']
        via = None
        if i in route:
            n_side, level = route[i]
            if down:
                via = [(level, py + GAP / 2 - 14 * n_side), (level, qy - GAP / 2 + 14 * n_side)]
            else:
                via = [(px + GAP / 2 - 14 * n_side, level), (qx - GAP / 2 + 14 * n_side, level)]
        elif i in early:  # 4 points: the label sits on the middle segment, the run
            c = layer[e['from']]
            s0 = layer_end[c] + STUB
            via = [(px, s0), (px, s0 + run[c])] if down else [(s0, py), (s0 + run[c], py)]
        color = CAUSAL_SIGNS[e['sign']][1] if e.get('sign') else INK
        dashed = bool(
            e.get('dashed') or byid[e['from']].get('hidden') or byid[e['to']].get('hidden')
        )
        arr = sc.connect(
            a,
            b,
            color=color,
            dashed=dashed,
            label=arrow_label(e),
            label_size=20,
            ends=((px, py), (qx, qy)),
            via=via,
        )
        if i in early:  # straight segments: a curve overshoots a short run into a hook
            arr['roundness'] = None
    box_of = [extent(el) for el in sc.elements[start:]]
    dx, dy = -min(b[0] for b in box_of), y0 - min(b[1] for b in box_of)
    for el in sc.elements[start:]:
        el['x'], el['y'] = round(el['x'] + dx, 1), round(el['y'] + dy, 1)
    width = max(b[2] for b in box_of) - min(b[0] for b in box_of)
    y = max(b[3] for b in box_of) + dy + 30
    if spec.get('verdict'):
        v = sc.verdict(0, y, max(width, 400), spec['verdict'])
        y = v['y'] + v['height'] + 24
    if any(n.get('hidden') for n in nodes) or any(e.get('dashed') for e in edges):  # legend
        sw = sc._add(
            'rectangle',
            0,
            y,
            34,
            22,
            strokeColor=MUTED,
            strokeStyle='dashed',
            roundness={'type': 3},
        )
        sc.group(sw, sc.text(44, y, spec.get('dashed_means', 'unobserved'), size=18, color=MUTED))


MAP_KINDS = ('fact', 'risk', 'tip')


def tpl_map(sc: Scene, spec: dict) -> None:
    """Whole-page overview: one lane per stage, the stage on the left, its cards to the right.

    Lanes run top to bottom; `ordered` stages are joined by arrows. A card's colour
    says whether it is a fact, a risk or a tip, and a card with a `section` links to
    that heading of the page. Kept under ~1,000px wide so it reads at column width.
    """
    stages = spec['stages']
    if not 2 <= len(stages) <= 7:
        raise SpecError('map needs 2–7 stages')
    if any(not 1 <= len(st.get('cards', [])) <= 3 for st in stages):
        raise SpecError('each map stage needs 1–3 cards')
    y = sc.header(spec)
    SW, CW, GAP, PADL, LANE_GAP = 180, 240, 16, 16, 26
    ncols = max(len(st['cards']) for st in stages)
    span = ncols * (CW + GAP) - GAP  # width the cards of every lane share
    row_w = PADL + SW + 24 + span + PADL
    used, prev = set(), None
    for i, st in enumerate(stages):
        fill, stroke = PALETTE[i % len(PALETTE)]
        start = len(sc.elements)
        top = y + PADL
        cards = st['cards']
        cw = (span - (len(cards) - 1) * GAP) / len(cards)  # cards stretch to fill the lane
        boxes = []
        for j, c in enumerate(cards):
            kind = c.get('kind', 'fact')
            if kind not in MAP_KINDS:
                raise SpecError(f'card kind must be one of {MAP_KINDS}, not {kind!r}')
            used.add(kind)
            cf, cs, ink = ('#ffffff', stroke, stroke) if kind == 'fact' else NOTE_COLORS[kind]
            b = sc.shape(
                'rectangle',
                PADL + SW + 24 + j * (cw + GAP),
                top,
                cw,
                c['label'],
                size=20,
                fill=cf,
                stroke=cs,
                text_color=ink,
                dashed=kind != 'fact',
                min_h=50,
            )
            if c.get('_link'):
                b['link'] = c['_link']
            boxes.append(b)
        card_h = max(b['height'] for b in boxes)
        bottom, members = top + 60, []
        for b, c in zip(boxes, cards, strict=True):
            sc.set_height(b, card_h)  # equal heights, so the details start on one line
            card, end = [b], top + card_h
            if c.get('detail'):
                p = sc.para(b['x'], end + 8, c['detail'], cw, size=17, color=INK)
                card.append(p)
                end = p['y'] + p['height']
            sc.group(*card)
            members += card
            bottom = max(bottom, end)
        stage = sc.shape(
            'rectangle', PADL, top, SW, st['label'], size=24, fill=fill, stroke=stroke, min_h=60
        )
        sc.set_height(stage, max(stage['height'], bottom - top))
        bottom = max(bottom, top + stage['height'])
        lane = backdrop(
            sc._add(
                'rectangle',
                0,
                y,
                row_w,
                bottom - y + PADL,
                backgroundColor=fill,
                strokeColor=fill,
                roundness={'type': 3},
            )
        )
        sc.elements.insert(start, sc.elements.pop())  # the lane sits behind its contents
        sc.group(lane, stage, *members)
        if prev is not None and spec.get('ordered', True):
            sc.connect(prev, stage, color=prev['strokeColor'])
        prev = stage
        y = bottom + PADL + LANE_GAP
    if spec.get('verdict'):
        v = sc.verdict(0, y, row_w, spec['verdict'])
        y = v['y'] + v['height'] + 24
    lx = 0
    for kind in ('risk', 'tip'):  # legend: only the kinds in use
        if kind in used:
            fill, stroke, ink = NOTE_COLORS[kind]
            sw = sc._add(
                'rectangle',
                lx,
                y,
                28,
                28,
                backgroundColor=fill,
                strokeColor=stroke,
                strokeStyle='dashed',
                roundness={'type': 3},
            )
            sc.group(sw, sc.text(lx + 38, y + 2, kind, size=18, color=ink))
            lx += 130


def stack(sc: Scene, points: list[str], x0: float, x1: float, cy: float, ink: str) -> list[dict]:
    """Points stacked and centred vertically on cy within [x0, x1]."""
    w = x1 - x0
    sizes = [len(wrap(p, int(w / (17 * CHAR_W)))) * 17 * LH for p in points]
    y = cy - (sum(sizes) + 14 * (len(points) - 1)) / 2
    out = []
    for p, h in zip(points, sizes, strict=True):
        out.append(sc.para(x0, y, p, w, size=17, color=ink))
        y += h + 14
    return out


# ---- template registry: what each draws, when to use it, its text -------
@dataclass
class Template:
    build: Callable[[Scene, dict], None]
    texts: Callable[[dict], tuple[list[str], list[str], list[str]]]  # labels, details, notes
    shape: str  # the meaning the shape carries
    use_when: str
    not_when: str
    fields: dict
    example: dict
    max_words: int = MAX_WORDS


def _labels_details(items, label='label', detail='detail'):
    return [i[label] for i in items], [i.get(detail, '') for i in items]


def texts_pipeline(s):
    labels, details = _labels_details(s.get('steps', []))
    return labels, details, [st['note']['text'] for st in s.get('steps', []) if st.get('note')]


def texts_hub(s):
    labels, details = _labels_details(s.get('spokes', []))
    groups = list(dict.fromkeys(sp['group'] for sp in s.get('spokes', []) if sp.get('group')))
    return [s.get('center', ''), *labels, *groups], details, []


def texts_contrast(s):
    sides = (s.get('left', {}), s.get('right', {}))
    return (
        [d.get('label', '') for d in sides],
        [p for d in sides for p in d.get('points', [])],
        [s.get('verdict', '')],
    )


def texts_cycle(s):
    labels, details = _labels_details(s.get('stages', []))
    return [*labels, s.get('center', '')], details, []


def texts_matrix(s):
    q = s.get('quadrants', {}).values()
    labels, details = _labels_details(q)
    axes = [
        a.get(k, '')
        for a in (s.get('x_axis', {}), s.get('y_axis', {}))
        for k in ('label', 'low', 'high')
    ]
    return labels + axes, details, [s.get('note', '')]


def texts_timeline(s):
    labels, details = _labels_details(s.get('phases', []))
    labels += [g['label'] for g in s.get('gaps', [])]
    if s.get('curve'):
        labels.append(s['curve']['label'])
    return [*labels, s.get('axis', 'time')], details, []


def texts_tree(s):
    if 'root' not in s:
        return [], [], []
    nodes = [n for n, _ in walk(s['root'])]
    return [n['label'] for n in nodes], [n.get('detail', '') for n in nodes], []


def texts_funnel(s):
    labels, details = _labels_details(s.get('stages', []))
    return labels, details, [s.get('note', '')]


def texts_venn(s):
    parts = (s.get('left', {}), s.get('both', {}), s.get('right', {}))
    labels = [p.get('label', '') for p in parts]
    return labels, [x for p in parts for x in p.get('points', [])], [s.get('verdict', '')]


def texts_spectrum(s):
    marks = s.get('marks', [])
    labels = [m['label'] for m in marks] + [b['label'] for b in s.get('bands', [])]
    labels.append(s.get('axis', {}).get('label', ''))
    return labels, [m.get('detail', '') for m in marks], [s.get('verdict', '')]


def texts_map(s):
    stages = s.get('stages', [])
    cards = [c for st in stages for c in st.get('cards', [])]
    labels = [st['label'] for st in stages] + [c['label'] for c in cards]
    return labels, [c.get('detail', '') for c in cards], [s.get('verdict', '')]


def texts_causal(s):
    nodes = s.get('nodes', [])
    return [n['label'] for n in nodes], [n.get('detail', '') for n in nodes], [s.get('verdict', '')]


TEMPLATES: dict[str, Template] = {
    'pipeline': Template(
        tpl_pipeline,
        texts_pipeline,
        'order: do A, then B',
        'a process, method or causal chain the reader carries out or follows step by step',
        'phases something passes through over time (timeline) or a loop that feeds back (cycle)',
        {
            'steps': '2–6 × {label, detail?, note?: {text, kind: "risk"|"tip"}}',
        },
        {
            'template': 'pipeline',
            'page': 'marketing-mix-modeling',
            'title': 'Marketing-mix modeling',
            'steps': [
                {'label': 'Collect', 'detail': 'sales, price, media, promo'},
                {
                    'label': 'Specify',
                    'detail': 'adstock, saturation',
                    'note': {'text': 'No carryover → inflated elasticity', 'kind': 'risk'},
                },
                {'label': 'Allocate', 'note': {'text': 'Optimum is a range', 'kind': 'tip'}},
            ],
        },
    ),
    'hub': Template(
        tpl_hub,
        texts_hub,
        'composition: one concept and its parts',
        'one concept and its parts, criteria or facets, none ranked above the others',
        'the parts are ranked or stacked (funnel/pyramid) or branch further (tree)',
        {
            'center': 'label',
            'spokes': '3–8 × {label, detail?, group?}  (spokes sharing a group share a colour)',
        },
        {
            'template': 'hub',
            'page': 'brand-elements',
            'title': 'Brand elements',
            'center': 'Brand element',
            'spokes': [
                {'label': 'Memorable', 'group': 'builds the brand'},
                {'label': 'Meaningful', 'group': 'builds the brand'},
                {'label': 'Protectable', 'group': 'defends the brand'},
            ],
        },
    ),
    'contrast': Template(
        tpl_contrast,
        texts_contrast,
        'tension: two positions side by side',
        'two schools, options or trade-offs whose differences are the point',
        'what the two share matters as much as how they differ (venn)',
        {
            'left': '{label, points: [detail…]}',
            'right': '{label, points: [detail…]}',
            'verdict': 'optional note',
        },
        {
            'template': 'contrast',
            'page': 'long-run-advertising-effects',
            'title': 'Long-run advertising effects',
            'left': {'label': 'Sharp', 'points': ['Grow penetration, not loyalty']},
            'right': {'label': 'Binet & Field', 'points': ['Brand-building vs activation']},
            'verdict': 'Brand building grows the stock; activation harvests it',
        },
    ),
    'cycle': Template(
        tpl_cycle,
        texts_cycle,
        'feedback: the last stage feeds the first',
        'a loop: the output of the last stage feeds the first (learning loops, iterate-and-test)',
        'the process ends (pipeline); the loop is incidental rather than the point',
        {'stages': '3–6 × {label, detail?}', 'center': 'optional label inside the loop'},
        {
            'template': 'cycle',
            'page': 'database-marketing-process',
            'title': 'Database marketing process',
            'center': 'Learning loop',
            'stages': [
                {'label': 'Define problem'},
                {'label': 'Analyse data'},
                {'label': 'Implement campaign'},
                {'label': 'Evaluate', 'detail': 'new data re-enters the database'},
            ],
        },
    ),
    'matrix': Template(
        tpl_matrix,
        texts_matrix,
        'classification: two axes make four kinds',
        'two binary dimensions cross into four named cases (Ansoff, 2×2 designs)',
        'one axis is continuous with many positions, or the cells are not named concepts',
        {
            'x_axis': '{label, low, high}',
            'y_axis': '{label, low, high}',
            'quadrants': '{top_left, top_right, bottom_left, bottom_right} × {label, detail?}  '
            '(top = y high, right = x high)',
            'note': 'optional note under the grid',
        },
        {
            'template': 'matrix',
            'page': 'product-market-growth-strategies',
            'title': 'Ansoff matrix',
            'x_axis': {'label': 'Products', 'low': 'current', 'high': 'new'},
            'y_axis': {'label': 'Markets', 'low': 'current', 'high': 'new'},
            'quadrants': {
                'top_left': {'label': 'Market development'},
                'top_right': {'label': 'Diversification'},
                'bottom_left': {'label': 'Market penetration'},
                'bottom_right': {'label': 'Product development'},
            },
        },
    ),
    'timeline': Template(
        tpl_timeline,
        texts_timeline,
        'time: phases something passes through',
        'stages a product, market or population passes through over time (life cycles, adoption)',
        'steps someone performs (pipeline); dated events with no phases',
        {
            'phases': '3–7 × {label, detail?, weight?}  (weight sets relative width, e.g. shares)',
            'gaps': 'optional [{after: phase index, label}] — a break between phases',
            'curve': 'optional {label, values: one number per phase} — a trend line above',
            'axis': "optional axis label (default 'time')",
        },
        {
            'template': 'timeline',
            'page': 'product-life-cycle',
            'title': 'Product life cycle',
            'phases': [
                {'label': 'Introduction'},
                {'label': 'Growth'},
                {'label': 'Maturity'},
                {'label': 'Decline'},
            ],
            'curve': {'label': 'Sales', 'values': [1, 3, 4, 2]},
        },
    ),
    'tree': Template(
        tpl_tree,
        texts_tree,
        'hierarchy: each branch splits into kinds',
        'a taxonomy or decision tree: a root splits into kinds, which may split again',
        'the levels are a ranked stack (funnel/pyramid) or the parts are peers (hub)',
        {
            'root': '{label, children: [{label, edge?, detail?, children?}]}  '
            '(≤3 levels below root, ≤6 leaves; edge ≤3 words labels the branch; '
            'detail shows on leaves)',
            'direction': '"right" (default: grows left to right, fits a page column) | "down"',
        },
        {
            'template': 'tree',
            'page': 'forecasting-methods-taxonomy',
            'title': 'Forecasting methods',
            'root': {
                'label': 'Forecast',
                'children': [
                    {'label': 'Qualitative', 'edge': 'no data'},
                    {'label': 'Quantitative', 'edge': 'past data'},
                ],
            },
        },
    ),
    'funnel': Template(
        tpl_funnel,
        texts_funnel,
        'rank: each level narrower than the last',
        'ordered stages that shrink (funnel) or levels that build on each other (pyramid)',
        'the stages are a loop (cycle) or the parts are unranked (hub)',
        {
            'stages': '3–6 × {label, detail?}  (top first)',
            'shape': '"funnel" (top widest, default) | "pyramid" (bottom widest)',
            'note': 'optional note under the stack',
        },
        {
            'template': 'funnel',
            'page': 'customer-acquisition-funnel',
            'title': 'Customer acquisition funnel',
            'stages': [
                {'label': 'Awareness'},
                {'label': 'Appeal'},
                {'label': 'Act'},
            ],
        },
    ),
    'venn': Template(
        tpl_venn,
        texts_venn,
        'overlap: what two things share and what is only theirs',
        'two schools or lenses whose common ground is as important as their differences',
        'they share nothing worth naming (contrast)',
        {
            'left': '{label, points: [detail…]}  (only left; ≤3 points)',
            'right': '{label, points: [detail…]}  (only right; ≤3 points)',
            'both': '{label?, points: [detail…]}  (shared; ≤3 short points)',
            'verdict': 'optional note',
        },
        {
            'template': 'venn',
            'page': 'customer-equity-vs-brand-equity',
            'title': 'Customer vs brand equity',
            'left': {'label': 'Customer equity', 'points': ['Financial value']},
            'right': {'label': 'Brand equity', 'points': ['Strategic guidance']},
            'both': {'points': ['Loyalty']},
        },
    ),
    'spectrum': Template(
        tpl_spectrum,
        texts_spectrum,
        'scale: values placed along one axis',
        'a handful of values on one scale where the gaps between them are the point '
        '(benchmarks, ranges, typical vs outlier)',
        'the values are categories with no common scale (hub), or phases in time (timeline)',
        {
            'axis': '{label, min, max, scale?: "linear" (default) | "log"}',
            'marks': '2–8 × {value, label, detail?, show?: value as printed (e.g. "-2.5"), '
            'kind?: "fact"|"risk"|"tip"}',
            'bands': 'optional [{from, to, label}] — shaded ranges of the axis',
            'verdict': 'optional closing note',
        },
        {
            'template': 'spectrum',
            'page': 'marketing-mix-modeling',
            'section': 'Elasticity benchmarks',
            'title': 'Elasticity benchmarks',
            'axis': {'label': 'elasticity', 'min': 0.08, 'max': 3, 'scale': 'log'},
            'bands': [
                {'from': 0.08, 'to': 1, 'label': 'inelastic'},
                {'from': 1, 'to': 3, 'label': 'elastic'},
            ],
            'marks': [
                {'value': 0.1, 'label': 'Ads, short run'},
                {'value': 2.5, 'label': 'Own price', 'detail': 'brand level'},
            ],
        },
    ),
    'causal-map': Template(
        tpl_causal,
        texts_causal,
        'causes: arrows from drivers to effects, each with its sign',
        'what drives an outcome, and in which direction (drivers of churn), or which '
        'variables cause which (a DAG: confounders, backdoor paths, colliders)',
        'a sequence someone carries out (pipeline), a loop that feeds back (cycle), or '
        'parts of one concept with no causal arrows between them (hub)',
        {
            'nodes': '2–9 × {id, label, detail?, role?: "factor" (default) | "cause" | '
            '"outcome", hidden?: true for an unobserved variable (dashed)}',
            'edges': '1–14 × {from, to, sign?: "+" | "-" | "mixed", label? (≤3 words), '
            'dashed?: true}; arrows must not loop',
            'dashed_means': 'optional legend for dashed nodes/arrows (default "unobserved")',
            'direction': '"right" (default) or "down", for chains too deep to fit across',
            'verdict': 'optional closing note',
        },
        {
            'template': 'causal-map',
            'page': 'confounders-and-backdoor-paths',
            'title': 'A confounder opens a backdoor path',
            'nodes': [
                {'id': 'x', 'label': 'Confounder X'},
                {'id': 'd', 'label': 'Treatment D', 'role': 'cause'},
                {'id': 'y', 'label': 'Outcome Y', 'role': 'outcome'},
            ],
            'edges': [
                {'from': 'x', 'to': 'd'},
                {'from': 'x', 'to': 'y'},
                {'from': 'd', 'to': 'y', 'label': 'causal effect'},
            ],
        },
    ),
    'map': Template(
        tpl_map,
        texts_map,
        'overview: the whole page as stages, each with its key facts, risks and tips',
        "the page-level overview (## Visual summary) of a page with several sections' worth "
        'of ideas: each stage is a phase or facet, each card one idea linked to its section',
        'a single idea, or one section (use the matching single-idea template)',
        {
            'stages': '2–7 × {label, cards: 1–3 × {label, detail?, kind?: "fact"|"risk"|"tip", '
            'section?: page heading (or a unique prefix of it) the card links to}}',
            'ordered': 'true (default): stages are a flow, joined by arrows; false: facets',
            'verdict': 'optional closing note under the lanes',
        },
        {
            'template': 'map',
            'page': 'marketing-mix-modeling',
            'title': 'Marketing-mix modeling',
            'stages': [
                {
                    'label': 'Specify',
                    'cards': [
                        {
                            'label': 'Model carryover',
                            'detail': 'omitted adstock inflates the elasticity',
                            'kind': 'risk',
                            'section': 'Carryover must be specified',
                        },
                    ],
                },
                {
                    'label': 'Allocate',
                    'cards': [{'label': 'Flat maximum', 'detail': 'the optimum is a range'}],
                },
            ],
        },
        max_words=MAP_MAX_WORDS,
    ),
}


# ---- checks -------------------------------------------------------------
def words(s: str) -> int:
    return len(re.findall(r'\S+', s))


def check_spec(spec: dict) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    t = spec.get('template')
    if t not in TEMPLATES:
        return [f'unknown template {t!r}; choose one of {sorted(TEMPLATES)}'], []
    for k in ('title', 'page'):
        if not spec.get(k):
            errors.append(f'missing {k!r}')
    try:
        labels, details, notes = TEMPLATES[t].texts(spec)
    except (KeyError, TypeError, AttributeError) as e:
        return [f'malformed {t} spec ({e!r}); see `visual_summary.py schema {t}`'], []
    for label in labels:
        if words(label) > MAX_LABEL_WORDS:
            errors.append(f'label over {MAX_LABEL_WORDS} words: {label!r}')
    for d in details:
        if words(d) > MAX_DETAIL_WORDS:
            errors.append(f'detail/point over {MAX_DETAIL_WORDS} words: {d!r}')
    for n in notes:
        if words(n) > MAX_NOTE_WORDS:
            errors.append(f'note/verdict over {MAX_NOTE_WORDS} words: {n!r}')
    edges = [n['edge'] for n, _ in walk(spec['root']) if n.get('edge')] if t == 'tree' else []
    if t == 'causal-map':
        edges = [e['label'] for e in spec.get('edges', []) if e.get('label')]
    for e in edges:
        if words(e) > MAX_EDGE_WORDS:
            errors.append(f'edge label over {MAX_EDGE_WORDS} words: {e!r}')
    if t == 'venn':
        for k in ('left', 'right', 'both'):
            if len(spec.get(k, {}).get('points', [])) > 3:
                errors.append(f'venn {k} has more than 3 points')
    odd = sorted({c for x in labels + details + notes + edges for c in x if not font_safe(c)})
    if odd:
        warnings.append(
            f'characters Excalifont may lack (shown in a fallback font): {" ".join(odd)}; '
            'prefer plain words'
        )
    total = sum(words(x) for x in labels + details + notes + edges)
    tpl = TEMPLATES[t]
    if total > tpl.max_words:
        errors.append(
            f"{total} words in the drawing (limit {tpl.max_words}); cut, don't shrink fonts"
        )
    return errors, warnings


# ---- section links ----------------------------------------------------------
def page_headings(out_path: Path, page: str) -> list[str] | None:
    """Headings (## and below) of the summarised page, if it can be found in the vault.

    The drawing is written to <vault>/wiki/visuals/, so the page is looked up under
    the nearest `wiki/` ancestor of the output path.
    """
    wiki = next((p for p in out_path.resolve().parents if p.name == 'wiki'), None)
    hits = list(wiki.rglob(f'{page}.md')) if wiki else []
    if len(hits) != 1:
        return None
    return re.findall(r'^#{2,6} +(.+?) *$', hits[0].read_text(encoding='utf-8'), re.M)


def resolve_section(want: str, headings: list[str] | None) -> tuple[str, str | None]:
    """The full heading `want` names (exactly or by unique prefix), and a problem if any."""
    if headings is None:
        return want, None
    exact = [h for h in headings if h.lower() == want.lower()]
    found = exact or [h for h in headings if h.lower().startswith(want.lower())]
    if len(found) == 1:
        return found[0], None
    return want, f'section {want!r} matches {len(found)} headings of the page'


def heading_link(page: str, heading: str) -> str:
    """Obsidian wikilink to a heading; characters links can't carry become spaces."""
    clean = ' '.join(re.sub(r'[#|^:%\[\]]', ' ', heading).split())
    return f'[[{page}#{clean}]]'


def resolve_links(spec: dict, out_path: Path) -> tuple[list[str], str | None]:
    """Attach `_link` to map cards and resolve the drawing's own section, if any.

    Returns warnings and the resolved top-level section heading.
    """
    headings = page_headings(out_path, spec['page'])
    warnings = (
        []
        if headings is not None
        else [f'page {spec["page"]!r} not found under wiki/; section links are not checked']
    )
    for st in spec.get('stages', []) if spec['template'] == 'map' else []:
        for c in st.get('cards', []):
            if c.get('section'):
                heading, problem = resolve_section(c['section'], headings)
                warnings += [problem] if problem else []
                c['_link'] = heading_link(spec['page'], heading)
    section = None
    if spec.get('section'):
        section, problem = resolve_section(spec['section'], headings)
        warnings += [problem] if problem else []
    return warnings, section


def font_safe(c: str) -> bool:
    """Latin text and common punctuation; arrows, maths and symbols are not."""
    return ord(c) < 0x250 and c not in '×÷±' or c in '–—‘’“”…'


def box(e: dict) -> tuple[float, float, float, float]:
    return e['x'], e['y'], e['x'] + e['width'], e['y'] + e['height']


def solid(elements: list[dict]) -> list[dict]:
    """Visible, free-standing elements: not arrows/lines, shape labels or backdrops.

    Arrow labels count: they can collide with each other and with other arrows.
    """
    arrows = {e['id'] for e in elements if e['type'] == 'arrow'}
    return [
        e
        for e in elements
        if e['type'] not in ('arrow', 'line')
        and (not e.get('containerId') or e['containerId'] in arrows)
        and e.get('_role') != 'backdrop'
    ]


def check_overlaps(elements: list[dict]) -> list[str]:
    """Pairs of solid elements whose boxes intersect."""

    def hit(a, b, m=4):
        ax0, ay0, ax1, ay1 = box(a)
        bx0, by0, bx1, by1 = box(b)
        return not (ax1 + m <= bx0 or bx1 + m <= ax0 or ay1 + m <= by0 or by1 + m <= ay0)

    els = solid(elements)
    return [
        f'overlap: {a["type"]} {a["id"]} ↔ {b["type"]} {b["id"]}'
        for i, a in enumerate(els)
        for b in els[i + 1 :]
        if hit(a, b)
    ]


def check_crossings(elements: list[dict]) -> list[str]:
    """Arrows whose path runs through an element other than the two they connect."""
    out = []
    els = solid(elements)
    for a in elements:
        if a['type'] != 'arrow':
            continue
        ends = {
            (a.get('startBinding') or {}).get('elementId'),
            (a.get('endBinding') or {}).get('elementId'),
        }
        pts = [(a['x'] + px, a['y'] + py) for px, py in a['points']]
        segs = list(zip(pts, pts[1:], strict=False))
        for e in els:
            if e['id'] in ends or e.get('containerId') == a['id']:
                continue
            if any(segment_hits_box(p, q, box(e), shrink=3) for p, q in segs):
                out.append(f'arrow {a["id"]} crosses {e["type"]} {e["id"]}')
    return out


def segment_hits_box(p, q, b, shrink=0.0) -> bool:
    """Liang–Barsky clip of segment pq against box b (shrunk by `shrink` px)."""
    x0, y0, x1, y1 = b[0] + shrink, b[1] + shrink, b[2] - shrink, b[3] - shrink
    dx, dy = q[0] - p[0], q[1] - p[1]
    t0, t1 = 0.0, 1.0
    for pk, qk in ((-dx, p[0] - x0), (dx, x1 - p[0]), (-dy, p[1] - y0), (dy, y1 - p[1])):
        if pk == 0:
            if qk < 0:
                return False
            continue
        r = qk / pk
        if pk < 0:
            t0 = max(t0, r)
        else:
            t1 = min(t1, r)
        if t0 > t1:
            return False
    return True


# ---- file format ---------------------------------------------------------
def spec_hash(spec: dict) -> str:
    return hashlib.sha256(json.dumps(spec, sort_keys=True).encode()).hexdigest()[:12]


def finalise(elements: list[dict], h: str) -> None:
    """Tag generated elements and drop build-time keys."""
    for e in elements:
        tag = {'specHash': h}
        role = e.pop('_role', None)
        if role:
            tag['role'] = role
        e['customData'] = {'visualSummary': tag}


def to_markdown(spec: dict, elements: list[dict], section: str | None = None) -> str:
    scene = {
        'type': 'excalidraw',
        'version': 2,
        'source': 'https://github.com/zsviczian/obsidian-excalidraw-plugin',
        'elements': elements,
        'appState': {'gridSize': None, 'viewBackgroundColor': '#ffffff'},
        'files': {},
    }
    texts = '\n\n'.join(f'{e["text"]} ^{e["id"]}' for e in elements if e['type'] == 'text')
    of = heading_link(spec['page'], section) if section else f'[[{spec["page"]}]]'
    section_fm = (
        f'visual-summary-section: {json.dumps(section, ensure_ascii=False)}\n' if section else ''
    )
    return f"""---
excalidraw-plugin: parsed
tags: [excalidraw, visual-summary]
visual-summary-of: "[[{spec['page']}]]"
{section_fm}visual-summary-template: {spec['template']}
visual-summary-date: {datetime.date.today().isoformat()}
visual-summary-spec-hash: {spec_hash(spec)}
---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==

Visual summary of {of} — generated by llm-wiki-kit/visual-summary.

%%
## Visual summary spec
```json
{json.dumps(spec, indent=1, ensure_ascii=False)}
```
%%

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


LZ_BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='


def lz_decompress_base64(data: str) -> str:
    """LZString.decompressFromBase64 (lz-string 1.5), as the Excalidraw plugin compresses.

    A port of the reference decoder: a stream of variable-width codes, 6 bits per
    base64 character, read low bit first.
    """
    if not data:
        return ''
    vals = [LZ_BASE64.index(c) for c in data]
    pos, val, bit = 0, vals[0], 32  # position in vals, current 6-bit value, bit mask

    def bits(n: int) -> int:
        nonlocal pos, val, bit
        out = 0
        for k in range(n):
            if val & bit:
                out |= 1 << k
            bit >>= 1
            if bit == 0:
                pos += 1
                val, bit = (vals[pos] if pos < len(vals) else 0), 32
        return out

    dictionary: list[str] = ['', '', '']  # 0, 1, 2 are the char-8, char-16 and end codes
    width, enlarge = 3, 4
    code = bits(2)
    if code == 2:
        return ''
    w = chr(bits(8 if code == 0 else 16))
    dictionary.append(w)
    out = [w]
    while True:
        if pos >= len(vals):
            raise ValueError('compressed-json ends without an end code')
        code = bits(width)
        if code in (0, 1):
            dictionary.append(chr(bits(8 if code == 0 else 16)))
            code = len(dictionary) - 1
            enlarge -= 1
        elif code == 2:  # JS strings are UTF-16: rejoin surrogate pairs
            return ''.join(out).encode('utf-16', 'surrogatepass').decode('utf-16')
        if enlarge == 0:
            enlarge, width = 1 << width, width + 1
        if code < len(dictionary):
            entry = dictionary[code]
        elif code == len(dictionary):
            entry = w + w[0]
        else:
            raise ValueError('compressed-json holds an invalid code')
        out.append(entry)
        dictionary.append(w + entry[0])
        enlarge -= 1
        w = entry
        if enlarge == 0:
            enlarge, width = 1 << width, width + 1


def read_scene(path: Path) -> dict:
    """The drawing's scene: plain ```json, or the ```compressed-json Obsidian re-saves.

    With the Excalidraw plugin's `compress` setting on, any edit in Obsidian rewrites
    the block as LZString base64, wrapped across lines; the whitespace is not data.
    """
    text = path.read_text(encoding='utf-8')
    m = re.search(r'## Drawing\n```json\n(.*?)\n```', text, re.S)
    if m:
        return json.loads(m.group(1))
    m = re.search(r'## Drawing\n```compressed-json\n(.*?)\n```', text, re.S)
    if not m:
        raise SystemExit(f'error: no ```json or ```compressed-json drawing block in {path}')
    try:
        return json.loads(lz_decompress_base64(re.sub(r'\s+', '', m.group(1))))
    except (ValueError, IndexError) as e:
        raise SystemExit(
            f'error: cannot decode the compressed-json drawing in {path}: {e}'
        ) from None


# ---- commands ------------------------------------------------------------
def cmd_list() -> int:
    for name, t in TEMPLATES.items():
        print(
            f'{name:9} {t.shape}\n          use when: {t.use_when}\n          not when: {t.not_when}'
        )
    return 0


def cmd_schema(name: str) -> int:
    t = TEMPLATES.get(name)
    if not t:
        print(
            f'error: unknown template {name!r}; choose one of {sorted(TEMPLATES)}', file=sys.stderr
        )
        return 2
    common = {
        'template': name,
        'page': 'slug of the summarised page (wikilink target)',
        'title': 'drawing title (not counted in the word budget)',
        'subtitle': 'optional one-liner (not counted)',
        'section': 'optional: the page heading (or unique prefix) a section drawing summarises',
    }
    limits = {
        'label_words': MAX_LABEL_WORDS,
        'detail_words': MAX_DETAIL_WORDS,
        'note_words': MAX_NOTE_WORDS,
        'max_total_words': t.max_words,
    }
    out = {
        'template': name,
        'shape': t.shape,
        'use_when': t.use_when,
        'not_when': t.not_when,
        'fields': {**common, **t.fields},
        'limits': limits,
        'example': t.example,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


def cmd_build(spec_path: str, out_path: str) -> int:
    raw = Path(spec_path).read_text(encoding='utf-8')
    spec, stored = json.loads(raw), json.loads(raw)  # the build annotates `spec`; `stored` is kept
    errors, warnings = check_spec(spec)
    section = None
    if not errors:
        link_warnings, section = resolve_links(spec, Path(out_path))
        warnings += link_warnings
    for w in warnings:
        print(f'warning: {w}', file=sys.stderr)
    if errors:
        for e in errors:
            print(f'error: {e}', file=sys.stderr)
        return 1
    sc = Scene()
    try:
        TEMPLATES[spec['template']].build(sc, spec)
    except SpecError as e:
        print(f'error: {e}', file=sys.stderr)
        return 1
    except (KeyError, TypeError) as e:
        print(
            f'error: malformed spec ({e!r}); see `visual_summary.py schema {spec["template"]}`',
            file=sys.stderr,
        )
        return 1
    for w in check_overlaps(sc.elements) + check_crossings(sc.elements):
        print(f'warning: {w}', file=sys.stderr)
    finalise(sc.elements, spec_hash(stored))
    Path(out_path).write_text(to_markdown(stored, sc.elements, section), encoding='utf-8')
    xs = [x for e in sc.elements for x in extent(e)[::2]]
    width = round(max(xs) - min(xs))
    stem = Path(out_path).name.removesuffix('.md')
    print(f'built: {out_path} ({len(sc.elements)} elements, template {spec["template"]})')
    print(f'embed: ![[{stem}|{width}]]')
    return 0


def cmd_render(in_path: str, out_png: str, no_text: bool = False) -> int:
    scene = read_scene(Path(in_path))
    if no_text:
        drop = {e['id'] for e in scene['elements'] if e['type'] == 'text'}
        scene['elements'] = [e for e in scene['elements'] if e['id'] not in drop]
        for e in scene['elements']:
            e['boundElements'] = [b for b in e.get('boundElements') or [] if b['id'] not in drop]
    cmd = shlex.split(os.environ.get('EXCALIDRAW_RENDER', RENDER_DEFAULT))
    with tempfile.TemporaryDirectory() as td:
        src = Path(td) / 'scene.excalidraw'
        src.write_text(json.dumps(scene), encoding='utf-8')
        r = subprocess.run(
            [*cmd, str(src), '--out', str(Path(out_png).resolve())],
            capture_output=True,
            text=True,
        )
    if r.returncode != 0:
        print(f'error: render failed ({" ".join(cmd)}):\n{r.stderr.strip()}', file=sys.stderr)
        return 1
    print(f'rendered: {out_png}')
    return 0


def cmd_spec(in_path: str) -> int:
    m = SPEC_BLOCK.search(Path(in_path).read_text(encoding='utf-8'))
    if not m:
        print(f'error: no visual summary spec in {in_path}', file=sys.stderr)
        return 1
    print(m.group(1))
    return 0


def main(argv: list[str]) -> int:
    if argv == ['list']:
        return cmd_list()
    if len(argv) == 2 and argv[0] == 'schema':
        return cmd_schema(argv[1])
    if len(argv) == 3 and argv[0] == 'build':
        return cmd_build(argv[1], argv[2])
    if argv[:1] == ['render'] and len(argv) in (3, 4) and argv[3:] in ([], ['--no-text']):
        return cmd_render(argv[1], argv[2], no_text=len(argv) == 4)
    if len(argv) == 2 and argv[0] == 'spec':
        return cmd_spec(argv[1])
    print(__doc__.split('Env:')[0].strip(), file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
