"""
Implement the following context manager

1. ssh into a host
2. Perform some set-up work, which might or might not need rebooting
3. Reboot if required and Wait for host to come back online
4. Yield control
5. Perform some clean-up work, which might or might not need rebooting
6. If needed, reboot
"""

import subprocess
import time

import fabric
from loguru import logger

from sshlib import run, ssh_context


def show_info(c: fabric.Connection):
    logger.info(f"Host: {run(c, 'hostname')}")
    logger.info(f"Uptime: {run(c, 'uptime -p')}")
    logger.info(f"User: {run(c, 'whoami')}")


def is_host_online(host: str):
    cmd = ["ping", "-W", "1", "-c", "1", host]
    proc = subprocess.run(cmd, check=False, capture_output=True)
    return proc.returncode == 0


def setup(conn: fabric.Connection):
    logger.info("Set up")
    show_info(conn)


def teardown(conn: fabric.Connection):
    logger.info("Tear down")
    show_info(conn)


def main():
    """Entry"""
    logger.info("DEMO 1")
    with ssh_context(host="test1", setup=setup, teardown=teardown, reboot=True) as conn:
        os_release = run(conn, "cat /etc/os-release")
        logger.info(f"Content of /etc/os-release\n{os_release}")

    time.sleep(3)
    logger.info("DEMO 2")
    with ssh_context(host="test1") as conn:
        show_info(conn)


if __name__ == "__main__":
    main()
