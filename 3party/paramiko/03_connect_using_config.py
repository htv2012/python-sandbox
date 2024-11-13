#!/usr/bin/env python3
"""
A Python skeleton script
"""
import pathlib

import paramiko

if __name__ == "__main__":
    config = paramiko.config.SSHConfig()
    config_path = pathlib.Path("~/.ssh/config").expanduser()
    with open(config_path) as file_stream:
        config.parse(file_stream)

    cfg = config.lookup("aws")
    print(cfg)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(
        cfg["hostname"], username=cfg["user"], key_filename=cfg["identityfile"][0]
    )
