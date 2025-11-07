import contextlib
import random
import time


def exec_catch(func, *args, **kwargs):
    """Execute a function, return the result, exception."""
    try:
        return func(*args, **kwargs), None
    except Exception as err:
        return None, err


def wait_for(func, predicate, timeout, interval=1.0):
    """
    Repeatedly calls `func()` until `predicate(result, exception)` returns True
    or timeout expires.

    Args:
        func (callable): A zero-argument function that returns a value.
        predicate (callable): A function that takes (result, exception)
                              and returns True if the wait should end.
        timeout (float): Maximum time (in seconds) to wait before giving up.
        interval (float): Time (in seconds) to sleep between calls.

    Returns:
        The last result from `func()` if predicate returns True before timeout,
        otherwise raises TimeoutError.
    """
    start = time.monotonic()

    while True:
        result = None
        exc = None

        try:
            result = func()
        except Exception as e:
            exc = e

        if predicate(result, exc):
            if exc is not None:
                raise exc
            return result

        if time.monotonic() - start > timeout:
            raise TimeoutError(f"Condition not met within {timeout} seconds.")

        time.sleep(interval)
