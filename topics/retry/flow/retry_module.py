#!/usr/bin/env python
import logging
import time


def linear_delay(duration):
    while True:
        yield duration


def exponential_delay(start, multiplier):
    duration = start
    while True:
        yield duration
        duration *= multiplier


def _create_logger(verbose):
    logging.basicConfig(level=logging.WARN)
    logger = logging.getLogger("retry")
    level = logging.DEBUG if verbose else logging.WARN
    logger.setLevel(level)
    return logger


def _create_delay(delay):
    if delay is None:
        delay = linear_delay(5)
    elif isinstance(delay, int):
        delay = linear_delay(delay)

    return delay


def retry(
    action,
    count=3,
    correction=None,
    expect=None,
    ignore=Exception,
    delay=None,
    logger=None,
):
    """
    Retries an `action` maximum `count` number of times until the expected
    result is returned or maximum number of trials reached.

    :param action: a function which returns a value.
    :param count: The number of trials
    :param correction: A function which is called to correct the
        failure. It is called before the next retry. If None, no correct
        will be made.
    :param expect: a predicate that takes the return value of the action
        as an input and return True if it is the desired value. Otherwise,
        it will return False
    :param ignore: a single exception or a tuple of exceptions that
        `action` might generate and we wish to ignore.
    :param delay: an int, any of the *_delay() generator, or None. If
        None, the delay will be a linear 5 seconds. If an int, a linear
        delay for that many seconds.
    :param verbose: A boolean indicating if extra debugging information
        should be logged to the console.
    """
    if logger is None:
        logger = _create_logger(verbose=False)
    delay = _create_delay(delay)

    if expect is None:
        expect = lambda result: True
    elif not callable(expect):
        expected_value = expect
        expect = lambda result: result == expected_value

    expect = expect or (lambda result: True)

    for trial in range(1, count + 1):
        try:
            logger.info(f"attemp #{trial}")
            result = action()
            logger.debug(f"result={result}")
            if expect(result):
                return result
        except ignore:
            if trial == count:
                raise

        if correction:
            logger.info(f"correction #{trial}")
            correction()

        timeout = next(delay)
        logger.info(f"wait for {timeout} seconds")
        time.sleep(timeout)
