#!/usr/bin/env bash
# Regenerates the project-context upload clone from canonical SKILL.md.
# The clone is a DERIVED ARTIFACT — never edit it directly.
set -euo pipefail
cd "$(dirname "$0")"
skill="$(basename "$PWD")"
{
  echo "> GENERATED COPY — do not edit. Source: SKILL.md. Regenerate: ./regenerate-clones.sh"
  echo ""
  cat SKILL.md
} > "${skill}-skill.md"
echo "regenerated: ${skill}-skill.md"

deploy="$HOME/.claude/skills/${skill}/${skill}-skill.md"
if [ -e "$deploy" ] && [ ! -L "$deploy" ]; then
  if ! diff -q "${skill}-skill.md" "$deploy" > /dev/null 2>&1; then
    echo "WARNING: $deploy is a regular file and differs from the regenerated clone — deployment is stale. Replace it with a symlink to $(pwd)/${skill}-skill.md"
  fi
fi
