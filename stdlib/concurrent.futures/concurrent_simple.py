#!/usr/bin/env python3
"""
Demonstrate the concurrent.futures
"""
import concurrent.futures
import logging
import os
import time

logging.basicConfig(
    level=os.getenv("LOGLEVEL", "DEBUG"),
    format="%(levelname)s:%(processName)s:%(threadName)s:%(message)s",
)
LOGGER = logging.getLogger(__name__)


def download(src, dest):
    """Do actual work."""
    LOGGER.debug("download(%r, %r)", src, dest)
    time.sleep(3)
    LOGGER.debug("download done")


def copy_script(src, dest):
    """Do actual work."""
    LOGGER.debug("copy_script(%r, %r)", src, dest)
    time.sleep(1)
    LOGGER.debug("copy_script done")


def main():
    """Create subtasks."""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.submit(download, "http://example.com/path/to/file.txt", "/tmp")
        executor.submit(copy_script, "setup.py", "/tmp")


if __name__ == "__main__":
    main()
