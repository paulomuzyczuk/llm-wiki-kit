"""read_scene: plain ```json drawings and the ```compressed-json Obsidian re-saves.

Fixtures:
- fixtures/carryover.excalidraw.md: a drawing as `build` writes it (copied from the
  a real vault page, marketing-mix-modeling--carryover).
- fixtures/carryover.compressed.excalidraw.md: the same file with its ```json block
  replaced by LZString.compressToBase64 output from lz-string 1.5.0 (Node), wrapped
  in 256-character lines separated by blank lines, as the Excalidraw plugin saves it.

The expected strings in test_lz_decompress_base64 were produced by the same
lz-string 1.5.0 `compressToBase64`.
"""

import importlib.util
import json
import re
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
FIXTURES = HERE / 'fixtures'
SCRIPT_PATH = HERE.parent / 'visual_summary.py'


def load_script():
    spec = importlib.util.spec_from_file_location('visual_summary_under_test', SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod  # dataclasses look the module up while it loads
    spec.loader.exec_module(mod)
    return mod


vs = load_script()


@pytest.mark.parametrize(
    ('compressed', 'plain'),
    [
        ('', ''),
        ('Q===', ''),
        ('IZA=', 'a'),
        ('IY18aQ==', 'a' * 24),
        (
            'MICwrgTgdgBIKAQwDYHsDuBTCBnGheDcEJ7MAP1APcDGyAJujIMjkMAhgEbktuvtA===',
            'Churn — lowers 🙂 ünïcode ✓ abcabcabcabc',
        ),
    ],
)
def test_lz_decompress_base64(compressed, plain):
    assert vs.lz_decompress_base64(compressed) == plain


def test_compressed_drawing_reads_as_the_plain_one():
    plain = vs.read_scene(FIXTURES / 'carryover.excalidraw.md')
    compressed = vs.read_scene(FIXTURES / 'carryover.compressed.excalidraw.md')
    assert compressed == plain
    assert plain['elements']


def test_compressed_block_round_trips_to_the_same_json_text():
    text = (FIXTURES / 'carryover.excalidraw.md').read_text(encoding='utf-8')
    original = re.search(r'## Drawing\n```json\n(.*?)\n```', text, re.S).group(1)
    ctext = (FIXTURES / 'carryover.compressed.excalidraw.md').read_text(encoding='utf-8')
    block = re.search(r'## Drawing\n```compressed-json\n(.*?)\n```', ctext, re.S).group(1)
    assert '\n\n' in block  # wrapped, as the plugin saves it
    assert vs.lz_decompress_base64(re.sub(r'\s+', '', block)) == original
    json.loads(original)


def test_missing_drawing_block_names_both_formats(tmp_path):
    p = tmp_path / 'empty.excalidraw.md'
    p.write_text('# Excalidraw Data\n', encoding='utf-8')
    with pytest.raises(SystemExit, match='compressed-json'):
        vs.read_scene(p)


def test_truncated_compressed_block_is_reported(tmp_path):
    ctext = (FIXTURES / 'carryover.compressed.excalidraw.md').read_text(encoding='utf-8')
    cut = re.sub(
        r'(```compressed-json\n)(.*?)(\n```)', lambda m: m[1] + m[2][:200] + m[3], ctext, flags=re.S
    )
    p = tmp_path / 'cut.excalidraw.md'
    p.write_text(cut, encoding='utf-8')
    with pytest.raises(SystemExit, match='cannot decode'):
        vs.read_scene(p)
