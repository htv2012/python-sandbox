#!/usr/bin/env python3
import asyncio
import random

from loguru import logger


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        logger.debug(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(random.randint(1, 3))
        f *= i
    logger.debug(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
        factorial("D", 5),
    )
    logger.info(L)


asyncio.run(main())
