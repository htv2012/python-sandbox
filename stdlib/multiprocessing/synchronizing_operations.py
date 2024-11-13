#!/usr/bin/env python
"""
Synchronize operations: stage_2 won't start until stage_1 finished.
http://pymotw.com/2/multiprocessing/communication.html
"""

import multiprocessing
from multiprocessing import Process
import time
from toolbox import logger
from toolbox.simulator import time_consuming_task


@time_consuming_task
def stage_1(condition):
    """perform first stage of work, then notify stage_2 to continue"""
    logger.info("Starting")
    time.sleep(2)
    with condition:
        logger.info("Done")
        condition.notify_all()


@time_consuming_task
def stage_2(condition):
    """wait for the condition telling us stage_1 is done"""
    logger.info("Waiting")
    with condition:
        condition.wait()
    logger.info("Running")


def main():
    condition = multiprocessing.Condition()
    s1 = Process(name="s1", target=stage_1, args=(condition,))
    s2_clients = [
        Process(name="s2(%d)" % i, target=stage_2, args=(condition,)) for i in range(3)
    ]

    for c in s2_clients:
        c.start()

    s1.start()
    s1.join()

    for c in s2_clients:
        c.join()


if __name__ == "__main__":
    main()
