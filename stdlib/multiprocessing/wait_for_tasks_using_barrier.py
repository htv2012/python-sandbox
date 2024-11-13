#!/usr/bin/env python
"""
Demo: performance multiple calculations at once. However, some
calculation such as average depends on others (total and count).
"""

import multiprocessing
from toolbox.simulator import time_consuming_task
from toolbox import logger


@time_consuming_task
def calculate_total(numbers, stat, barrier):
    stat.total = sum(numbers)
    logger.debug(f"total({numbers})={stat.total}")
    barrier.wait()


@time_consuming_task
def calculate_count(numbers, stat, barrier):
    stat.count = len(numbers)
    logger.debug(f"count({numbers})={stat.count}")
    barrier.wait()


@time_consuming_task
def calculate_average(stat, barrier):
    logger.debug("Wait for total and count")
    barrier.wait()
    logger.debug("Start calculating")
    stat.average = 1.0 * stat.total / stat.count
    logger.debug(f"average={stat.average}")


if __name__ == "__main__":
    mgr = multiprocessing.Manager()
    stat = mgr.Namespace()
    numbers = [1, 3, 5, 7, 9]

    # Creates a barrier object which is shared among 3 processes. When
    # A process calls barrier.wait(), it will be blocked until the
    # barrier is called 3 times. At which point, all processes will be
    # unlocked and move forward.
    barrier = multiprocessing.Barrier(parties=3)

    tasks = [
        multiprocessing.Process(
            name="CalculateAverate",
            target=calculate_average,
            args=(stat, barrier),
        ),
        multiprocessing.Process(
            name="CalculateTotal",
            target=calculate_total,
            args=(numbers, stat, barrier),
        ),
        multiprocessing.Process(
            name="CalculateCount",
            target=calculate_count,
            args=(numbers, stat, barrier),
        ),
    ]

    for task in tasks:
        task.start()

    for task in tasks:
        task.join()

    logger.info(f"Result: {stat}")
