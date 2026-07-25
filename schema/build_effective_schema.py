#!/usr/bin/env python3
"""build_effective_schema.py — assemble a vault's effective frontmatter schema.

The fleet frontmatter contract is split into:
  * schema/base.schema.json         — universal fields (the SOT)
  * schema/vaults/<slug>.json        — per-vault overlay (legitimate variance only)

The *effective* schema for a vault is base + overlay. This module builds it and,
crucially, cross-checks the overlay's token-derived values (entity_field,
handoff_type) against the vault's existing substitution map
(check-conformance/subs/<slug>.json) so the two SOTs cannot silently drift apart.

Importable:  load_effective_schema(slug) -> (schema_dict, warnings)
CLI:         python3 build_effective_schema.py <vault-slug>
"""

import copy
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_HERE)
_SUBS_DIR = os.path.join(_REPO_ROOT, 'check-conformance', 'subs')


def _is_sentinel(val):
    """A subs token is a documentation-only sentinel when it is a parenthesised
    note (e.g. '(exec-handoff machinery absent — documentation-only vault)')."""
    return isinstance(val, str) and val.strip().startswith('(')


def _load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def load_effective_schema(slug, schema_dir=None, subs_dir=None):
    """Return (effective_schema_dict, warnings). Never raises for a missing subs
    file (consistency check is skipped with a warning); raises FileNotFoundError
    only if the base schema or the overlay is absent."""
    schema_dir = schema_dir or _HERE
    subs_dir = subs_dir or _SUBS_DIR
    warnings = []

    base = _load_json(os.path.join(schema_dir, 'base.schema.json'))
    overlay = _load_json(os.path.join(schema_dir, 'vaults', f'{slug}.json'))

    # --- Cross-check overlay against the subs map (the pre-existing token SOT) ---
    subs_path = os.path.join(subs_dir, f'{slug}.json')
    if os.path.exists(subs_path):
        subs = _load_json(subs_path)
        subs_entity = subs.get('ENTITY_SUBJECT-singular')
        subs_handoff = subs.get('EXEC_HANDOFF')
        expected_entity = None if _is_sentinel(subs_entity) else subs_entity
        expected_handoff = None if _is_sentinel(subs_handoff) else subs_handoff
        if overlay.get('entity_field') != expected_entity:
            warnings.append(
                f'overlay entity_field={overlay.get("entity_field")!r} disagrees with '
                f'subs ENTITY_SUBJECT-singular (expected {expected_entity!r})'
            )
        if overlay.get('handoff_type') != expected_handoff:
            warnings.append(
                f'overlay handoff_type={overlay.get("handoff_type")!r} disagrees with '
                f'subs EXEC_HANDOFF (expected {expected_handoff!r})'
            )
    else:
        warnings.append(f'subs file not found for consistency check: {subs_path}')

    # --- Merge base + overlay into the effective schema ---
    eff = copy.deepcopy(base)
    props = eff['properties']
    conf = eff.setdefault('$conformance', {})

    # type enum: insert the vault's exec-handoff record type, if any.
    handoff = overlay.get('handoff_type')
    if handoff and handoff not in props['type']['enum']:
        # keep it next to the other handoff type for readability
        enum = props['type']['enum']
        insert_at = enum.index('planning-handoff') if 'planning-handoff' in enum else len(enum)
        props['type']['enum'] = enum[:insert_at] + [handoff] + enum[insert_at:]

    # roles enum (membership itself is reported by phase_2_role_drift, but keep the
    # enum here so the effective schema is a complete, self-describing document).
    if overlay.get('roles'):
        props['roles']['items']['enum'] = overlay['roles']

    # status enum extensions (e.g. FG's needs-review).
    for extra in overlay.get('status_add', []):
        if extra not in props['status']['enum']:
            props['status']['enum'].append(extra)

    # entity field: a typed, optional property named per vault (null → none expected).
    entity_field = overlay.get('entity_field')
    if entity_field:
        props[entity_field] = {'type': ['string', 'null']}
    conf['entity_field'] = entity_field

    # extra per-vault fields (e.g. FG volatility / next_review).
    for name, spec in (overlay.get('extra_fields') or {}).items():
        props[name] = spec

    # topics prefix constraint (IS / SS).
    conf['topics_prefix'] = overlay.get('topics_prefix')
    conf['vault_slug'] = slug

    return eff, warnings


def main(argv):
    if len(argv) != 2:
        print('usage: build_effective_schema.py <vault-slug>', file=sys.stderr)
        return 2
    slug = argv[1]
    try:
        eff, warnings = load_effective_schema(slug)
    except FileNotFoundError as e:
        print(f'ERROR: {e}', file=sys.stderr)
        return 2
    for w in warnings:
        print(f'WARNING: {w}', file=sys.stderr)
    print(json.dumps(eff, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
