#!/usr/bin/env python3
"""Resolve dependencies."""
import logging
import random
import time
from concurrent.futures import ThreadPoolExecutor
from graphlib import TopologicalSorter

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def remove_object(obj, g: TopologicalSorter):
    logging.info("    - Removing %r", obj)
    duration = random.randint(1, 3)
    time.sleep(duration)
    g.done(obj)


def perform_cleanup(g: TopologicalSorter):
    logging.info("# Clean up")
    g.prepare()
    while g.is_active():
        with ThreadPoolExecutor() as executor:
            ready = g.get_ready()
            logging.info("  - We can clean these concurrently: %s", ", ".join(ready))
            for node in ready:
                executor.submit(remove_object, node, g)


def main():
    """Entry"""
    dependencies = {
        "a": ["b", "c"],
        "d": ["a", "b", "c"],
        "e": ["a", "f"],
    }
    g = TopologicalSorter(dependencies)
    print("# Dependencies")
    for k, v in dependencies.items():
        logging.info("  - Before cleaning %s, we must clean up %s", k, ", ".join(v))
    perform_cleanup(g)


if __name__ == "__main__":
    main()
