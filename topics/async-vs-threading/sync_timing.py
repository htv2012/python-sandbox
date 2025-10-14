#!/usr/bin/env python3
import time

import httpx
from loguru import logger

from common import FRUIT_COUNT, url


def get_fruit(client: httpx.Client, fruit_id: int) -> dict:
    response = client.get(url(fruit_id))
    response.raise_for_status()
    return response.json()


def main():
    start_time = time.perf_counter()
    logger.info("Get fruit synchronously")
    with httpx.Client() as client:
        for i in range(1, FRUIT_COUNT + 1):
            get_fruit(client, i)

    end_time = time.perf_counter()
    logger.info(f"Tasks done in {end_time - start_time:.1f} seconds")


if __name__ == "__main__":
    main()
