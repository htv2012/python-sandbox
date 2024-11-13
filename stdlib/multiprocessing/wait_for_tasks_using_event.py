#!/usr/bin/env python
"""
Demo: performance multiple calculations at once. However, some
calculation such as average depends on others (total and count).
"""

import multiprocessing
from toolbox.simulator import time_consuming_task
from toolbox import logger


@time_consuming_task
def calculate_total(numbers, stat, event):
    stat.total = sum(numbers)
    logger.debug(f"total({numbers})={stat.total}")
    event.set()


@time_consuming_task
def calculate_count(numbers, stat, event):
    stat.count = len(numbers)
    logger.debug(f"count({numbers})={stat.count}")
    event.set()


@time_consuming_task
def calculate_average(stat, total_event, count_event):
    logger.debug("Wait for total and count")
    if total_event.wait():
        logger.debug("Got total")
    if count_event.wait():
        logger.debug("Got count")
    logger.debug("Start calculating")
    stat.average = 1.0 * stat.total / stat.count
    logger.debug(f"average={stat.average}")


if __name__ == "__main__":
    mgr = multiprocessing.Manager()
    stat = mgr.Namespace()
    numbers = (1, 3, 5, 7, 9)

    total_event = multiprocessing.Event()
    count_event = multiprocessing.Event()

    tasks = [
        multiprocessing.Process(
            name="CalculateAverate",
            target=calculate_average,
            args=(stat, total_event, count_event),
        ),
        multiprocessing.Process(
            name="CalculateTotal",
            target=calculate_total,
            args=(numbers, stat, total_event),
        ),
        multiprocessing.Process(
            name="CalculateCount",
            target=calculate_count,
            args=(numbers, stat, count_event),
        ),
    ]

    for task in tasks:
        task.start()

    for task in tasks:
        task.join()

    logger.info(f"Result: {stat}")
