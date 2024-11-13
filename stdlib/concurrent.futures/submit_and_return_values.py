#!/usr/bin/env python3
import logging
import os
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# logging.basicConfig(
#     level=os.getenv("LOGLEVEL", "WARN"),
#     format="%(levelname)s:%(processName)s:%(threadName)s:%(message)s",
# )
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(threadName)-24s | %(funcName)-18s | %(message)s",
)
LOGGER = logging.getLogger(__name__)


def split_check(total, tip, number_of_parties):
    LOGGER.debug(
        "split_check(total=%r, tip=%r, number_of_parties=%r)",
        total,
        tip,
        number_of_parties,
    )
    duration = random.randint(1, 3)
    time.sleep(duration)
    per_person = (total + total * tip) / number_of_parties
    LOGGER.debug(
        "split_check(total=%r, tip=%r, number_of_parties=%r) -> %r",
        total,
        tip,
        number_of_parties,
        per_person,
    )
    return per_person


def main():
    workload = [
        (45.5, 0.2, 2),
        (135.95, 0.2, 4),
        (45.5, 0.15, 2),
    ]

    futures = dict()
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(split_check, *params): params
            for params in workload
        }

        for future in as_completed(futures):
            total, tip, number_of_parties = futures[future]
            per_person = future.result()
            logging.info(
                "For total of $%0.2f, and %0.0f%% tip, "
                "splitting %d ways, "
                "each person pays $%0.2f",
                total, tip * 100.0, number_of_parties, per_person
            )


if __name__ == "__main__":
    main()
