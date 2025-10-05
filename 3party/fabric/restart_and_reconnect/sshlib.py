"""
Implement the following context manager

1. ssh into a host
2. Perform some set-up work, which might or might not need rebooting
3. Reboot if required and Wait for host to come back online
4. Yield control
5. Perform some clean-up work, which might or might not need rebooting
6. If needed, reboot
"""

import contextlib
import subprocess
import time

import fabric
import paramiko
from loguru import logger


def run(c: fabric.Connection, cmd):
    result = c.run(cmd, hide=True)
    return result.stdout.strip()


@contextlib.contextmanager
def ssh_connect(host: str, timeout=None):
    with fabric.Connection(host=host) as conn:
        logger.info(f"Connect to {host}")
        while True:
            try:
                conn.open()
                logger.info(f"Connected to {host}")
                break
            except (
                EOFError,
                OSError,
                paramiko.ssh_exception.SSHException,
                paramiko.ssh_exception.NoValidConnectionsError,
            ):
                logger.info(f".. Wait for connection to {host}")
                time.sleep(3)
    yield conn


def is_host_online(host: str):
    cmd = ["ping", "-W", "1", "-c", "1", host]
    proc = subprocess.run(cmd, check=False, capture_output=True)
    return proc.returncode == 0


@contextlib.contextmanager
def ssh_context(host: str, setup=None, teardown=None, reboot: bool = False):
    """
    Create a ssh client and perform some prep works remotely.
    """
    if setup is not None:
        with ssh_connect(host=host) as conn:
            setup(conn)
            if reboot:
                logger.info("Reboot")
                conn.sudo("shutdown -r now")

        if reboot:
            time.sleep(3)
            logger.info(f"Wait for host {host} goes offline")
            while is_host_online(host):
                time.sleep(2)
                logger.info(f"Wait for host {host} goes offline")
            logger.info("Wait host comes online")

    with ssh_connect(host=host) as conn:
        yield conn
        if teardown is not None:
            teardown(conn)

        if reboot:
            logger.info("Reboot")
            conn.sudo("shutdown -r now")
