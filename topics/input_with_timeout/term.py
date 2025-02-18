#!/usr/bin/env python3
import signal


def ask(msg: str, timeout: int = None, default: str = "stranger"):
    def _handler(signum, frame):
        if signum == signal.SIGALRM:
            signal.alarm(0)
            raise TimeoutError()

    if timeout is not None:
        signal.signal(signal.SIGALRM, _handler)
        signal.alarm(timeout)

    try:
        return input(msg)
    except TimeoutError:
        print()
        return default
