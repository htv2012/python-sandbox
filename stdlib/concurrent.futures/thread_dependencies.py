#!/usr/bin/env python3
"""Show how to manage thread dependencies.

In this example:

- open_db: does not have any dependency
- update_db: depends on open_db
- read_db: depends on open_db and update_db

(open_db) -> (update_db) -> (read_db)
"""
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import logger


def slackoff():
    duration = random.randint(1, 5)
    time.sleep(duration)


def open_db(connected_event):
    logger.debug("Connecting...")
    slackoff()
    logger.debug("Open: Connected, set event %r", connected_event)
    connected_event.set()


def read_db(updated_event, query):
    logger.debug("Read: query=%r", query)
    logger.debug("Read: wait for event %r", updated_event)
    updated_event.wait()
    logger.debug("Read: Received event %r", updated_event)
    slackoff()
    logger.debug("Done: %r", query)


def update_db(connected_event, updated_event, query):
    logger.debug("Update: query=%r", query)
    logger.debug("Update: waiting for event %r", connected_event)
    connected_event.wait()
    logger.debug(
        "Update: Signal received for event %r, start updating", connected_event
    )
    slackoff()
    logger.debug("Update: Finished, send the event")
    updated_event.set()
    logger.debug("Done: %r", query)


def main():
    """Start script here."""
    logger.debug("Enter main")
    connected_event = threading.Event()
    updated_event = threading.Event()

    with ThreadPoolExecutor() as executor:
        executor.submit(read_db, updated_event, "read1")
        executor.submit(read_db, updated_event, "read2")
        executor.submit(update_db, connected_event, updated_event, "update1")
        executor.submit(open_db, connected_event)

    logger.debug("Exit main")


if __name__ == "__main__":
    main()
