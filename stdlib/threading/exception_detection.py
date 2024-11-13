"""
Detects exception within a thread using Event
"""
import logging
import random
import sys
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(threadName)-15s | %(funcName)-18s | %(message)s",
)


def thread_func(delay: int, should_exit: threading.Event):
    while not should_exit.is_set():
        time.sleep(delay)
        value = random.randint(0, 5)
        logging.debug("value=%r", value)
        value = 100 // value  # Might generates exception

    logging.debug("Exit thread")


def main():
    exception_obj = None
    exception_encountered = threading.Event()
    should_exit = threading.Event()

    def custom_excepthook(args):
        nonlocal exception_obj
        nonlocal exception_encountered

        logging.debug("Enter custom exception hook")
        exception_obj = args.exc_value
        exception_encountered.set()

    threading.excepthook = custom_excepthook
    thread_obj = threading.Thread(
        target=thread_func,
        kwargs={"delay": 1, "should_exit": should_exit},
        name="SecondaryThread",
    )
    thread_obj.start()

    logging.debug("Waiting for secondary thread")
    exit_code = 0
    if exception_encountered.wait(timeout=5):
        exit_code = 1
        logging.debug("Exception encountered: %r", exception_obj)

    if thread_obj.is_alive():
        logging.debug("Terminate secondary thread")
        should_exit.set()
        thread_obj.join()

    logging.debug("Exit with code: %d", exit_code)
    return exit_code


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
