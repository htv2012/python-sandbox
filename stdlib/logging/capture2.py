#!/usr/bin/env python3
"""
Captures part of the log by adding an additional handler to the root
logger. This trick relies on loggers without any handlers that propagate
logging to the root.
"""
import contextlib
import io
import logging


@contextlib.contextmanager
def capture(stream=None):
    stream = stream or io.StringIO()
    start = stream.tell()
    handler = logging.StreamHandler(stream)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    yield stream
    stream.seek(start)
    root_logger.removeHandler(handler)


def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Before capturing")
    with capture() as buffer:
        logger.info("During capturing I")
        logger.info("During capturing II")
    logger.info("After capturing")

    print("-" * 80)
    captured = buffer.read()
    print(captured)


if __name__ == '__main__':
    main()
