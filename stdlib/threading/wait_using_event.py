#!/usr/bin/env python
"""
Logging is thread-safe. Example copied format
http://pymotw.com/2/threading/index.html
"""
import random
import threading

import logger
from simulator import slackoff, time_consuming_task


@time_consuming_task
def read_from_db(connected_event):
    logger.debug("Wait for DB connection.")
    connected_event.wait()
    logger.debug("Read from DB")


@time_consuming_task
def open_db(connected_event):
    logger.debug("Connecting to DB...")
    slackoff()
    logger.debug("Connected.")
    connected_event.set()


@time_consuming_task
def update_db(connected_event):
    logger.debug("Wait for DB connection.")
    connected_event.wait()
    logger.debug("Update DB")


if __name__ == "__main__":
    random.seed()

    connected_event = threading.Event()
    tasks = [
        threading.Thread(name="update", target=update_db, args=(connected_event,)),
        threading.Thread(name="read1", target=read_from_db, args=(connected_event,)),
        threading.Thread(name="read2", target=read_from_db, args=(connected_event,)),
        threading.Thread(name="open", target=open_db, args=(connected_event,)),
    ]

    for task in tasks:
        task.start()

    # List the thread names
    logger.debug("Current threads: %s", [t.name for t in threading.enumerate()])

    for task in tasks:
        task.join()

    logger.debug("Done")
