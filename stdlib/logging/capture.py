#!/usr/bin/env python3
"""
Captures part of the log
"""
import contextlib
import io
import logging


@contextlib.contextmanager
def capture(logger, stream=None):
    stream = stream or io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)
    yield stream

    logger.removeHandler(handler)


def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Before capturing")
    with capture(logger) as buffer:
        logger.info("During capturing I")
        logger.info("During capturing II")
    logger.info("After capturing")

    print("-" * 80)
    print(buffer.getvalue())


if __name__ == '__main__':
    main()
