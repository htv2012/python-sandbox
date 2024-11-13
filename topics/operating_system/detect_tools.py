#!/usr/bin/env python3
"""Detects Python version and command-line tools."""
import shutil
import sys

REQUIRED_PYTHON_VERSION = "3.9"
REQUIRED_TOOLS = [
    "curl",
    "jq",
    "ssh",
]


def main():
    """Entry"""
    # Detect Python version
    actual_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    if actual_version != REQUIRED_PYTHON_VERSION:
        raise SystemExit(
            f"Expected Python {REQUIRED_PYTHON_VERSION}, " f"but found {sys.version}"
        )

    # Detect tools
    not_found = [tool for tool in REQUIRED_TOOLS if shutil.which(tool) is None]
    if not_found:
        raise SystemExit(f"Tools not found: {not_found}")


if __name__ == "__main__":
    main()
