#!/usr/bin/env python3
"""
Demonstrate the concurrent.futures
"""
import concurrent.futures
import logging
import random
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(processName)-16s | %(funcName)-18s | %(message)s",
)
LOGGER = logging.getLogger(__name__)


def do_work(work_id, infile):
    """Do actual work."""
    LOGGER.debug("do_work(%d, %r)", work_id, infile)

    # Trigger an exception
    dummy = work_id // (work_id - 5)
    logging.debug("dummy=%r", dummy)

    time.sleep(random.randint(1, 4))
    outfile = f"outfile_{work_id}.txt"

    # Simulate failure: 1 out of 8, or 12.5%
    if random.randint(1, 8) == 1:
        raise ValueError(f"{work_id=}, {infile=}")

    LOGGER.debug(f"Return {outfile}")
    return outfile


def main():
    """Create subtasks."""
    logging.info("Start")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(do_work, tid, f"infile_{tid}.txt") for tid in range(10)
        ]

    for future in futures:
        exception = future.exception()
        if exception is not None:
            logging.error("Error: %s", exception)
        else:
            logging.info("Result: %r", future.result())
    logging.info("End")


if __name__ == "__main__":
    main()
