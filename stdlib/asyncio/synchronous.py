#!/usr/bin/env python3
import logging
import os
import time

import requests

logging.basicConfig(
    level=os.getenv("LOGLEVEL", "WARN"),
    format="%(asctime)s | %(levelname)-8s | %(funcName)-12s | %(message)s",
)


def get_fruit(session: requests.Session, fruit_id: int) -> dict:
    logging.info("Get fruit ID %d", fruit_id)
    response = session.get(f"https://pokeapi.co/api/v2/berry/{fruit_id}")
    assert response.ok
    logging.info("Fruit %d: done")
    return response.json()


def main():
    session = requests.Session()
    start_time = time.perf_counter()

    print("ID Name")
    print("-- ----")
    for i in range(1, 65):
        fruit = get_fruit(session, i)
        print("{0[id]:2} {0[name]}".format(fruit))
    end_time = time.perf_counter()
    print(f"Tasks take {end_time - start_time:.1f} second(s)")


if __name__ == "__main__":
    main()
