#!/usr/bin/env bash
#
# install.sh — link (or unlink) the LLM-Wiki Kit skills into your Claude Code
# skills directory. There is nothing to compile: the skills are Markdown read
# by Claude Code, so "installing" just means symlinking each skill folder into
# ~/.claude/skills/ so Claude Code can discover it.
#
# Usage:
#   ./install.sh                 Link every skill into the skills directory.
#   ./install.sh --uninstall     Remove only the symlinks that point back here.
#   ./install.sh --dir <path>    Use <path> instead of ~/.claude/skills.
#   ./install.sh --copy          Copy skill folders instead of symlinking.
#   ./install.sh --help          Show this help.
#
# Environment:
#   CLAUDE_SKILLS_DIR            Default target dir if --dir is not given.
#
# Re-running install is safe: existing links are replaced, not duplicated.

set -euo pipefail

# Absolute path to this repo (the directory containing this script).
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SKILLS_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
MODE="install"
USE_COPY=0

usage() {
  sed -n '3,21p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
}

while [ $# -gt 0 ]; do
  case "$1" in
    --uninstall) MODE="uninstall" ;;
    --copy) USE_COPY=1 ;;
    --dir)
      [ $# -ge 2 ] || { echo "error: --dir needs a path" >&2; exit 2; }
      SKILLS_DIR="$2"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "error: unknown argument: $1" >&2; usage >&2; exit 2 ;;
  esac
  shift
done

# Discover skills: any top-level directory in the repo that contains a SKILL.md.
discover_skills() {
  local d
  for d in "$REPO_DIR"/*/; do
    [ -f "${d}SKILL.md" ] && basename "$d"
  done
}

# Portable array fill (works on bash 3.2, the macOS default — no `mapfile`).
SKILLS=()
while IFS= read -r line; do
  [ -n "$line" ] && SKILLS+=("$line")
done < <(discover_skills)
if [ "${#SKILLS[@]}" -eq 0 ]; then
  echo "error: no skills found under $REPO_DIR (looked for */SKILL.md)" >&2
  exit 1
fi

if [ "$MODE" = "uninstall" ]; then
  removed=0
  for skill in "${SKILLS[@]}"; do
    target="$SKILLS_DIR/$skill"
    # Only remove a symlink that resolves into this repo — never touch a real
    # directory or a link the user pointed somewhere else.
    if [ -L "$target" ]; then
      dest="$(cd "$(dirname "$target")" && readlink "$target")"
      case "$dest" in
        "$REPO_DIR"/*|"$REPO_DIR")
          rm "$target"; echo "unlinked  $target"; removed=$((removed + 1)) ;;
        *)
          echo "skipped   $target (links elsewhere: $dest)" ;;
      esac
    elif [ -e "$target" ]; then
      echo "skipped   $target (not a symlink — left in place)"
    fi
  done
  echo "Done. Removed $removed link(s) from $SKILLS_DIR."
  exit 0
fi

# install
mkdir -p "$SKILLS_DIR"
for skill in "${SKILLS[@]}"; do
  src="$REPO_DIR/$skill"
  target="$SKILLS_DIR/$skill"
  if [ -e "$target" ] && [ ! -L "$target" ]; then
    echo "error: $target exists and is not a symlink — refusing to overwrite" >&2
    echo "       move it aside or pass --dir to use a different location." >&2
    exit 1
  fi
  if [ "$USE_COPY" -eq 1 ]; then
    rm -rf "$target"
    cp -R "$src" "$target"
    echo "copied    $target"
  else
    ln -sfn "$src" "$target"
    echo "linked    $target -> $src"
  fi
done

echo
echo "Installed ${#SKILLS[@]} skill(s) into $SKILLS_DIR:"
printf '  - %s\n' "${SKILLS[@]}"
echo
echo "Next: create a vault with ./new-vault.sh (see README → Install)."
