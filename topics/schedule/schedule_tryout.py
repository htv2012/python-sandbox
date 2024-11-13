#!/usr/bin/env python3
import time

import schedule


def job():
    print("job")


def job2():
    print("job2")


last = None
schedule.every(10).seconds.do(job)
schedule.every(7).seconds.do(job2)

while True:
    schedule.run_pending()

    # Display next run, without repeat

    if (next_run := schedule.next_run()) != last:
        print(f"Next run: {next_run:%I:%M:%S}")
    last = next_run

    time.sleep(1)
