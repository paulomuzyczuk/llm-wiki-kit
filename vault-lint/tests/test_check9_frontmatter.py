"""Tests for check_9_frontmatter_schema and the effective-schema loader.

Two layers:
  * Unit tests drive check_9 with a hand-built effective schema so they do not
    couple to overlay evolution.
  * Integration tests exercise the real schema/ files (base + the shipped
    software-craft overlay) through lint._load_effective_schema, pinning that the
    overlay and its subs map agree, and that a missing overlay skips cleanly.
"""

from conftest import frontmatter, lint, make_pages

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def eff_schema(
    entity_field='project',
    extra_props=None,
    status_enum=None,
    topics_prefix=None,
    handoff='coding-handoff',
    roles=None,
):
    """A minimal stand-in for build_effective_schema output."""
    roles_items = {'type': 'string'}
    if roles is not None:
        roles_items['enum'] = roles
    props = {
        'title': {'type': 'string'},
        'aliases': {'type': 'array', 'items': {'type': 'string'}},
        'date': {'type': 'string', 'format': 'date'},
        'last_updated': {'type': 'string', 'format': 'date'},
        'type': {
            'type': 'string',
            'enum': ['entity', 'topic', handoff, 'planning-handoff', 'book', 'digest'],
        },
        'topics': {'type': 'array', 'items': {'type': 'string'}},
        'roles': {'type': 'array', 'items': roles_items},
        'source_tier': {'type': 'integer', 'enum': [1, 2, 3]},
        'source_count': {'type': 'integer'},
        'status': {'type': 'string', 'enum': status_enum or ['active', 'stub', 'archived']},
        'note': {'type': 'string'},
        'size_note': {'type': 'string'},
    }
    if entity_field:
        props[entity_field] = {'type': ['string', 'null']}
    if extra_props:
        props.update(extra_props)
    return {
        'properties': props,
        'required': ['title', 'type'],
        'additionalProperties': False,
        '$conformance': {
            'required_on_type': {
                'topic': [
                    'title',
                    'aliases',
                    'date',
                    'last_updated',
                    'topics',
                    'source_tier',
                    'source_count',
                    'status',
                ],
            },
            'additional_properties_severity': 'warn',
            'topics_prefix': topics_prefix,
        },
    }


def good_topic(**overrides):
    fields = dict(
        title='X',
        aliases=[],
        date='2026-01-01',
        last_updated='2026-01-02',
        type='topic',
        topics=['t'],
        roles=['code-craftsperson'],
        source_tier=1,
        source_count=2,
        status='active',
        project='null',
    )
    fields.update(overrides)
    return frontmatter(**fields) + '\n# X\n'


def run_c9(mapping, schema, warnings=()):
    pages, _ = make_pages(mapping)
    return lint.check_9_frontmatter_schema(pages, schema, warnings)


# ---------------------------------------------------------------------------
# unit tests
# ---------------------------------------------------------------------------


def test_clean_topic_passes():
    r = run_c9({'wiki/topics/a.md': good_topic()}, eff_schema())
    assert r['errors'] == []
    assert r['warnings'] == []


def test_missing_required_field_errors():
    page = good_topic()
    page = page.replace('source_tier: 1\n', '')  # drop a required field
    r = run_c9({'wiki/topics/a.md': page}, eff_schema())
    assert any(e['field'] == 'source_tier' and 'required' in e['msg'] for e in r['errors'])


def test_bad_status_enum_errors():
    r = run_c9({'wiki/topics/a.md': good_topic(status='frobnicate')}, eff_schema())
    assert any(e['field'] == 'status' for e in r['errors'])


def test_bad_source_tier_enum_errors():
    r = run_c9({'wiki/topics/a.md': good_topic(source_tier=9)}, eff_schema())
    assert any(e['field'] == 'source_tier' for e in r['errors'])


def test_malformed_date_errors():
    r = run_c9({'wiki/topics/a.md': good_topic(last_updated='2026/01/02')}, eff_schema())
    assert any(e['field'] == 'last_updated' and 'date' in e['msg'] for e in r['errors'])


def test_unexpected_field_warns_not_errors():
    # 'volatility' is not in this (SC-shaped) schema → advisory warning, no error.
    r = run_c9({'wiki/topics/a.md': good_topic(volatility='live')}, eff_schema())
    assert r['errors'] == []
    assert any(w['field'] == 'volatility' for w in r['warnings'])


def test_wrong_entity_field_warns():
    # A page carrying `portfolio` in a project-vault schema → unexpected-field warn
    # (this is exactly the fleet-wide role-MoC project: drift, inverted).
    sch = eff_schema(entity_field='portfolio')  # vault expects portfolio, page has project
    r = run_c9({'wiki/topics/a.md': good_topic()}, sch)  # good_topic carries project:
    assert any(w['field'] == 'project' for w in r['warnings'])


def test_roles_not_reported_by_check9():
    # roles is owned by phase_2_role_drift; check_9 must not report its absence.
    page = good_topic()
    page = page.replace('roles: [code-craftsperson]\n', '')
    r = run_c9({'wiki/topics/a.md': page}, eff_schema())
    assert not any(e['field'] == 'roles' for e in r['errors'])
    assert not any(w['field'] == 'roles' for w in r['warnings'])


def test_non_topic_page_not_field_validated():
    # A book entity with its own frontmatter vocabulary must not flood warnings.
    book = frontmatter(title='B', type='book', author='Someone', year=2020, slug='b') + '\n# B\n'
    r = run_c9({'wiki/entities/books/b.md': book}, eff_schema())
    assert r['errors'] == []
    assert not any(w['field'] in ('author', 'year', 'slug') for w in r['warnings'])


def test_bad_type_enum_caught_on_any_page():
    # `type` is enum-checked everywhere, so a typo is caught even on a non-topic page.
    bad = frontmatter(title='B', type='entty') + '\n# B\n'
    r = run_c9({'wiki/entities/b.md': bad}, eff_schema())
    assert any(e['field'] == 'type' for e in r['errors'])


def test_archived_tombstone_skipped():
    stub = frontmatter(title='old', type='topic', status='archived') + '\nMerged into [[new]]\n'
    r = run_c9({'wiki/topics/old.md': stub}, eff_schema())
    assert r['errors'] == []


def test_topics_prefix_warns():
    sch = eff_schema(entity_field=None, topics_prefix='my-domain')
    page = good_topic(topics=['roles', 'navigation'], project=None)
    r = run_c9({'wiki/topics/role-x.md': page}, sch)
    assert any(w['field'] == 'topics' and 'my-domain' in w['msg'] for w in r['warnings'])


def test_role_moc_exempt_from_topics_prefix():
    # A genuine role-MoC (slug == role-<role in enum>) leads topics with `roles`
    # and must NOT trigger the topics-prefix warning.
    sch = eff_schema(
        entity_field=None,
        topics_prefix='my-domain',
        roles=['maintainer', 'release-manager'],
    )
    page = good_topic(topics=['roles', 'navigation'], project=None)
    r = run_c9({'wiki/topics/role-maintainer.md': page}, sch)
    assert not any(w['field'] == 'topics' for w in r['warnings'])


def test_non_moc_role_prefixed_page_still_checked():
    # A content page that merely starts with 'role-' but is not a role slug
    # (e.g. role-of-testing) is still subject to the topics-prefix rule.
    sch = eff_schema(entity_field=None, topics_prefix='my-domain', roles=['maintainer'])
    page = good_topic(topics=['metadata'], project=None)
    r = run_c9({'wiki/topics/role-of-testing.md': page}, sch)
    assert any(w['field'] == 'topics' for w in r['warnings'])


def test_schema_build_warnings_surface():
    r = run_c9({'wiki/topics/a.md': good_topic()}, eff_schema(), warnings=['overlay/subs disagree'])
    assert any('overlay/subs disagree' in w['msg'] for w in r['warnings'])


# ---------------------------------------------------------------------------
# integration tests — the real schema/ files
#
# This example kit ships a single example overlay (schema/vaults/software-craft.json)
# paired with check-conformance/subs/software-craft.json. Any other vault's overlays
# are not shipped here, so the integration tests cover only what the kit ships;
# the unit tests above already exercise the documentation-only (null entity) and
# freshness-extra-field code paths against hand-built schemas.
# ---------------------------------------------------------------------------

SHIPPED_VAULTS = ['software-craft']


def test_load_effective_schema_software_craft():
    eff, warnings = lint._load_effective_schema('software-craft')
    assert eff is not None
    assert warnings == []
    assert 'coding-handoff' in eff['properties']['type']['enum']
    assert eff['$conformance']['entity_field'] == 'project'


def test_all_overlays_agree_with_subs():
    # Zero consistency warnings for every shipped overlay — guards overlay vs subs drift.
    for slug in SHIPPED_VAULTS:
        eff, warnings = lint._load_effective_schema(slug)
        assert eff is not None, slug
        assert warnings == [], f'{slug}: {warnings}'


def test_missing_overlay_schema_skips_cleanly():
    # A vault with no shipped overlay must not crash the lint: _load_effective_schema
    # returns (None, warnings) so check_9 is skipped rather than raising.
    eff, warnings = lint._load_effective_schema('no-such-vault')
    assert eff is None
    assert warnings and any('not found' in w for w in warnings)
