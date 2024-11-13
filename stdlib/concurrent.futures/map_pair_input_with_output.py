#!/usr/bin/env python3
"""Pair input and output using map"""

import logging
import os
import random
from concurrent.futures import ThreadPoolExecutor
from rand_things import random_title

logging.basicConfig(
    level=os.getenv("LOGLEVEL", "WARN"),
    format="%(levelname)s:%(processName)s:%(threadName)s:%(message)s",
)
LOGGER = logging.getLogger(__name__)


def get_title(url: str, words_count: int):
    LOGGER.debug("Working on (url=%r, words_count=%r)", url, words_count)
    title = random_title(words_count)
    LOGGER.debug("return (%r, %r)", url, title)
    return title


def main():
    data_count = 10
    urls = [f"http://url{x}" for x in range(data_count)]
    words_count_list = [random.randint(2, 6) for _ in range(data_count)]

    with ThreadPoolExecutor() as executor:
        results = executor.map(get_title, urls, words_count_list)

    in_out = sorted(
        ((url, title) for url, title in zip(urls, results)), key=lambda x: (x[1], x[0])
    )
    print()
    print("RESULTS")
    for url, title in in_out:
        print(f"{url=} -> {title=}")


if __name__ == "__main__":
    main()
