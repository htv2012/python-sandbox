#!/usr/bin/env python
"""
Wrapper for docker
"""
import time


def stop_and_wait(dc, container_name_or_id):
    pass


def start(dc, name_id):
    for _ in range(5):
        container = dc.containers.get(name_id)
        if container.status == "running":
            return container

        container = dc.containers.get(name_id)
        container.start()
        time.sleep(0.5)

    return None
    