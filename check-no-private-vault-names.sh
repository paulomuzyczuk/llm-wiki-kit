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
# The denylist is NOT stored in this repo (that would itself leak the names).
# Supply it out-of-band via either:
#   * env var  LWK_PRIVATE_DENYLIST  — a pipe-separated ERE of slugs, e.g.
#         export LWK_PRIVATE_DENYLIST='foo-vault|bar-vault'
#     (in CI, set this as a repository/organization secret), or
#   * file     .private-denylist     — one slug per line (blank lines and lines
#     starting with '#' are ignored). This path is git-ignored.
# If neither is present, the guard cannot run and exits 0 with a warning, so a
# fresh clone without the secret does not fail spuriously.
set -euo pipefail

cd "$(dirname "$0")"

DENYFILE="${LWK_PRIVATE_DENYLIST_FILE:-.private-denylist}"

if [ -n "${LWK_PRIVATE_DENYLIST:-}" ]; then
  DENY="$LWK_PRIVATE_DENYLIST"
elif [ -f "$DENYFILE" ]; then
  # Join non-comment, non-blank lines into a pipe-separated ERE.
  DENY="$(grep -vE '^[[:space:]]*(#|$)' "$DENYFILE" | paste -sd '|' -)"
else
  echo "::warning::privacy guard skipped — no denylist provided."
  echo "  Set LWK_PRIVATE_DENYLIST (pipe-separated slugs) or create $DENYFILE (one slug per line)."
  echo "  See the header of $(basename "$0") for details."
  exit 0
fi

if [ -z "$DENY" ]; then
  echo "::warning::privacy guard skipped — denylist is empty."
  exit 0
fi

# Scan tracked files only (never untracked WIP or .git). Skip binary (-I).
hits="$(git grep -nIE "$DENY" -- . 2>/dev/null || true)"

if [ -n "$hits" ]; then
  echo "::error::private vault name(s) found in tracked files — this public repo may name only 'software-craft'"
  echo "$hits"
  echo
  echo "Scrub the name(s) above before pushing (the denylist is set out-of-band; see the guard's header)."
  exit 1
fi

echo "OK: no denylisted private vault names in tracked files (only 'software-craft' is public)."
