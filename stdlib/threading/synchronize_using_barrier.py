#!/usr/bin/env python3
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


def calculate_count(seq, stat, barrier):
    simulate_long_task()
    stat["count"] = len(seq)
    logging.debug("Done, stat=%r", stat)
    barrier.wait()


def calculate_total(seq, stat, barrier):
    simulate_long_task()
    stat["total"] = sum(seq)
    logging.debug("Done, stat=%r", stat)
    barrier.wait()


def calculate_mean(stat, barrier):
    logging.debug("Wait for count and total")
    barrier.wait()
    simulate_long_task()
    stat["mean"] = stat["total"] * 1.0 / stat["count"]
    logging.debug("Done, stat=%r", stat)


def main():
    threading.main_thread().name = "main"
    sequence = list(range(1, 11))
    logging.debug("sequence=%r", sequence)
    stat = dict.fromkeys(["total", "count", "mean"])
    barrier = threading.Barrier(
        parties=3,
        action=lambda: logging.debug("Got count and total, stat=%r", stat),
    )

    tasks = [
        threading.Thread(
            name="calculate_mean", target=calculate_mean, args=(stat, barrier)
        ),
        threading.Thread(
            name="calculate_total",
            target=calculate_total,
            args=(sequence, stat, barrier),
        ),
        threading.Thread(
            name="calculate_count",
            target=calculate_count,
            args=(sequence, stat, barrier),
        ),
    ]

    for task in tasks:
        task.start()
    for task in tasks:
        task.join()

    logging.debug("All done, stat=%r", stat)


if __name__ == "__main__":
    main()
