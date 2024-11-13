#!/usr/bin/env python3
"""
A worker can also be an object of type threading.Thread

Why do we want this? A function is much simpler, right? When A
worker is complex, may be it needs lots of support functions, then
a class makes more sense.
"""
import logging
import os
import random
import threading
import time

logging.basicConfig(
    level=os.getenv("LOGLEVEL", "DEBUG"),
    format="%(asctime)s | %(levelname)-12s | %(threadName)-16s | %(message)s",
)


def simulate_long_task():
    duration = random.randint(2, 5)
    time.sleep(duration)


class Worker(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.debug("Created")

    def run(self):
        logging.debug("Start")
        simulate_long_task()
        logging.debug("Done")


def main():
    """Entry"""
    threading.main_thread().name = "main"

    tasks = [Worker(name=f"task{i}") for i in range(5)]

    for task in tasks:
        task.start()
    for task in tasks:
        task.join()


if __name__ == "__main__":
    main()
