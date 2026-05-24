import argparse
import os
import pathlib
import subprocess

from . import data
from .data import SETTINGS
from .parse import extract_details


def create_uv_project(root, name):
    os.chdir(root)
    subprocess.run(["uv", "init", "--name", name])
    subprocess.run(["uv", "add", "--dev", "pytest", "ruff", "ty"])


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

    # Create the directories
    project_dir = options.root / details["dir"]
    project_dir.mkdir()
    vscode_dir = project_dir / ".vscode"
    vscode_dir.mkdir()

    create_uv_project(project_dir, details["project_id"])

    # Create the files
    data.write_file(project_dir, "README.md", details["readme"])
    data.write_file(project_dir, "Makefile")
    data.write_file(project_dir, "solution.py", details["code"])
    data.write_file(project_dir, "test_solution.py", details["test"])
    data.write_file(vscode_dir, "settings.json", SETTINGS)
    pathlib.Path("/tmp/leetdir").write_text(f"cd {project_dir}")
