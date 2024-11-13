#!/usr/bin/env python
"""
Demo: performance multiple calculations at once. However, some
calculation such as average depends on others (total and count).
"""
import multiprocessing

from toolbox.simulator import time_consuming_task
from toolbox import logger


@time_consuming_task
def calculate_total(numbers, stat):
    stat.total = sum(numbers)
    logger.debug(f"total({numbers})={stat.total}")


@time_consuming_task
def calculate_count(numbers, stat):
    stat.count = len(numbers)
    logger.debug(f"count({numbers})={stat.count}")


@time_consuming_task
def calculate_average(numbers, stat):
    stat.average = 1.0 * stat.total / stat.count
    logger.debug(f"average({numbers})={stat.average}")


if __name__ == "__main__":
    mgr = multiprocessing.Manager()
    stat = mgr.Namespace()
    numbers = list(range(1, 11))

    total_task = multiprocessing.Process(
        name="TotalTask", target=calculate_total, args=(numbers, stat)
    )
    total_task.start()

    count_task = multiprocessing.Process(
        name="CountTask", target=calculate_count, args=(numbers, stat)
    )
    count_task.start()

    logger.info("Waiting for total and count")
    total_task.join()
    count_task.join()
    logger.info("Got total and count")

    average_task = multiprocessing.Process(
        name="AverageTask", target=calculate_average, args=(numbers, stat)
    )
    average_task.start()
    average_task.join()

    logger.info(f"Result: {stat}")
