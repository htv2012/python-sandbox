#!/usr/bin/env python3
import time
from concurrent.futures import ThreadPoolExecutor

import httpx
from loguru import logger

from common import FRUIT_COUNT, url


def get_fruit(client: httpx.Client, fruit_id: int) -> dict:
    response = client.get(url(fruit_id))
    assert response.status_code == 200
    return response.json()


def main():
    start_time = time.perf_counter()
    logger.info("Get fruit using threading")
    with httpx.Client() as client, ThreadPoolExecutor() as executor:
        tasks = [
            executor.submit(get_fruit, client, i) for i in range(1, FRUIT_COUNT + 1)
        ]

    for task in tasks:
        task.result()

    end_time = time.perf_counter()
    logger.info(f"Tasks done in {end_time - start_time:.1f} seconds")


if __name__ == "__main__":
    main()
