#!/usr/bin/env python3
r"""install-obsidian-plugins.py — install the kit's default Obsidian plugin set into vaults.

The agent writes the vault; these plugins only help a human read and navigate
it. Nothing here rewrites notes on its own: a second writer would race with
ingestion and compete with schema/ as the frontmatter source of truth. Left out
deliberately: Linter (rewrites frontmatter on save), Tag Wrangler (renames tags
around the controlled vocabulary), auto-committing git plugins (race the
agent's commits), AI chat/embedding plugins (a second, uncontrolled index) and
Templater (the agent creates the pages).

For each vault this:
  * downloads the latest release of every plugin in PLUGINS (main.js,
    manifest.json, styles.css when the release ships one) into
    .obsidian/plugins/<id>/ — the repo is resolved through Obsidian's own
    community registry, so it is the same source the in-app browser uses;
  * merges the ids into .obsidian/community-plugins.json (existing entries kept);
  * uninstalls anything in RETIRED_PLUGINS (plugin folder and enabled entry);
  * ensures the core Bases plugin is on in .obsidian/core-plugins.json (when
    that file is absent Obsidian creates its defaults on first open, which
    already include Bases);
  * adds ignore rules to the vault's .gitignore, so only community-plugins.json
    and each plugin's data.json (its settings) are versioned — plugin code is
    reinstalled by this script, never committed — and Obsidian's per-session
    workspace*.json state stays out of git.

Re-running is safe and doubles as an update: it re-downloads the latest release.
Quit Obsidian first; it rewrites .obsidian/ config when a vault closes. After
the first install, turn off Restricted mode once per vault (Settings →
Community plugins) — that trust step is deliberately left to the human.

Usage:
  ./install-obsidian-plugins.py <vault-path> [...]   Install into the named vaults.
  ./install-obsidian-plugins.py --all                 Install into every vault under the vaults dir.

Env:
  LWK_VAULTS_DIR   Override the vaults directory for --all (default: ~/vaults).
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

VAULTS_DIR = Path(os.environ.get('LWK_VAULTS_DIR', str(Path.home() / 'vaults')))
REGISTRY_URL = (
    'https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json'
)
RELEASE_URL = 'https://github.com/{repo}/releases/latest/download/{asset}'

# Community plugin ids, as listed in Obsidian's community registry.
PLUGINS = [
    'obsidian-hover-editor',  # Hover Editor — preview/edit a wikilink without leaving the page
    'obsidian42-strange-new-worlds',  # Strange New Worlds — inline backlink counts (orphans, central pages)
    'omnisearch',  # Omnisearch — fuzzy full-text search
    'text-extractor',  # Text Extractor — lets Omnisearch search text inside PDFs and images
    'pdf-plus',  # PDF++ — page/selection-level links into source PDFs
    'obsidian-excalidraw-plugin',  # Excalidraw — renders the visual-summary skill's drawings
    'supercharged-links-obsidian',  # Supercharged Links — styles links by the target's frontmatter
    'obsidian-quiet-outline',  # Quiet Outline — searchable heading outline for long pages
]
# Formerly in the default set; removed from every vault on the next run.
RETIRED_PLUGINS = [
    'better-word-count',  # unmaintained since 2024-01; core Word Count covers it
]
CORE_PLUGINS_ON = ['bases']

GITIGNORE_MARKER = (
    '# Obsidian plugin code (reinstalled by llm-wiki-kit/install-obsidian-plugins.py)'
)
GITIGNORE_RULES = [
    '.obsidian/workspace*.json',
    '.obsidian/plugins/*/*',
    '!.obsidian/plugins/*/data.json',
]


def fetch(url: str) -> bytes | None:
    """GET url; None on 404, raise on anything else."""
    try:
        with urllib.request.urlopen(url, timeout=60) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def resolve_repos() -> dict[str, str]:
    registry = json.loads(fetch(REGISTRY_URL) or b'[]')
    repos = {p['id']: p['repo'] for p in registry}
    missing = [pid for pid in PLUGINS if pid not in repos]
    if missing:
        sys.exit(f'error: not in the Obsidian community registry: {", ".join(missing)}')
    return {pid: repos[pid] for pid in PLUGINS}


def download_plugins(repos: dict[str, str]) -> dict[str, dict[str, bytes]]:
    """Download each plugin's release assets once, shared across vaults."""
    assets: dict[str, dict[str, bytes]] = {}
    for pid, repo in repos.items():
        files: dict[str, bytes] = {}
        for name in ('manifest.json', 'main.js', 'styles.css'):
            data = fetch(RELEASE_URL.format(repo=repo, asset=name))
            if data is None:
                if name == 'styles.css':
                    continue
                sys.exit(f'error: {pid}: latest release of {repo} has no {name}')
            files[name] = data
        manifest = json.loads(files['manifest.json'])
        if manifest.get('id') != pid:
            sys.exit(f'error: {repo} manifest id is {manifest.get("id")!r}, expected {pid!r}')
        print(
            f'downloaded: {pid} {manifest.get("version")} (min Obsidian {manifest.get("minAppVersion")})'
        )
        assets[pid] = files
    return assets


def read_json(path: Path, default):
    return json.loads(path.read_text(encoding='utf-8')) if path.is_file() else default


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')


def ensure_gitignore(vault: Path) -> None:
    gi = vault / '.gitignore'
    text = gi.read_text(encoding='utf-8') if gi.is_file() else ''
    if GITIGNORE_MARKER in text:
        return
    block = '\n'.join([GITIGNORE_MARKER, *GITIGNORE_RULES]) + '\n'
    gi.write_text(
        text + ('\n' if text and not text.endswith('\n\n') else '') + block, encoding='utf-8'
    )


def install(vault: Path, assets: dict[str, dict[str, bytes]]) -> None:
    obsidian = vault / '.obsidian'
    for pid, files in assets.items():
        pdir = obsidian / 'plugins' / pid
        pdir.mkdir(parents=True, exist_ok=True)
        for name, data in files.items():
            (pdir / name).write_bytes(data)

    for pid in RETIRED_PLUGINS:
        shutil.rmtree(obsidian / 'plugins' / pid, ignore_errors=True)

    enabled_path = obsidian / 'community-plugins.json'
    enabled = [pid for pid in read_json(enabled_path, []) if pid not in RETIRED_PLUGINS]
    write_json(enabled_path, enabled + [pid for pid in PLUGINS if pid not in enabled])

    core_path = obsidian / 'core-plugins.json'
    if core_path.is_file():
        core = read_json(core_path, {})
        if isinstance(core, dict):
            missing = [pid for pid in CORE_PLUGINS_ON if core.get(pid) is not True]
            core.update({pid: True for pid in missing})
        else:  # pre-1.x list format: the list holds the enabled ids
            missing = [pid for pid in CORE_PLUGINS_ON if pid not in core]
            core += missing
        if missing:
            write_json(core_path, core)

    ensure_gitignore(vault)
    print(f'installed: {vault}')


def obsidian_running() -> bool:
    return subprocess.run(['pgrep', '-x', 'Obsidian'], capture_output=True).returncode == 0


def main(argv: list[str]) -> int:
    if argv == ['--all']:
        vaults = (
            sorted(d for d in VAULTS_DIR.iterdir() if (d / 'CLAUDE.md').is_file())
            if VAULTS_DIR.is_dir()
            else []
        )
        if not vaults:
            print(f'error: no vaults found under {VAULTS_DIR}', file=sys.stderr)
            return 1
    elif argv and not any(a.startswith('-') for a in argv):
        vaults = [Path(a).expanduser().resolve() for a in argv]
        bad = [v for v in vaults if not (v / 'CLAUDE.md').is_file()]
        if bad:
            print(f'error: not a vault (no CLAUDE.md): {", ".join(map(str, bad))}', file=sys.stderr)
            return 1
    else:
        print(__doc__.split('Usage:')[1].split('Env:')[0].strip(), file=sys.stderr)
        return 2

    if obsidian_running():
        print(
            'warning: Obsidian is running — quit it, or it may overwrite .obsidian/ config when a vault closes.',
            file=sys.stderr,
        )

    assets = download_plugins(resolve_repos())
    for vault in vaults:
        install(vault, assets)
    print('next: open each vault and turn off Restricted mode (Settings → Community plugins).')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
