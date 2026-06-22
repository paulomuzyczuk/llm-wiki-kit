#!/usr/bin/env python3
"""check-conformance.py — template-vs-vault mechanical probe.

CLI:   check-conformance.py --vault PATH --template PATH --subs PATH
Exit:  0 = no non-sanctioned diffs; 1 = diffs found; 2 = error.
"""
import argparse
import difflib
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Anchors for sanctioned sub-regions (prose-pattern, per design survey)
# ---------------------------------------------------------------------------
_ROLES_START_EXPECTED = re.compile(r"^\*\*Roles for this vault:\*\*")
_ROLES_START_VAULT    = re.compile(r"^\*\*Roles for this vault:\*\*")
_ROLES_END_SENTINEL   = "The `source_tier:` field is required"
_OOS_ROW_PAT          = re.compile(r"^\|\s*`out-of-scope`\s*\|")
_TOKEN_PAT            = re.compile(r"\{\{([^}]+)\}\}")

CONVENTIONS_NAME   = "Conventions"
_PH_ROLES          = "[[[SANCTIONED-ROLES-TABLE]]]\n"
_PH_OOS            = "[[[SANCTIONED-OOS-ROW]]]\n"


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def _die(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(2)


def _emit(line: str) -> None:
    sys.stdout.write(line if line.endswith("\n") else line + "\n")


# ---------------------------------------------------------------------------
# Template processing
# ---------------------------------------------------------------------------

def _strip_header(text: str) -> str:
    """Remove all leading HTML comment blocks (version comments + instantiation header) and blank lines."""
    while text.startswith("<!--"):
        end = text.index("-->")
        text = text[end + 3:].lstrip("\n")
    return text


def _discover_tokens(text: str) -> set:
    return set(_TOKEN_PAT.findall(text))


def _validate_subs(subs: dict, discovered: set) -> None:
    real = {k: v for k, v in subs.items() if not k.startswith("_")}
    errors = []
    for tok in sorted(discovered - set(real)):
        errors.append(f"ERROR: token missing from subs: {tok}")
    for tok in sorted(set(real) - discovered):
        errors.append(f"ERROR: token not in template body (extra in subs): {tok}")
    if errors:
        for msg in errors:
            print(msg, file=sys.stderr)
        sys.exit(2)


def _substitute(text: str, subs: dict) -> str:
    for token, value in subs.items():
        if not token.startswith("_"):
            text = text.replace("{{" + token + "}}", value)
    return text


# ---------------------------------------------------------------------------
# Region model  (derived from text at runtime, never hardcoded)
# ---------------------------------------------------------------------------

def _build_regions(text: str) -> dict:
    """Return ordered dict: region_name -> list[str] (lines with newlines)."""
    lines    = text.splitlines(keepends=True)
    h2_idx   = [i for i, ln in enumerate(lines) if ln.startswith("## ")]
    regions  = {}
    preamble_end = h2_idx[0] if h2_idx else len(lines)
    regions["preamble"] = lines[:preamble_end]
    for j, idx in enumerate(h2_idx):
        name = lines[idx][3:].rstrip()          # strip "## " and trailing whitespace
        end  = h2_idx[j + 1] if j + 1 < len(h2_idx) else len(lines)
        regions[name] = lines[idx:end]
    return regions


# ---------------------------------------------------------------------------
# Sanctioned-anchor location
# ---------------------------------------------------------------------------

def _find_roles_region(lines: list, start_pat, label: str):
    """Return (start_idx, end_idx) where end_idx is the first blank of the
    blank-line run that immediately precedes the sentinel line.  Tolerates
    one or more blank lines before the sentinel."""
    start = None
    for i, ln in enumerate(lines):
        if start_pat.match(ln.rstrip()):
            start = i
            break
    if start is None:
        _die(f"Anchor not found: {label}")
    # Find the sentinel line anywhere after start.
    sentinel_idx = None
    for i in range(start + 1, len(lines)):
        if lines[i].startswith(_ROLES_END_SENTINEL):
            sentinel_idx = i
            break
    if sentinel_idx is None:
        _die(f"Anchor not found: roles table end (sentinel '{_ROLES_END_SENTINEL}') — searched after {label}")
    # Walk backward from the sentinel to find the first blank of the preceding run.
    end_idx = sentinel_idx - 1
    while end_idx > start and lines[end_idx].rstrip() == "":
        end_idx -= 1
    # end_idx now points to the last non-blank before the sentinel; advance by 1
    # to get the first blank of the run (i.e. the exclusive end of the roles region).
    end_idx += 1
    return start, end_idx


def _find_oos_row(lines: list, label: str) -> int:
    for i, ln in enumerate(lines):
        if _OOS_ROW_PAT.match(ln):
            return i
    _die(f"Anchor not found: {label}")


def _oos_cell_conforms(line: str, domain: str) -> bool:
    parts = line.split("|")
    cell  = parts[2].strip() if len(parts) >= 3 else ""
    return bool(re.match(r"^Outside " + re.escape(domain) + r"(\s*\(.*\))?$", cell))


def _check_sanctioned(exp_regions: dict, vault_regions: dict, domain: str) -> dict:
    """Locate all sanctioned sub-region anchors. Exit 2 on any failure."""
    if CONVENTIONS_NAME not in exp_regions:
        _die(f"Anchor not found: '## {CONVENTIONS_NAME}' heading in expected/template")

    conv_exp = exp_regions[CONVENTIONS_NAME]
    exp_rs, exp_re = _find_roles_region(conv_exp, _ROLES_START_EXPECTED, "expected roles table start")
    exp_oos        = _find_oos_row(conv_exp, "expected out-of-scope row")

    conv_vault = vault_regions.get(CONVENTIONS_NAME)
    if conv_vault is None:
        _die("Anchor not found: vault roles table start (## Conventions region absent from vault)")

    vlt_rs, vlt_re = _find_roles_region(conv_vault, _ROLES_START_VAULT, "vault roles table start")
    vlt_oos        = _find_oos_row(conv_vault, "vault out-of-scope row")

    oos_ok = _oos_cell_conforms(conv_vault[vlt_oos], domain)

    return dict(
        conv_exp=conv_exp, conv_vault=conv_vault,
        exp_rs=exp_rs, exp_re=exp_re,
        vlt_rs=vlt_rs, vlt_re=vlt_re,
        exp_oos=exp_oos, vlt_oos=vlt_oos,
        oos_ok=oos_ok,
    )


# ---------------------------------------------------------------------------
# Masking  (replaces sanctioned lines with identical placeholders on both sides)
# ---------------------------------------------------------------------------

def _mask(lines: list, rs: int, re_: int, oos: int, oos_ok: bool) -> list:
    """
    Return a copy of lines with sanctioned sub-regions replaced by placeholders.

    Single left-to-right pass over original indices — no shifted arithmetic,
    safe regardless of which sanctioned range comes first in the list.
    """
    ranges = [(rs, re_, _PH_ROLES)]
    if oos_ok:
        ranges.append((oos, oos + 1, _PH_OOS))
    ranges.sort(key=lambda r: r[0])

    out = []
    i = 0
    ri = 0
    while i < len(lines):
        if ri < len(ranges) and i == ranges[ri][0]:
            start, end, ph = ranges[ri]
            out.append(ph)
            i = end
            ri += 1
        else:
            out.append(lines[i])
            i += 1
    return out


# ---------------------------------------------------------------------------
# Region comparison
# ---------------------------------------------------------------------------

def _cmp_regular(name: str, exp: list, vlt) -> tuple:
    if vlt is None:
        hunks = list(difflib.unified_diff(
            exp, [], fromfile=f"expected/{name}", tofile=f"vault/{name} (absent)"
        ))
        return "DIFF", hunks
    hunks = list(difflib.unified_diff(exp, vlt, fromfile=f"expected/{name}", tofile=f"vault/{name}"))
    return ("PASS", []) if not hunks else ("DIFF", hunks)


def _cmp_conventions(s: dict) -> tuple:
    """
    Compare the Conventions region.  All diffs attributable to sanctioned
    sub-regions → EXEMPT-CONTAINED.  Any non-sanctioned diff → DIFF.
    """
    exp = s["conv_exp"]
    vlt = s["conv_vault"]

    m_exp = _mask(exp, s["exp_rs"], s["exp_re"], s["exp_oos"], s["oos_ok"])
    m_vlt = _mask(vlt, s["vlt_rs"], s["vlt_re"], s["vlt_oos"], s["oos_ok"])

    if list(difflib.unified_diff(m_exp, m_vlt)):
        # Non-sanctioned difference — show full unmasked hunks
        hunks = list(difflib.unified_diff(
            exp, vlt,
            fromfile=f"expected/{CONVENTIONS_NAME}",
            tofile=f"vault/{CONVENTIONS_NAME}",
        ))
        return "DIFF", hunks

    # All diffs are sanctioned
    out = []
    out.append("--- EXEMPT: roles table (expected) ---\n")
    out.extend(exp[s["exp_rs"]:s["exp_re"]])
    out.append("--- EXEMPT: roles table (vault) ---\n")
    out.extend(vlt[s["vlt_rs"]:s["vlt_re"]])
    out.append("---\n")
    if s["oos_ok"]:
        out.append("--- EXEMPT: out-of-scope row (vault) ---\n")
        out.append(vlt[s["vlt_oos"]])
        out.append("---\n")
    return "EXEMPT-CONTAINED", out


# ---------------------------------------------------------------------------
# Main comparison loop and output
# ---------------------------------------------------------------------------

def _run(exp_regions: dict, vault_regions: dict, s: dict) -> bool:
    counts   = {"PASS": 0, "DIFF": 0, "EXEMPT-CONTAINED": 0}
    has_diff = False

    for name, exp_lines in exp_regions.items():
        if name == CONVENTIONS_NAME:
            status, extra = _cmp_conventions(s)
        else:
            status, extra = _cmp_regular(name, exp_lines, vault_regions.get(name))

        counts[status] = counts.get(status, 0) + 1
        print(f"REGION {name}: {status}")
        for ln in extra:
            _emit(ln)
        if status == "DIFF":
            has_diff = True

    n_p = counts["PASS"]
    n_d = counts["DIFF"]
    n_e = counts["EXEMPT-CONTAINED"]
    note = "exit 0: no non-sanctioned diffs" if not has_diff else "exit 1: diffs found"
    print(f"\nSummary: {n_p} PASS, {n_d} DIFF, {n_e} EXEMPT-CONTAINED. {note}.")
    return has_diff


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="Template-vs-vault conformance probe.")
    p.add_argument("--vault",    required=True, help="Instantiated CLAUDE.md")
    p.add_argument("--template", required=True, help="CLAUDE.template.md")
    p.add_argument("--subs",     required=True, help="JSON token substitution map")
    a = p.parse_args()

    template_raw = Path(a.template).read_text()
    vault_raw    = Path(a.vault).read_text()
    try:
        subs = json.loads(Path(a.subs).read_text())
    except json.JSONDecodeError as e:
        _die(f"subs file is not valid JSON: {e}")

    body   = _strip_header(template_raw)
    tokens = _discover_tokens(body)
    _validate_subs(subs, tokens)

    expected      = _substitute(body, subs)
    exp_regions   = _build_regions(expected)
    vault_regions = _build_regions(vault_raw)

    s = _check_sanctioned(exp_regions, vault_regions, subs["DOMAIN"])

    has_diff = _run(exp_regions, vault_regions, s)
    sys.exit(1 if has_diff else 0)


if __name__ == "__main__":
    main()
