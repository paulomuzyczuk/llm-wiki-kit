#!/usr/bin/env python3
"""
lint.py — Karpathy-style LLM Wiki vault health-check.

Usage: python3 lint.py <vault-path>

Implements every phase of the vault-lint spec (SKILL.md):
  Phase 1:   7 universal checks
  Phase 1.5: activity since last lint
  Phase 2:   role-count drift (topic pages only, canonical reference impl)
  Phase 2.5: regression guard
  Phase 3:   vault-specific extension checks

Writes:  <vault>/wiki/digests/lint-YYYY-MM-DD.md
Appends: <vault>/wiki/log.md
Exit 0:  lint completed (with or without findings)
Exit 1:  Phase 2.5 FATAL fired
Exit 2:  vault structure invalid or script crash
"""

import datetime
import difflib
import fnmatch
import glob
import math
import os
import re
import sys
import urllib.parse

TODAY = datetime.date.today()
TODAY_STR = TODAY.isoformat()


# ══════════════════════════════════════════════════════════════════════════════
# §1  CANONICAL WIKILINK PARSER — verbatim from SKILL.md; do not modify
# ══════════════════════════════════════════════════════════════════════════════


def extract_wikilink_targets(content):
    """
    Extract wikilink targets from markdown content, correctly handling
    Obsidian's table-pipe escape syntax.

    Wikilinks: [[target]] or [[target|display]] or [[target\\|display]]
    (the third form embeds a piped wikilink inside a markdown table cell).

    Returns a list of target slugs in source order, with anchor fragments
    (#section) stripped. May contain duplicates.
    """
    results = []
    for match in re.finditer(r'\[\[([^\]]+)\]\]', content):
        inner = match.group(1)
        # \\| OR | are both target/display separators; take before first.
        target = re.split(r'\\\||\|', inner, maxsplit=1)[0]
        target = target.split('#', 1)[0].strip()
        if target:
            results.append(target)
    return results


# ══════════════════════════════════════════════════════════════════════════════
# §2  FRONTMATTER PARSER — regex-based, no PyYAML
# ══════════════════════════════════════════════════════════════════════════════


def parse_frontmatter(content):
    """
    Parse YAML frontmatter from a markdown file.
    Handles: scalars, inline lists [a, b, c], block lists (- item).
    Returns dict or None. Defensive — logs warnings, never raises.
    """
    if not content.startswith('---'):
        return None
    try:
        end_idx = content.index('\n---', 3)
    except ValueError:
        return None
    fm_text = content[3:end_idx]

    result = {}
    lines = fm_text.split('\n')
    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped or stripped.startswith('#'):
            i += 1
            continue

        m = re.match(r'^([\w][\w\-]*)\s*:\s*(.*)', raw)
        if not m:
            i += 1
            continue

        key = m.group(1)
        val = m.group(2).strip()
        # Strip trailing inline YAML comment (# preceded by space)
        val = re.sub(r'\s+#\s.*$', '', val).strip()

        if val.startswith('[') and val.endswith(']'):
            inner = val[1:-1].strip()
            result[key] = _parse_inline_list(inner) if inner else []
        elif val == '':
            # Block value — look ahead for indented list items
            items = []
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if nxt.strip() == '':
                    j += 1
                    continue
                li_m = re.match(r'^[ \t]+-\s+(.*)', nxt)
                if li_m:
                    items.append(li_m.group(1).strip().strip('"\''))
                    j += 1
                elif re.match(r'^[\w][\w\-]*\s*:', nxt):
                    break
                else:
                    j += 1
            result[key] = items
            i = j
            continue
        else:
            result[key] = val.strip('"\'')

        i += 1

    return result


def _parse_inline_list(inner):
    """Parse 'a, b, c' or '"a b", c' into a list of stripped strings."""
    items = []
    current = []
    in_q = False
    q_char = None
    for ch in inner:
        if in_q:
            if ch == q_char:
                in_q = False
            else:
                current.append(ch)
        elif ch in ('"', "'"):
            in_q = True
            q_char = ch
        elif ch == ',':
            v = ''.join(current).strip()
            if v:
                items.append(v)
            current = []
        else:
            current.append(ch)
    v = ''.join(current).strip()
    if v:
        items.append(v)
    return items


# ══════════════════════════════════════════════════════════════════════════════
# §3  CLAUDE.MD CONFIG PARSER
# ══════════════════════════════════════════════════════════════════════════════


def parse_claude_config(claude_md_text):
    """
    Parse CLAUDE.md for vault-lint configuration.
    Returns dict: vault_slug, freshness_model, depth_table, projects,
                  extension_checks, canonical_roles.
    """
    config = {
        'vault_slug': None,
        'freshness_model': 'structural',
        'depth_table': {},
        'projects': [],
        'extension_checks': [],
        'canonical_roles': [],
    }

    # VAULT-LINT-EXTENSIONS block
    ext_m = re.search(
        r'<!--\s*VAULT-LINT-EXTENSIONS-BEGIN\s*-->(.*?)<!--\s*VAULT-LINT-EXTENSIONS-END\s*-->',
        claude_md_text,
        re.DOTALL,
    )
    if ext_m:
        _parse_extensions_block(ext_m.group(1), config)

    # Canonical roles under "**Roles for this vault:**"
    roles_m = re.search(
        r'\*\*Roles for this vault:\*\*\s*\n(.*?)(?=\n(?:##|\*\*[A-Z]|---)|\Z)',
        claude_md_text,
        re.DOTALL,
    )
    if roles_m:
        table_text = roles_m.group(1)
        for row_m in re.finditer(r'^\|\s*`([\w\-]+)`', table_text, re.MULTILINE):
            role = row_m.group(1)
            if role and role not in config['canonical_roles']:
                config['canonical_roles'].append(role)

    return config


def _parse_extensions_block(text, config):
    """Line-by-line parser for the VAULT-LINT-EXTENSIONS YAML-like block."""
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            i += 1
            continue

        m = re.match(r'^(\w[\w_]*)\s*:\s*(.*)', line)
        if not m:
            i += 1
            continue

        key = m.group(1)
        val = m.group(2).strip().split('#')[0].strip()

        if key == 'vault_slug':
            config['vault_slug'] = val or None
            i += 1

        elif key == 'freshness_model':
            config['freshness_model'] = val or 'structural'
            i += 1

        elif key == 'depth_table':
            i += 1
            while i < len(lines):
                dl = lines[i]
                if dl and not dl[0].isspace():
                    break
                kv = re.match(r'\s+"([^"]+)"\s*:\s*"([^"]*)"', dl)
                if kv:
                    config['depth_table'][kv.group(1)] = kv.group(2)
                i += 1

        elif key == 'projects':
            i += 1
            while i < len(lines):
                pl = lines[i]
                if pl and not pl[0].isspace():
                    break
                pm = re.match(r'\s+-\s+(\S+)', pl)
                if pm:
                    config['projects'].append(pm.group(1).strip())
                i += 1

        elif key == 'extension_checks':
            current_check = None
            i += 1
            while i < len(lines):
                el = lines[i]
                if not el.strip():
                    i += 1
                    continue
                # New check item: "  - id: <value>"
                item_m = re.match(r'^[ \t]+-\s+id:\s+(\S+)', el)
                if item_m:
                    if current_check and current_check.get('id'):
                        config['extension_checks'].append(current_check)
                    current_check = {'id': item_m.group(1)}
                    i += 1
                    continue
                # Sub-key of current check (indented ≥2 spaces, not starting with -)
                sub_m = re.match(r'^[ \t]{2,}(\w+):\s*(.*)', el)
                if sub_m and current_check is not None:
                    k, v = sub_m.group(1), sub_m.group(2).strip()
                    if v.lower() == 'true':
                        v = True
                    elif v.lower() == 'false':
                        v = False
                    current_check[k] = v
                    i += 1
                    continue
                # Non-indented line — end of extension_checks block
                if el and not el[0].isspace():
                    break
                i += 1
            if current_check and current_check.get('id'):
                config['extension_checks'].append(current_check)

        else:
            i += 1


# ══════════════════════════════════════════════════════════════════════════════
# §4  LIVE PAGE LOADER
# ══════════════════════════════════════════════════════════════════════════════


def load_live_pages(vault_path):
    """
    Load all live wiki pages (topics + entities, excluding digests/handoffs/log).
    Returns dict: relpath -> {'content': str, 'fm': dict|None, 'wikilinks': [str]}
    """
    pages = {}
    for pattern in ['wiki/topics/**/*.md', 'wiki/entities/**/*.md']:
        for fpath in sorted(glob.glob(os.path.join(vault_path, pattern), recursive=True)):
            relpath = os.path.relpath(fpath, vault_path).replace('\\', '/')
            try:
                with open(fpath, encoding='utf-8') as f:
                    content = f.read()
                pages[relpath] = {
                    'content': content,
                    'fm': parse_frontmatter(content),
                    'wikilinks': extract_wikilink_targets(content),
                }
            except Exception as e:
                print(f'WARNING: could not read {relpath}: {e}', file=sys.stderr)
    return pages


def get_slug(relpath):
    return os.path.splitext(os.path.basename(relpath))[0]


def build_slug_index(pages):
    """slug -> [relpath, ...] for all live pages."""
    index = {}
    for relpath in pages:
        slug = get_slug(relpath)
        index.setdefault(slug, []).append(relpath)
    return index


# ══════════════════════════════════════════════════════════════════════════════
# §5  LOG.MD UTILITIES
# ══════════════════════════════════════════════════════════════════════════════


def find_watermark(log_text, vault_slug):
    """
    Find the latest lint watermark: ## [YYYY-MM-DD] lint | <vault-slug> |
    Returns datetime.date or None. Uses max date, not file position.
    """
    pattern = re.compile(
        r'^##\s+\[(\d{4}-\d{2}-\d{2})\]\s+lint\s+\|\s+' + re.escape(vault_slug) + r'\s+\|',
        re.MULTILINE,
    )
    best = None
    for m in pattern.finditer(log_text):
        try:
            d = datetime.date.fromisoformat(m.group(1))
            if best is None or d > best:
                best = d
        except ValueError:
            pass
    return best


def _watermark_char_pos(log_text, vault_slug, watermark_date):
    """Character position of the (last) watermark line for the given date."""
    if watermark_date is None:
        return -1
    pattern = re.compile(
        r'^##\s+\['
        + re.escape(watermark_date.isoformat())
        + r'\]\s+lint\s+\|\s+'
        + re.escape(vault_slug)
        + r'\s+\|',
        re.MULTILINE,
    )
    last_pos = -1
    for m in pattern.finditer(log_text):
        last_pos = m.start()
    return last_pos


def count_activity_since(log_text, vault_slug, watermark_date):
    """
    Count vault operations logged AFTER the watermark line (by file position).
    Returns dict: books, articles, other_ingests, handoffs, handoff_types.
    """
    counts = {'books': 0, 'articles': 0, 'other_ingests': 0, 'handoffs': 0, 'handoff_types': {}}

    if watermark_date is None:
        return counts

    wm_pos = _watermark_char_pos(log_text, vault_slug, watermark_date)
    if wm_pos < 0:
        return counts

    # Skip past the watermark line itself
    after_start = log_text.find('\n', wm_pos)
    if after_start < 0:
        return counts
    after_text = log_text[after_start + 1 :]

    entry_pat = re.compile(r'^##\s+\[\d{4}-\d{2}-\d{2}\]\s+([\w\-]+)\s+\|\s+(.*)', re.MULTILINE)
    for m in entry_pat.finditer(after_text):
        operation = m.group(1).strip()
        rest = m.group(2).strip()
        parts = [p.strip() for p in rest.split('|')]

        if operation == 'ingest':
            topic = parts[0] if parts else ''
            if topic == 'article':
                counts['articles'] += 1
            else:
                counts['other_ingests'] += 1

        elif operation == 'digest':
            topic = parts[0] if parts else ''
            summary = parts[1] if len(parts) > 1 else ''
            if 'ingest complete' in topic or 'ingest complete' in summary:
                counts['books'] += 1

        elif operation == 'distil':
            counts['handoffs'] += 1
            counts['handoff_types']['planning'] = counts['handoff_types'].get('planning', 0) + 1

        elif 'handoff' in operation:
            counts['handoffs'] += 1
            counts['handoff_types'][operation] = counts['handoff_types'].get(operation, 0) + 1

    return counts


# ══════════════════════════════════════════════════════════════════════════════
# §6  CHECK 1 — CITATION RESOLUTION
# ══════════════════════════════════════════════════════════════════════════════


def check_1_citations(vault_path, pages, depth_table):
    """
    Resolve every raw-input citation in live pages.
    Tests file existence; if depth_table present, also validates prefix.
    """
    findings = []
    total = 0
    resolving = 0

    for relpath, data in pages.items():
        file_dir = os.path.dirname(os.path.join(vault_path, relpath))
        page_dir = os.path.dirname(relpath)  # e.g. "wiki/topics"

        for m in re.finditer(r'\]\(([^)]+)\)', data['content']):
            href = m.group(1).split('#')[0].strip()
            if 'raw-input' not in href:
                continue
            total += 1

            abs_target = os.path.normpath(os.path.join(file_dir, urllib.parse.unquote(href)))
            exists = os.path.isfile(abs_target)

            if not exists:
                findings.append(
                    {
                        'type': 'not-found',
                        'file': relpath,
                        'cited': href,
                        'defect': _diagnose_citation(href),
                    }
                )
                continue

            resolving += 1

            # Depth-table prefix validation (only when table is declared)
            if depth_table:
                expected = _match_depth_table(page_dir, depth_table)
                if expected and not href.startswith(expected):
                    findings.append(
                        {
                            'type': 'wrong-prefix',
                            'file': relpath,
                            'cited': href,
                            'expected_prefix': expected,
                            'actual_prefix': _extract_rel_prefix(href),
                        }
                    )

    return {
        'total': total,
        'resolving': resolving,
        'findings': findings,
        'depth_validated': bool(depth_table),
    }


def _match_depth_table(page_dir, depth_table):
    """Return expected prefix for page_dir by matching against depth_table keys."""
    # Normalise to trailing-slash form for fnmatch
    dir_slash = page_dir.rstrip('/') + '/'
    for pattern, prefix in depth_table.items():
        if fnmatch.fnmatch(dir_slash, pattern):
            return prefix
    return None


def _extract_rel_prefix(href):
    m = re.match(r'^((?:\.\./)+)', href)
    return m.group(1) if m else ''


def _diagnose_citation(href):
    if '%20' in href or ' ' in href:
        return 'encoded/embedded spaces in filename'
    if not href.startswith('..'):
        return 'missing relative prefix (no leading ../)'
    return 'file not found on disk — check path slug and prefix depth'


# ══════════════════════════════════════════════════════════════════════════════
# §7  CHECK 2 — ORPHAN PAGES
# ══════════════════════════════════════════════════════════════════════════════


def check_2_orphans(vault_path, pages, slug_index):
    """Find live pages with no inbound wikilinks or path references."""
    inbound = {rp: set() for rp in pages}

    for src, data in pages.items():
        # Wikilink inbound
        for target_slug in data['wikilinks']:
            for tgt in slug_index.get(target_slug, []):
                if tgt != src:
                    inbound[tgt].add(src)

        # Path reference inbound — ](path.md)
        src_abs_dir = os.path.dirname(os.path.join(vault_path, src))
        for m in re.finditer(r'\]\(([^)#\s]+\.md)', data['content']):
            href = m.group(1).strip()
            abs_tgt = os.path.normpath(os.path.join(src_abs_dir, href))
            tgt_rel = os.path.relpath(abs_tgt, vault_path).replace('\\', '/')
            if tgt_rel in inbound and tgt_rel != src:
                inbound[tgt_rel].add(src)

    # Archived pages (status: archived) are intentional tombstones — e.g. merge
    # redirects whose inbound links were deliberately retargeted elsewhere. They
    # are expected to have no inbound links and must not be reported as orphans.
    #
    # Role MOCs (wiki/topics/role-<name>.md) are navigation entry points reached
    # from the index's role surface, not content pages that need discovery via
    # inbound wikilinks. The orphan scan deliberately does not treat index.md as a
    # source, so a role MOC linked only from the index would always false-positive.
    # Exclude them — they are top-level browse surfaces, like index.md itself.
    orphans = sorted(
        p
        for p, srcs in inbound.items()
        if not srcs
        and (pages[p].get('fm') or {}).get('status') != 'archived'
        and not _is_role_moc(p)
    )
    return {'orphans': orphans, 'total': len(pages)}


# ══════════════════════════════════════════════════════════════════════════════
# §8  CHECK 3 — CONCEPTS LACKING A PAGE
# ══════════════════════════════════════════════════════════════════════════════


def check_3_pass_a(vault_path, pages, slug_index):
    """Pass A: dangling wikilinks — targets with no live page.

    Digest artifacts (wiki/digests/*.md — ingest reports, review/lint digests) are
    legitimate wikilink targets even though they are not loaded as live pages, so a
    link resolving to a digest filename is not dangling.
    """
    digest_slugs = set()
    for fpath in glob.glob(os.path.join(vault_path, 'wiki/digests/**/*.md'), recursive=True):
        digest_slugs.add(os.path.splitext(os.path.basename(fpath))[0])
    dangling = {}
    for relpath, data in pages.items():
        for target in data['wikilinks']:
            if target not in slug_index and target not in digest_slugs:
                dangling.setdefault(target, set()).add(relpath)
    return {'dangling': {t: sorted(ps) for t, ps in sorted(dangling.items())}}


_META_STOPLIST = frozenset(
    [
        'author',
        'publisher',
        'isbn',
        'pdf',
        'source',
        'date',
        'year',
        'edition',
        'page',
        'chapter',
        'section',
        'decision criterion',
        'key concept',
        'summary',
        'tldr',
        'note',
        'warning',
        'todo',
        'fixme',
        'status',
        'version',
    ]
)
_STRUCT_STOPLIST = frozenset(
    [
        'scope',
        'purpose',
        'monitoring',
        'trade-off',
        'tradeoff',
        'overview',
        'summary',
        'background',
        'context',
        'rationale',
        'example',
        'examples',
        'definition',
        'conclusion',
        'approach',
        'motivation',
        'problem',
        'solution',
        'observation',
        'observations',
        'result',
        'results',
        'principle',
        'principles',
        'pattern',
        'patterns',
        'antipattern',
        'anti-pattern',
        # Additions: generic domain words that appear as emphasis markers, not concepts.
        # "fault tolerance" dropped here because it's too broad to warrant a dedicate page
        # candidate signal; "Circuit Breaker" (a real pattern name) intentionally excluded.
        'structure',
        'communication',
        'collaboration',
        'simplicity',
        'metrics',
        'logging',
        'tickets',
        'throughput',
        'asynchronous',
        'event-based',
        'time-based',
        'root cause',
        'best practice',
        'best practices',
        'caveat',
        'caveats',
        'fault tolerance',
    ]
)

# Substring words that mark section-label constructs rather than concept terms.
# Any bold term containing one of these words (case-insensitive) is treated as
# structural labelling and filtered out (e.g. "Synthesis strategy", "Footnotes 1–16").
_SECTION_LABEL_WORDS = frozenset(
    [
        'strategy',
        'steps',
        'mechanics',
        'footnote',
        'footnotes',
        'intentionally',
        'omitted',
    ]
)


def check_3_pass_b(pages, slug_index):
    """
    Pass B: bold terms (≥3 pages) not in canonical concept set.
    Applies the full metadata-label filter chain from spec.
    """
    # Build canonical concept set from all page titles + aliases
    canonical = set()
    for data in pages.values():
        fm = data['fm']
        if not fm:
            continue
        title = fm.get('title', '')
        if title and isinstance(title, str):
            canonical.add(title.strip().lower())
        aliases = fm.get('aliases', [])
        if isinstance(aliases, list):
            for a in aliases:
                if a and isinstance(a, str) and a.strip():
                    canonical.add(a.strip().lower())

    term_pages = {}  # term -> set of relpaths
    bold_pat = re.compile(r'\*\*([^*\n]{1,}?)\*\*')
    _neg_space_heading = re.compile(r'^##\s+negative\s+space', re.IGNORECASE)
    _h1_or_h2 = re.compile(r'^#{1,2}\s+\S')

    for relpath, data in pages.items():
        seen = set()
        in_negative_space = False
        for line in data['content'].splitlines():
            if _h1_or_h2.match(line):
                in_negative_space = bool(_neg_space_heading.match(line))
            if in_negative_space:
                continue
            for m in bold_pat.finditer(line):
                inner = m.group(1).strip()

                # Filter chain (spec §Check 3 Pass B)
                if inner.endswith(':'):
                    continue
                if inner.lower() in _META_STOPLIST:
                    continue
                if len(inner) < 4 or len(inner) > 60:
                    continue
                if re.match(r'^\[\[.*\]\]$', inner):
                    # Bold wikilink construct — handled by Check 4
                    continue
                if inner.lower() in _STRUCT_STOPLIST:
                    continue
                # Section-label filter: multi-word phrases containing structural
                # label words are heading/section markers, not concept candidates.
                inner_lower = inner.lower()
                if any(word in inner_lower for word in _SECTION_LABEL_WORDS):
                    continue

                # Recognized concept → skip (missing link, not missing page)
                if inner.lower() in canonical:
                    continue

                if inner not in seen:
                    seen.add(inner)
                    term_pages.setdefault(inner, set()).add(relpath)

    candidates = {t: sorted(ps) for t, ps in term_pages.items() if len(ps) >= 3}
    return {'candidates': candidates, 'canonical_set_size': len(canonical)}


# ══════════════════════════════════════════════════════════════════════════════
# §9  CHECK 4 — MISSING CROSS-REFERENCES
#     Ports the reference implementation from SKILL.md verbatim.
# ══════════════════════════════════════════════════════════════════════════════


def _is_role_moc(relpath):
    return relpath.startswith('wiki/topics/') and get_slug(relpath).startswith('role-')


def _is_book_entity(relpath):
    return relpath.startswith('wiki/entities/books/')


def _excluded_pair(a, b):
    """Structural exclusions (a) book-vs-role, (b) role-vs-role, (c) book-vs-book."""
    a_book, b_book = _is_book_entity(a), _is_book_entity(b)
    a_role, b_role = _is_role_moc(a), _is_role_moc(b)
    if (a_book and b_role) or (b_book and a_role):
        return True
    if a_role and b_role:
        return True
    if a_book and b_book:
        return True
    return False


# ── Check 4 tuning — hub-inflation suppression ────────────────────────────────
# Raw shared-neighbor counts inflate any pair that merely co-cites the vault's
# universal hubs. These knobs weight evidence by distinctiveness instead.
CHECK4_STOPWORD_DF_RATIO = 0.25  # neighbors linked by > this fraction of pages are stopwords
CHECK4_MIN_SHARED_NEIGHBORS = 2  # min non-stopword shared neighbors to report a pair
CHECK4_MIN_WEIGHT = 3.0  # min summed IDF weight (ln); just above two at-cutoff neighbors
CHECK4_TOPK_HUBS = 10  # a pair sharing only these global hubs is suppressed
CHECK4_MAX_REPORT = 50  # cap on reported pairs, ranked by weighted score
CHECK4_REQUIRE_SHARED_TOPIC = False  # optional: also require a shared non-generic frontmatter topic
CHECK4_GENERIC_TOPICS = frozenset({'fixed-income', 'bonds'})


def check_4_cross_refs(vault_path, pages):
    """
    Page pairs that *should* cross-link but don't, scored by the IDF-weighted
    distinctiveness of the concepts they share — not by raw shared count, which
    inflates pairs that merely both cite universal hubs.

    Scope: wiki/topics/*.md + wiki/entities/books/*.md (non-recursive).

    Hub-inflation defenses:
      1. Entity/book pages are dropped from the shared-neighbor evidence set —
         they are intentional hubs, not signs of a bilateral relationship.
      2. Each surviving shared neighbor is IDF-weighted: w = ln(N / df), where
         df is how many scanned pages link to it. Ubiquitous neighbors weigh ~0.
      3. "Stopword" neighbors (df > CHECK4_STOPWORD_DF_RATIO of all pages) are
         dropped from the evidence set before scoring.
      4. A pair is reported only if it shares >= CHECK4_MIN_SHARED_NEIGHBORS
         non-stopword neighbors AND its summed IDF weight >= CHECK4_MIN_WEIGHT.
         Pairs whose surviving shared neighbors are *all* global top-K hubs are
         suppressed.
      5. (Optional, CHECK4_REQUIRE_SHARED_TOPIC) require >= 1 shared frontmatter
         topic beyond the generic ones.
    Output is ranked and capped by weighted score, not raw count.

    Returns: {'actionable': [(a, b, weight, ranked_shared)], 'total_pages': N}.
    """
    page_links = {}
    for pattern in ['wiki/topics/*.md', 'wiki/entities/books/*.md']:
        for fpath in sorted(glob.glob(os.path.join(vault_path, pattern))):
            rp = os.path.relpath(fpath, vault_path).replace('\\', '/')
            if rp in pages:
                page_links[rp] = set(pages[rp]['wikilinks'])
            else:
                try:
                    with open(fpath, encoding='utf-8') as f:
                        page_links[rp] = set(extract_wikilink_targets(f.read()))
                except Exception:
                    page_links[rp] = set()

    page_list = sorted(page_links.keys())
    N = len(page_list)
    if N == 0:
        return {'actionable': [], 'total_pages': 0}

    # Rule 1: slugs of every entity/book page — excluded from neighbor evidence.
    entity_slugs = {get_slug(rp) for rp in pages if rp.startswith('wiki/entities/')}

    # Document frequency of each neighbor across the scanned page set.
    df = {}
    for p in page_list:
        for n in page_links[p]:
            df[n] = df.get(n, 0) + 1

    # Rule 3: stopword neighbors. Rule 4: global top-K most-linked pages.
    stopword_cutoff = CHECK4_STOPWORD_DF_RATIO * N
    stopwords = {n for n, d in df.items() if d > stopword_cutoff}
    top_k_hubs = set(sorted(df, key=lambda n: (-df[n], n))[:CHECK4_TOPK_HUBS])

    # Rule 5 (optional): non-generic frontmatter topics per scanned page.
    page_topics = {}
    for p in page_list:
        fm = (pages.get(p) or {}).get('fm') or {}
        raw = fm.get('topics', []) or []
        if not isinstance(raw, list):
            raw = [raw]
        page_topics[p] = {
            str(t).strip().lower() for t in raw if str(t).strip()
        } - CHECK4_GENERIC_TOPICS

    def idf(n):
        return math.log(N / df[n])

    actionable = []
    for i, a in enumerate(page_list):
        slug_a = get_slug(a)
        links_a = page_links[a]
        for j in range(i + 1, len(page_list)):
            b = page_list[j]
            slug_b = get_slug(b)
            links_b = page_links[b]
            if slug_b in links_a or slug_a in links_b:
                continue
            if _excluded_pair(a, b):
                continue

            shared = (links_a & links_b) - {slug_a, slug_b}
            shared -= entity_slugs  # rule 1
            shared -= stopwords  # rule 3
            if len(shared) < CHECK4_MIN_SHARED_NEIGHBORS:
                continue
            if shared <= top_k_hubs:  # rule 4: all-hub evidence = no signal
                continue
            if CHECK4_REQUIRE_SHARED_TOPIC and not (page_topics[a] & page_topics[b]):
                continue

            weight = sum(idf(n) for n in shared)
            if weight < CHECK4_MIN_WEIGHT:  # rule 4: weighted floor
                continue

            ranked = sorted(shared, key=lambda n: (-idf(n), n))
            actionable.append((a, b, round(weight, 3), ranked))

    # Rule: rank and cap by weighted score, not raw count.
    actionable.sort(key=lambda x: (-x[2], x[0], x[1]))
    return {'actionable': actionable[:CHECK4_MAX_REPORT], 'total_pages': N}


# ══════════════════════════════════════════════════════════════════════════════
# §10 CHECK 5 — DUPLICATE CONCEPT PAGES
# ══════════════════════════════════════════════════════════════════════════════

# ── Check 5 tuning — duplicate-vs-de-alias discrimination ─────────────────────
# Generic finance terms that two pages can legitimately both carry without being
# duplicates — they never count as duplicate evidence.
CHECK5_GENERIC_TERMS = frozenset(
    {
        'option greeks',
        'premium/discount',
        'alpha/beta',
        'risk premium',
        'cap/floor',
        'hedge ratio',
        'average life',
        'yield ratio',
    }
)
CHECK5_JACCARD_THRESHOLD = 0.5  # min alias-set Jaccard to call a pair duplicate
CHECK5_TITLE_SIMILARITY = 0.9  # SequenceMatcher ratio for "near-identical" titles


def _resolves_elsewhere(term, dedicated, titles, exclude):
    """True if `term` is the title/slug of a dedicated page outside `exclude`."""
    for rp in dedicated.get(term, ()):
        if rp in exclude:
            continue
        if titles.get(rp) == term or get_slug(rp).lower() == term:
            return True
    return False


def check_5_duplicates(pages):
    """
    Distinguish genuine duplicate pages from two weaker signals that a single
    shared term used to masquerade as duplication:

    (a) Generic-term stoplist (CHECK5_GENERIC_TERMS) — terms like "risk premium"
        or "hedge ratio" never count as duplicate evidence.
    (b) Alias-should-resolve-to-dedicated-page — if a page's alias equals the
        title/slug of a *different* dedicated page, that is a de-alias signal,
        reported separately in 'alias_resolve' and excluded from duplicate
        evidence. It means "make this alias a link", not "merge these pages".
    (c) A pair is a true duplicate only when its cleaned alias-set Jaccard
        exceeds CHECK5_JACCARD_THRESHOLD OR its titles are near-identical
        (>= CHECK5_TITLE_SIMILARITY) — never on a single shared term.

    Returns: {'pairs': [(a, b, shared, otype, jaccard)], 'alias_resolve': [...]}.
    """
    titles = {}
    alias_sets = {}
    for rp, data in pages.items():
        fm = data['fm'] or {}
        titles[rp] = (fm.get('title') or '').strip().lower()
        aliases = set()
        for a in fm.get('aliases', []) or []:
            if a and isinstance(a, str) and a.strip():
                aliases.add(a.strip().lower())
        alias_sets[rp] = aliases - CHECK5_GENERIC_TERMS  # rule (a)

    # Dedicated-page index: normalised title or slug -> {relpaths}.
    dedicated = {}
    for rp in pages:
        if titles[rp]:
            dedicated.setdefault(titles[rp], set()).add(rp)
        dedicated.setdefault(get_slug(rp).lower(), set()).add(rp)

    # Rule (b): per-page de-alias hygiene findings.
    alias_resolve = []
    for rp in sorted(pages):
        for al in sorted(alias_sets[rp]):
            targets = sorted(
                t
                for t in dedicated.get(al, set()) - {rp}
                if titles[t] == al or get_slug(t).lower() == al
            )
            if targets:
                alias_resolve.append({'page': rp, 'alias': al, 'dedicated': targets})

    pairs = []
    page_list = sorted(alias_sets.keys())
    for i, a in enumerate(page_list):
        for j in range(i + 1, len(page_list)):
            b = page_list[j]
            exclude = {a, b}
            # Drop aliases that resolve to a *third* dedicated page (rule b) and
            # generic terms (already stripped) before measuring overlap.
            ca = {
                t for t in alias_sets[a] if not _resolves_elsewhere(t, dedicated, titles, exclude)
            }
            cb = {
                t for t in alias_sets[b] if not _resolves_elsewhere(t, dedicated, titles, exclude)
            }
            inter = ca & cb
            union = ca | cb
            jaccard = len(inter) / len(union) if union else 0.0

            ta, tb = titles[a], titles[b]
            titles_near = (
                bool(ta)
                and bool(tb)
                and (
                    ta == tb
                    or difflib.SequenceMatcher(None, ta, tb).ratio() >= CHECK5_TITLE_SIMILARITY
                )
            )

            # Rule (c): need strong alias overlap OR near-identical titles.
            if jaccard < CHECK5_JACCARD_THRESHOLD and not titles_near:
                continue

            shared = set(inter)
            if titles_near and ta == tb:
                shared.add(ta)
            shared = sorted(shared) or sorted({ta, tb} - {''})

            ta_in = ta in shared
            tb_in = tb in shared
            if ta_in and tb_in:
                otype = 'title-vs-title'
            elif ta_in or tb_in:
                otype = 'title-vs-alias'
            else:
                otype = 'alias-vs-alias'
            pairs.append((a, b, shared, otype, round(jaccard, 3)))

    return {'pairs': pairs, 'alias_resolve': alias_resolve}


# ══════════════════════════════════════════════════════════════════════════════
# §11 CHECK 6 — STALE CLAIMS
# ══════════════════════════════════════════════════════════════════════════════


def check_6_stale_claims(pages):
    """
    Condition A: last_updated > 12 months ago + status: active.
    Condition B: explicit CONTRADICTS: marker in frontmatter or body.
                 (Replaced the polarity-inference heuristic, which produced
                  17 false positives and zero true positives in software-craft.)
    """
    cutoff = TODAY - datetime.timedelta(days=365)
    stale_active = []

    for rp, data in pages.items():
        fm = data['fm']
        if not fm:
            continue
        if fm.get('status', 'active') != 'active':
            continue
        lu = fm.get('last_updated', '')
        if not lu:
            continue
        try:
            d = datetime.date.fromisoformat(str(lu))
            if d < cutoff:
                topics = fm.get('topics', [])
                stale_active.append(
                    {
                        'page': rp,
                        'last_updated': str(lu),
                        'topics': topics if isinstance(topics, list) else [topics],
                    }
                )
        except (ValueError, TypeError):
            pass

    # Condition B: pages containing the literal string CONTRADICTS: anywhere
    # in their content (the vault convention for flagging inline contradictions).
    # Zero false-positive rate; one true positive per real contradiction marker.
    contradicts_findings = []
    for rp, data in pages.items():
        content = data['content']
        if 'CONTRADICTS:' not in content:
            continue
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'CONTRADICTS:' not in line:
                continue
            # Capture line plus one line of context each side
            before = lines[i - 1].strip() if i > 0 else ''
            after = lines[i + 1].strip() if i + 1 < len(lines) else ''
            contradicts_findings.append(
                {
                    'page': rp,
                    'line': line.strip()[:200],
                    'context_before': before[:120],
                    'context_after': after[:120],
                }
            )

    return {'stale_active': stale_active, 'opposing_candidates': contradicts_findings}


# ══════════════════════════════════════════════════════════════════════════════
# §12 CHECK 7 — DATA GAPS
# ══════════════════════════════════════════════════════════════════════════════


def check_7_data_gaps(pages):
    """
    Stubs (Condition A) and explicit gap markers (Condition B).

    Condition B markers (all case-sensitive except where noted):
      TODO:   FIXME:   [?]   ??   > Q:
    The bare-? heuristic was removed — it surfaced 30 false positives
    (example questions in book prose) and could not distinguish them from
    real open factual questions.
    """
    stubs = []
    todos = []
    open_questions = []

    # Explicit gap markers only. TODO/FIXME require the colon suffix to avoid
    # matching the word as prose (e.g. "things to do" patterns in body text).
    # [?] is the bracket-marker convention. ?? flags genuine uncertainty notation.
    # > Q: is the explicit question-block syntax.
    todo_pat = re.compile(r'(TODO:|FIXME:|\[?\?\]|\?\?|^> Q:)', re.MULTILINE)

    for rp, data in pages.items():
        fm = data['fm'] or {}
        content = data['content']

        if fm.get('status') == 'stub':
            stubs.append(rp)

        # Body only (strip frontmatter)
        body = content
        if content.startswith('---'):
            try:
                end_idx = content.index('\n---', 3)
                body = content[end_idx + 4 :]
            except ValueError:
                pass

        seen_keys = set()
        for m in todo_pat.finditer(body):
            marker = m.group(0).strip()
            key = (rp, marker)
            if key in seen_keys:
                continue
            seen_keys.add(key)
            ls = body.rfind('\n', 0, m.start()) + 1
            le = body.find('\n', m.end())
            line = body[ls : (le if le >= 0 else len(body))].strip()
            # Route to the right bucket
            if marker in ('TODO:', 'FIXME:'):
                todos.append({'page': rp, 'marker': marker, 'line': line[:120]})
            else:
                open_questions.append({'page': rp, 'marker': marker, 'line': line[:120]})

    return {
        'stubs': stubs,
        'todos': todos,
        'open_questions': open_questions,
    }


# ══════════════════════════════════════════════════════════════════════════════
# §12.5 CHECK 8 — CONTROLLED-VOCABULARY RESOLUTION (topics-authority SOT)
#     Resolves `topics:` against the Subjects tier and `aliases:` against the
#     Concepts tier of wiki/topics-authority.md (a lightweight thesaurus:
#     preferred term + use-for variants). Report-only. Skips cleanly when the
#     SOT file is absent, so vaults without one are unaffected.
# ══════════════════════════════════════════════════════════════════════════════


def _extract_authority_section(text, *headings):
    """Body text under the first matching ## heading (until the next ## or EOF)."""
    for h in headings:
        m = re.search(
            r'^#{2,}\s+' + re.escape(h) + r'[^\n]*\n(.*?)(?=^\s*#{2,}\s|\Z)',
            text,
            re.MULTILINE | re.DOTALL | re.IGNORECASE,
        )
        if m:
            return m.group(1)
    return ''


def _parse_authority_table(section_text):
    """
    Parse a two-column markdown table — | `preferred` | variant, variant | —
    into (preferred_set, variant_map). variant_map maps each lower-cased
    use-for variant to its preferred term. Header/separator rows are skipped.
    """
    preferred = set()
    variants = {}
    for line in section_text.split('\n'):
        line = line.strip()
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) < 2:
            continue
        pref = cells[0].strip().strip('`').strip()
        if (
            not pref
            or pref.lower() in ('preferred', 'preferred (page)', 'canonical')
            or set(pref) <= set('-: ')
        ):
            continue
        preferred.add(pref.lower())
        for v in re.split(r'[,;]', cells[1]):
            v = v.strip().strip('`').strip()
            if v and v not in ('—', '-', ''):
                variants[v.lower()] = pref.lower()
    return preferred, variants


def parse_topics_authority(vault_path):
    """
    Parse wiki/topics-authority.md into the controlled vocabulary.
    Returns None when the file is absent (the check is then skipped).
    """
    path = os.path.join(vault_path, 'wiki', 'topics-authority.md')
    if not os.path.isfile(path):
        return None
    try:
        with open(path, encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f'WARNING: could not read topics-authority.md: {e}', file=sys.stderr)
        return None

    fm = parse_frontmatter(text) or {}
    subj_pref, subj_var = _parse_authority_table(
        _extract_authority_section(text, 'Subject categories', 'Subjects')
    )
    conc_pref, conc_var = _parse_authority_table(
        _extract_authority_section(text, 'Concept aliases', 'Concepts')
    )
    reserved = set()
    for line in _extract_authority_section(
        text, 'Reserved non-subject tags', 'Reserved tags'
    ).split('\n'):
        for tok in re.findall(r'`([^`]+)`', line):
            reserved.add(tok.strip().lower())

    return {
        'subjects': {'preferred': subj_pref, 'variants': subj_var},
        'concepts': {'preferred': conc_pref, 'variants': conc_var},
        'reserved': reserved,
        # The file's declared type — should be `authority` (governance record).
        'declared_type': fm.get('type'),
        # A well-formed authority file has both vocabulary sections.
        'has_sections': bool(
            re.search(r'^#{2,}\s+Subject categories', text, re.M)
            and re.search(r'^#{2,}\s+Concept aliases', text, re.M)
        ),
        # Unpopulated scaffolder skeleton: no vocabulary registered at all.
        'is_skeleton': not subj_pref and not conc_pref,
    }


def _nearest_preferred(value, preferred, threshold=0.6):
    """Best-matching preferred term for an unresolved value, or None."""
    best, best_r = None, 0.0
    vt = set(value.lower().split('-'))
    for p in preferred:
        r = difflib.SequenceMatcher(None, value.lower(), p).ratio()
        pt = set(p.split('-'))
        if vt & pt:  # shared hyphen-token → boost
            r = max(r, 0.5 + 0.5 * len(vt & pt) / max(len(vt | pt), 1))
        if r > best_r:
            best, best_r = p, r
    return best if best_r >= threshold else None


def check_8_vocabulary(pages, authority):
    """
    CHECK 8 — controlled-vocabulary resolution against topics-authority.md.

    Subjects tier: every `topics:` value must resolve to a preferred subject
    (or a reserved non-subject tag). A registered use-for variant is flagged
    "use the canonical"; an unresolved value is flagged with the nearest
    preferred term suggested. Concepts tier: enforce the de-alias guarantees —
    no alias may belong to two pages (collision) and no alias may shadow a
    different page's canonical slug/title (homonym). Report-only.

    Returns {'skipped': True} when no SOT file is present.
    """
    if authority is None:
        return {'skipped': True}

    subj = authority['subjects']
    reserved = authority['reserved']

    topic_unregistered = []  # topics: value resolves to nothing
    topic_use_preferred = []  # topics: value is a use-for variant → use canonical
    alias_collision = []  # alias owned by >1 page
    alias_shadows = []  # alias equals a different page's canonical

    # ── Subjects tier ──
    for relpath, p in sorted(pages.items()):
        fm = p['fm'] or {}
        topics = fm.get('topics') or []
        if not isinstance(topics, list):
            topics = [topics]
        for t in topics:
            tl = str(t).strip().lower()
            if not tl or tl in reserved or tl in subj['preferred']:
                continue
            if tl in subj['variants']:
                topic_use_preferred.append(
                    {'page': relpath, 'value': t, 'canonical': subj['variants'][tl]}
                )
            elif subj['preferred']:  # only meaningful once a vocabulary is declared
                topic_unregistered.append(
                    {
                        'page': relpath,
                        'value': t,
                        'suggestion': _nearest_preferred(tl, subj['preferred']),
                    }
                )

    # ── Concepts tier — alias uniqueness from frontmatter (the de-alias guarantee) ──
    canonical_slugs = {get_slug(rp): rp for rp in pages}
    canonical_titles = {}
    for rp, p in pages.items():
        title = (p['fm'] or {}).get('title')
        if isinstance(title, str):
            canonical_titles[title.strip().lower()] = rp

    alias_owner = {}
    for relpath, p in sorted(pages.items()):
        aliases = (p['fm'] or {}).get('aliases') or []
        if not isinstance(aliases, list):
            aliases = [aliases]
        for a in aliases:
            al = str(a).strip().lower()
            if not al:
                continue
            alias_owner.setdefault(al, set()).add(relpath)
            owner = canonical_slugs.get(al) or canonical_titles.get(al)
            if owner and owner != relpath:
                alias_shadows.append({'page': relpath, 'alias': a, 'canonical_page': owner})

    for al, owners in sorted(alias_owner.items()):
        if len(owners) > 1:
            alias_collision.append({'alias': al, 'pages': sorted(owners)})

    # Unseeded-skeleton backstop: the scaffolder ships an empty topics-authority.md
    # that the first ingest is meant to seed. If the vault has accumulated real
    # content but the SOT is still empty, the first-ingest seed was skipped.
    SKELETON_UNSEEDED_MIN_PAGES = 3
    skeleton_unseeded = bool(
        authority.get('is_skeleton') and len(pages) >= SKELETON_UNSEEDED_MIN_PAGES
    )

    # Authority-file checks (this category is exempt from the topic-page checks,
    # so it is validated here instead): correct declared type + well-formed.
    authority_type_wrong = authority.get('declared_type') != 'authority'
    authority_malformed = not authority.get('has_sections')

    return {
        'skipped': False,
        'topic_unregistered': topic_unregistered,
        'topic_use_preferred': topic_use_preferred,
        'alias_collision': alias_collision,
        'alias_shadows': alias_shadows,
        'skeleton_unseeded': skeleton_unseeded,
        'authority_type_wrong': authority_type_wrong,
        'authority_declared_type': authority.get('declared_type'),
        'authority_malformed': authority_malformed,
        'page_count': len(pages),
        'subject_vocab_size': len(subj['preferred']),
        'concept_vocab_size': len(authority['concepts']['preferred']),
    }


# ══════════════════════════════════════════════════════════════════════════════
# §13 PHASE 2 — ROLE-COUNT DRIFT
#     Reference implementation from SKILL.md, inlined verbatim.
# ══════════════════════════════════════════════════════════════════════════════


def _parse_frontmatter_roles(content):
    """
    Extract roles list from YAML frontmatter.
    Handles: roles: [a, b, c]  and block form with - items.
    Returns None (field absent), [] (empty), or [str, ...].
    Verbatim from SKILL.md reference implementation.
    """
    if not content.startswith('---'):
        return None
    try:
        end = content.index('\n---', 3)
    except ValueError:
        return None
    fm = content[3:end]

    inline = re.search(r'^roles:\s*\[(.*?)\]\s*$', fm, re.MULTILINE)
    if inline:
        raw = inline.group(1).strip()
        if not raw:
            return []
        return [s.strip().strip('\'"') for s in raw.split(',') if s.strip()]

    block = re.search(r'^roles:\s*\n((?:\s*-\s*.+\n?)+)', fm, re.MULTILINE)
    if block:
        items = []
        for line in block.group(1).split('\n'):
            m = re.match(r'\s*-\s*(.+)', line)
            if m:
                items.append(m.group(1).strip().strip('\'"'))
        return items

    if re.search(r'^roles:\s*$', fm, re.MULTILINE):
        return []

    return None


def phase_2_role_drift(vault_path, canonical_roles, index_md_text):
    """
    Compute actual role counts from wiki/topics/*.md ONLY (not entities).
    Compare to reported counts in index.md. Return full result dict.
    """
    counts = {r: 0 for r in canonical_roles}
    missing_roles = []
    unknown_roles = {}
    over_assigned = []
    total_scanned = 0

    for fpath in sorted(glob.glob(os.path.join(vault_path, 'wiki/topics/*.md'))):
        total_scanned += 1
        rp = os.path.relpath(fpath, vault_path)
        try:
            with open(fpath, encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f'WARNING: could not read {rp}: {e}', file=sys.stderr)
            continue

        roles = _parse_frontmatter_roles(content)
        if roles is None or roles == []:
            missing_roles.append(rp)
            continue

        unique = list(dict.fromkeys(r.strip() for r in roles))
        if len(unique) >= 4:
            over_assigned.append((rp, unique))

        for role in unique:
            if role in counts:
                counts[role] += 1
            else:
                unknown_roles.setdefault(role, []).append(rp)

    reported, fmt_type, fmt_lines = _parse_index_role_counts(index_md_text, canonical_roles)
    skipped = fmt_type == 'unknown'
    delta = {} if skipped else {r: counts[r] - reported.get(r, 0) for r in canonical_roles}

    actual_vals = [counts[r] for r in canonical_roles]
    med = _median(actual_vals)
    anemic = [r for r in canonical_roles if counts[r] < 3]
    dominant = [r for r in canonical_roles if counts[r] > 2 * med and med > 0]

    return {
        'actual': counts,
        'reported': reported,
        'delta': delta,
        'skipped': skipped,
        'total_scanned': total_scanned,
        'missing_roles': missing_roles,
        'unknown_roles': unknown_roles,
        'over_assigned': over_assigned,
        'anemic': anemic,
        'dominant': dominant,
        'fmt_type': fmt_type,
        'fmt_lines': fmt_lines,
    }


def _median(vals):
    if not vals:
        return 0
    s = sorted(vals)
    n = len(s)
    return (s[n // 2 - 1] + s[n // 2]) / 2 if n % 2 == 0 else s[n // 2]


def _parse_index_role_counts(index_md_text, canonical_roles):
    """
    Detect and parse the role-page-counts surface in index.md.
    Returns (reported_counts, format_type, (start_line, end_line)).
    format_type: 'list', 'table', or 'unknown'
    """
    reported = {r: 0 for r in canonical_roles}
    if not index_md_text:
        return reported, 'unknown', (-1, -1)

    lines = index_md_text.split('\n')

    # Find section heading containing "Role"
    sec_start = next((i for i, ln in enumerate(lines) if re.match(r'^##\s+.*[Rr]ole', ln)), -1)
    if sec_start < 0:
        return reported, 'unknown', (-1, -1)

    # Find section end
    sec_end = next(
        (i for i in range(sec_start + 1, len(lines)) if re.match(r'^##\s+', lines[i])), len(lines)
    )

    section = lines[sec_start:sec_end]
    has_list = any(re.match(r'^-\s+\[Role', ln) for ln in section)
    has_table = any('|' in ln and not re.match(r'^[\|\s\-:]+$', ln) for ln in section)

    if has_list:
        for ln in section:
            # - [Role — Name](topics/role-<id>.md) — N pages; ...
            m = re.match(r'^-\s+\[.*?\]\((.*?)\).*?—\s+(\d+)\s+pages?', ln)
            if not m:
                continue
            path_slug = os.path.splitext(os.path.basename(m.group(1)))[0]
            role_id = path_slug[len('role-') :] if path_slug.startswith('role-') else path_slug
            if role_id in reported:
                reported[role_id] = int(m.group(2))
        return reported, 'list', (sec_start, sec_end)

    if has_table:
        for ln in section:
            if '|' not in ln or re.match(r'^[\|\s\-:]+$', ln):
                continue
            cells = [c.strip() for c in ln.split('|') if c.strip()]
            if len(cells) < 2:
                continue
            for role_id in canonical_roles:
                if role_id in cells[0].lower() or role_id.replace('-', ' ') in cells[0].lower():
                    try:
                        reported[role_id] = int(re.search(r'\d+', cells[1]).group())
                    except (AttributeError, ValueError):
                        pass
                    break
        return reported, 'table', (sec_start, sec_end)

    return reported, 'unknown', (sec_start, sec_end)


# ══════════════════════════════════════════════════════════════════════════════
# §14 PHASE 2.5 — REGRESSION GUARD
# ══════════════════════════════════════════════════════════════════════════════


def phase_2_5_guard(activity, p2_result, watermark_date):
    """
    Returns FATAL dict if ALL three conditions hold, else None:
      1. watermark exists
      2. zero activity across all categories
      3. Phase 2 was not skipped AND at least one role has non-zero delta
    """
    if watermark_date is None:
        return None
    if p2_result.get('skipped'):
        return None
    total_activity = (
        activity['books'] + activity['articles'] + activity['other_ingests'] + activity['handoffs']
    )
    if total_activity > 0:
        return None
    if not any(d != 0 for d in p2_result['delta'].values()):
        return None
    return {
        'watermark_date': watermark_date.isoformat(),
        'delta': p2_result['delta'],
        'reported': p2_result['reported'],
        'actual': p2_result['actual'],
    }


# ══════════════════════════════════════════════════════════════════════════════
# §15 PHASE 3 — VAULT-SPECIFIC EXTENSIONS
# ══════════════════════════════════════════════════════════════════════════════


def phase_3_extensions(vault_path, extension_checks, config):
    """Run each declared extension check. Returns list of result dicts."""
    results = []
    for check in extension_checks:
        cid = check.get('id', '')
        desc = check.get('description', cid)
        handler = _EXT_HANDLERS.get(cid)
        if handler is None:
            results.append(
                {
                    'id': cid,
                    'description': desc,
                    'findings': [],
                    'error': f'CONFIG-ERROR: unknown extension check id "{cid}"',
                }
            )
        else:
            try:
                findings = handler(vault_path, config, check)
                results.append({'id': cid, 'description': desc, 'findings': findings})
            except Exception as e:
                results.append(
                    {
                        'id': cid,
                        'description': desc,
                        'findings': [],
                        'error': f'ERROR: {type(e).__name__}: {e}',
                    }
                )
    return results


def _ext_project_entity_recent_handoff(vault_path, config, check):
    projects = config.get('projects', [])
    if not projects:
        return [{'info': 'No projects declared in VAULT-LINT-EXTENSIONS.'}]

    handoff_dir = os.path.join(vault_path, 'wiki', 'handoffs', 'coding-handoffs')
    if not os.path.isdir(handoff_dir):
        return [{'info': 'Handoff directory not found: wiki/handoffs/coding-handoffs/'}]

    cutoff_90d = TODAY - datetime.timedelta(days=90)
    per_project = {p: [] for p in projects}
    malformed = []

    for fname in sorted(os.listdir(handoff_dir)):
        if not fname.endswith('.md'):
            continue
        parts = fname[:-3].split('-')  # strip .md then split on hyphen
        if len(parts) < 2:
            malformed.append((fname, 'fewer than 2 hyphen-delimited segments'))
            continue

        project_code = parts[1]  # second segment = project code

        # Date: last YYYY-MM-DD occurrence in the filename
        date_matches = re.findall(r'\d{4}-\d{2}-\d{2}', fname)
        if not date_matches:
            malformed.append((fname, 'no YYYY-MM-DD date found in filename'))
            continue
        try:
            handoff_date = datetime.date.fromisoformat(date_matches[-1])
        except ValueError:
            malformed.append((fname, f'unparseable date: {date_matches[-1]}'))
            continue

        if project_code not in per_project:
            malformed.append((fname, f'project code "{project_code}" not in declared list'))
            continue

        per_project[project_code].append(handoff_date)

    findings = []
    for project in projects:
        dates = sorted(per_project[project], reverse=True)
        recent_count = sum(1 for d in dates if d >= cutoff_90d)
        most_recent = dates[0] if dates else None
        days_since = (TODAY - most_recent).days if most_recent else None
        status = 'active' if recent_count > 0 else 'quiescent'
        findings.append(
            {
                'project': project,
                'handoffs_last_90d': recent_count,
                'most_recent': most_recent.isoformat() if most_recent else 'none found',
                'days_since': days_since,
                'status': status,
            }
        )

    if malformed:
        findings.append({'malformed': malformed})
    return findings


def _ext_cross_vault_reference_format(vault_path, config, check):
    findings = []
    marker = 'See also (cross-vault):'
    for pattern in ['wiki/topics/**/*.md', 'wiki/entities/**/*.md']:
        for fpath in sorted(glob.glob(os.path.join(vault_path, pattern), recursive=True)):
            rp = os.path.relpath(fpath, vault_path)
            try:
                with open(fpath, encoding='utf-8') as f:
                    flines = f.readlines()
            except Exception:
                continue
            for lineno, line in enumerate(flines, 1):
                if marker in line and re.search(r'\[\[', line):
                    findings.append(
                        {
                            'file': rp,
                            'line': lineno,
                            'text': line.strip()[:200],
                            'violation': 'uses [[wikilink]] instead of plain labelled path',
                        }
                    )
    return findings


def _ext_calendar_staleness_sweep(vault_path, config, check):
    findings = []
    for fpath in sorted(glob.glob(os.path.join(vault_path, 'wiki/topics/**/*.md'), recursive=True)):
        rp = os.path.relpath(fpath, vault_path)
        try:
            with open(fpath, encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        fm = parse_frontmatter(content)
        if not fm:
            continue
        next_review_str = fm.get('next_review', '')
        status = fm.get('status', '')
        if not next_review_str or status in ('needs-review', 'archived'):
            continue
        try:
            nr = datetime.date.fromisoformat(str(next_review_str))
            if nr <= TODAY:
                findings.append(
                    {
                        'page': rp,
                        'volatility': fm.get('volatility', ''),
                        'next_review': str(next_review_str),
                        'status': status,
                    }
                )
        except (ValueError, TypeError):
            pass
    return findings


_PT_ACCENTED = re.compile(r'[çãõáéíóúâêôà]', re.IGNORECASE)
_PT_SIGNAL = re.compile(
    r'\b(come-cotas|renda|fixa|variável|Tesouro|Selic|IPCA|Prefixado|debênture|'
    r'marcação|mercado|inventário|previdência|holding|familiar|FII|PGBL|VGBL|'
    r'FGC|IOF|ITCMD)\b',
    re.IGNORECASE,
)


def _ext_alias_bilingual_coverage(vault_path, config, check):
    findings = []
    for fpath in sorted(glob.glob(os.path.join(vault_path, 'wiki/topics/**/*.md'), recursive=True)):
        rp = os.path.relpath(fpath, vault_path)
        try:
            with open(fpath, encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        fm = parse_frontmatter(content)
        if not fm:
            continue
        title = fm.get('title', '') or ''
        if not (_PT_ACCENTED.search(title) or _PT_SIGNAL.search(title)):
            continue
        aliases = fm.get('aliases', [])
        if not aliases:
            findings.append({'page': rp, 'title': title, 'aliases': str(aliases)})
    return findings


_PT_STOPWORDS = re.compile(r'\b(de|da|do|das|dos|com|ao|aos)\b', re.IGNORECASE)


def _ext_english_first_naming(vault_path, config, check):
    """Flag topic pages whose title reads Portuguese-first, unless the slug is an
    approved Brazilian term-of-art listed in the check's comma-separated `allowlist`
    sub-key. Detection: a PT accented character or a PT function word in the title.
    English titles that legitimately embed a protected term (e.g. 'Renda Fixa
    Indices', 'DI Futures Contracts') carry neither signal and are not flagged."""
    allow = set(s.strip() for s in str(check.get('allowlist', '')).split(',') if s.strip())
    findings = []
    for fpath in sorted(glob.glob(os.path.join(vault_path, 'wiki/topics/**/*.md'), recursive=True)):
        rp = os.path.relpath(fpath, vault_path)
        slug = os.path.basename(fpath)[:-3]
        if slug in allow:
            continue
        try:
            with open(fpath, encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        fm = parse_frontmatter(content)
        if not fm:
            continue
        title = fm.get('title', '') or ''
        if _PT_ACCENTED.search(title) or _PT_STOPWORDS.search(title):
            findings.append(
                {
                    'page': rp,
                    'title': title,
                    'reason': 'Portuguese-first title; slug not in terms-of-art allowlist',
                }
            )
    return findings


def _ext_book_entity_backlink(vault_path, config, check):
    """Every topic page that cites a book's PDF must wikilink that book's entity
    page; otherwise the entity is orphaned (the orphan check excludes index.md, so
    a catalogue entry does not save it). Enforces the per-page Source-entity
    backlink rule from book-ingestion at vault scope — a backstop to the orphan
    check, which only sees the aggregate (>=1 inbound link), not per-page coverage.

    The book *folder* slug may differ from the *entity* slug (e.g.
    books/periodization/ -> entities/books/periodization-book.md, named to avoid
    colliding with the `periodization` concept page), and an entity page need not
    cite its own PDF — so map each book folder to its entity deterministically from
    the filesystem: prefer an entity file named exactly for the folder, else fall
    back to `<folder>-book`. The check is edge-based: any wikilink to the entity
    (`[[slug]]` or `[[slug|display]]`) anywhere on the page satisfies it.

    Hardening: a cited book whose entity cannot be resolved is never silently
    skipped (that was a false-negative risk — a misnamed or missing entity would
    hide). Two cases are distinguished:
      - HARD finding: the entity exists but the citing page does not link it.
      - WARN: the book folder exists and is cited, but no entity page resolves
        (neither `<folder>.md` nor `<folder>-book.md`). The benign cause is a book
        mid-ingest whose entity page is not created yet; it could also be a missing
        or misnamed entity. Emitted once per book (not per citing page) to stay
        quiet, and as WARN rather than a hard finding so an in-progress ingest is
        not punished.
    A citation pointing at a book *folder that does not exist on disk* is left to
    Check 1 (citation resolution), which owns broken citations — flagging it here
    too would only duplicate that finding."""
    cite_re = re.compile(r'raw-input/books/([^/)]+)/')
    ent_dir = os.path.join(vault_path, 'wiki/entities/books')
    folder_to_entity = {}
    existing_folders = set()
    for bdir in sorted(glob.glob(os.path.join(vault_path, 'raw-input/books/*/'))):
        folder = os.path.basename(bdir.rstrip('/'))
        existing_folders.add(folder)
        for cand in (folder, folder + '-book'):
            if os.path.isfile(os.path.join(ent_dir, cand + '.md')):
                folder_to_entity[folder] = cand
                break

    findings = []
    unresolved = {}  # book folder (exists, cited, no entity) -> [citing pages]
    for fpath in sorted(glob.glob(os.path.join(vault_path, 'wiki/topics/**/*.md'), recursive=True)):
        rp = os.path.relpath(fpath, vault_path)
        try:
            with open(fpath, encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        for folder in sorted(set(cite_re.findall(content))):
            if folder not in existing_folders:
                continue  # broken citation — owned by Check 1, not duplicated here
            entity = folder_to_entity.get(folder)
            if entity is None:
                unresolved.setdefault(folder, []).append(rp)
                continue
            if not re.search(r'\[\[' + re.escape(entity) + r'(?:\]\]|\|)', content):
                findings.append(
                    {
                        'page': rp,
                        'book': folder,
                        'entity': entity,
                        'reason': f'cites book "{folder}" but does not wikilink its entity [[{entity}]]',
                    }
                )

    for folder in sorted(unresolved):
        citers = unresolved[folder]
        findings.append(
            {
                'severity': 'warn',
                'book': folder,
                'entity': None,
                'citing_count': len(citers),
                'citing_sample': citers[:3],
                'reason': (
                    f'book "{folder}" is cited by {len(citers)} topic page(s) but no entity '
                    f'page resolves (expected wiki/entities/books/{folder}.md or '
                    f'{folder}-book.md) — book mid-ingest, or entity missing/misnamed'
                ),
            }
        )
    return findings


_MERGE_PTR = re.compile(r'[Mm]erged into \[\[([^\]|#]+)')


def _ext_merge_tombstone_hygiene(vault_path, config, check):
    """Merge-tombstone hygiene — the automatable proxy for the book-ingestion
    pair-and-split rule (book-ingestion SKILL.md). It cannot judge whether a merge
    wrongly conflated two *contrasting* concepts (that is book-review Check 2 and a
    manual-review item), but it does verify a merge preserved *retrievability*:

    For each archived page (status: archived) carrying a 'Merged into [[X]]' pointer:
      (a) FAIL — the merge target [[X]] must exist as a live page (no broken redirect);
      (b) WARN — the tombstone must carry no aliases (they migrate to the target, so a
          term has one owner; leftover aliases re-split retrievability and re-collide);
      (c) WARN — no live page may still wikilink the tombstone (all inbound links must
          be redirected to the target).
    """
    findings = []
    live_slugs = set()
    files = {}  # relpath -> (fm, content)
    for pattern in ['wiki/topics/**/*.md', 'wiki/entities/**/*.md']:
        for fpath in sorted(glob.glob(os.path.join(vault_path, pattern), recursive=True)):
            rp = os.path.relpath(fpath, vault_path).replace('\\', '/')
            try:
                with open(fpath, encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue
            fm = parse_frontmatter(content) or {}
            files[rp] = (fm, content)
            if fm.get('status') != 'archived':
                live_slugs.add(os.path.splitext(os.path.basename(rp))[0])

    # Inbound wikilinks per slug, counted from live pages only.
    inbound = {}
    for rp, (fm, content) in files.items():
        if fm.get('status') == 'archived':
            continue
        for tgt in extract_wikilink_targets(content):
            inbound.setdefault(tgt, set()).add(rp)

    for rp, (fm, content) in sorted(files.items()):
        if fm.get('status') != 'archived':
            continue
        m = _MERGE_PTR.search(content)
        if not m:
            continue  # archived but not a merge redirect — out of this check's scope
        slug = os.path.splitext(os.path.basename(rp))[0]
        target = m.group(1).strip()
        if target not in live_slugs:
            findings.append(
                {
                    'page': rp,
                    'severity': 'fail',
                    'reason': f'merge target [[{target}]] is not a live page (broken redirect)',
                }
            )
        aliases = fm.get('aliases', []) or []
        if aliases:
            findings.append(
                {
                    'page': rp,
                    'severity': 'warn',
                    'reason': f'tombstone still carries {len(aliases)} alias(es); migrate them to [[{target}]] so each term has one owner',
                }
            )
        stragglers = sorted(inbound.get(slug, set()))
        if stragglers:
            shown = ', '.join(stragglers[:8]) + ('…' if len(stragglers) > 8 else '')
            findings.append(
                {
                    'page': rp,
                    'severity': 'warn',
                    'reason': f'{len(stragglers)} live page(s) still wikilink this tombstone instead of [[{target}]]: {shown}',
                }
            )
    return findings


_EXT_HANDLERS = {
    'project-entity-recent-handoff': _ext_project_entity_recent_handoff,
    'merge-tombstone-hygiene': _ext_merge_tombstone_hygiene,
    'cross-vault-reference-format': _ext_cross_vault_reference_format,
    'calendar-staleness-sweep': _ext_calendar_staleness_sweep,
    'alias-bilingual-coverage': _ext_alias_bilingual_coverage,
    'english-first-naming': _ext_english_first_naming,
    'book-entity-backlink': _ext_book_entity_backlink,
}


# ══════════════════════════════════════════════════════════════════════════════
# §16 REPORT RENDERING
# ══════════════════════════════════════════════════════════════════════════════


def _fmt_delta(d):
    return f'+{d}' if d > 0 else str(d)


def render_fatal_report(vault_slug, fatal):
    L = []
    L += [
        '---',
        f'title: Vault Lint — {vault_slug} — {TODAY_STR} — FATAL: counting inconsistency',
        f'date: {TODAY_STR}',
        'type: digest',
        'status: active',
        '---',
        '',
        f'# Vault Lint — {vault_slug} — {TODAY_STR} — FATAL: counting inconsistency',
        '',
        '## FATAL — counting inconsistency',
        '',
        '**Phase 2 drift table:**',
        '',
        '| Role | Reported | Actual | Delta |',
        '|---|---|---|---|',
    ]
    for role in sorted(fatal['delta']):
        L.append(
            f'| {role} | {fatal["reported"].get(role, 0)} | {fatal["actual"].get(role, 0)} | {_fmt_delta(fatal["delta"][role])} |'
        )
    L += [
        '',
        f'**Watermark date:** {fatal["watermark_date"]}',
        '**Activity since watermark:** zero across all categories (books: 0, articles: 0, other ingests: 0, handoffs: 0)',
        '',
        '**Three possible causes:**',
        "(a) The current lint's counting logic differs from the prior lint's — runtime non-determinism in Phase 2.",
        '(b) The vault received page edits outside logged operations (manual frontmatter changes).',
        "(c) The prior lint's counting was wrong.",
        '',
        "**Recommendation:** Run the deterministic verification script (see Phase 2 calibration notes) against the vault. Compare its output to both the prior lint's actuals and this lint's actuals. Whichever matches identifies the run with correct counting logic; the other run is the bug. If neither matches, the vault has changed outside logged operations — check `git log` for non-ingest edits since the watermark date.",
    ]
    return '\n'.join(L)


def render_report(vault_slug, findings):
    """Render the full normal (non-FATAL) lint digest."""
    c1 = findings['c1']
    c2 = findings['c2']
    c3a = findings['c3a']
    c3b = findings['c3b']
    c4 = findings['c4']
    c5 = findings['c5']
    c6 = findings['c6']
    c7 = findings['c7']
    c8 = findings['c8']
    p15 = findings['p15']
    p2 = findings['p2']
    p3 = findings['p3']
    index_md_text = findings.get('index_md_text', '')

    c8_count = (
        0
        if c8.get('skipped')
        else (
            len(c8['topic_unregistered'])
            + len(c8['topic_use_preferred'])
            + len(c8['alias_collision'])
            + len(c8['alias_shadows'])
            + (1 if c8.get('skeleton_unseeded') else 0)
            + (1 if c8.get('authority_type_wrong') else 0)
            + (1 if c8.get('authority_malformed') else 0)
        )
    )

    # Counts for summary
    ph1 = (
        len(c1['findings'])
        + len(c2['orphans'])
        + len(c3a['dangling'])
        + len(c3b['candidates'])
        + min(20, len(c4['actionable']))
        + len(c5['pairs'])
        + len(c5['alias_resolve'])
        + len(c6['stale_active'])
        + len(c6['opposing_candidates'])
        + len(c7['stubs'])
        + len(c7['todos'])
        + len(c7['open_questions'])
        + c8_count
    )
    drift_n = 0 if p2.get('skipped') else sum(1 for d in p2['delta'].values() if d != 0)
    ph3_n = sum(len(r.get('findings', [])) for r in p3)
    act = p15['activity']
    wm = p15.get('watermark_date')

    L = []

    # Frontmatter
    L += [
        '---',
        f'title: Vault Lint — {vault_slug} — {TODAY_STR}',
        f'date: {TODAY_STR}',
        'type: digest',
        'status: active',
        '---',
        '',
        f'# Vault Lint — {vault_slug} — {TODAY_STR}',
        '',
        '## Summary',
        f'- Universal checks: {ph1} findings',
        f'- Role-count drift: {"skipped (no surface in index.md)" if p2.get("skipped") else f"{drift_n} roles with non-zero delta"}',
        f'- Structural signals: {len(p2["anemic"])} anemic / {len(p2["dominant"])} dominant / {len(p2["over_assigned"])} over-assigned pages',
        f'- Vault-specific extensions: {ph3_n} findings',
        f'- Controlled vocabulary: {"skipped (no topics-authority.md)" if c8.get("skipped") else f"{c8_count} findings"}',
        f'- Activity since last lint: {act["books"]} books, {act["articles"]} articles, {act["other_ingests"]} other ingests, {act["handoffs"]} handoffs',
        '',
        '## Phase 1 — Universal checks',
        '',
    ]

    # ── Check 1
    L.append('### Check 1 — Citation-resolution sweep')
    if not c1['findings']:
        dv = (
            'depth-validated'
            if c1['depth_validated']
            else 'depth validation skipped — no depth table'
        )
        L.append(f'PASS — {c1["total"]} citations checked, all resolving ({dv})')
    else:
        nf = len(c1['findings'])
        L.append(
            f'{c1["total"]} citations checked, {c1["resolving"]} resolving, {nf} non-resolving.'
        )
        if not c1['depth_validated']:
            L.append('(depth validation skipped — no depth table)')
        for f in c1['findings']:
            if f['type'] == 'not-found':
                L.append(f'- **NOT FOUND** `{f["cited"]}` in `{f["file"]}` — {f["defect"]}')
            else:
                L.append(
                    f'- **WRONG PREFIX** `{f["cited"]}` in `{f["file"]}` — expected `{f["expected_prefix"]}`, got `{f["actual_prefix"]}`'
                )
    L.append('')

    # ── Check 2
    L.append('### Check 2 — Orphan pages')
    if not c2['orphans']:
        L.append('PASS — no orphan pages found')
    else:
        L.append(f'{len(c2["orphans"])} orphan pages (no inbound links):')
        by_dir = {}
        for p in c2['orphans']:
            by_dir.setdefault(os.path.dirname(p), []).append(p)
        for d, ps in sorted(by_dir.items()):
            L.append(f'\n**{d}/**')
            for p in ps:
                L.append(f'- `{p}`')
    L.append('')

    # ── Check 3
    L.append('### Check 3 — Concepts lacking a page')
    if not c3a['dangling'] and not c3b['candidates']:
        L.append('PASS — no dangling wikilinks or missing concept pages')
    else:
        if c3a['dangling']:
            L.append(f'**Pass A — Dangling wikilinks ({len(c3a["dangling"])} unique targets):**')
            for tgt, citers in sorted(c3a['dangling'].items()):
                sample = ', '.join(f'`{p}`' for p in citers[:5])
                overflow = f'… +{len(citers) - 5} more' if len(citers) > 5 else ''
                L.append(f'- `[[{tgt}]]` ← {sample}{overflow}')
        else:
            L.append('Pass A — No dangling wikilinks.')
        if c3b['candidates']:
            L.append('')
            L.append(
                f'**Pass B — Recurrent bold terms without a page ({len(c3b["candidates"])} candidates, canonical set: {c3b["canonical_set_size"]}):**'
            )
            for term, plist in sorted(c3b['candidates'].items(), key=lambda x: -len(x[1])):
                L.append(f'- **{term}** appears in {len(plist)} pages — candidate for a topic page')
        else:
            L.append('Pass B — No recurrent bold terms without a concept page.')
    L.append('')

    # ── Check 4
    L.append('### Check 4 — Missing cross-references')
    actionable = c4['actionable']
    if not actionable:
        L.append('PASS — no actionable missing cross-reference pairs found')
    else:
        n_show = min(20, len(actionable))
        L.append(f'Total pages scanned: {c4["total_pages"]}')
        L.append(
            f'Actionable pairs: {len(actionable)} '
            '(IDF-weighted; entity/book hubs and stopword neighbors excluded)'
        )
        L.append('')
        L.append(f'Top {n_show} by weighted score:')
        for a, b, weight, shared in actionable[:n_show]:
            L.append(
                f'- `{get_slug(a)}` ↔ `{get_slug(b)}`: score {weight} '
                f'({len(shared)} distinctive shared, sample: {shared[:3]})'
            )
        if len(actionable) > 20:
            L.append(f'*Overflow: {len(actionable) - 20} additional pairs not shown*')
    L.append('')

    # ── Check 5
    L.append('### Check 5 — Duplicate concept pages')
    if not c5['pairs']:
        L.append('PASS — no duplicate titles or overlapping aliases')
    else:
        L.append(f'{len(c5["pairs"])} candidate duplicate pairs:')
        L.append('')
        L.append('| Page A | Page B | Shared identifier(s) | Overlap type | Alias Jaccard |')
        L.append('|---|---|---|---|---|')
        for a, b, shared, otype, jaccard in c5['pairs']:
            ids_str = ', '.join(f'"{s}"' for s in shared)
            L.append(f'| `{a}` | `{b}` | {ids_str} | {otype} | {jaccard} |')
    L.append('')

    # ── Check 5 (hygiene) — aliases that should resolve to a dedicated page
    alias_resolve = c5.get('alias_resolve', [])
    if alias_resolve:
        L.append(f'**Alias should resolve to dedicated page ({len(alias_resolve)}):**')
        L.append(
            '*De-alias signal — make the alias a link to the dedicated page; not a duplicate.*'
        )
        L.append('')
        L.append('| Page | Alias | Dedicated page(s) |')
        L.append('|---|---|---|')
        for item in alias_resolve:
            ded = ', '.join(f'`{d}`' for d in item['dedicated'])
            L.append(f'| `{item["page"]}` | "{item["alias"]}" | {ded} |')
        L.append('')

    # ── Check 6
    L.append('### Check 6 — Contradictions and stale claims')
    if not c6['stale_active'] and not c6['opposing_candidates']:
        L.append('PASS — no stale-active pages; no CONTRADICTS: markers found')
    else:
        if c6['stale_active']:
            L.append(f'**Condition A — Stale-active pages ({len(c6["stale_active"])}):**')
            for item in c6['stale_active']:
                topics_str = (
                    ', '.join(item['topics'])
                    if isinstance(item['topics'], list)
                    else str(item['topics'])
                )
                L.append(
                    f'- `{item["page"]}` — last_updated: {item["last_updated"]} — topics: {topics_str}'
                )
        if c6['opposing_candidates']:
            L.append(
                f'**Condition B — Explicit CONTRADICTS: markers ({len(c6["opposing_candidates"])}):**'
            )
            for item in c6['opposing_candidates']:
                L.append(f'- `{item["page"]}`: {item["line"]}')
                if item.get('context_before'):
                    L.append(f'  ↑ `{item["context_before"]}`')
                if item.get('context_after'):
                    L.append(f'  ↓ `{item["context_after"]}`')
    L.append('')

    # ── Check 7
    L.append('### Check 7 — Data gaps fillable by web search')
    if not c7['stubs'] and not c7['todos'] and not c7['open_questions']:
        L.append('PASS — no open factual questions found')
    else:
        if c7['stubs']:
            L.append(f'**Stub pages ({len(c7["stubs"])}):**')
            for p in c7['stubs']:
                L.append(f'- `{p}`')
        if c7['todos']:
            L.append(f'**TODO markers ({len(c7["todos"])}):**')
            for item in c7['todos'][:20]:
                L.append(f'- `{item["page"]}` [{item["marker"]}]: {item["line"]}')
            if len(c7['todos']) > 20:
                L.append(f'*… and {len(c7["todos"]) - 20} more*')
        if c7['open_questions']:
            L.append(f'**Explicit gap markers — [?] / ?? / > Q: ({len(c7["open_questions"])}):**')
            for item in c7['open_questions']:
                L.append(f'- `{item["page"]}` [{item["marker"]}]: {item["line"]}')
    L.append('')

    # ── Check 8 — controlled-vocabulary resolution (topics-authority SOT)
    L.append('### Check 8 — Controlled-vocabulary resolution (topics-authority)')
    if c8.get('skipped'):
        L.append(
            'SKIPPED — no `wiki/topics-authority.md` in this vault. '
            'Add one to control the `topics:` and `aliases:` vocabularies.'
        )
    elif c8_count == 0:
        L.append(
            f'PASS — all `topics:` resolve against {c8["subject_vocab_size"]} '
            f'subject terms; no alias collisions or canonical shadows.'
        )
    else:
        if c8.get('authority_type_wrong'):
            L.append(
                f'**WARN — wrong type:** `topics-authority.md` declares '
                f'`type: {c8.get("authority_declared_type")}` — it should be '
                '`type: authority` (a governance record, exempt from topic-page checks).'
            )
            L.append('')
        if c8.get('authority_malformed'):
            L.append(
                '**WARN — malformed authority file:** `topics-authority.md` is missing '
                'a `## Subject categories` and/or `## Concept aliases` section.'
            )
            L.append('')
        if c8.get('skeleton_unseeded'):
            L.append(
                f'**WARN — unpopulated SOT ({c8["page_count"]} pages exist):** '
                '`topics-authority.md` is still an empty scaffolder skeleton. The '
                'first-ingest seed (≤10 subjects, ≤30 aliases) was skipped — seed it '
                'now, or remove the file if this vault opts out of vocabulary control.'
            )
            L.append('')
        if c8['topic_use_preferred']:
            L.append(
                f'**Use the preferred term ({len(c8["topic_use_preferred"])}) — '
                '`topics:` value is a registered use-for variant:**'
            )
            for f in c8['topic_use_preferred']:
                L.append(f'- `{f["page"]}` — `{f["value"]}` → use `{f["canonical"]}`')
        if c8['topic_unregistered']:
            L.append('')
            L.append(
                f'**Unregistered `topics:` values ({len(c8["topic_unregistered"])}) — '
                'reconcile to a preferred term or register in the SOT:**'
            )
            for f in c8['topic_unregistered']:
                sug = (
                    f' → nearest: `{f["suggestion"]}`'
                    if f['suggestion']
                    else ' (no close match — new category?)'
                )
                L.append(f'- `{f["page"]}` — `{f["value"]}`{sug}')
        if c8['alias_collision']:
            L.append('')
            L.append(
                f'**Alias collisions ({len(c8["alias_collision"])}) — '
                'one alias claimed by multiple pages (breaks uniqueness):**'
            )
            for f in c8['alias_collision']:
                pgs = ', '.join(f'`{p}`' for p in f['pages'])
                L.append(f'- "{f["alias"]}" ← {pgs}')
        if c8['alias_shadows']:
            L.append('')
            L.append(
                f'**Alias shadows a canonical ({len(c8["alias_shadows"])}) — '
                "alias equals another page's title/slug:**"
            )
            for f in c8['alias_shadows']:
                L.append(f'- `{f["page"]}` alias "{f["alias"]}" shadows `{f["canonical_page"]}`')
    L.append('')

    # ── Phase 1.5
    L.append('## Phase 1.5 — Activity since last lint')
    if wm is None:
        L.append('no prior lint — full history out of scope')
    else:
        ht = act.get('handoff_types', {})
        ht_str = ', '.join(f'{k}: {v}' for k, v in ht.items()) if ht else 'none'
        L += [
            f'Watermark: {wm}',
            f'- Books completed: {act["books"]}',
            f'- Articles ingested: {act["articles"]}',
            f'- Other ingest events: {act["other_ingests"]}',
            f'- Handoffs filed: {act["handoffs"]} ({ht_str})',
        ]
    L.append('')

    # ── Phase 2
    L += [
        '## Phase 2 — Role-count drift',
        '',
        f'Scanned: {p2["total_scanned"]} files under wiki/topics/',
        '',
    ]
    if p2.get('skipped'):
        L.append(
            'No role-page-counts surface declared in wiki/index.md. '
            'Phase 2 (drift detection) skipped. '
            'To enable drift tracking, add either a markdown table or a bulleted list '
            'with the format `- [Role — Name](path) — N pages; description` under a heading '
            "matching 'Role' or 'Roles' or 'Role Maps' in index.md."
        )
        L.append('')
    else:
        L += [
            '| Role | Reported | Actual | Delta |',
            '|---|---|---|---|',
        ]
        for role in p2['actual']:
            r = p2['reported'].get(role, 0)
            a = p2['actual'][role]
            d = p2['delta'][role]
            L.append(f'| {role} | {r} | {a} | {_fmt_delta(d)} |')
        L.append('')

    signals = []
    if p2['anemic']:
        signals.append(f'**Anemic roles** (< 3 pages): {", ".join(p2["anemic"])}')
    if p2['dominant']:
        signals.append(f'**Dominant roles** (> 2× median): {", ".join(p2["dominant"])}')
    if p2['over_assigned']:
        oa_strs = [f'`{pg}` ({len(roles)} roles)' for pg, roles in p2['over_assigned'][:10]]
        signals.append(f'**Over-assigned pages** (≥4 roles): {"; ".join(oa_strs)}')

    if signals:
        L.append('**Structural signals:**')
        for s in signals:
            L.append(f'- {s}')
    else:
        L.append('No structural signals.')
    L.append('')

    if p2['missing_roles']:
        n = len(p2['missing_roles'])
        L.append(
            f'**Frontmatter-completeness warnings** ({n} pages missing or empty `roles:` field):'
        )
        for pg in p2['missing_roles'][:20]:
            L.append(f'- `{pg}`')
        if n > 20:
            L.append(f'*… and {n - 20} more*')
        L.append('')

    if p2['unknown_roles']:
        L.append('**Unknown roles** (in frontmatter but not in canonical list):')
        for role, pgs in p2['unknown_roles'].items():
            L.append(f'- `{role}`: {len(pgs)} pages')
        L.append('')

    # ── Phase 3
    L.append('## Phase 3 — Vault-specific extensions')
    L.append('')
    if not p3:
        L.append('No vault-specific extensions declared.')
    else:
        for ext in p3:
            L.append(f'### {ext["description"]}')
            if 'error' in ext:
                L.append(f'**{ext["error"]}**')
            elif not ext['findings']:
                L.append('PASS — no findings.')
            else:
                _render_ext_findings(L, ext['id'], ext['findings'])
            L.append('')

    # ── Patch block
    if drift_n > 0:
        _render_patch_block(L, p2, index_md_text)

    return '\n'.join(L)


def _render_ext_findings(L, cid, findings):
    if cid == 'project-entity-recent-handoff':
        malformed_block = None
        for f in findings:
            if 'info' in f:
                L.append(f['info'])
            elif 'malformed' in f:
                malformed_block = f['malformed']
            elif 'project' in f:
                days = f['days_since'] if f['days_since'] is not None else '—'
                L.append(
                    f'- **{f["project"]}**: {f["handoffs_last_90d"]} handoffs in last 90 days'
                    f' | most recent: {f["most_recent"]} | days since: {days}'
                    f' | **{f["status"].upper()}**'
                )
        if malformed_block:
            L.append('')
            L.append('**Malformed handoff filenames:**')
            for fname, reason in malformed_block:
                L.append(f'- `{fname}` — {reason}')

    elif cid == 'cross-vault-reference-format':
        for f in findings:
            if 'file' in f:
                L.append(f'- `{f["file"]}` line {f["line"]}: {f["violation"]}')
                L.append(f'  `{f["text"]}`')

    elif cid == 'calendar-staleness-sweep':
        for f in findings:
            if 'page' in f:
                L.append(
                    f'- `{f["page"]}` — volatility: {f["volatility"]} — next_review: {f["next_review"]} — status: {f["status"]}'
                )

    elif cid == 'alias-bilingual-coverage':
        for f in findings:
            if 'page' in f:
                L.append(f'- `{f["page"]}` — title: "{f["title"]}" — aliases: {f["aliases"]}')

    elif cid == 'english-first-naming':
        for f in findings:
            if 'page' in f:
                L.append(f'- `{f["page"]}` — title: "{f["title"]}" — {f["reason"]}')

    elif cid == 'book-entity-backlink':
        for f in findings:
            if f.get('severity') == 'warn':
                L.append(f'- **WARN** — {f["reason"]}')
            elif 'page' in f:
                L.append(f'- `{f["page"]}` — {f["reason"]}')

    elif cid == 'merge-tombstone-hygiene':
        for f in findings:
            sev = f.get('severity', 'info').upper()
            L.append(f'- **{sev}** `{f["page"]}` — {f["reason"]}')

    else:
        for f in findings:
            L.append(f'- {f}')


def _render_patch_block(L, p2, index_md_text):
    """Append READY-TO-APPLY PATCH section. Mirrors exact index.md line format."""
    if not index_md_text:
        L.append('## READY-TO-APPLY PATCH — wiki/index.md role table')
        L.append('index.md not available — patch cannot be auto-generated.')
        return

    fmt_type = p2['fmt_type']
    sec_start, sec_end = p2['fmt_lines']
    index_lines = index_md_text.split('\n')

    if fmt_type == 'unknown':
        L.append('## READY-TO-APPLY PATCH — wiki/index.md role table')
        L.append(
            'Could not detect role-page-counts format in index.md — patch cannot be auto-generated.'
        )
        return

    if fmt_type == 'list':
        L.append(
            f'## READY-TO-APPLY PATCH — wiki/index.md role list (lines {sec_start + 1}–{sec_end})'
        )
        L.append('')
        L.append('Replace the Role Maps of Content section in `wiki/index.md`:')
        L.append('')
        L.append('```markdown')
        for ln in index_lines[sec_start:sec_end]:
            # Match list item: - [Role — Name](topics/role-<id>.md) — N pages; rest
            m = re.match(
                r'^(-\s+\[.*?\]\(topics/role-([\w\-]+)\.md\).*?—\s+)(\d+)(\s+pages?.*)', ln
            )
            if m:
                role_id = m.group(2)
                actual = p2['actual'].get(role_id)
                if actual is not None:
                    L.append(f'{m.group(1)}{actual}{m.group(4)}')
                    continue
            L.append(ln)
        L.append('```')

    elif fmt_type == 'table':
        L.append(
            f'## READY-TO-APPLY PATCH — wiki/index.md role table (lines {sec_start + 1}–{sec_end})'
        )
        L.append('')
        L.append('Replace the role table in `wiki/index.md`:')
        L.append('')
        L.append('```markdown')
        for ln in index_lines[sec_start:sec_end]:
            if '|' not in ln or re.match(r'^[\|\s\-:]+$', ln):
                L.append(ln)
                continue
            updated = ln
            for role_id, actual in p2['actual'].items():
                role_disp = role_id.replace('-', ' ')
                if role_disp.lower() in ln.lower() or role_id in ln.lower():
                    old_count = str(p2['reported'].get(role_id, -999))
                    updated = re.sub(r'\b' + re.escape(old_count) + r'\b', str(actual), ln, count=1)
                    break
            L.append(updated)
        L.append('```')


# ══════════════════════════════════════════════════════════════════════════════
# §17 FILE I/O
# ══════════════════════════════════════════════════════════════════════════════


def write_report(report_path, text):
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(text)


def append_log_entry(log_path, vault_slug, ph1_count, drift_count):
    """Append lint watermark entry to log.md."""
    report_name = f'digests/lint-{TODAY_STR}.md'
    entry = (
        f'\n## [{TODAY_STR}] lint | {vault_slug} | '
        f'{ph1_count} total findings; {drift_count} drift roles; '
        f'report: {report_name}\n'
    )
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(entry)


def clear_pending_marker(log_path, vault_slug):
    """Remove 'lint | pending | <vault-slug>' marker lines from log.md."""
    try:
        with open(log_path, encoding='utf-8') as f:
            text = f.read()
        pattern = re.compile(
            r'\n?##\s+\[[\d\-]+\]\s+lint\s+\|\s+pending\s+\|\s+'
            + re.escape(vault_slug)
            + r'[^\n]*',
            re.MULTILINE,
        )
        new_text, n = pattern.subn('', text)
        if n > 0:
            with open(log_path, 'w', encoding='utf-8') as f:
                f.write(new_text)
    except Exception as e:
        print(f'WARNING: could not clear pending marker: {e}', file=sys.stderr)


# ══════════════════════════════════════════════════════════════════════════════
# §18 MAIN
# ══════════════════════════════════════════════════════════════════════════════


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 lint.py <vault-path>', file=sys.stderr)
        return 2

    vault_path = os.path.abspath(sys.argv[1])

    if not os.path.isdir(vault_path):
        print(f'ERROR: vault path does not exist: {vault_path}', file=sys.stderr)
        return 2

    claude_md_path = os.path.join(vault_path, 'CLAUDE.md')
    if not os.path.isfile(claude_md_path):
        print(f'ERROR: CLAUDE.md not found at {claude_md_path}', file=sys.stderr)
        return 2

    # ── Step 0: Load config ────────────────────────────────────
    try:
        with open(claude_md_path, encoding='utf-8') as f:
            claude_md_text = f.read()
    except Exception as e:
        print(f'ERROR: could not read CLAUDE.md: {e}', file=sys.stderr)
        return 2

    config = parse_claude_config(claude_md_text)
    vault_slug = config['vault_slug']
    if not vault_slug:
        print('ERROR: vault_slug not found in VAULT-LINT-EXTENSIONS block', file=sys.stderr)
        return 2

    canonical_roles = config['canonical_roles']
    if not canonical_roles:
        print('WARNING: no canonical roles found in CLAUDE.md', file=sys.stderr)

    index_md_path = os.path.join(vault_path, 'wiki', 'index.md')
    index_md_text = ''
    if os.path.isfile(index_md_path):
        with open(index_md_path, encoding='utf-8') as f:
            index_md_text = f.read()
    else:
        print('WARNING: wiki/index.md not found', file=sys.stderr)

    log_md_path = os.path.join(vault_path, 'wiki', 'log.md')
    log_md_text = ''
    if os.path.isfile(log_md_path):
        with open(log_md_path, encoding='utf-8') as f:
            log_md_text = f.read()
    else:
        print('WARNING: wiki/log.md not found', file=sys.stderr)

    print(f'[vault-lint] vault: {vault_slug} | date: {TODAY_STR}')
    print(f'[vault-lint] canonical roles ({len(canonical_roles)}): {canonical_roles}')

    watermark_date = find_watermark(log_md_text, vault_slug)
    print(f'[vault-lint] watermark: {watermark_date or "none (first lint)"}')

    # ── Load all live pages ────────────────────────────────────
    print('[vault-lint] loading live pages...')
    pages = load_live_pages(vault_path)
    slug_index = build_slug_index(pages)
    print(f'[vault-lint] {len(pages)} live pages, {len(slug_index)} unique slugs')

    # ── Phase 1 ───────────────────────────────────────────────
    print('[vault-lint] Phase 1 — universal checks')

    c1 = check_1_citations(vault_path, pages, config['depth_table'])
    print(f'  Check 1 (citations):    {c1["total"]} total, {len(c1["findings"])} issues')

    c2 = check_2_orphans(vault_path, pages, slug_index)
    print(f'  Check 2 (orphans):      {len(c2["orphans"])} of {c2["total"]} pages')

    c3a = check_3_pass_a(vault_path, pages, slug_index)
    print(f'  Check 3a (dangling):    {len(c3a["dangling"])} unique dangling targets')

    c3b = check_3_pass_b(pages, slug_index)
    print(f'  Check 3b (bold terms):  {len(c3b["candidates"])} candidate missing pages')

    c4 = check_4_cross_refs(vault_path, pages)
    print(f'  Check 4 (cross-refs):   {len(c4["actionable"])} actionable pairs (IDF-weighted)')

    c5 = check_5_duplicates(pages)
    print(
        f'  Check 5 (duplicates):   {len(c5["pairs"])} pairs, '
        f'{len(c5["alias_resolve"])} alias-resolve'
    )

    c6 = check_6_stale_claims(pages)
    print(
        f'  Check 6 (stale):        {len(c6["stale_active"])} stale-active, {len(c6["opposing_candidates"])} CONTRADICTS: markers'
    )

    c7 = check_7_data_gaps(pages)
    print(
        f'  Check 7 (data gaps):    {len(c7["stubs"])} stubs, {len(c7["todos"])} TODOs, {len(c7["open_questions"])} questions'
    )

    authority = parse_topics_authority(vault_path)
    c8 = check_8_vocabulary(pages, authority)
    if c8.get('skipped'):
        print('  Check 8 (vocabulary):   skipped — no wiki/topics-authority.md')
    else:
        print(
            f'  Check 8 (vocabulary):   {len(c8["topic_unregistered"])} unregistered, '
            f'{len(c8["topic_use_preferred"])} use-preferred, '
            f'{len(c8["alias_collision"])} alias collisions, '
            f'{len(c8["alias_shadows"])} shadows'
            f'{"; SOT skeleton unseeded" if c8.get("skeleton_unseeded") else ""}'
        )

    # ── Phase 1.5 ─────────────────────────────────────────────
    print('[vault-lint] Phase 1.5 — activity since last lint')
    activity = count_activity_since(log_md_text, vault_slug, watermark_date)
    p15 = {
        'watermark_date': watermark_date.isoformat() if watermark_date else None,
        'activity': activity,
    }

    # ── Phase 2 ───────────────────────────────────────────────
    print('[vault-lint] Phase 2 — role-count drift')
    p2 = phase_2_role_drift(vault_path, canonical_roles, index_md_text)
    if p2.get('skipped'):
        drift_roles = []
        print('  Phase 2 skipped — no role-counts surface in index.md')
    else:
        drift_roles = [r for r, d in p2['delta'].items() if d != 0]
        print(f'  {len(drift_roles)} roles with drift: {drift_roles}')

    # ── Phase 2.5 ─────────────────────────────────────────────
    print('[vault-lint] Phase 2.5 — regression guard')
    fatal = phase_2_5_guard(activity, p2, watermark_date)

    if fatal:
        print('[vault-lint] FATAL: counting inconsistency — aborting (no log entry written)')
        report_path = os.path.join(vault_path, 'wiki', 'digests', f'lint-{TODAY_STR}.md')
        write_report(report_path, render_fatal_report(vault_slug, fatal))
        print(f'FATAL | report: {report_path}')
        print('No log entry written. Investigate counting discrepancy before proceeding.')
        return 1

    # ── Phase 3 ───────────────────────────────────────────────
    print('[vault-lint] Phase 3 — vault-specific extensions')
    p3 = phase_3_extensions(vault_path, config['extension_checks'], config)

    # ── Render and write report ────────────────────────────────
    all_findings = dict(
        c1=c1,
        c2=c2,
        c3a=c3a,
        c3b=c3b,
        c4=c4,
        c5=c5,
        c6=c6,
        c7=c7,
        c8=c8,
        p15=p15,
        p2=p2,
        p3=p3,
        index_md_text=index_md_text,
    )
    report_text = render_report(vault_slug, all_findings)
    report_path = os.path.join(vault_path, 'wiki', 'digests', f'lint-{TODAY_STR}.md')
    write_report(report_path, report_text)
    print(f'[vault-lint] report written: {report_path}')

    # ── Log entry + pending marker cleanup ─────────────────────
    c8_total = (
        0
        if c8.get('skipped')
        else (
            len(c8['topic_unregistered'])
            + len(c8['topic_use_preferred'])
            + len(c8['alias_collision'])
            + len(c8['alias_shadows'])
            + (1 if c8.get('skeleton_unseeded') else 0)
            + (1 if c8.get('authority_type_wrong') else 0)
            + (1 if c8.get('authority_malformed') else 0)
        )
    )
    ph1_total = (
        len(c1['findings'])
        + len(c2['orphans'])
        + len(c3a['dangling'])
        + len(c3b['candidates'])
        + min(20, len(c4['actionable']))
        + len(c5['pairs'])
        + len(c5['alias_resolve'])
        + len(c6['stale_active'])
        + len(c6['opposing_candidates'])
        + len(c7['stubs'])
        + len(c7['todos'])
        + len(c7['open_questions'])
        + c8_total
    )
    drift_count = len(drift_roles)
    append_log_entry(log_md_path, vault_slug, ph1_total, drift_count)
    clear_pending_marker(log_md_path, vault_slug)
    print('[vault-lint] log entry appended; pending marker cleared (if any)')

    # ── Summary stdout ─────────────────────────────────────────
    quiescent = sum(
        1
        for r in p3
        if r.get('id') == 'project-entity-recent-handoff'
        for f in r.get('findings', [])
        if isinstance(f, dict) and f.get('status') == 'quiescent'
    )
    print('')
    print('─' * 60)
    print(f'Lint complete: {vault_slug} {TODAY_STR}')
    print(f'  Phase 1 findings:    {ph1_total}')
    print(f'  Role drift:          {drift_count} roles')
    print(
        f'  Structural signals:  {len(p2["anemic"])} anemic / {len(p2["dominant"])} dominant / {len(p2["over_assigned"])} over-assigned'
    )
    print(f'  Phase 3 findings:    {sum(len(r.get("findings", [])) for r in p3)}')
    print(f'  Quiescent projects:  {quiescent}')
    print('  FATAL:               no')
    print(f'  Report:              {report_path}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
