import time
import logging

def wait_for(func, predicate, timeout, interval=1.0, logger=None):
    """
    Repeatedly calls `func()` until `predicate(result, exception)` returns True
    or the timeout expires.

    Args:
        func (callable): A zero-argument function that returns a value.
        predicate (callable): A function that takes (result, exception)
                              and returns True if the wait should end.
        timeout (float): Maximum time (in seconds) to wait before giving up.
        interval (float): Time (in seconds) to sleep between calls.
        logger (logging.Logger, optional): Logger for debug info.
                                           If None, a silent logger is used.

    Returns:
        The last result from `func()` if predicate returns True before timeout,
        otherwise raises TimeoutError.
    """
    # Use a no-op logger if none is provided
    if logger is None:
        logger = logging.getLogger("wait_for.null")
        logger.addHandler(logging.NullHandler())

    start = time.monotonic()

    while True:
        result = None
        exc = None

        try:
            result = func()
        except Exception as e:
            exc = e
            logger.debug(f"func() raised {type(e).__name__}: {e}")

        if predicate(result, exc):
            if exc is not None:
                logger.debug("predicate accepted exception, re-raising it.")
                raise exc
            logger.debug("predicate satisfied, returning result.")
            return result

        elapsed = time.monotonic() - start
        if elapsed > timeout:
            logger.warning(f"timeout after {elapsed:.2f}s (limit {timeout}s).")
            raise TimeoutError(f"Condition not met within {timeout} seconds.")

        logger.debug(f"condition not met, retrying in {interval}s...")
        time.sleep(interval)
