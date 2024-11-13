#!/usr/bin/env python
"""
Regulate how many threads can run at the same time.
"""
import random
import threading

import logger
from simulator import slackoff, time_consuming_task


@time_consuming_task
def download(semaphore):
    logger.debug("Wait for resource")
    with semaphore:
        logger.debug("got it")
        slackoff()


if __name__ == "__main__":
    random.seed()

    MAX_THREADS = 5
    MAX_THREADS_AT_ONCE = 2

    pool = threading.Semaphore(MAX_THREADS_AT_ONCE)
    tasks = [
        threading.Thread(target=download, args=(pool,)) for _ in range(MAX_THREADS)
    ]

    for task in tasks:
        task.start()

    for task in tasks:
        task.join()

    logger.debug("Done")
