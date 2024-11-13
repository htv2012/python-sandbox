import json
import logging
import time

import paramiko
import paramiko.ssh_exception

logging.basicConfig(level="INFO")


def connect_ssh():
    with open("config.json") as stream:
        test_config = json.load(stream)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    # Keep trying to connect until succeeded
    while True:
        try:
            logging.info("Connecting...")
            client.connect(**test_config, timeout=10)
            logging.info("Connected.")
            return client
        except (
            TimeoutError,
            paramiko.ssh_exception.AuthenticationException,
            paramiko.ssh_exception.NoValidConnectionsError,
        ) as error:
            logging.error(error)
        time.sleep(2)


def main():
    """Entry"""
    client = connect_ssh()
    logging.info("Get /etc/os-release")
    _, stdout, _ = client.exec_command("cat /etc/os-release")
    os_release = stdout.read().decode()
    print(os_release)


if __name__ == "__main__":
    main()
