import threading
import time

from loguru import logger


class Callbacks:
    def worker(self):
        logger.info("Start worker")
        while True:
            time.sleep(2)
            logger.info("Working")

    def pre_hook(self):
        logger.info("pre_hook")

    def in_hook(self):
        logger.info("Start in_hook")
        job = threading.Thread(
            target=self.worker,
            daemon=True,
        )
        job.start()
        logger.info("End in_hook")

    def post_hook(self):
        logger.info("post_hook")


class Callbacks2:
    def pre_hook(self):
        logger.info("pre_hook2")

    def in_hook(self):
        logger.info("in_hook2")

    def post_hook(self):
        logger.info("post_hook2")


class CallbacksChain:
    def __init__(self, *others):
        self.others = others

    def pre_hook(self):
        for cb in self.others:
            cb.pre_hook()

    def in_hook(self):
        for cb in self.others:
            cb.in_hook()

    def post_hook(self):
        for cb in self.others:
            cb.post_hook()


def hookup(callback: Callbacks):
    logger.info("Start hookup")
    time.sleep(1)
    callback.pre_hook()

    callback.in_hook()
    logger.info("Waiting for work done")
    time.sleep(5)
    logger.info("Done")

    callback.post_hook()
    logger.info("End hookup")


def main():
    logger.info("Start main")
    cb1 = Callbacks()
    cb2 = Callbacks2()
    chain = CallbacksChain(cb1, cb2)

    hookup(chain)
    logger.info("End main")


if __name__ == "__main__":
    main()
