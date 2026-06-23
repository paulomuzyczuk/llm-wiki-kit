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
