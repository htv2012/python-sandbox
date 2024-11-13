#!/usr/bin/env python
# -*- coding: utf-8 -*-


import multiprocessing
from toolbox.simulator import time_consuming_task
from toolbox import logger


@time_consuming_task
def worker(workload):
    logger.info('Working on %s', workload)


def main():
    pool = multiprocessing.Pool()

    logger.info('Assigning workloads')
    for workload in range(6):
        pool.apply_async(worker, args=(workload,))

    logger.info('Wait for workers')
    pool.close()
    pool.join()
    logger.info('Finished')

if __name__ == '__main__':
    main()
