#!/usr/bin/env python3
"""Create a reusable context manager.

To create such a context manager, we cannot use the
contextlib.contextmanager decorator because it is meant for single
use.  Instead, we need to use a class with __enter__ and __exit__.
We don't have to subclass from AbstractContextManager, but it ensure
that we don't forget to implement __enter__ and __exit__.
"""
import contextlib
import time


class ElapseTime(contextlib.AbstractContextManager):
    def __init__(self):
        self._start_time = None
        self._end_time = None
        self.elapsed = None
        self.cummulative_elapsed = 0.0

    def __enter__(self):
        self._start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._end_time = time.time()
        self.elapsed = self._end_time - self._start_time
        self.cummulative_elapsed += self.elapsed


def main():
    """Entry"""
    # First use
    with ElapseTime() as elapsed_time:
        time.sleep(0.5)

    print(f"After first use, {elapsed_time.elapsed=:.2f} second(s)")
    print(f"After first use, {elapsed_time.cummulative_elapsed=:.2f} second(s)")

    # Second use
    with elapsed_time:
        time.sleep(0.7)

    print(f"After second use, {elapsed_time.elapsed=:.2f} second(s)")
    print(f"After second use, {elapsed_time.cummulative_elapsed=:.2f} second(s)")


if __name__ == "__main__":
    main()
