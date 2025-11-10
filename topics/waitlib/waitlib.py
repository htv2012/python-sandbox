import asyncio
import logging
from typing import Any, Awaitable, Callable, Optional

AsyncFunc = Callable[[], Awaitable[Any]]
AsyncPredicate = Callable[[Any, Optional[Exception]], bool]


async def _wait_for_condition(
    func: AsyncFunc,
    predicate: AsyncPredicate,
    interval: float,
    logger: logging.Logger,
    start_time: float,
    args,
    kwargs,
) -> Any:
    """
    Core polling logic. Calls func() repeatedly until predicate is True.
    Uses the event loop's time for elapsed time tracking.
    """
    event_loop = asyncio.get_event_loop()

    while True:
        result: Any = None
        exc: Optional[Exception] = None
        elapsed = event_loop.time() - start_time

        try:
            result = await func(*args, **kwargs)
        except Exception as e:
            exc = e
            logger.debug(
                f"wait_for_async: {func.__name__}() raised {type(e).__name__}: {e}"
            )

        if predicate(result, exc):
            if exc is not None:
                logger.debug(
                    "wait_for_async: predicate accepted exception, re-raising it."
                )
                raise exc
            logger.debug("wait_for_async: predicate satisfied, returning result.")
            return result

        logger.debug(
            f"wait_for_async: condition not met (Elapsed: {elapsed:.2f}s), retrying in {interval}s..."
        )
        await asyncio.sleep(interval)


async def wait_for_async(
    func: AsyncFunc,
    predicate: AsyncPredicate,
    timeout: float,
    interval: float = 1.0,
    logger: Optional[logging.Logger] = None,
    args=None,
    kwargs=None,
) -> Any:
    """
    Asynchronously calls `await func()` until `predicate(result, exception)`
    returns True or the total timeout expires.
    """
    if logger is None:
        logger = logging.getLogger("wait_for_async")
        logger.setLevel(logging.WARNING)

    event_loop = asyncio.get_event_loop()
    start_time = event_loop.time()

    try:
        return await asyncio.wait_for(
            _wait_for_condition(
                func=func,
                predicate=predicate,
                interval=interval,
                logger=logger,
                start_time=start_time,
                args=args or tuple(),
                kwargs=kwargs or {},
            ),
            timeout=timeout,
        )
    except asyncio.TimeoutError:
        logger.warning(f"wait_for: total timeout {timeout}s reached.")
        raise asyncio.TimeoutError(f"Condition not met within {timeout} seconds.")
