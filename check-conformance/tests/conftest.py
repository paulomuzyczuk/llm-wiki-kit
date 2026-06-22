"""Shared helpers for check-conformance tests."""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_PATH = REPO_ROOT / "CLAUDE.template.md"
SCRIPT_PATH = REPO_ROOT / "check-conformance" / "check-conformance.py"

# Fixed substitution table covering every {{TOKEN}} in the template body.
TEST_SUBS = {
    "DOMAIN": "pair programming",
    "VAULT_PREFIX": "pp",
    "VAULT_SLUG": "pair-programming",
    "EXEC_HANDOFF": "coding-handoff",
    "EXEC_NOUN": "coding",
    "ENTITY_SUBJECT": "projects",
    "ENTITY_SUBJECT-singular": "project",
    "EXTERNAL_WORK_PATH": "~/projects/<name>/",
    "LOG_CLASSIFIER": "subject",
    "SCHEDULE_TIME": "08:00",
}

# Roles table that replaces the template's example block in a conformant vault.
VAULT_ROLES_HEADING = "**Roles for this vault:**"
VAULT_ROLES_TABLE = """\
| Role | Definition | Assign when… |
|---|---|---|
| `code-craftsperson` | Writing or reviewing code | Page is about code-level decisions |
| `system-designer` | Architecture decisions | Page spans components or services |
"""


def _strip_header(text: str) -> str:
    """Remove all leading HTML comment blocks (version comments + instantiation header) and blank lines."""
    while text.startswith("<!--"):
        end = text.index("-->")
        text = text[end + 3:].lstrip("\n")
    return text


def _substitute(text: str, subs: dict) -> str:
    for token, value in subs.items():
        text = text.replace("{{" + token + "}}", value)
    return text


def _swap_roles_table(lines: list) -> list:
    """
    Replace the template example-roles block with the vault-specific block.
    Start anchor: line starting with '**Roles for this vault:**'
    End anchor: blank line immediately before 'The `source_tier:` field is required'
    """
    start_pat = re.compile(r"^\*\*Roles for this vault:\*\*")
    end_sentinel = "The `source_tier:` field is required"

    # Find start
    start_idx = None
    for i, line in enumerate(lines):
        if start_pat.match(line.rstrip()):
            start_idx = i
            break
    if start_idx is None:
        raise ValueError("Roles table start anchor not found in template body")

    # Find end: blank line immediately before end_sentinel paragraph
    end_idx = None
    for i in range(start_idx + 1, len(lines)):
        if lines[i].rstrip() == "" and i + 1 < len(lines) and lines[i + 1].startswith(end_sentinel):
            end_idx = i  # the blank line itself is the boundary (exclusive end)
            break
    if end_idx is None:
        raise ValueError("Roles table end anchor not found in template body")

    replacement = [
        VAULT_ROLES_HEADING + "\n",
        "\n",
        VAULT_ROLES_TABLE,
    ]
    return lines[:start_idx] + replacement + lines[end_idx:]


def make_vault(
    mutations=None,
    out_of_scope_suffix: str | None = None,
) -> str:
    """
    Build a conformant vault string from the real template, then apply mutations.

    mutations: list of callables (lines: list[str]) -> list[str]
    out_of_scope_suffix: if given, appended to the out-of-scope cell, e.g.
        ' (vendor tools, productivity software)'
    """
    raw = TEMPLATE_PATH.read_text()
    body = _strip_header(raw)
    body = _substitute(body, TEST_SUBS)
    lines = body.splitlines(keepends=True)
    lines = _swap_roles_table(lines)

    if out_of_scope_suffix is not None:
        oos_pat = re.compile(r"^(\|\s*`out-of-scope`\s*\|\s*Outside\s+\S.*?)(\s*\|)")
        for i, line in enumerate(lines):
            m = oos_pat.match(line.rstrip("\n"))
            if m:
                lines[i] = m.group(1) + out_of_scope_suffix + " |\n"
                break

    if mutations:
        for mut in mutations:
            lines = mut(lines)

    return "".join(lines)


def run_check(vault_text: str, subs: dict | None = None, tmp_path=None) -> subprocess.CompletedProcess:
    """Write temp files and invoke check-conformance.py; return CompletedProcess."""
    if subs is None:
        subs = TEST_SUBS
    vault_file = tmp_path / "CLAUDE.md"
    subs_file = tmp_path / "subs.json"
    vault_file.write_text(vault_text)
    subs_file.write_text(json.dumps(subs))
    return subprocess.run(
        [sys.executable, str(SCRIPT_PATH),
         "--vault", str(vault_file),
         "--template", str(TEMPLATE_PATH),
         "--subs", str(subs_file)],
        capture_output=True,
        text=True,
    )
