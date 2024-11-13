#!/usr/bin/env python
import multiprocessing
import time
from toolbox import logger


def worker(event, timeout=None):
    """ wait and do some job """
    logger.info("wait for resource")
    if event.wait(timeout):
        logger.info("got resource")
    else:
        logger.info("timed out")


def main():
    event = multiprocessing.Event()
    w1 = multiprocessing.Process(name="PatientWorker", target=worker, args=(event,))
    w1.start()

    w2 = multiprocessing.Process(name="ImpatientWorker", target=worker, args=(event, 2))
    w2.start()

    time.sleep(4)
    logger.info("create resource")
    event.set()

    w1.join()
    w2.join()
    logger.info("Goodbye")


if __name__ == "__main__":
    main()
