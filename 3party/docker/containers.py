#!/usr/bin/env python3
""" Shows containers """

import docker


def main():
    """ Entry """
    client = docker.DockerClient.from_env()
    for container in client.containers.list():
        print(f"Name: {container.name}")
        print(f"ID: {container.id}")
        print(f"Short ID: {container.short_id}")
        print(f"Image: {container.image}")
        print(f"Status: {container.status}")
        print("-" * 80)


if __name__ == '__main__':
    main()
