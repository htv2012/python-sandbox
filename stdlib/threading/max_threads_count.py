#!/usr/bin/env python3
"""How many threads before crash?"""
import time
import threading
import itertools


def worker():
    time.sleep(60*60)


def main():
    threads = []
    for i in itertools.count():
        print(f"Threads count: {threading.active_count()}")
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)





if __name__ == '__main__':
    main()
