import logging
import re

DEFAULT_SEARCH_REPLACE = [
    (r"password=.*?\s", "password=***"),
]


class RedactFormatter(logging.Formatter):
    def __init__(
        self, fmt=None, datefmt=None, style="%", validate=True, search_replace=None
    ):
        super().__init__(fmt, datefmt, style, validate)
        self.search_replace = search_replace or DEFAULT_SEARCH_REPLACE

    def format(self, record):
        text = super().format(record)
        for search_pattern, replace_text in self.search_replace:
            text = re.sub(search_pattern, replace_text, text)
        return text


def setup_logger(filename):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(
        "%(filename)s(%(lineno)d) %(levelname)s %(message)s"
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    if filename != "none":
        file_handler = logging.FileHandler(filename=filename, mode="w")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(
            RedactFormatter(
                "%(asctime)s %(filename)s(%(lineno)d) %(levelname)s %(message)s"
            )
        )
        logger.addHandler(file_handler)

    return logger


def main():
    logger = setup_logger("/tmp/redact.log")
    logger.info("My password=abc?123 ")


if __name__ == "__main__":
    main()
