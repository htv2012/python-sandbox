#!/usr/bin/env python3
import logging
import logging.handlers

import requests


class MyHttpHandler(logging.handlers.HTTPHandler):
    def mapLogRecord(self, record):
       return {
           "asctime": record.asctime,
           "levelno": record.levelno,
           "message": record.message,
       }
    def __init__(self, endpoint: str):
        super().__init__("", "")
        self.endpoint = endpoint

    def mapLogRecord(self, record):
        ret = {
            "asctime": record.asctime,
            "levelno": record.levelno,
            "message": record.message,
        }
        print(f"Return {ret}")
        return ret

    def emit(self, record):
        data = self.mapLogRecord(record)
        resp = requests.post(
            url=self.endpoint,
            headers={"Content-Type": "application/json"},
            data=data,
        )
        print(f"{resp=}")
        breakpoint()
        print()


def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create console handler and set appropriate level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)-8s %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # logger.addHandler(MyHttpHandler(host="127.0.0.1:8000", url="/log/", method="POST"))
    logger.addHandler(MyHttpHandler(endpoint="http://127.0.0.1:8000/log/"))

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
