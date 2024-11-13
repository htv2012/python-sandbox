#!/usr/bin/env python
import argparse
import logging
import multiprocessing
import signal
import time


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(processName)-12s; %(message)s",
)
logger = logging.getLogger(__name__)


def myproc(duration):
    logger.info(f"Wait for {duration} seconds")
    time.sleep(duration)


def format_exitcode(exitcode):
    if exitcode is None:
        reason = "Still alive"
    elif exitcode == 0:
        reason = "Normal exit"
    else:
        reason = signal.strsignal(abs(exitcode))
    return f"{exitcode} ({reason})"


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--timeout", default=15, type=int)
    parser.add_argument("-d", "--duration", default=10, type=int)
    options = parser.parse_args()

    # Create a process and terminate it if Ctrl+C pressed
    process = multiprocessing.Process(
        name="myproc",
        target=myproc,
        args=(options.duration,),
    )
    signal.signal(
        signal.SIGINT,
        lambda signal_number, stack_frame: process.terminate(),
    )

    # Start the process and wait
    process.start()
    logger.info(f"Will time out in {options.timeout} seconds")
    process.join(timeout=options.timeout)

    # The process now is either
    #   - Exited normally
    #   - Interrupted by Ctrl+C,\
    #   - Still alive, but process.join() has timed out
    logger.info("After join")
    logger.info(f"Process exit code: {format_exitcode(process.exitcode)}")
    logger.info(f"Process is alive: {process.is_alive()}")

    # Some process requires some time to exit, we need to retry
    # terminating it a few times
    for _ in range(1):
        if process.is_alive():
            process.terminate()
            time.sleep(1)
        else:
            break

    logger.info("After terminate")
    logger.info(f"Process exit code: {format_exitcode(process.exitcode)}")
    logger.info(f"Process is alive: {process.is_alive()}")


if __name__ == "__main__":
    main()
