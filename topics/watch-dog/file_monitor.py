#!/usr/bin/env python3
import pathlib
import watch_dog
import logging
import time


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def greeting(name: str):
    logger.info("greeting %s", name)


watcher = watch_dog.WatchDog(10, greeting, args=("world",), kwargs={})
watcher.start()
for i in range(10):
    logger.info(f"Iteration {i+1}")
    time.sleep(4)
