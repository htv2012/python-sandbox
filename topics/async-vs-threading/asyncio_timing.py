#!/usr/bin/env python3
import asyncio
import time

import httpx
from loguru import logger

from common import FRUIT_COUNT, url


async def get_fruit(client: httpx.Client, fruit_id: int) -> dict:
    response = client.get(url(fruit_id))
    assert response.status_code == 200
    return response.json()


async def main():
    logger.info("Get fruit asynchronously")
    with httpx.Client() as client:
        start_time = time.perf_counter()
        tasks = [get_fruit(client, i) for i in range(1, FRUIT_COUNT + 1)]
        await asyncio.gather(*tasks)
        end_time = time.perf_counter()
        logger.info(f"Tasks done in {end_time - start_time:.1f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
