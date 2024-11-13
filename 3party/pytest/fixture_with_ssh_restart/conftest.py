import logging
import time

import paramiko
import pytest


@pytest.fixture(scope="session")
def ssh_client():
    """
    Create a ssh client and perform some prep works remotely.
    """
    logging.info("First connection...")
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect("192.168.64.18", username="ubuntu")
    logging.info("Connected")

    logging.info("Prep the remote host")
    # Perform prep works here

    logging.info("Reboot the remote host")
    client.exec_command("sudo shutdown -r now")

    logging.info("Second connection...")
    while True:
        try:
            client.connect("192.168.64.18", username="ubuntu")
            logging.info("Connected again")
            break
        except (
            paramiko.SSHException,
            paramiko.ssh_exception.NoValidConnectionsError,
        ):
            time.sleep(3)

    yield client

    logging.info("Clean up remote host")
    # Do something here to clean up
