import datetime
import logging
import os


def get_logger_filename(log_file, overwrite, mode):
    if log_file == "none":
        return log_file
    if log_file is None:
        now = datetime.datetime.now()
        log_file = now.strftime(f"log-%Y-%m-%dT%H-%M-%S-cw-{mode}.txt")
        log_file = os.path.join("/tmp", log_file)
    if os.path.exists(log_file) and not overwrite:
        raise SystemExit(
            f"Log file {log_file} exists, to overwrite, use --log-overwrite"
        )
    return log_file


def setup_zt_loop_logger(filename):
    logger = logging.getLogger("zt-loop")
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
        file_formatter = logging.Formatter(
            "%(asctime)s %(filename)s(%(lineno)d) %(levelname)s %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger
