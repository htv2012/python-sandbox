#!/usr/bin/env python

import multiprocessing
import random
import sys
import logging
import logging.config
import time
from toolbox.simulator import time_consuming_task, slackoff


logging.config.fileConfig('logging.ini')
logger = logging.getLogger('main')


@time_consuming_task
def producer(queue, lock):
    logger.info('Start')
    lorem = "Lorem ipsum dolor sit amet, consectetur ac.".split()

    for word in lorem:
        queue.put(word)
        with lock:
            logger.info('Put: %s', word)
            slackoff()
    logger.info('Finished')


@time_consuming_task
def consumer(queue, lock):
    logger.info('Start')
    while True:
        with lock:
            word = queue.get()
            logger.info('Get: %s', word)
            slackoff()
        if word == 'ac.':
            break
    logger.info('Finished')


if __name__ == '__main__':
    logger.info('Start')
    random.seed()
    queue = multiprocessing.Queue()
    lock = multiprocessing.Lock()

    logger.info('Create producer')
    p1 = multiprocessing.Process(
        target=producer,
        name='producer',
        args=(queue, lock))
    p1.start()

    logger.info('Create consumer')
    p2 = multiprocessing.Process(
        target=consumer,
        name='consumer',
        args=(queue, lock))
    p2.start()

    logger.info('Wait')
    p1.join()
    p2.join()
    logger.info('Finished')
