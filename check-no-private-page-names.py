#!/usr/bin/env python3
"""Privacy guard, part 2: private vault PAGE names must not appear in tracked files.

check-no-private-vault-names.sh stops private vault *slugs* leaking into this public
repo. This catches the other half: the names of pages inside those vaults (topic,
entity and drawing slugs such as a book or a method), which give away what a private
vault is about even when its slug is never named.

The names are supplied out-of-band, never committed (the list would itself leak):
  * env LWK_PRIVATE_PAGENAMES / file .private-pagenames   pipe-separated / one per line
  * or derived from the private vaults themselves: the vault slugs are the denylist
    (LWK_PRIVATE_DENYLIST or .private-denylist) and the vaults' parent directory is
    LWK_PRIVATE_VAULTS_DIR or the first line of .private-vaults-root; every
    <vault>/wiki/**/*.md stem becomes a name.
With neither source the guard skips (exit 0), like its sibling.

Not flagged: names without a hyphen (too generic), stems that are also pages of the
public example vault, stems shared by two or more private vaults (structural terms),
`lint-YYYY-...` digests, and anything in check-no-private-page-names.allow.

Modes:
  (default)            fail on any hit, listing file:line
  --fix                rewrite hits using .private-pagenames-map (git-ignored, one
                       `private-name=public-name` per line), picking public names that
                       fit the software-craft example; hits with no mapping still fail
  --export-pagenames   print the pipe-separated list, e.g. to set as a CI secret
"""

from __future__ import annotations

import importlib.util
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PUBLIC_VAULT = 'software-craft'
ALLOW_FILE = ROOT / 'check-no-private-page-names.allow'
MAP_FILE = ROOT / '.private-pagenames-map'
GENERIC = re.compile(r'^lint-\d{4}-')


def read_lines(path: Path) -> list[str]:
    if not path.is_file():
        return []
    lines = (ln.strip() for ln in path.read_text(encoding='utf-8').splitlines())
    return [ln for ln in lines if ln and not ln.startswith('#')]


def vault_slugs() -> list[str]:
    env = os.environ.get('LWK_PRIVATE_DENYLIST')
    if env:
        return [s for s in env.split('|') if s]
    return read_lines(ROOT / '.private-denylist')


def vaults_dir() -> Path | None:
    env = os.environ.get('LWK_PRIVATE_VAULTS_DIR')
    root = env or next(iter(read_lines(ROOT / '.private-vaults-root')), '')
    return Path(root).expanduser() if root else None


def stems_of(vault: Path) -> set[str]:
    out = set()
    for page in (vault / 'wiki').rglob('*.md'):
        stem = page.name[: -len('.md')]
        out.add(stem[: -len('.excalidraw')] if stem.endswith('.excalidraw') else stem)
    return out


def private_names() -> set[str]:
    explicit = os.environ.get('LWK_PRIVATE_PAGENAMES')
    names = set(explicit.split('|')) if explicit else set(read_lines(ROOT / '.private-pagenames'))
    base = vaults_dir()
    if base and base.is_dir():
        per_vault = {s: stems_of(base / s) for s in vault_slugs() if (base / s / 'wiki').is_dir()}
        seen: dict[str, int] = {}
        for stems in per_vault.values():
            for s in stems:
                seen[s] = seen.get(s, 0) + 1
        names |= {s for s, n in seen.items() if n == 1}
    public = stems_of(ROOT / 'examples' / PUBLIC_VAULT)
    allow = set(read_lines(ALLOW_FILE))
    return {
        n for n in names if '-' in n and n not in public and n not in allow and not GENERIC.match(n)
    }


def tracked_files() -> list[Path]:
    out = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode()
    return [ROOT / f for f in out.split('\0') if f]


def decode_drawing(text: str) -> str:
    """The plain text of a ```compressed-json drawing, which a grep cannot see into."""
    m = re.search(r'## Drawing\n```compressed-json\n(.*?)\n```', text, re.S)
    if not m:
        return ''
    spec = importlib.util.spec_from_file_location(
        'vs', ROOT / 'visual-summary' / 'visual_summary.py'
    )
    if spec is None or spec.loader is None:
        return ''
    mod = importlib.util.module_from_spec(spec)
    sys.modules['vs'] = mod  # @dataclass looks the module up by name
    spec.loader.exec_module(mod)
    try:
        return mod.lz_decompress_base64(re.sub(r'\s+', '', m.group(1)))
    except Exception:  # noqa: BLE001 — an undecodable block is simply not scanned
        return ''


def pattern(names: set[str]) -> re.Pattern[str]:
    alt = '|'.join(re.escape(n) for n in sorted(names, key=len, reverse=True))
    return re.compile(rf'(?<![\w-])(?:{alt})(?![\w-])')


def main(argv: list[str]) -> int:
    names = private_names()
    if '--export-pagenames' in argv:
        print('|'.join(sorted(names)))
        return 0
    if not names:
        print('::warning::page-name guard skipped — no private page names available.')
        print('  Set LWK_PRIVATE_PAGENAMES, or LWK_PRIVATE_VAULTS_DIR + the vault denylist.')
        return 0

    rx = pattern(names)
    mapping = dict(ln.split('=', 1) for ln in read_lines(MAP_FILE) if '=' in ln)
    fix = '--fix' in argv
    unresolved: list[str] = []
    fixed = 0

    for path in tracked_files():
        try:
            text = path.read_text(encoding='utf-8')
        except (UnicodeDecodeError, OSError):
            continue
        rel = path.relative_to(ROOT)
        if path.name.endswith('.excalidraw.md') and rx.search(decode_drawing(text)):
            unresolved.append(
                f'{rel}: private page name inside the compressed drawing (rebuild it)'
            )
        if not rx.search(text):
            continue
        if fix:
            new = rx.sub(lambda m: mapping.get(m.group(0), m.group(0)), text)
            if new != text:
                path.write_text(new, encoding='utf-8')
                fixed += 1
            text = new
        for n, line in enumerate(text.splitlines(), 1):
            for m in rx.finditer(line):
                # Public CI logs are public: show the name only on a local run.
                shown = '<private page name>' if os.environ.get('CI') else m.group(0)
                unresolved.append(f'{rel}:{n}: {shown}')

    if fix:
        print(f'rewrote {fixed} file(s)')
    if unresolved:
        print('::error::private vault page name(s) found in tracked files')
        print('\n'.join(unresolved))
        print('\nReplace them with a name that fits the public example (see --fix).')
        return 1
    print('OK: no private vault page names in tracked files.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
