#!/usr/bin/env python3
import concurrent.futures
import logging
import os
import random
import time


def pause():
    duration = random.randint(5, 10)
    time.sleep(duration)


logging.basicConfig(
    level=os.getenv("LOGLEVEL", "DEBUG"),
    format="%(levelname)s:%(processName)s:%(message)s",
)
LOGGER = logging.getLogger(__name__)


def do_work(work_id, file1, file2):
    LOGGER.debug("do_work(%d, %r, %r)", work_id, file1, file2)
    pause()
    LOGGER.debug("done")


def main():
    ids = [1, 2, 3]
    files1 = [f"infile{tid}" for tid in ids]
    files2 = [f"outfile{tid}" for tid in ids]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(do_work, ids, files1, files2)


if __name__ == "__main__":
    main()
