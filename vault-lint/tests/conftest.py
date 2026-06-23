"""Shared helpers for vault-lint tests.

Characterization/regression suite: every assertion pins the CURRENT observed
behaviour of lint.py. Pure stdlib + pytest only.

The module under test (`lint.py`) lives in a non-package dir with a hyphen-free
name, so it is imported via importlib.util.spec_from_file_location — mirroring
check-conformance/tests/test_check_conformance.py test 8.
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = REPO_ROOT / "vault-lint" / "lint.py"


def load_lint():
    """Import lint.py as a module object without running main()."""
    spec = importlib.util.spec_from_file_location("lint_under_test", str(SCRIPT_PATH))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Single shared import — lint.py is side-effect-free at import time except for
# reading datetime.date.today() into module constants.
lint = load_lint()


# ---------------------------------------------------------------------------
# In-memory page builders (matching load_live_pages return shape)
# ---------------------------------------------------------------------------
#
# load_live_pages returns: relpath -> {'content', 'fm', 'wikilinks'}
# These builders construct equivalent dict entries from raw content so Phase 1
# checks can be exercised without touching disk.

def make_page(content):
    """Build one page-data dict the way load_live_pages would."""
    return {
        "content": content,
        "fm": lint.parse_frontmatter(content),
        "wikilinks": lint.extract_wikilink_targets(content),
    }


def make_pages(mapping):
    """mapping: relpath -> content  ->  pages dict + slug_index."""
    pages = {rp: make_page(c) for rp, c in mapping.items()}
    slug_index = lint.build_slug_index(pages)
    return pages, slug_index


def frontmatter(**fields):
    """Render a minimal YAML frontmatter block from scalar/list fields."""
    lines = ["---"]
    for k, v in fields.items():
        if isinstance(v, list):
            inner = ", ".join(str(x) for x in v)
            lines.append(f"{k}: [{inner}]")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Minimal valid CLAUDE.md (derived from parse_claude_config + the template's
# VAULT-LINT-EXTENSIONS block). This is the smallest input that yields a
# usable config: vault_slug set, a depth_table, canonical roles, and an
# (empty) extension_checks list.
# ---------------------------------------------------------------------------

def minimal_claude_md(vault_slug="test-vault", roles=("alpha", "beta"),
                      extension_checks_block="extension_checks: []"):
    role_rows = "\n".join(
        f"| `{r}` | def {r} | when {r} |" for r in roles
    )
    return f"""# Test Vault Contract

**Roles for this vault:**

| Role | Definition | Assign when… |
|---|---|---|
{role_rows}

The `source_tier:` field is required on every topic page.

<!-- VAULT-LINT-EXTENSIONS-BEGIN -->

vault_slug: {vault_slug}

freshness_model: structural

depth_table:
  "wiki/topics/": "../../"
  "wiki/entities/*/": "../../../"

{extension_checks_block}

<!-- VAULT-LINT-EXTENSIONS-END -->
"""


# ---------------------------------------------------------------------------
# On-disk vault scaffolder for end-to-end (subprocess) tests
# ---------------------------------------------------------------------------

def build_vault(tmp_path, claude_md=None, topic_pages=None, entity_pages=None,
                index_md=None, log_md=""):
    """Create a minimal vault skeleton under tmp_path and return its path.

    topic_pages / entity_pages: dict slug -> content (written under
    wiki/topics/<slug>.md and wiki/entities/<slug>.md respectively).
    """
    vault = tmp_path / "vault"
    (vault / "wiki" / "topics").mkdir(parents=True)
    (vault / "wiki" / "entities").mkdir(parents=True)
    (vault / "wiki" / "digests").mkdir(parents=True)

    if claude_md is None:
        claude_md = minimal_claude_md()
    (vault / "CLAUDE.md").write_text(claude_md, encoding="utf-8")

    if index_md is None:
        index_md = "# Index\n"
    (vault / "wiki" / "index.md").write_text(index_md, encoding="utf-8")
    (vault / "wiki" / "log.md").write_text(log_md, encoding="utf-8")

    for slug, content in (topic_pages or {}).items():
        (vault / "wiki" / "topics" / f"{slug}.md").write_text(content, encoding="utf-8")
    for slug, content in (entity_pages or {}).items():
        (vault / "wiki" / "entities" / f"{slug}.md").write_text(content, encoding="utf-8")

    return vault


def run_lint(vault_path):
    """Invoke lint.py as a subprocess; return CompletedProcess."""
    return subprocess.run(
        [sys.executable, str(SCRIPT_PATH), str(vault_path)],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
    )
