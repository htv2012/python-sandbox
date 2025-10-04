import contextlib
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
def ensure_rebooted(hostname: str):
    """
    Create a ssh client and perform some prep works remotely.
    """
    logger.info(f"Connect to {hostname}")
    with fabric.Connection(host=hostname) as conn:
        logger.info("Reboot")
        conn.sudo("shutdown -r now")

    time.sleep(1)
    logger.info("Wait host comes online")
    with fabric.Connection(host=hostname) as conn:
        while True:
            try:
                conn.open()
                break
            except (
                EOFError,
                OSError,
                paramiko.ssh_exception.SSHException,
                paramiko.ssh_exception.NoValidConnectionsError,
            ):
                logger.info("Still offline...")
                time.sleep(3)

        logger.info("Yield control to caller")
        yield conn

    logger.info("Clean up")


def main():
    """Entry"""
    with ensure_rebooted(hostname="test1") as conn:
        show_info(conn)
        os_release = run(conn, "cat /etc/os-release")
        logger.info(f"Content of /etc/os-release\n{os_release}")


if __name__ == "__main__":
    main()
