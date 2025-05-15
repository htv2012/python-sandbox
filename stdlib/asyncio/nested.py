import asyncio
import random
import time

from loguru import logger


async def delay():
    duration = random.randint(1, 4)
    await asyncio.sleep(duration)


async def eval_term(term):
    logger.debug(f"eval_term({term=})")
    await delay()

    a, b = term
    result = a**b
    
    logger.debug(f"eval_term({term=}) => {result}")
    return result


async def eval_poly(terms):
    logger.debug(f"eval_poly({terms=})")
    
    result = await asyncio.gather(*[eval_term(term) for term in terms])
    result = sum(result)

    logger.debug(f"eval_poly({terms=}) => {result}")
    return result


async def main():
    logger.info("Start")

    data = [
        [(2, 2), (3, 3)],
        [(5, 3), (4, 2), (3, 1)],
        [(5, 2), (-3, 1)],
    ]

    logger.info("Start calculations")
    tasks = [eval_poly(terms) for terms in data]
    results = await asyncio.gather(*tasks)

    logger.info("Results")
    for datum, result in zip(data, results):
        equation = " + ".join(f"{a}^{b}" for a, b in datum)
        equation = equation.replace("+ -", "- ")
        logger.info(f"{equation} = {result}")

    logger.info("End")


if __name__ == "__main__":
    asyncio.run(main())
