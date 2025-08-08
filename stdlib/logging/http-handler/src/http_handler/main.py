#!/usr/bin/env python3
import logging
import logging.handlers


class MyHttpHandler(logging.handlers.HTTPHandler):
    def mapLogRecord(self, record):
        return {"foo": "bar"}

    #    return {
    #        "asctime": record.asctime,
    #        "levelno": record.levelno,
    #        "message": record.message,
    #    }


def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create console handler and set appropriate level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)-8s %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logger.addHandler(MyHttpHandler(host="127.0.0.1:8000", url="/log/", method="POST"))

    return logger


def main():
    logger = create_logger()

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")


if __name__ == "__main__":
    main()
