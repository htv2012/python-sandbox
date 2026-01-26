import logging
import time
from typing import override

import periodic_task

logging.basicConfig(
    level="DEBUG", format="%(asctime)s | %(levelname)s | %(threadName)s | %(message)s"
)
logger = logging.getLogger(__name__)


class Hello(periodic_task.PeriodicTask):
    @override
    def on_timeout(self):
        logger.info("Hi")


def main():
    logger.info("Start")
    hello = Hello(3)
    hello.start()
    time.sleep(10)
    hello.stop()
    logger.info("End")


if __name__ == "__main__":
    main()
