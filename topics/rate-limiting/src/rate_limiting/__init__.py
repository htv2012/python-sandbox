# import functools

import datetime
import functools
import time

from loguru import logger


def calls_per_second(calls: int):
    def decorator(func):
        last_call = datetime.datetime.now()
        gap = datetime.timedelta(milliseconds=1000.0 / calls)
        logger.debug(f"{gap=}")

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal gap, last_call

            logger.debug(f"{last_call=}")
            since_last_call = datetime.datetime.now() - last_call
            logger.debug(f"{since_last_call=}")

            if since_last_call < gap:
                sleep_time = (gap - since_last_call).total_seconds()
                logger.debug(f"Wait for {sleep_time} second(s)")
                time.sleep(sleep_time)

            logger.debug(f"{args=}, {kwargs=}")
            result = func(*args, **kwargs)
            logger.debug(f"{result=}")

            last_call = datetime.datetime.now()
            logger.debug(f"{last_call=} (updated)")

            return result

        return wrapper

    return decorator
