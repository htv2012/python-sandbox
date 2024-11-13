#!/usr/bin/env python
"""
Starts/stops a container
"""
import docker

import docker_wrapper


def main():
    dc = docker.from_env()
    container = docker_wrapper.start(dc, "karaoke-php1.0")
    if container is not None:
        print("Started")
    else:
        print("Fail to start")


if __name__ == "__main__":
    main()
