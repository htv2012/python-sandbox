import argparse
import os
import pathlib

from .data import CONFTEST_TEMPLATE, ENV, MAKE, PYPROJECT, SETTINGS, SOLUTION_TEMPLATE
from .parse import extract_details


def main():
    """Entry"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r",
        "--root",
        type=pathlib.Path,
        default=pathlib.Path("~/Projects/interview-questions/leetcode").expanduser(),
    )
    parser.add_argument("-d", "--dump")
    parser.add_argument("url")
    options = parser.parse_args()

    details = extract_details(options.url, options.dump)

    # Determine the root: leetcode dir
    assert options.root.exists()
    os.chdir(options.root)

    # Create directories and files
    project_dir = options.root / details["dir"]
    project_dir.mkdir()
    vscode_dir = project_dir / ".vscode"
    vscode_dir.mkdir()

    (project_dir / "README.md").write_text(details["readme"])
    (project_dir / ".env").write_text(ENV)
    (project_dir / "conftest.py").write_text(CONFTEST_TEMPLATE % details["fut"])
    (project_dir / "Makefile").write_text(MAKE)
    (project_dir / "pyproject.toml").write_text(PYPROJECT)
    (project_dir / "solution.py").write_text(SOLUTION_TEMPLATE % details["code"])
    (project_dir / "test_solution.py").write_text(details["test"])
    (vscode_dir / "settings.json").write_text(SETTINGS)

    pathlib.Path("/tmp/leetdir").write_text(f"cd {project_dir}")
