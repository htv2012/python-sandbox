#!/usr/bin/env python3
"""Removing objects concurrently."""

import logging
import random
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from graphlib import TopologicalSorter

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def remove_object(obj):
    logging.info("    - Removing %r", obj)
    time.sleep(random.random() * 1.0)


def perform_cleanup(g: TopologicalSorter):
    logging.info("# Clean up")
    g.prepare()
    while g.is_active():
        ready = g.get_ready()
        logging.info("  - We can remove these concurrently: %s", ", ".join(ready))
        with ProcessPoolExecutor() as executor:
            futures = {executor.submit(remove_object, node): node for node in ready}
            for future in as_completed(futures):
                node = futures[future]
                logging.info("    - Done: %r", node)
                g.done(node)


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
        logging.info("  - Before removing %s, we must remove %s", k, ", ".join(v))
    perform_cleanup(g)


if __name__ == "__main__":
    main()
