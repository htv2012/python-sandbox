#!/usr/bin/env python
# Demo: download many files concurrently

import multiprocessing
from toolbox.simulator import time_consuming_task
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('main')


def schedule_tasks(max_processes, input_queue, target):
    for i in range(max_processes):
        process = multiprocessing.Process(
            # name="worker{}".format(i),
            target=target,
            args=(input_queue,))
        process.daemon = True
        process.start()


@time_consuming_task
def download(url):
    logger.info('downloading %s', url)


def worker(input_queue):
    while True:
        try:
            url = input_queue.get()
            download(url)
        finally:
            input_queue.task_done()


def wait_for_tasks(input_queue):
    try:
        input_queue.join()
    except KeyboardInterrupt:
        logger.info('Canceling tasks')


if __name__ == '__main__':
    max_processes = multiprocessing.cpu_count()
    input_queue = multiprocessing.JoinableQueue()
    for i in range(10):
        input_queue.put('URL{}'.format(i))

    schedule_tasks(max_processes, input_queue, worker)
    wait_for_tasks(input_queue)
