#!/usr/bin/env python3
import asyncio
import logging
import logging.config
import pathlib
import time

import requests

FRUIT_COUNT = 64
logging.config.fileConfig(pathlib.Path(__file__).with_name("logging.ini"))


async def get_fruit(session: requests.Session, fruit_id: int) -> dict:
    logging.debug("Get fruit ID %d", fruit_id)
    response = session.get(f"https://pokeapi.co/api/v2/berry/{fruit_id}")
    assert response.ok
    logging.debug("Fruit %d: done")
    return response.json()


async def main():
    logging.info("Get fruit asynchronously")
    session = requests.Session()
    start_time = time.perf_counter()
    tasks = [get_fruit(session, i) for i in range(1, FRUIT_COUNT + 1)]
    logging.info("ID Name")
    logging.info("-- ----")
    for task in asyncio.as_completed(tasks):
        fruit = await task
        logging.info("%2d %s", fruit["id"], fruit["name"])

    end_time = time.perf_counter()
    logging.info("Tasks done in %.1f seconds", end_time - start_time)


if __name__ == "__main__":
    asyncio.run(main())
