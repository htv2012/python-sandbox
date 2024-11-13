# asyncio_coroutine.py
# https://pymotw.com/3/asyncio/coroutines.html
import asyncio
import time

import logger


async def coroutine():
    logger.info("enter coroutine")
    time.sleep(1)
    logger.info("exit coroutine")
    return 99


def main():
    """Entry"""
    event_loop = asyncio.get_event_loop()
    try:
        logger.info("start")
        coro = coroutine()
        logger.info("enter event loop")
        value = event_loop.run_until_complete(coro)
        logger.info(f"Return value: {value}")
    finally:
        logger.info("end")
        event_loop.close()


if __name__ == "__main__":
    main()
