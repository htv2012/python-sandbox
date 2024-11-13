#!/usr/bin/env python
import docker


client = docker.from_env()
for image in client.images.list():
    print()
    print(f"id: {image.id}")
    print(f"short_id: {image.short_id}")
    print(f"labels: {image.labels}")