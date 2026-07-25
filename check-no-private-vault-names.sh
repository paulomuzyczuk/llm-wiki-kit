#!/usr/bin/env bash
#
# Privacy guard: this is a PUBLIC repo. The only real vault it may name is the
# populated example, `software-craft`. Private fleet vaults must never be named
# in a tracked file — not in docs, examples, tests, schema overlays, or comments.
#
# This scans tracked files (working tree) for any denylisted private vault slug
# and fails if one is found. Run locally with `./check-no-private-vault-names.sh`;
# CI runs it on every push (see .github/workflows/ci.yml).
#
# To retire a name into the public repo deliberately (rare), remove it from DENY.
# To protect a new private vault, add its slug to DENY.
set -euo pipefail

# Pipe-separated ERE of private vault slugs that must not appear publicly.
DENY='example-domain-1|example-domain-2|example-domain-3|example-domain-4|example-domain-5'

# Scan tracked files only (never untracked WIP or .git). Skip binary (-I) and
# this guard itself — it necessarily spells the slugs out in DENY above.
hits="$(git grep -nIE "$DENY" -- . ":(exclude)$(basename "$0")" 2>/dev/null || true)"

if [ -n "$hits" ]; then
  echo "::error::private vault name(s) found in tracked files — this public repo may name only 'software-craft'"
  echo "$hits"
  echo
  echo "Scrub the name(s) above (or, to publish one deliberately, edit DENY in $(basename "$0"))."
  exit 1
fi

echo "OK: no private vault names in tracked files (only 'software-craft' is public)."
