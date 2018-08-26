# coding=utf-8
"""
Contains various utility functions
"""
from ._av import AV
from ._console import cmd_end, cmd_start, error, info, std_err, std_out
from ._ensure_exe import ensure_exe
from ._exe_version import VersionInfo, get_product_version
from ._find_exe import find_executable
from ._gitignore import add_to_gitignore
from ._next_version import get_next_version
from ._repo import Repo
from ._resource_path import resource_path
from ._run import run, run
from ._run_once import run_once
from ._stashed import stashed
