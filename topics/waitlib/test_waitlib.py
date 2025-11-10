import asyncio
import logging
from unittest.mock import Mock, call, patch

import pytest

from waitlib import wait_for_async

# Note: Adjust the import path above based on your actual file structure

# --- Test Helpers ---

# A simple counter to track function calls
call_count = 0


async def async_counter_func(target_count: int, delay: float = 0.1) -> int:
    """An async function that increments a global counter."""
    global call_count
    await asyncio.sleep(delay)
    call_count += 1
    return call_count


def is_greater_than(target: int):
    """A predicate factory: checks if result > target."""

    def predicate(result, exception) -> bool:
        return exception is None and result > target

    return predicate


@pytest.mark.asyncio
async def test_successful_completion():
    """Tests that polling stops immediately when the predicate is met."""

    async def fut():
        return 5

    result = await wait_for_async(
        fut,
        lambda res, exc: res == 5,
        timeout=5,
        interval=0.1,
    )
    assert result == 5


@pytest.mark.asyncio
async def test_timeout_exceeded():
    """Tests that an asyncio.TimeoutError is raised when the condition is never met."""
    global call_count
    call_count = 0

    # The counter will only reach 1 or 2, but we demand > 10
    target = 10

    with pytest.raises(asyncio.TimeoutError):
        # We set a tight timeout of 0.3s
        await wait_for_async(
            lambda: async_counter_func(target, delay=0.1),
            is_greater_than(target),
            timeout=0.3,
            interval=0.05,
        )

    # Assertions: Should have been called a few times before timing out
    assert call_count >= 1


@pytest.mark.asyncio
async def test_func_raises_exception_and_retries():
    """Tests that the loop continues if the func raises an exception, and the predicate ignores it."""

    class RetryableError(Exception):
        pass

    # Mock function that raises an error twice, then succeeds
    mock_func = Mock(
        side_effect=[
            RetryableError("Attempt 1 failed"),
            RetryableError("Attempt 2 failed"),
            "Success!",
        ]
    )

    # Predicate that ignores the exception and only checks for a successful result
    def success_predicate(result, exception) -> bool:
        return exception is None and result == "Success!"

    result = await wait_for_async(
        mock_func, success_predicate, timeout=1, interval=0.05
    )

    # Assertions
    assert result == "Success!"
    # Must be called 3 times (2 failures + 1 success)
    assert mock_func.call_count == 3


# ---


@pytest.mark.asyncio
async def test_func_raises_exception_and_predicate_accepts_it():
    """Tests that if the predicate returns True while an exception is active, the exception is re-raised."""

    class FatalError(Exception):
        pass

    # Mock func raises the error immediately
    mock_func = Mock(side_effect=[FatalError("Fatal")])

    # Predicate that accepts any non-None exception to stop polling
    def exception_predicate(result, exception) -> bool:
        return exception is not None

    with pytest.raises(FatalError, match="Fatal"):
        await wait_for_async(mock_func, exception_predicate, timeout=1, interval=0.05)

    # Assertions: Should only be called once
    assert mock_func.call_count == 1


@pytest.mark.asyncio
async def test_logging(caplog):
    """Tests that the logger receives expected debug and warning messages."""
    global call_count
    call_count = 0

    test_logger = logging.getLogger("test_wait_for_logging")
    test_logger.setLevel(logging.DEBUG)  # Must set to DEBUG to capture debug messages

    # Use a challenging target that requires multiple calls
    target = 3

    # Set logging capture for this test
    with caplog.at_level(logging.DEBUG, logger="test_wait_for_logging"):
        await wait_for_async(
            lambda: async_counter_func(target),
            is_greater_than(target),
            timeout=5,
            interval=0.05,
            logger=test_logger,
        )

    # The function should be called 4 times (result 1, 2, 3, 4)
    # This means 3 failed predicate checks and 1 success.

    # Assertions
    debug_calls = [r.message for r in caplog.records if r.levelname == "DEBUG"]

    # Check for the correct number of "condition not met" logs (3 retries)
    retry_logs = [msg for msg in debug_calls if "condition not met" in msg]
    assert len(retry_logs) == 3

    # Check for the final success log
    success_logs = [msg for msg in debug_calls if "predicate satisfied" in msg]
    assert len(success_logs) == 1


@patch("asyncio.sleep", new=Mock(wraps=asyncio.sleep))
@pytest.mark.asyncio
async def test_correct_interval_sleep(mock_sleep):
    """Tests that asyncio.sleep is called with the specified interval."""
    global call_count
    call_count = 0

    await wait_for_async(
        lambda: async_counter_func(2),
        is_greater_than(2),
        timeout=5,
        interval=0.25,  # Test interval is 0.25s
    )

    # The function must have run 3 times, meaning it slept 2 times
    assert mock_sleep.call_count == 2

    # Assert that sleep was called with the correct interval
    mock_sleep.assert_has_calls([call(0.25), call(0.25)])
