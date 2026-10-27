"""check-no-private-page-names.py: detect and rewrite private vault page names."""

import subprocess
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / 'check-no-private-page-names.py'


def make_repo(tmp_path, files, extra=None):
    (tmp_path / 'check-no-private-page-names.py').write_text(SRC.read_text())
    for rel, text in {**files, **(extra or {})}.items():
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    subprocess.run(['git', 'init', '-q'], cwd=tmp_path, check=True)
    subprocess.run(['git', 'add', '-A'], cwd=tmp_path, check=True)
    return tmp_path


def run(repo, *args, names='secret-topic|other-secret'):
    env = {'PATH': '/usr/bin:/bin', 'LWK_PRIVATE_PAGENAMES': names}
    return subprocess.run(
        [sys.executable, '-I', 'check-no-private-page-names.py', *args],
        cwd=repo,
        env=env,
        capture_output=True,
        text=True,
    )


def test_flags_a_private_page_name(tmp_path):
    r = run(make_repo(tmp_path, {'doc.md': 'see secret-topic here\n'}))
    assert r.returncode == 1
    assert 'doc.md:1' in r.stdout


def test_whole_token_only(tmp_path):
    r = run(make_repo(tmp_path, {'doc.md': 'secret-topics and my-secret-topic\n'}))
    assert r.returncode == 0


def test_allowlist_and_public_vault_stems_are_exempt(tmp_path):
    repo = make_repo(
        tmp_path,
        {'doc.md': 'secret-topic other-secret\n'},
        extra={
            'check-no-private-page-names.allow': 'secret-topic\n',
            'examples/software-craft/wiki/topics/other-secret.md': '# x\n',
        },
    )
    assert run(repo).returncode == 0


def test_fix_rewrites_mapped_names_and_fails_on_unmapped(tmp_path):
    repo = make_repo(
        tmp_path,
        {
            'doc.md': 'secret-topic and other-secret\n',
            '.private-pagenames-map': 'secret-topic=release-notes\n',
        },
    )
    r = run(repo, '--fix')
    assert (repo / 'doc.md').read_text() == 'release-notes and other-secret\n'
    assert r.returncode == 1


def test_ci_log_hides_the_name(tmp_path):
    repo = make_repo(tmp_path, {'doc.md': 'secret-topic\n'})
    env = {'PATH': '/usr/bin:/bin', 'LWK_PRIVATE_PAGENAMES': 'secret-topic', 'CI': 'true'}
    r = subprocess.run(
        [sys.executable, '-I', 'check-no-private-page-names.py'],
        cwd=repo,
        env=env,
        capture_output=True,
        text=True,
    )
    assert r.returncode == 1 and 'secret-topic' not in r.stdout
