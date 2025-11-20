#!/usr/bin/env python3
"""Demo: Colorize text using logging.Formatter."""

import logging


class Colors:
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    RED = "\033[91m"
    YELLOW = "\033[93m"

    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class CustomFormatter(logging.Formatter):
    def __init__(self, keyword_color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keyword_color = keyword_color

    def format(self, record):
        msg = record.msg
        for kw, color in self.keyword_color.items():
            msg = msg.replace(kw, f"{color}{kw}{Colors.RESET}")
        record.msg = msg
        out = super().format(record)
        return out


def setup_logger():
    color = {
        "PID": Colors.YELLOW,
        "Process Name": Colors.YELLOW,
        "Hello": Colors.MAGENTA,
        "Pass": Colors.GREEN,
        "Fail": Colors.RED,
    }

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_formatter = CustomFormatter(
        color, "%(filename)s(%(lineno)d) %(levelname)s %(message)s"
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    return logger


def main():
    logger = setup_logger()
    logger.info("Hello world")
    logger.debug("PID: 33445")
    logger.info("Process Name: Hello")
    logger.info("Test result: Pass")
    logger.info("Test result: Fail")


if __name__ == "__main__":
    main()
