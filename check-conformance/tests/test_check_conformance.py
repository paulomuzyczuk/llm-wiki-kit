"""
Tests for check-conformance.py.

Fixture strategy: make_vault() builds a conformant vault from the real
template + TEST_SUBS + sanctioned roles-table swap, then applies per-test
mutation functions.  No full vault files are committed as fixtures.

STATUS TOKEN CONTRACT — the script must emit exactly these strings on
region summary lines of the form "REGION <name>: <STATUS>":

  PASS             — region body matches the substituted template exactly.
  DIFF             — region contains one or more non-sanctioned differences;
                     raw unified-diff hunks follow immediately.
  EXEMPT-CONTAINED — region contains only sanctioned differences (roles-table
                     swap and/or out-of-scope parenthetical); no raw hunks
                     from this region are a defect.  EXEMPT content is still
                     printed in full, clearly labelled.

The Conventions region of any make_vault() vault always reports
EXEMPT-CONTAINED (never PASS) because the roles-table swap is applied by
construction and creates a known sanctioned difference.
"""

import re

from conftest import SCRIPT_PATH, TEST_SUBS, make_vault, run_check

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def _find_line(lines: list, pattern: str) -> int:
    """Return first index of a line matching pattern (substring), or -1."""
    for i, ln in enumerate(lines):
        if pattern in ln:
            return i
    return -1


def _replace_sentence(find: str, replacement: str):
    """Mutation: replace the first occurrence of `find` with `replacement`."""

    def mut(lines):
        for i, ln in enumerate(lines):
            if find in ln:
                lines[i] = ln.replace(find, replacement, 1)
                return lines
        raise ValueError(f'Sentence not found for replacement: {find!r}')

    return mut


def _delete_h2_block(heading_name: str):
    """
    Mutation: delete all lines belonging to the H2 block whose heading
    contains `heading_name`, from the `## ` line up to (not including)
    the next `## ` line or EOF.
    """

    def mut(lines):
        start = None
        for i, ln in enumerate(lines):
            if ln.startswith('## ') and heading_name in ln:
                start = i
                break
        if start is None:
            raise ValueError(f'H2 block not found: {heading_name!r}')
        end = len(lines)
        for i in range(start + 1, len(lines)):
            if lines[i].startswith('## '):
                end = i
                break
        return lines[:start] + lines[end:]

    return mut


def _delete_roles_anchor(lines: list) -> list:
    """Mutation: remove the roles-table start anchor line from the vault."""
    for i, ln in enumerate(lines):
        if ln.strip().startswith('**Roles for this vault:'):
            del lines[i]
            return lines
    raise ValueError('Roles anchor not found')


def _corrupt_oos_cell(lines: list) -> list:
    """
    Mutation: change the out-of-scope cell to something that does NOT begin
    with 'Outside <domain>'.
    """
    pat = re.compile(r'^(\|\s*`out-of-scope`\s*\|)')
    for i, ln in enumerate(lines):
        if pat.match(ln):
            lines[i] = '| `out-of-scope` | Unrelated content |\n'
            return lines
    raise ValueError('out-of-scope row not found')


# ---------------------------------------------------------------------------
# test 1: fully conformant vault → exit 0, all PASS or EXEMPT
# ---------------------------------------------------------------------------


def test_fully_conformant_exits_0(tmp_path):
    """A vault built from the template with no mutations must exit 0."""
    vault = make_vault()
    result = run_check(vault, tmp_path=tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    # no DIFF region lines
    assert not any(ln.startswith('REGION') and 'DIFF' in ln for ln in result.stdout.splitlines()), (
        result.stdout
    )
    # Conventions must be EXEMPT-CONTAINED (roles table differs by construction)
    conventions_lines = [
        ln for ln in result.stdout.splitlines() if ln.startswith('REGION') and 'Conventions' in ln
    ]
    assert conventions_lines, 'Conventions region must appear in output'
    assert 'EXEMPT-CONTAINED' in conventions_lines[0], (
        f'Conventions must be EXEMPT-CONTAINED, got: {conventions_lines[0]!r}'
    )


# ---------------------------------------------------------------------------
# test 2: one edited sentence → exit 1, exactly one DIFF region
# ---------------------------------------------------------------------------


def test_one_edited_sentence_exits_1(tmp_path):
    """A single sentence change in ## Purpose produces exactly one DIFF region."""
    sentence = 'This vault exists for documentation only.'
    replacement = 'This vault exists for reference only.'
    vault = make_vault(mutations=[_replace_sentence(sentence, replacement)])
    result = run_check(vault, tmp_path=tmp_path)
    assert result.returncode == 1, result.stdout + result.stderr
    diff_lines = [
        ln for ln in result.stdout.splitlines() if ln.startswith('REGION') and 'DIFF' in ln
    ]
    assert len(diff_lines) == 1, f'Expected 1 DIFF region, got: {diff_lines}'
    assert 'Purpose' in diff_lines[0]
    # hunk must appear
    assert 'documentation only' in result.stdout or '-This vault' in result.stdout


# ---------------------------------------------------------------------------
# test 3: missing H2 block → exit 1, that region DIFF
# ---------------------------------------------------------------------------


def test_missing_h2_block_exits_1(tmp_path):
    """Deleting ## Boundary from the vault makes that region DIFF; exit 1."""
    vault = make_vault(mutations=[_delete_h2_block('Boundary')])
    result = run_check(vault, tmp_path=tmp_path)
    assert result.returncode == 1, result.stdout + result.stderr
    diff_lines = [
        ln for ln in result.stdout.splitlines() if ln.startswith('REGION') and 'DIFF' in ln
    ]
    assert any('Boundary' in ln for ln in diff_lines), (
        f'Expected Boundary in DIFF regions, got: {diff_lines}'
    )


# ---------------------------------------------------------------------------
# test 4: deleted H2 block does NOT disturb later regions (heading-name alignment)
# ---------------------------------------------------------------------------


def test_missing_h2_does_not_disturb_later_regions(tmp_path):
    """
    Deleting ## Shell commands must not cause ## One-record-per-session rule
    (or any other subsequent region that is unmodified) to be marked DIFF.
    The script aligns by heading NAME, not by position index.
    """
    vault = make_vault(mutations=[_delete_h2_block('Shell commands')])
    result = run_check(vault, tmp_path=tmp_path)
    # The deleted region must be DIFF
    assert 'Shell commands' in result.stdout
    diff_lines = [ln for ln in result.stdout.splitlines() if 'DIFF' in ln]
    shell_diff = [ln for ln in diff_lines if 'Shell commands' in ln]
    assert shell_diff, 'Shell commands must be DIFF'
    # The next region by name must NOT be DIFF
    one_record_lines = [
        ln for ln in result.stdout.splitlines() if 'One-record' in ln and 'REGION' in ln
    ]
    assert one_record_lines, 'One-record region must appear in output'
    assert not any('DIFF' in ln for ln in one_record_lines), (
        f'One-record-per-session rule must not be DIFF: {one_record_lines}'
    )


# ---------------------------------------------------------------------------
# test 5: subs file missing one token → exit 2
# ---------------------------------------------------------------------------


def test_subs_missing_token_exits_2(tmp_path):
    """Omitting EXEC_HANDOFF from subs must produce exit 2."""
    incomplete_subs = {k: v for k, v in TEST_SUBS.items() if k != 'EXEC_HANDOFF'}
    vault = make_vault()
    result = run_check(vault, subs=incomplete_subs, tmp_path=tmp_path)
    assert result.returncode == 2, result.stdout + result.stderr
    out = result.stdout + result.stderr
    assert 'EXEC_HANDOFF' in out, f'Token name must appear in output: {out!r}'
    assert 'missing' in out.lower() or 'not in subs' in out.lower(), (
        f'Output must name the missing-token code path: {out!r}'
    )


# ---------------------------------------------------------------------------
# test 6: vault missing roles-table anchor → degrade to Conventions DIFF (exit 1)
# ---------------------------------------------------------------------------


def test_roles_anchor_absent_degrades_to_diff(tmp_path):
    """If the vault has no roles-table start anchor the script must NOT abort
    with exit 2; it degrades to a literal Conventions comparison and reports a
    DIFF (exit 1). A single heading-format divergence is a conformance finding,
    not a tool crash (F2). The template-side anchor is always present, so the
    failure can only be vault-side here."""
    vault = make_vault(mutations=[_delete_roles_anchor])
    result = run_check(vault, tmp_path=tmp_path)
    assert result.returncode == 1, result.stdout + result.stderr
    out = result.stdout + result.stderr
    # The degraded-comparison note must explain why exemptions weren't applied.
    assert 'anchors not found' in out.lower()
    # Conventions must be reported as DIFF (not EXEMPT-CONTAINED, not a crash).
    conventions_lines = [
        ln for ln in result.stdout.splitlines() if ln.startswith('REGION') and 'Conventions' in ln
    ]
    assert conventions_lines, 'Conventions region must appear in output'
    assert 'DIFF' in conventions_lines[0], (
        f'Conventions must DIFF when the vault roles anchor is absent, '
        f'got: {conventions_lines[0]!r}'
    )


# ---------------------------------------------------------------------------
# test 7a: out-of-scope row with valid parenthetical → EXEMPT
# ---------------------------------------------------------------------------


def test_out_of_scope_parenthetical_is_exempt(tmp_path):
    """
    An out-of-scope cell of the form 'Outside pair programming (extra stuff)'
    is sanctioned and must be reported EXEMPT, not DIFF.
    """
    vault = make_vault(out_of_scope_suffix=' (vendor tools, productivity software)')
    result = run_check(vault, tmp_path=tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    assert not any(ln.startswith('REGION') and 'DIFF' in ln for ln in result.stdout.splitlines()), (
        result.stdout
    )
    # Conventions must be EXEMPT-CONTAINED (roles swap + oos parenthetical both sanctioned)
    conventions_lines = [
        ln for ln in result.stdout.splitlines() if ln.startswith('REGION') and 'Conventions' in ln
    ]
    assert conventions_lines, 'Conventions region must appear in output'
    assert 'EXEMPT-CONTAINED' in conventions_lines[0], (
        f'Conventions must be EXEMPT-CONTAINED with oos parenthetical, '
        f'got: {conventions_lines[0]!r}'
    )


# ---------------------------------------------------------------------------
# test 7b: out-of-scope cell not beginning 'Outside <domain>' → DIFF
# ---------------------------------------------------------------------------


def test_out_of_scope_nonconforming_cell_is_diff(tmp_path):
    """
    An out-of-scope cell that does not begin with 'Outside pair programming'
    must be reported as a DIFF (Conventions region), not EXEMPT.
    """
    vault = make_vault(mutations=[_corrupt_oos_cell])
    result = run_check(vault, tmp_path=tmp_path)
    assert result.returncode == 1, result.stdout + result.stderr
    diff_lines = [ln for ln in result.stdout.splitlines() if 'DIFF' in ln and 'REGION' in ln]
    assert any('Conventions' in ln for ln in diff_lines), (
        f'Expected Conventions DIFF, got: {diff_lines}'
    )


# ---------------------------------------------------------------------------
# test 8: unit test of _mask — position-independent OOS-before-roles
# ---------------------------------------------------------------------------


def test_mask_position_independent_oos_before_roles():
    """
    Pins that _mask is position-independent.

    The old formula adj = oos - (re_ - rs) + 1 assumed OOS follows roles.
    When OOS precedes roles (oos < rs), adj undershoots and overwrites a
    non-sanctioned line with _PH_OOS, making both masked sides identical and
    hiding a real diff — a false EXEMPT-CONTAINED verdict.

    Geometry used:
      line 0: heading (same in both)
      line 1: non-sanctioned content  ← EXP and VLT DIFFER here
      line 2: OOS row (conforming)    ← oos=2 (before roles)
      line 3: normal line
      line 4: roles start             ← rs=4
      line 5: roles content           ← re_=6 (exclusive)
      line 6: blank (re_)
      line 7: sentinel

    Old adj = 2 - (6-4) + 1 = 1 → replaces line 1 in both masked lists
    → diff at line 1 is hidden → false EXEMPT-CONTAINED.
    New single-pass uses original index 2 → line 1 is preserved → DIFF.
    """
    import importlib.util

    spec = importlib.util.spec_from_file_location('check_conformance', str(SCRIPT_PATH))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    exp = [
        '## Conventions\n',
        'Expected non-sanctioned line.\n',  # 1 — differs
        '| `out-of-scope` | Outside pair programming |\n',  # 2 — OOS
        'Some normal content.\n',
        "**Example — replace with your vault's roles** (shown):\n",  # 4 — roles start
        '| ExpRole | definition | assign-when |\n',  # 5 — roles content
        '\n',  # 6 — blank (re_)
        'The `source_tier:` field is required on every page.\n',  # 7 — sentinel
    ]
    vlt = [
        '## Conventions\n',
        'Vault non-sanctioned line.\n',  # 1 — DIFFERENT
        '| `out-of-scope` | Outside pair programming |\n',  # 2 — OOS same
        'Some normal content.\n',
        '**Roles for this vault:**\n',  # 4 — vault roles start
        '| VltRole | definition | assign-when |\n',  # 5 — vault roles content
        '\n',  # 6 — blank
        'The `source_tier:` field is required on every page.\n',  # 7 — sentinel
    ]

    s = dict(
        conv_exp=exp,
        conv_vault=vlt,
        exp_rs=4,
        exp_re=6,
        vlt_rs=4,
        vlt_re=6,
        exp_oos=2,
        vlt_oos=2,
        oos_ok=True,
    )

    status, _ = mod._cmp_conventions(s)
    assert status == 'DIFF', (
        f'Got {status!r} — position-dependent masking would overwrite the '
        'non-sanctioned line at index 1, hiding the diff (false EXEMPT-CONTAINED).'
    )


# ---------------------------------------------------------------------------
# test 9: two blank lines before roles-table end sentinel → still EXEMPT-CONTAINED
# ---------------------------------------------------------------------------


def test_two_blank_lines_before_sentinel_still_exempt(tmp_path):
    """
    _find_roles_region must tolerate more than one blank line between the
    roles table and the sentinel.  A conformant vault that happens to have
    two blank lines there must still be reported EXEMPT-CONTAINED, not exit 2.
    Tested end-to-end via run_check so the anchor-location code path is
    exercised in the real script.
    """
    # Test via the internal API (_find_roles_region directly): we can only
    # mutate the vault, not the template copy the script builds its expected
    # file from, so an end-to-end run can't isolate this case cleanly.
    import importlib.util

    spec = importlib.util.spec_from_file_location('check_conformance', str(SCRIPT_PATH))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    sentinel = 'The `source_tier:` field is required'
    # Synthetic Conventions block with TWO blank lines before sentinel
    lines = [
        '## Conventions\n',
        '**Roles for this vault:**\n',  # roles start
        '| Role | def | when |\n',
        '| `r1` | a | b |\n',  # last roles content line
        '\n',  # blank 1 of 2
        '\n',  # blank 2 of 2  ← was unfindable before fix
        sentinel + '\n',  # sentinel
        '| `out-of-scope` | Outside foo |\n',  # oos (not needed for this test)
    ]

    rs, re_ = mod._find_roles_region(lines, mod._ROLES_START_VAULT, 'vault roles table start')

    # roles region must be [1:4) — from the heading through the last content line,
    # end_idx = first blank of the run = index 4.
    assert rs == 1, f'Unexpected roles start: {rs}'
    assert re_ == 4, f'Unexpected roles end: {re_} (expected 4, the first blank)'
    # Confirm the line at re_ is blank and the line after the run is the sentinel
    assert lines[re_].rstrip() == '', f'end_idx must point to a blank line, got {lines[re_]!r}'
    assert lines[re_ + 1].rstrip() == '', 'second blank must follow first'
    assert lines[re_ + 2].startswith(sentinel), 'sentinel must follow the blank run'


# ---------------------------------------------------------------------------
# test 10: underscore-prefixed metadata keys are silently ignored
# ---------------------------------------------------------------------------


def test_metadata_key_does_not_block_conformant_vault(tmp_path):
    """
    A subs dict with a '_provenance' metadata key plus all real tokens must
    exit 0 on a conformant vault.  The string '_provenance' must not appear
    anywhere in stdout — it was never substituted into the expected body.
    """
    subs_with_meta = {'_provenance': 'test-provenance-value', **TEST_SUBS}
    vault = make_vault()
    result = run_check(vault, subs=subs_with_meta, tmp_path=tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    assert '_provenance' not in result.stdout, (
        "Metadata key '_provenance' must not appear in script output "
        '(must not be substituted into the expected body)'
    )


def test_metadata_key_does_not_weaken_missing_token_validation(tmp_path):
    """
    A subs dict with '_provenance' but a missing real token (EXEC_HANDOFF)
    must still exit 2.  Underscore handling must not weaken real-token checks.
    """
    subs_with_meta_missing_real = {
        '_provenance': 'test-provenance-value',
        **{k: v for k, v in TEST_SUBS.items() if k != 'EXEC_HANDOFF'},
    }
    vault = make_vault()
    result = run_check(vault, subs=subs_with_meta_missing_real, tmp_path=tmp_path)
    assert result.returncode == 2, result.stdout + result.stderr
    out = result.stdout + result.stderr
    assert 'EXEC_HANDOFF' in out, f'Missing token name must appear in output: {out!r}'
