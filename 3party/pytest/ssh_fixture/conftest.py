import json
import logging

import paramiko
import pytest


def ssh_connect():
    with open("config.json") as stream:
        test_config = json.load(stream)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(**test_config, timeout=3)
    return client


@pytest.fixture
def ssh_client(request: pytest.FixtureRequest):
    logging.info("Root: %s", request.config.rootpath)
    with ssh_connect() as client:
        yield client
