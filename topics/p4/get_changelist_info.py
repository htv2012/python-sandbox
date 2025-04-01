#!/usr/bin/env python


import logging

INFO = logging.INFO
DEBUG = logging.DEBUG
WARNING = logging.WARNING


def create_logger(logger_name, log_level=logging.WARNING, filename=None):
    """Create a logger that log to the console, if a filename is
    supplied, log to that file as well.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    # create console handler and set appropriate level
    ch = logging.StreamHandler()
    formatter = logging.Formatter("%(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Create a file handler and set appropriate level
    if filename:
        fh = logging.FileHandler(filename=filename, mode="w")
        fformatter = logging.Formatter(
            "%(asctime)s;%(filename)s;%(lineno)d;%(levelname)s;%(message)s",
            "%Y-%m-%d %H:%M:%S",
        )
        fh.setFormatter(fformatter)
        logger.addHandler(fh)
    return logger


logger = create_logger(__name__, DEBUG)


def get_changelist_info(p4_describe_output):
    # Change 22 by haiv@haimac on 2014/10/30 20:46:29
    # ==> 22,haiv@haimac,2014/10/30 20:46:29
    line = next(p4_describe_output)
    _, changelist, _, who, _, date_str, time_str = line.split()
    try:
        _, changelist, _, who, _, date_str, time_str = line.split()
    except ValueError:
        logger.error("Failed to parse line: %r", line)
        raise

    return changelist, who, date_str, time_str


if __name__ == "__main__":
    with open("changelist22.txt") as f:
        changelist, who, date_str, time_str = get_changelist_info(f)
        logger.info("Change list: %s", changelist)
        logger.info("Who:         %s", who)
        logger.info("Date:        %s", date_str)
        logger.info("Time:        %s", time_str)
