#!/usr/bin/env python3
import logging
import os
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(
    level=os.getenv("LOGLEVEL", "WARN"),
    format="%(levelname)s:%(processName)s:%(threadName)s:%(message)s",
)
LOGGER = logging.getLogger(__name__)


def random_title():
    title = " ".join(
        "".join(random.sample(string.ascii_letters, 3))
        for _ in range(random.randint(2, 6))
    )
    return title


def get_title(url):
    LOGGER.debug("do_work(url=%r)", url)
    duration = random.randint(1, 3)
    time.sleep(duration)
    title = random_title()
    LOGGER.debug("return (%r, %r)", url, title)
    return url, title


def main():
    URLS = [
        "http://url1",
        "http://url2",
        "http://url3",
    ]

    with ThreadPoolExecutor() as executor:
        results = executor.map(get_title, URLS)

    # After the with block, all tasks are completed, we can
    # print the URLs and title, or write them to file
    print()
    print("RESULTS")
    for url, title in results:
        print(f"{url=}, {title=}")


if __name__ == "__main__":
    main()
