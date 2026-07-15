import logging
import sys
from logging import FileHandler


def create_logger(logger_name="battleship", log_file="/tmp/battleship.log"):
    # 1. Create a custom logger
    logger = logging.getLogger(logger_name)

    # Prevent duplicate logs if the logger is fetched multiple times
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.DEBUG)  # Capture everything at the logger level

    # 2. Create formatters
    # A cleaner format for the console, and a detailed one for the log file
    console_formatter = logging.Formatter("[%(levelname)s] %(message)s")
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - [%(funcName)s] - %(levelname)s - %(message)s"
    )
    # 3. Create Console Handler (Streams to stdout)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)  # Only show INFO and above in console
    console_handler.setFormatter(console_formatter)

    # 4. Create File Handler
    file_handler = FileHandler(log_file, mode="w")
    file_handler.setLevel(logging.DEBUG)  # Log everything to the file
    file_handler.setFormatter(file_formatter)

    # 5. Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = create_logger()
