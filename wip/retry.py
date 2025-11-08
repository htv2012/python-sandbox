import asyncio
import logging
import time
from typing import Any, Awaitable, Callable, Optional

AsyncPredicate = Callable[[Any, Optional[Exception]], bool]
AsyncFunc = Callable[[], Awaitable[Any]]


async def wait_for_async(
    func: AsyncFunc,
    predicate: AsyncPredicate,
    timeout: float,
    interval: float = 1.0,
    logger: Optional[logging.Logger] = None,
) -> Any:
    """
    Asynchronously calls `await func()` until `predicate(result, exception)`
    returns True or the timeout expires.

    Args:
        func: Async function returning a value.
        predicate: Function taking (result, exception) -> bool.
        timeout: Maximum total time (seconds) to wait.
        interval: Seconds to sleep between calls.
        logger: Optional logger; if None, a silent logger is used.

    Returns:
        The last result from func() if predicate returns True before timeout.

    Raises:
        asyncio.TimeoutError: If total timeout is exceeded.
        Exception: If predicate returns True but func() raised an exception.
    """
    if logger is None:
        logger = logging.getLogger("wait_for.null")
        logger.addHandler(logging.NullHandler())

    start = asyncio.get_event_loop().time()

    while True:
        result: Any = None
        exc: Optional[Exception] = None

        # Remaining time for total timeout
        elapsed = asyncio.get_event_loop().time() - start
        remaining = timeout - elapsed
        if remaining <= 0:
            logger.warning(f"wait_for: total timeout {timeout}s reached.")
            raise asyncio.TimeoutError(f"Condition not met within {timeout} seconds.")

        try:
            # Enforce per-call timeout
            result = await asyncio.wait_for(func(), timeout=remaining)
        except asyncio.TimeoutError:
            logger.warning("wait_for: func() execution exceeded timeout.")
            raise
        except Exception as e:
            exc = e
            logger.debug(f"wait_for: func() raised {type(e).__name__}: {e}")

        if predicate(result, exc):
            if exc is not None:
                logger.debug("wait_for: predicate accepted exception, re-raising it.")
                raise exc
            logger.debug("wait_for: predicate satisfied, returning result.")
            return result

        elapsed = asyncio.get_event_loop().time() - start
        if elapsed > timeout:
            logger.warning(
                f"wait_for: timeout after {elapsed:.2f}s (limit {timeout}s)."
            )
            raise asyncio.TimeoutError(f"Condition not met within {timeout} seconds.")

        logger.debug(f"wait_for: condition not met, retrying in {interval}s...")
        await asyncio.sleep(interval)


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
