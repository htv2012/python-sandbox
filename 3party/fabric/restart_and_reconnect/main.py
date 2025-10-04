import contextlib
import subprocess
import time

import fabric
import paramiko
from loguru import logger


def run(c: fabric.Connection, cmd):
    result = c.run(cmd, hide=True)
    return result.stdout.strip()


def show_info(c: fabric.Connection):
    logger.info(f"Host: {run(c, 'hostname')}")
    logger.info(f"Uptime: {run(c, 'uptime -p')}")
    logger.info(f"User: {run(c, 'whoami')}")


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
                logger.info("Wait for connection")
                time.sleep(3)
    yield conn


def is_host_online(host: str):
    cmd = ["ping", "-W", "1", "-c", "1", host]
    proc = subprocess.run(cmd, check=False, capture_output=True)
    return proc.returncode == 0


@contextlib.contextmanager
def ensure_rebooted(hostname: str):
    """
    Create a ssh client and perform some prep works remotely.
    """
    with ssh_connect(host=hostname) as conn:
        show_info(conn)
        logger.info("Reboot")
        conn.sudo("shutdown -r now")

    time.sleep(3)
    logger.info("Wait for host goes offline")
    while is_host_online(hostname):
        time.sleep(2)

    logger.info("Wait host comes online")
    with ssh_connect(host=hostname) as conn:
        yield conn


def main():
    """Entry"""
    with ensure_rebooted(hostname="test1") as conn:
        show_info(conn)
        os_release = run(conn, "cat /etc/os-release")
        logger.info(f"Content of /etc/os-release\n{os_release}")


if __name__ == "__main__":
    main()
