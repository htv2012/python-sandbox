#!/usr/bin/env python3
"""Given a logger, patch it to redact password."""

import logging
import re


def redact(logger):
    """Redact a logger to remove password."""

    def patch(existing_formatter):
        def do_format(record):
            text = existing_formatter(record)
            return re.sub(r"password=.*? ", "password=*** ", text)

        return do_format

    for handler in logger.handlers:
        handler.formatter.format = patch(handler.formatter.format)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()
    redact(logger)
    logger.info("My password=foo@bar123 Please do not lose it")


if __name__ == "__main__":
    main()
