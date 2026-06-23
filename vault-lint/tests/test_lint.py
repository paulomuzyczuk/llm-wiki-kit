"""Characterization tests for vault-lint/lint.py.

Every assertion pins the CURRENT behaviour of lint.py against the current
code. Where behaviour looked surprising it is captured as-is and flagged with
a `# NOTE:` comment for human review rather than "corrected".
"""
import datetime

from conftest import (
    lint,
    make_page,
    make_pages,
    frontmatter,
    minimal_claude_md,
    build_vault,
    run_lint,
)


# ===========================================================================
# 1. PARSER UNIT TESTS
# ===========================================================================

# --- extract_wikilink_targets ----------------------------------------------

def test_wikilink_plain():
    assert lint.extract_wikilink_targets("see [[alpha]] here") == ["alpha"]


def test_wikilink_with_display():
    assert lint.extract_wikilink_targets("[[alpha|Alpha Display]]") == ["alpha"]


def test_wikilink_table_pipe_escape():
    # Obsidian table-pipe escape: [[target\|display]] -> target
    assert lint.extract_wikilink_targets(r"| [[alpha\|Display]] |") == ["alpha"]


def test_wikilink_anchor_stripped():
    assert lint.extract_wikilink_targets("[[alpha#section]]") == ["alpha"]


def test_wikilink_order_and_dups():
    content = "[[a]] [[b]] [[a]]"
    assert lint.extract_wikilink_targets(content) == ["a", "b", "a"]


def test_wikilink_empty_target_skipped():
    # A wikilink whose target is empty (only an anchor) is dropped.
    assert lint.extract_wikilink_targets("[[#anchor-only]]") == []


# --- parse_frontmatter -----------------------------------------------------

def test_frontmatter_scalar():
    fm = lint.parse_frontmatter("---\ntitle: Hello\nstatus: active\n---\nbody")
    assert fm == {"title": "Hello", "status": "active"}


def test_frontmatter_none_without_marker():
    assert lint.parse_frontmatter("no frontmatter here") is None


def test_frontmatter_inline_list():
    fm = lint.parse_frontmatter("---\nroles: [a, b, c]\n---\n")
    assert fm["roles"] == ["a", "b", "c"]


def test_frontmatter_empty_inline_list():
    fm = lint.parse_frontmatter("---\naliases: []\n---\n")
    assert fm["aliases"] == []


def test_frontmatter_block_list():
    content = "---\nroles:\n  - alpha\n  - beta\n---\n"
    fm = lint.parse_frontmatter(content)
    assert fm["roles"] == ["alpha", "beta"]


def test_frontmatter_quoted_inline_list():
    fm = lint.parse_frontmatter('---\naliases: ["a, b", c]\n---\n')
    # Quoted comma kept inside the first element.
    assert fm["aliases"] == ["a, b", "c"]


def test_frontmatter_strips_inline_comment():
    fm = lint.parse_frontmatter("---\ntitle: Hi # trailing comment\n---\n")
    assert fm["title"] == "Hi"


# --- _parse_inline_list ----------------------------------------------------

def test_parse_inline_list_basic():
    assert lint._parse_inline_list("a, b, c") == ["a", "b", "c"]


def test_parse_inline_list_quoted():
    assert lint._parse_inline_list('"a b", c') == ["a b", "c"]


# --- parse_claude_config ---------------------------------------------------

def test_parse_claude_config_minimal():
    cfg = lint.parse_claude_config(minimal_claude_md())
    assert cfg["vault_slug"] == "test-vault"
    assert cfg["canonical_roles"] == ["alpha", "beta"]
    assert cfg["depth_table"] == {
        "wiki/topics/": "../../",
        "wiki/entities/*/": "../../../",
    }
    assert cfg["extension_checks"] == []
    assert cfg["freshness_model"] == "structural"


def test_parse_claude_config_extension_checks():
    block = (
        "extension_checks:\n"
        "  - id: book-entity-backlink\n"
        "    description: backlink check\n"
        "  - id: english-first-naming\n"
        "    description: naming check\n"
        "    allowlist: foo,bar\n"
    )
    cfg = lint.parse_claude_config(minimal_claude_md(extension_checks_block=block))
    ids = [c["id"] for c in cfg["extension_checks"]]
    assert ids == ["book-entity-backlink", "english-first-naming"]
    assert cfg["extension_checks"][1]["allowlist"] == "foo,bar"


def test_parse_claude_config_no_vault_slug():
    # Block present but vault_slug omitted -> None.
    md = minimal_claude_md().replace("vault_slug: test-vault\n", "")
    cfg = lint.parse_claude_config(md)
    assert cfg["vault_slug"] is None


# --- watermark + activity counting -----------------------------------------

def _log(*entries):
    return "\n".join(entries) + "\n"


def test_find_watermark_latest():
    log = _log(
        "## [2024-01-01] lint | myvault | foo",
        "## [2024-06-01] lint | myvault | bar",
        "## [2024-03-01] lint | other | baz",
    )
    assert lint.find_watermark(log, "myvault") == datetime.date(2024, 6, 1)


def test_find_watermark_none():
    assert lint.find_watermark("no entries", "myvault") is None


def test_count_activity_since():
    log = _log(
        "## [2024-01-01] lint | myvault | prior",
        "## [2024-01-02] ingest | article | something",
        "## [2024-01-03] ingest | some-book | chapter",
        "## [2024-01-04] digest | foo | ingest complete",
        "## [2024-01-05] coding-handoff | proj | did stuff",
    )
    counts = lint.count_activity_since(log, "myvault", datetime.date(2024, 1, 1))
    assert counts["articles"] == 1
    assert counts["other_ingests"] == 1
    assert counts["books"] == 1
    assert counts["handoffs"] == 1
    assert counts["handoff_types"].get("coding-handoff") == 1


def test_count_activity_none_watermark():
    counts = lint.count_activity_since("anything", "v", None)
    assert counts == {"books": 0, "articles": 0, "other_ingests": 0,
                      "handoffs": 0, "handoff_types": {}}


# --- get_slug / build_slug_index -------------------------------------------

def test_get_slug():
    assert lint.get_slug("wiki/topics/alpha.md") == "alpha"


def test_build_slug_index_collision():
    pages = {"wiki/topics/a.md": {}, "wiki/entities/a.md": {}}
    idx = lint.build_slug_index(pages)
    assert sorted(idx["a"]) == ["wiki/entities/a.md", "wiki/topics/a.md"]


# --- _match_depth_table ----------------------------------------------------

def test_match_depth_table():
    dt = {"wiki/topics/": "../../", "wiki/entities/*/": "../../../"}
    assert lint._match_depth_table("wiki/topics", dt) == "../../"
    assert lint._match_depth_table("wiki/entities/books", dt) == "../../../"


# --- _diagnose_citation ----------------------------------------------------

def test_diagnose_citation_spaces():
    assert "spaces" in lint._diagnose_citation("../raw-input/a b.pdf")


def test_diagnose_citation_no_prefix():
    assert "missing relative prefix" in lint._diagnose_citation("raw-input/a.pdf")


# ===========================================================================
# 2. PHASE 1 CHECKS
# ===========================================================================

# --- check_1_citations -----------------------------------------------------

def test_check_1_clean(tmp_path):
    # Create a real vault with a topic page citing an existing raw-input file.
    vault = build_vault(
        tmp_path,
        topic_pages={
            "a": "# A\n\nClaim ([Author 2020](../../raw-input/books/x/x.pdf#page=1), p. 1)\n",
        },
    )
    (vault / "raw-input" / "books" / "x").mkdir(parents=True)
    (vault / "raw-input" / "books" / "x" / "x.pdf").write_text("pdf")
    pages = lint.load_live_pages(str(vault))
    res = lint.check_1_citations(str(vault), pages, {})
    assert res["total"] == 1
    assert res["resolving"] == 1
    assert res["findings"] == []


def test_check_1_unresolved(tmp_path):
    vault = build_vault(
        tmp_path,
        topic_pages={
            "a": "# A\n\nClaim ([Author 2020](../../raw-input/books/x/missing.pdf), p. 1)\n",
        },
    )
    pages = lint.load_live_pages(str(vault))
    res = lint.check_1_citations(str(vault), pages, {})
    assert res["total"] == 1
    assert res["resolving"] == 0
    assert len(res["findings"]) == 1
    assert res["findings"][0]["type"] == "not-found"


# --- check_2_orphans -------------------------------------------------------

def test_check_2_no_orphan():
    pages, slug_index = make_pages({
        "wiki/topics/a.md": "# A\nlinks to [[b]]\n",
        "wiki/topics/b.md": "# B\nlinks to [[a]]\n",
    })
    res = lint.check_2_orphans("/nonexistent", pages, slug_index)
    assert res["orphans"] == []


def test_check_2_orphan_found():
    pages, slug_index = make_pages({
        "wiki/topics/a.md": "# A\nlinks to [[b]]\n",
        "wiki/topics/b.md": "# B\nno inbound\n",
        "wiki/topics/c.md": "# C\norphan with no inbound\n",
    })
    res = lint.check_2_orphans("/nonexistent", pages, slug_index)
    # a is orphan (nothing links to it), c is orphan. b is linked by a.
    assert "wiki/topics/a.md" in res["orphans"]
    assert "wiki/topics/c.md" in res["orphans"]
    assert "wiki/topics/b.md" not in res["orphans"]


# --- check_3_pass_a (dangling wikilinks) -----------------------------------

def test_check_3a_clean():
    pages, slug_index = make_pages({
        "wiki/topics/a.md": "# A\n[[b]]\n",
        "wiki/topics/b.md": "# B\n",
    })
    res = lint.check_3_pass_a(pages, slug_index)
    assert res["dangling"] == {}


def test_check_3a_dangling():
    pages, slug_index = make_pages({
        "wiki/topics/a.md": "# A\n[[ghost]]\n",
    })
    res = lint.check_3_pass_a(pages, slug_index)
    assert "ghost" in res["dangling"]
    assert res["dangling"]["ghost"] == ["wiki/topics/a.md"]


# --- check_3_pass_b (recurrent bold terms) ---------------------------------

def test_check_3b_clean():
    pages, slug_index = make_pages({
        "wiki/topics/a.md": "# A\nNothing bold here.\n",
    })
    res = lint.check_3_pass_b(pages, slug_index)
    assert res["candidates"] == {}


def test_check_3b_candidate():
    # A bold term appearing on >=3 pages, not a stoplist word, not canonical.
    term = "**Widget Framework**"
    pages, slug_index = make_pages({
        "wiki/topics/a.md": f"# A\n{term} matters.\n",
        "wiki/topics/b.md": f"# B\n{term} matters.\n",
        "wiki/topics/c.md": f"# C\n{term} matters.\n",
    })
    res = lint.check_3_pass_b(pages, slug_index)
    assert "Widget Framework" in res["candidates"]
    assert len(res["candidates"]["Widget Framework"]) == 3


# --- check_4_cross_refs ----------------------------------------------------

def test_check_4_clean(tmp_path):
    # Two topic pages that DO link each other -> no actionable pair.
    vault = build_vault(
        tmp_path,
        topic_pages={
            "a": "# A\n[[b]] [[x]] [[y]] [[z]]\n",
            "b": "# B\n[[a]] [[x]] [[y]] [[z]]\n",
        },
    )
    pages = lint.load_live_pages(str(vault))
    res = lint.check_4_cross_refs(str(vault), pages)
    assert res["actionable"] == []


def test_check_4_actionable(tmp_path):
    # Two pages sharing >=3 concepts, neither links the other.
    vault = build_vault(
        tmp_path,
        topic_pages={
            "a": "# A\n[[x]] [[y]] [[z]]\n",
            "b": "# B\n[[x]] [[y]] [[z]]\n",
        },
    )
    pages = lint.load_live_pages(str(vault))
    res = lint.check_4_cross_refs(str(vault), pages)
    assert len(res["actionable"]) == 1
    a, b, n, shared = res["actionable"][0]
    assert n == 3
    assert shared == ["x", "y", "z"]


# --- check_5_duplicates ----------------------------------------------------

def test_check_5_clean():
    pages, _ = make_pages({
        "wiki/topics/a.md": frontmatter(title="Alpha"),
        "wiki/topics/b.md": frontmatter(title="Beta"),
    })
    res = lint.check_5_duplicates(pages)
    assert res["pairs"] == []


def test_check_5_title_collision():
    pages, _ = make_pages({
        "wiki/topics/a.md": frontmatter(title="Same Title"),
        "wiki/entities/b.md": frontmatter(title="Same Title"),
    })
    res = lint.check_5_duplicates(pages)
    assert len(res["pairs"]) == 1
    a, b, shared, otype = res["pairs"][0]
    assert shared == ["same title"]
    assert otype == "title-vs-title"


def test_check_5_alias_collision():
    pages, _ = make_pages({
        "wiki/topics/a.md": frontmatter(title="Alpha", aliases=["shared-alias"]),
        "wiki/topics/b.md": frontmatter(title="Beta", aliases=["shared-alias"]),
    })
    res = lint.check_5_duplicates(pages)
    assert len(res["pairs"]) == 1
    _, _, shared, otype = res["pairs"][0]
    assert shared == ["shared-alias"]
    assert otype == "alias-vs-alias"


# --- check_6_stale_claims --------------------------------------------------

def test_check_6_clean():
    fresh = datetime.date.today().isoformat()
    pages, _ = make_pages({
        "wiki/topics/a.md": frontmatter(title="A", status="active",
                                        last_updated=fresh),
    })
    res = lint.check_6_stale_claims(pages)
    assert res["stale_active"] == []
    assert res["opposing_candidates"] == []


def test_check_6_stale_active():
    pages, _ = make_pages({
        "wiki/topics/a.md": frontmatter(title="A", status="active",
                                        last_updated="2000-01-01"),
    })
    res = lint.check_6_stale_claims(pages)
    assert len(res["stale_active"]) == 1
    assert res["stale_active"][0]["page"] == "wiki/topics/a.md"


def test_check_6_contradicts_marker():
    content = frontmatter(title="A") + "\nCONTRADICTS: prior claim about X\n"
    pages, _ = make_pages({"wiki/topics/a.md": content})
    res = lint.check_6_stale_claims(pages)
    assert len(res["opposing_candidates"]) == 1
    assert res["opposing_candidates"][0]["page"] == "wiki/topics/a.md"


# --- check_7_data_gaps -----------------------------------------------------

def test_check_7_clean():
    pages, _ = make_pages({
        "wiki/topics/a.md": frontmatter(title="A", status="active") + "\nClean body.\n",
    })
    res = lint.check_7_data_gaps(pages)
    assert res["stubs"] == []
    assert res["todos"] == []
    assert res["open_questions"] == []


def test_check_7_stub():
    pages, _ = make_pages({
        "wiki/topics/a.md": frontmatter(title="A", status="stub") + "\nbody\n",
    })
    res = lint.check_7_data_gaps(pages)
    assert res["stubs"] == ["wiki/topics/a.md"]


def test_check_7_todo():
    pages, _ = make_pages({
        "wiki/topics/a.md": frontmatter(title="A") + "\nTODO: fill this in\n",
    })
    res = lint.check_7_data_gaps(pages)
    assert len(res["todos"]) == 1
    assert res["todos"][0]["marker"] == "TODO:"


def test_check_7_open_question():
    pages, _ = make_pages({
        "wiki/topics/a.md": frontmatter(title="A") + "\nUnknown value [?] here\n",
    })
    res = lint.check_7_data_gaps(pages)
    assert len(res["open_questions"]) == 1


# ===========================================================================
# 3. PHASE 2 — ROLE-COUNT DRIFT
# ===========================================================================

def test_parse_index_role_counts_list():
    canonical = ["alpha", "beta"]
    index = (
        "# Index\n\n"
        "## Role Maps of Content\n\n"
        "- [Role — Alpha](topics/role-alpha.md) — 5 pages; desc\n"
        "- [Role — Beta](topics/role-beta.md) — 2 pages; desc\n"
    )
    reported, fmt, lines = lint._parse_index_role_counts(index, canonical)
    assert fmt == "list"
    assert reported == {"alpha": 5, "beta": 2}


def test_parse_index_role_counts_unknown():
    canonical = ["alpha"]
    reported, fmt, lines = lint._parse_index_role_counts("# Index\nno role surface\n", canonical)
    assert fmt == "unknown"
    assert reported == {"alpha": 0}


def test_phase_2_role_drift_skipped(tmp_path):
    # index.md with no role-counts surface -> skipped=True.
    vault = build_vault(
        tmp_path,
        topic_pages={"a": frontmatter(title="A", roles=["alpha"])},
        index_md="# Index\nno role surface\n",
    )
    res = lint.phase_2_role_drift(str(vault), ["alpha", "beta"], "# Index\nno role surface\n")
    assert res["skipped"] is True
    assert res["delta"] == {}


def test_phase_2_role_drift_with_drift(tmp_path):
    # One topic page with role alpha; index reports alpha=5 -> delta alpha=-4.
    vault = build_vault(
        tmp_path,
        topic_pages={"a": frontmatter(title="A", roles=["alpha"])},
    )
    index = (
        "## Role Maps of Content\n\n"
        "- [Role — Alpha](topics/role-alpha.md) — 5 pages; desc\n"
        "- [Role — Beta](topics/role-beta.md) — 0 pages; desc\n"
    )
    res = lint.phase_2_role_drift(str(vault), ["alpha", "beta"], index)
    assert res["skipped"] is False
    assert res["actual"]["alpha"] == 1
    assert res["reported"]["alpha"] == 5
    assert res["delta"]["alpha"] == -4
    assert res["delta"]["beta"] == 0


def test_parse_frontmatter_roles_inline():
    assert lint._parse_frontmatter_roles("---\nroles: [a, b]\n---\n") == ["a", "b"]


def test_parse_frontmatter_roles_absent():
    assert lint._parse_frontmatter_roles("---\ntitle: X\n---\n") is None


# ===========================================================================
# 4. PHASE 2.5 — REGRESSION GUARD
# ===========================================================================

def _zero_activity():
    return {"books": 0, "articles": 0, "other_ingests": 0, "handoffs": 0,
            "handoff_types": {}}


def test_phase_2_5_consistent_no_fatal():
    # Zero delta -> no FATAL even with watermark + zero activity.
    p2 = {"skipped": False, "delta": {"alpha": 0, "beta": 0},
          "reported": {}, "actual": {}}
    fatal = lint.phase_2_5_guard(_zero_activity(), p2, datetime.date(2024, 1, 1))
    assert not fatal


def test_phase_2_5_no_watermark_no_fatal():
    p2 = {"skipped": False, "delta": {"alpha": 5}, "reported": {}, "actual": {}}
    assert lint.phase_2_5_guard(_zero_activity(), p2, None) is None


def test_phase_2_5_activity_suppresses_fatal():
    p2 = {"skipped": False, "delta": {"alpha": 5}, "reported": {}, "actual": {}}
    activity = _zero_activity()
    activity["books"] = 1
    assert lint.phase_2_5_guard(activity, p2, datetime.date(2024, 1, 1)) is None


def test_phase_2_5_fatal_fires():
    # Watermark + zero activity + non-zero delta + not skipped -> FATAL.
    p2 = {"skipped": False, "delta": {"alpha": 3},
          "reported": {"alpha": 0}, "actual": {"alpha": 3}}
    fatal = lint.phase_2_5_guard(_zero_activity(), p2, datetime.date(2024, 1, 1))
    assert fatal
    assert fatal["delta"] == {"alpha": 3}
    assert fatal["watermark_date"] == "2024-01-01"


def test_phase_2_5_skipped_no_fatal():
    p2 = {"skipped": True, "delta": {}, "reported": {}, "actual": {}}
    assert lint.phase_2_5_guard(_zero_activity(), p2, datetime.date(2024, 1, 1)) is None


# ===========================================================================
# 5. END-TO-END (subprocess)
# ===========================================================================

def test_e2e_missing_vault_dir_exit_2(tmp_path):
    missing = tmp_path / "does-not-exist"
    result = run_lint(missing)
    assert result.returncode == 2, result.stdout + result.stderr
    assert "does not exist" in result.stderr


def test_e2e_missing_claude_md_exit_2(tmp_path):
    vault = tmp_path / "vault"
    (vault / "wiki").mkdir(parents=True)
    result = run_lint(vault)
    assert result.returncode == 2, result.stdout + result.stderr
    assert "CLAUDE.md not found" in result.stderr


def test_e2e_no_vault_slug_exit_2(tmp_path):
    # CLAUDE.md present but VAULT-LINT-EXTENSIONS lacks vault_slug.
    md = minimal_claude_md().replace("vault_slug: test-vault\n", "")
    vault = build_vault(tmp_path, claude_md=md)
    result = run_lint(vault)
    assert result.returncode == 2, result.stdout + result.stderr
    assert "vault_slug not found" in result.stderr


def test_e2e_minimal_valid_vault_exit_0(tmp_path):
    vault = build_vault(
        tmp_path,
        topic_pages={
            "a": frontmatter(title="Alpha", roles=["alpha"]) + "\n# Alpha\n[[beta]]\n",
            "beta": frontmatter(title="Beta", roles=["beta"]) + "\n# Beta\n[[a]]\n",
        },
    )
    result = run_lint(vault)
    assert result.returncode == 0, result.stdout + result.stderr

    # A digest report was written.
    today = datetime.date.today().isoformat()
    report = vault / "wiki" / "digests" / f"lint-{today}.md"
    assert report.is_file(), "lint digest report should be written"
    report_text = report.read_text()
    assert "Vault Lint" in report_text

    # A log entry was appended.
    log_text = (vault / "wiki" / "log.md").read_text()
    assert f"[{today}] lint | test-vault |" in log_text
