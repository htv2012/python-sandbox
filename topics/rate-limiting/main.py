import datetime

from loguru import logger
from rate_limiting import calls_per_second


@calls_per_second(5)
def hello(n: int):
    """Return a greeting"""
    out = f"hello #{n}"
    logger.info(out)
    return out


def main():
    start_time = datetime.datetime.now()
    count = 10
    for i in range(count):
        result = hello(i)
        logger.info(f"{result=}")
    duration = datetime.datetime.now() - start_time
    actual_calls_per_second = count / duration.total_seconds()
    logger.info(f"Duration: {duration.total_seconds()}")
    logger.info(f"Actual calls per second: {actual_calls_per_second}")


if __name__ == "__main__":
    main()
