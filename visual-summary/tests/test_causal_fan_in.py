"""causal-map: labelled arrows converging on a node build without collisions.

MZY-365: four or more labelled arrows into one node carry their labels at the
source end. MZY-369: a source with several such arrows (it feeds two crowded
nodes) spreads their ports so its labels clear each other.
"""

import importlib.util
import sys
from pathlib import Path

import pytest

SCRIPT_PATH = Path(__file__).resolve().parents[1] / 'visual_summary.py'


def load_script():
    spec = importlib.util.spec_from_file_location('visual_summary_fan_in', SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod  # dataclasses look the module up while it loads
    spec.loader.exec_module(mod)
    return mod


vs = load_script()


def warnings_for(spec):
    sc = vs.Scene()
    vs.TEMPLATES[spec['template']].build(sc, spec)
    return vs.check_overlaps(sc.elements) + vs.check_crossings(sc.elements)


def five_into_one(direction, detail):
    """The shape of the 2026-10-17 churn spec that failed: five drivers, one outcome."""
    labels = ['more satisfied', 'costly to leave', 'varies by study', 'flat-rate caution']
    labels.append('little verification')
    nodes = [
        {'id': f's{k}', 'label': f'Driver {k}', **({'detail': 'two short words'} if detail else {})}
        for k in range(5)
    ]
    nodes.append({'id': 'y', 'label': 'Churn', 'role': 'outcome'})
    edges = [{'from': f's{k}', 'to': 'y', 'sign': '-', 'label': labels[k]} for k in range(5)]
    return {'template': 'causal-map', 'title': 't', 'page': 'p', 'direction': direction,
            'nodes': nodes, 'edges': edges}  # fmt: skip


def four_into_two(direction):
    """Every source feeds both crowded outcomes."""
    srcs = ['a', 'b', 'c', 'd']
    nodes = [{'id': s, 'label': s.upper()} for s in srcs]
    nodes += [{'id': t, 'label': t.upper(), 'role': 'outcome'} for t in ('y', 'z')]
    edges = [
        {'from': s, 'to': t, 'sign': '+', 'label': 'some effect'} for s in srcs for t in ('y', 'z')
    ]
    return {'template': 'causal-map', 'title': 't', 'page': 'p', 'direction': direction,
            'nodes': nodes, 'edges': edges}  # fmt: skip


@pytest.mark.parametrize('direction', ['right', 'down'])
@pytest.mark.parametrize('detail', [True, False])
def test_five_labelled_arrows_into_one_node(direction, detail):
    assert warnings_for(five_into_one(direction, detail)) == []


@pytest.mark.parametrize('direction', ['right', 'down'])
def test_sources_feeding_two_crowded_nodes(direction):
    assert warnings_for(four_into_two(direction)) == []
