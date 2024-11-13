#!/usr/bin/env python3
import logging
import random
import time
from concurrent.futures import Future, ThreadPoolExecutor

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(threadName)-24s | %(funcName)-24s | %(message)s",
)


def worker(work_id: int):
    logging.debug("Working on ID: %d", work_id)
    time.sleep(random.randint(1, 3))
    return f"Done task {work_id}"


def report(future: Future):
    if future.done():
        result = future.result()
        logging.debug("Result: %s", result)


def main():
    """Entry"""
    logging.debug("Start")
    with ThreadPoolExecutor() as executor:
        for work_id in range(5):
            future = executor.submit(worker, work_id=work_id)
            future.add_done_callback(report)
    logging.debug("End")


if __name__ == "__main__":
    main()
