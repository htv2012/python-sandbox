#!/usr/bin/env python3
import logging
import os
import random
import time

logging.basicConfig(level=os.getenv("LOGLEVEL", "WARNING"))
log = logging.getLogger()
random.seed(time.time())


def log_func(n, func, args, kwargs):
    func_name = func.__name__
    args_str = ", ".join(repr(x) for x in args)
    kwargs_str = ", ".join("%s=%r" % kv for kv in kwargs.items())
    if kwargs_str:
        kwargs_str = ", " + kwargs_str
    log.debug("Retry up to %d times: %s(%s%s)", n, func_name, args_str, kwargs_str)


def retry(n, exceptions, wait_time, func, *args, **kwargs):
    """Retry n times."""
    log_func(n, func, args, kwargs)

    for attempt in range(1, n + 1):
        try:
            result = func(*args, **kwargs)
            log.debug("Attempt %d/%d succeeded, return %r", attempt, n, result)
            return result
        except exceptions as e:
            log.error("Attempt %d/%d failed with exception %r", attempt, n, e)
            if attempt == n:
                raise
            time.sleep(wait_time)


def flaky(a, b):
    if random.randint(1, 3) == 1:
        return " ".join(a for _ in range(b))
    raise RuntimeError("Randomly crash")


def main():
    result = retry(3, RuntimeError, 2, flaky, "Ho", b=3)
    print(result)


if __name__ == "__main__":
    main()
