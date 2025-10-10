#!/usr/bin/env python3
import asyncio
import random

from loguru import logger


async def factorial(task_id, number):
    logger.debug(f"Task {task_id}: Calculating factorial({number})")
    out = 1
    for i in range(2, number + 1):
        await asyncio.sleep(random.random())
        out *= i
    logger.debug(f"Task {task_id}: factorial({number}) = {out}")
    return out


async def main():
    tasks_input = [("A", 6), ("B", 3), ("C", 4)]
    tasks = [factorial(*task_input) for task_input in tasks_input]
    results = await asyncio.gather(*tasks)

    # gather() keeps the order of input/output
    for (task_id, input_value), output_value in zip(tasks_input, results):
        logger.info(f"{task_id}: factorial({input_value}) -> {output_value}")


if __name__ == "__main__":
    asyncio.run(main())
