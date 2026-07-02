#!/usr/bin/env bash
# regenerate-clones.sh — regenerate the project-context upload clones from
# canonical SKILL.md files. The clones are DERIVED ARTIFACTS — never edit
# them directly.
#
# Usage:
#   ./regenerate-clones.sh                 Regenerate every skill's clone.
#   ./regenerate-clones.sh <skill> [...]   Regenerate only the named skills.
set -euo pipefail
cd "$(dirname "$0")"

regenerate() {
  local skill="$1"
  [ -f "$skill/SKILL.md" ] || { echo "error: no such skill: $skill (no $skill/SKILL.md)" >&2; return 1; }
  {
    echo "> GENERATED COPY — do not edit. Source: ${skill}/SKILL.md. Regenerate: ./regenerate-clones.sh"
    echo ""
    cat "$skill/SKILL.md"
  } > "$skill/${skill}-skill.md"
  echo "regenerated: $skill/${skill}-skill.md"

  # A deployed clone that is a regular file (not a symlink back here) goes
  # stale silently the moment SKILL.md changes — warn so it gets re-linked.
  local deploy="$HOME/.claude/skills/${skill}/${skill}-skill.md"
  if [ -e "$deploy" ] && [ ! -L "$deploy" ]; then
    if ! diff -q "$skill/${skill}-skill.md" "$deploy" > /dev/null 2>&1; then
      echo "WARNING: $deploy is a regular file and differs from the regenerated clone — deployment is stale. Replace it with a symlink to $(pwd)/$skill/${skill}-skill.md"
    fi
  fi
}

if [ $# -gt 0 ]; then
  for skill in "$@"; do
    regenerate "${skill%/}"
  done
else
  # Discover skills the same way install.sh does: any top-level directory
  # containing a SKILL.md.
  found=0
  for d in */; do
    if [ -f "${d}SKILL.md" ]; then
      regenerate "${d%/}"
      found=1
    fi
  done
  [ "$found" -eq 1 ] || { echo "error: no skills found (looked for */SKILL.md)" >&2; exit 1; }
fi
