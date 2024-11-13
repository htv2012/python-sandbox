#!/usr/bin/env python
"""
Create a pool of workers and assign workloads to them. In the real
world, there might be 4 workers, but with hundreds of workloads.
"""
import argparse
import multiprocessing
from toolbox.simulator import time_consuming_task
from toolbox import logger


@time_consuming_task
def worker(workload):
    result = workload * 2
    logger.debug(f"working: {workload} ==> {result}")
    return result


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m", "--method", choices=["map", "imap", "imap_unordered"], default="map"
    )
    parser.add_argument("-c", "--chunksize", type=int, default=1)
    parser.add_argument("-n", "--number-of-jobs", default=10, type=int)
    options = parser.parse_args()

    logger.info(f"Method: {options.method}")
    logger.info(f"Chunk size: {options.chunksize}")
    logger.info(f"Number of jobs: {options.number_of_jobs}")

    return options


def main():
    options = parse_command_line()
    with multiprocessing.Pool() as p:
        map_method = getattr(p, options.method)
        results = map_method(
            worker, range(options.number_of_jobs), chunksize=options.chunksize
        )

        results = list(results)
        logger.info(f"Results: {results}")


if __name__ == "__main__":
    main()
