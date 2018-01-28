# coding=utf-8
"""
Click command to write the requirements
"""
import re
from pathlib import Path

import click

import epab.utils
from epab.core import CTX

RE_REQ_PATTERN = re.compile(r'^.*==[\d\.]')
LOCK_FILE = Path('Pipfile.lock')


def _write_reqs_file(cmd, file_path):
    epab.utils.info(f'Writing {file_path}')
    output = []
    raw_output, _ = epab.utils.run(cmd, mute=True, filters='Courtesy Notice: ')
    # raw_output = raw_output.encode('utf8').replace(b'\r\n', b'\n').decode('utf8')
    for line in raw_output.splitlines():
        if RE_REQ_PATTERN.match(line):
            output.append(line)
    Path(file_path).write_text('\n'.join(output))


def _remove_lock_file():
    if LOCK_FILE.exists():
        LOCK_FILE.unlink()


@epab.utils.run_once
@epab.utils.stashed
def _write_reqs(amend: bool = False, stage: bool = False):
    """
    Writes the requirement files

    Args:
        amend: amend last commit with changes
        stage: stage changes
    """
    _remove_lock_file()
    epab.utils.info('Writing requirements')
    if CTX.dry_run:
        epab.utils.info('Skipping requirements; DRY RUN')
        return

    base_cmd = 'pipenv lock -r'
    _write_reqs_file(f'{base_cmd}', 'requirements.txt')
    _write_reqs_file(f'{base_cmd} -d', 'requirements-dev.txt')
    files_to_add = ['Pipfile', 'requirements.txt', 'requirements-dev.txt']

    if amend:
        CTX.repo.amend_commit(append_to_msg='update requirements [auto]', files_to_add=files_to_add)
    elif stage:
        CTX.repo.stage_subset(*files_to_add)
    _remove_lock_file()


@click.command()
@click.option('-a', '--amend', is_flag=True, help='Amend last commit')
@click.option('-s', '--stage', is_flag=True, help='Stage changed files')
def reqs(amend: bool = False, stage: bool = False):
    """
    Write requirements files

    Args:
        amend: amend last commit with changes
        stage: stage changes
    """
    changed_files = CTX.repo.changed_files()
    if 'requirements.txt' in changed_files or 'requirements-dev.txt' in changed_files:
        epab.utils.error('Requirements have changed; cannot update them')
        exit(-1)
    _write_reqs(amend, stage)
