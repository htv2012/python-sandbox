#!/usr/bin/env python3
"""
Demo: Join with a time out
"""

import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(threadName)-9s %(levelname)-6s %(message)s",
)
logger = logging.getLogger()


def worker():
    duration = 10
    logger.debug("Start heavy calculation.")
    time.sleep(duration)
    logger.debug("Done.")


def main():
    """Entry"""
    task = threading.Thread(target=worker, name="TaskThread")
    task.start()

    logger.info("Wait with time out.")
    task.join(timeout=3)

    if task.is_alive():
        logger.info("Still not done, wait until completion this time.")
        task.join()

    logger.info("Task is %s.", "not completed" if task.is_alive() else "completed")


if __name__ == "__main__":
    main()
