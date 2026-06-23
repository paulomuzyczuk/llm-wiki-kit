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
    --subs) subs="$2"; shift 2 ;;
    --dest) dest="$2"; shift 2 ;;
    --template) template="$2"; shift 2 ;;
    --force) force=1; shift ;;
    -h|--help) sed -n '2,20p' "$0"; exit 0 ;;
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
