"""Start/stop a local httpbin server"""
# from typing import Optional

import shutil
import socket
import subprocess


def get_container_manager():
    """Return path to docker or podman."""
    for name in ["docker", "podman"]:
        path = shutil.which(name)
        if path is not None:
            return path
    raise RuntimeError("Cannot find docker or alternative")


def get_free_port():
    """Get a free public port."""
    with socket.socket() as sock:
        sock.bind(("", 0))
        _, port = sock.getsockname()
    return port


def start() -> tuple[str, str]:
    """Start a httpbin container."""
    port = get_free_port()
    manager = get_container_manager()
    if "docker" in manager:
        command = [
            manager,
            "container",
            "run",
            "--detach",
            "--publish",
            f"{port}:80",
            "kennethreitz/httpbin",
        ]
    elif "podman" in manager:
        command = [
            manager,
            "container",
            "run",
            "--detach",
            "--publish",
            f"{port}:80",
            "docker.io/kennethreitz/httpbin",
        ]
    else:
        raise ValueError(f"Unknown manager: {manager}")

    process = subprocess.run(
        command,
        text=True,
        capture_output=True,
        check=True,
    )

    container_id = process.stdout.strip()
    return container_id, f"http://localhost:{port}"


def stop(container_id: str):
    """Stop a container."""
    manager = get_container_manager()
    command = [manager, "stop", container_id]
    subprocess.run(command, check=True, capture_output=True)


class HttpBin:
    """Wrapper for start/stop, with context."""

    def __init__(self):
        self.container_id = None
        self.root = None

    def start(self):
        self.container_id, self.root = start()

    def stop(self):
        stop(self.container_id)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()
        self.container_id = None
        self.root = None
