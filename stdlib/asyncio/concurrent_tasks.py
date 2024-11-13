#!/usr/bin/env python3
import asyncio
import logging
import os

logging.basicConfig(
    level=os.getenv("LOGLEVEL", "INFO"),
    format="%(asctime)s | %(levelname)-8s | %(funcName)-12s | %(message)s",
)


async def brew_coffee():
    logging.info("Brewing coffee")
    await asyncio.sleep(2)
    logging.info("Coffee is ready")
    return "coffee"


async def toast():
    logging.info("Toasting bread")
    await asyncio.sleep(3)
    logging.info("Toast is ready")
    return "toast"


async def fry_eggs():
    logging.info("Frying eggs")
    await asyncio.sleep(5)
    logging.info("Eggs are ready")
    return "frieg eggs"


async def main():
    logging.info("Start breakfast preparation")
    everything = await asyncio.gather(
        brew_coffee(),
        toast(),
        fry_eggs(),
    )
    logging.info("Breakfast is ready with %s", ", ".join(everything))


if __name__ == "__main__":
    asyncio.run(main())
