import contextlib
import logging
import logging.config
import pathlib
import time

import fabric
import paramiko

config_path = pathlib.Path(__file__).with_name("logging.ini")
logging.config.fileConfig(config_path)


@contextlib.contextmanager
def ssh_connection():
    """
    Create a ssh client and perform some prep works remotely.
    """
    logging.info("First connection...")
    with fabric.Connection(host="primary") as connection:
        logging.info("Connected")

        logging.info("Prep the remote host")
        # Perform prep works here

        logging.info("Reboot the remote host")
        connection.sudo("shutdown -r now")

    time.sleep(1)
    logging.info("Second connection...")
    with fabric.Connection(host="primary") as connection:
        while True:
            try:
                connection.open()
                logging.info("Connected again")
                break
            except (
                EOFError,
                OSError,
                paramiko.ssh_exception.SSHException,
                paramiko.ssh_exception.NoValidConnectionsError,
            ):
                logging.debug("Retrying...")
                time.sleep(3)

        logging.info("Yield control to caller")
        yield connection

    logging.info("Clean up")


def main():
    """Entry"""
    # Suppress paramiko log
    logging.getLogger("paramiko").setLevel(logging.CRITICAL)
    with ssh_connection() as conn:
        logging.info("Run WHOAMI")
        response = conn.run("whoami", hide=True)
        logging.info("User name: %r", response.stdout.strip())
        logging.info("Done WHOAMI")


if __name__ == "__main__":
    main()
