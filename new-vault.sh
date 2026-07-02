#!/usr/bin/env bash
# new-vault.sh — scaffold a new LLM-Wiki vault from CLAUDE.template.md + a subs file.
#
# Does the mechanical 80% of instantiation:
#   - validates the subs file covers exactly the template's tokens
#   - strips the instantiation header, substitutes every {{TOKEN}}, writes <dest>/CLAUDE.md
#   - creates the folder tree and seeds empty index/log/gaps/quality-debt/_provenance
#
# It does NOT make the judgment calls the template leaves to a human: the roles
# table, the notation-block / vault-specific-extensions inclusion decisions, and
# the VAULT-LINT-EXTENSIONS contents stay at their template defaults for you to
# fill in. Run check-conformance.py afterwards to verify the result.
#
# The subs file is the SAME format check-conformance.py consumes, so one file
# both instantiates a vault and later audits it for drift.
#
# Usage:
#   ./new-vault.sh --subs <subs.json> --dest <vault-dir> [--template <path>] [--force]
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
template="$here/CLAUDE.template.md"
subs=""
dest=""
force=0

while [ $# -gt 0 ]; do
  case "$1" in
    --subs)
      [ $# -ge 2 ] || { echo "ERROR: --subs needs a value" >&2; exit 2; }
      subs="$2"; shift 2 ;;
    --dest)
      [ $# -ge 2 ] || { echo "ERROR: --dest needs a value" >&2; exit 2; }
      dest="$2"; shift 2 ;;
    --template)
      [ $# -ge 2 ] || { echo "ERROR: --template needs a value" >&2; exit 2; }
      template="$2"; shift 2 ;;
    --force) force=1; shift ;;
    # Print the header comment block (everything between the shebang and the
    # first non-comment line) so editing the header can't garble the help text.
    -h|--help) awk 'NR == 1 { next } /^#/ { print; next } { exit }' "$0"; exit 0 ;;
    *) echo "ERROR: unknown argument: $1" >&2; exit 2 ;;
  esac
done

[ -n "$subs" ]     || { echo "ERROR: --subs is required" >&2; exit 2; }
[ -n "$dest" ]     || { echo "ERROR: --dest is required" >&2; exit 2; }
[ -f "$subs" ]     || { echo "ERROR: subs file not found: $subs" >&2; exit 2; }
[ -f "$template" ] || { echo "ERROR: template not found: $template" >&2; exit 2; }

if [ -e "$dest/CLAUDE.md" ] && [ "$force" -ne 1 ]; then
  echo "ERROR: $dest/CLAUDE.md already exists (use --force to overwrite)" >&2
  exit 2
fi

# --- Validate tokens + substitute, then write CLAUDE.md (python3 does the text work).
#     Header-strip + token-discovery match check-conformance.py so a fresh scaffold
#     diffs clean against the template. Nothing is created until validation passes.
python3 - "$template" "$subs" "$dest/CLAUDE.md" <<'PY'
import json, os, re, sys
template_path, subs_path, out_path = sys.argv[1:4]

raw = open(template_path, encoding="utf-8").read()
# Cut the leading template header (version comment + instantiation-header HTML
# comment block) by jumping to the contract's first top-level "# " heading.
# The header body contains literal "-->" strings (documented marker examples),
# so it can't be parsed by comment delimiters — index("-->") would stop at the
# first embedded example and leak ~190 header lines into CLAUDE.md. This matches
# check-conformance.py's _strip_header so a fresh scaffold diffs clean.
m = re.search(r"(?m)^# ", raw)
if m is None:
    print("ERROR: template has no top-level '# ' heading", file=sys.stderr)
    sys.exit(2)
raw = raw[m.start():]

discovered = set(re.findall(r"\{\{([^}]+)\}\}", raw))
subs = json.load(open(subs_path, encoding="utf-8"))
real = {k: v for k, v in subs.items() if not k.startswith("_")}  # _-prefixed keys = notes

errors = []
for tok in sorted(discovered - set(real)):
    errors.append(f"token missing from subs: {tok}")
for tok in sorted(set(real) - discovered):
    errors.append(f"token in subs but not in template body: {tok}")
if errors:
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)
    sys.exit(2)

for tok, val in real.items():
    if not isinstance(val, str):
        print(f"ERROR: subs value for {tok} is not a string", file=sys.stderr)
        sys.exit(2)
    raw = raw.replace("{{" + tok + "}}", val)

os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
open(out_path, "w", encoding="utf-8").write(raw)
print(f"wrote {out_path}")
PY

# --- The two tokens that name folders in the tree.
exec_handoff="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["EXEC_HANDOFF"])' "$subs")"
entity_subject="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["ENTITY_SUBJECT"])' "$subs")"

# --- Folder tree (per the template's FOLDER STRUCTURE TO CREATE block).
mkdir -p \
  "$dest/raw-input/_pending" \
  "$dest/raw-input/articles" \
  "$dest/raw-input/books" \
  "$dest/raw-input/${exec_handoff}s" \
  "$dest/raw-input/notes" \
  "$dest/raw-input/planning-handoffs" \
  "$dest/wiki/handoffs/${exec_handoff}s" \
  "$dest/wiki/handoffs/planning-handoffs" \
  "$dest/wiki/entities/${entity_subject}" \
  "$dest/wiki/entities/books" \
  "$dest/wiki/topics" \
  "$dest/wiki/digests" \
  "$dest/claude"

# --- Seed files (only if absent; never clobber).
seed() { [ -e "$1" ] || printf '%s\n' "$2" > "$1"; }
seed "$dest/wiki/index.md"         "# Index"
seed "$dest/wiki/log.md"           "# Log"
seed "$dest/wiki/gaps.md"          $'# Gaps\n\n## \xc2\xa71 \xe2\x80\x94 Knowledge gaps found in ingested content\n\n## \xc2\xa72 \xe2\x80\x94 Books not yet in the vault'
seed "$dest/wiki/quality-debt.md"  "# Quality debt"
seed "$dest/claude/_provenance.md" $'# Provenance \xe2\x80\x94 audit trail for vault-specific CLAUDE.md amendments'

# --- topics-authority.md: controlled-vocabulary SOT skeleton.
#     Created unpopulated; the FIRST ingest (book-planner Phase 0 or the first
#     article/notes ingest) seeds it with up to 10 subjects and 30 aliases.
if [ ! -e "$dest/wiki/topics-authority.md" ]; then
  domain="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["DOMAIN"])' "$subs")"
  today="$(date +%Y-%m-%d)"
  cat > "$dest/wiki/topics-authority.md" <<EOF
---
title: Topics Authority — ${domain}
type: authority
status: stub
date: ${today}
last_updated: ${today}
---

# Topics Authority — ${domain}

Controlled-vocabulary source of truth for this vault — a lightweight thesaurus
(a preferred term plus its use-for variants). \`/vault-lint\` Check 8 resolves
every \`topics:\` value against **Subjects** and validates \`aliases:\` against
**Concepts**. Report-only.

<!-- SEED-ME: unpopulated skeleton. The FIRST ingest into this vault — book-planner
     Phase 0 if a book is added first, otherwise the first article/notes ingest —
     seeds this file with up to 10 subject categories and up to 30 aliases drawn
     from that first content and the domain. The 10/30 caps apply to the INITIAL
     SEED ONLY: afterwards, resolve every new term against this file before minting
     it, grow the vocabulary as the vault grows, and let /vault-lint reconcile any
     scatter. Set status: active and delete this comment once seeded. -->

## Subject categories

Governs \`topics:\`. A value must be a preferred term below (or a reserved tag).
List variant spellings/synonyms that should resolve to a preferred term in its
Use-for column.

| Preferred | Use-for (variants that resolve to it) |
|---|---|

## Concept aliases

Governs \`aliases:\` / page identity — each topic page is a preferred concept and
its frontmatter \`aliases:\` are its use-for variants. No alias may belong to two
pages or shadow another page's canonical title/slug.

| Preferred (page) | Use-for (aliases) |
|---|---|

## Reserved non-subject tags

Tags legal in the topics field but not subject categories: \`stub\`.
EOF
  echo "wrote $dest/wiki/topics-authority.md (controlled-vocabulary skeleton)"
fi

echo
echo "Scaffolded vault at: $dest"
echo
echo "Next steps (the judgment calls the scaffolder leaves to you):"
echo "  1. Replace the example roles table under '**Roles for this vault:**' with this vault's roles."
echo "  2. Decide the Notation-hygiene block (keep / strengthen / remove both marker pairs) per the template's inclusion rule."
echo "  3. Decide the Vault-specific-extensions block (fill or remove)."
echo "  4. Fill the VAULT-LINT-EXTENSIONS block (freshness_model, extension_checks)."
echo "  5. If this vault has no execution/thinking split, remove the '${exec_handoff}s' folders and prune the exec-handoff references."
echo "  6. Verify: python3 check-conformance/check-conformance.py \\"
echo "       --vault \"$dest/CLAUDE.md\" --template \"$template\" --subs \"$subs\""
