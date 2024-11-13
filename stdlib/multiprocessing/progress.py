#!/usr/bin/env python

"""
Scenario: many threads for download, one thread for reporting progress.

Scenario: User keys in a list of URLS, the script spawns a number of
processes to download. At some point, the user decided to cancel all
downloads by pressing Ctrl+C.
"""

import collections
import multiprocessing
import random
import time
import sys
from toolbox.simulator import time_consuming_task, slackoff
import logging
import signal

# Globals
MAX_POOL_SIZE = 3


def control_C_handler(signal, frame):
    global tasks
    global main_process
    if multiprocessing.current_process() == main_process:
        logging.debug("Ctrl-C detected, will try to quit ASAP")
        for task in tasks:
            if task.is_alive():
                logging.debug("Kill task: %s", task.name)
                task.terminate()


@time_consuming_task
def download(url, progress, pool):
    # logging.debug('Waiting for pool')
    with pool:
        # logging.debug('Downloading...')
        download_size = random.randint(5, 10)
        downloaded = 0
        progress[url] = (downloaded, download_size)
        for i in range(download_size):
            downloaded += 1
            # logging.debug('%d of %d', downloaded, download_size)
            progress[url] = (url, downloaded, download_size)
            slackoff()

        # logging.debug('Done.')


def show_progress(progress):
    while True:
        time.sleep(2)
        for url in sorted(progress):
            logging.info("%-3s - %2d of %2d", *(progress[url]))


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG, format="[%(levelname)s] (%(processName)-10s) %(message)s"
    )
    random.seed()
    main_process = multiprocessing.current_process()
    pool = multiprocessing.BoundedSemaphore(MAX_POOL_SIZE)
    queue = multiprocessing.Queue()
    signal.signal(signal.SIGINT, control_C_handler)
    shared_resource = multiprocessing.Manager()
    progress = shared_resource.dict()

    print("Enter a list of URLS, q to end.")
    while True:
        url = input("url: ")
        if url == "q":
            break
        queue.put(url)

    tasks = []
    while not queue.empty():
        url = queue.get()
        task = multiprocessing.Process(target=download, args=(url, progress, pool))
        task.start()
        tasks.append(task)

    progress_task = multiprocessing.Process(target=show_progress, args=(progress,))
    progress_task.start()

    for task in tasks:
        task.join()

    progress_task.terminate()
    logging.debug("All done.")
