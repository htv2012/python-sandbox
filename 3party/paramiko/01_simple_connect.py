#!/usr/bin/env python3
"""
A simple ssh session to cat a file
"""
import argparse
import pathlib

import paramiko


def main():
    """Entry"""
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    options = parser.parse_args()

    config_path = str(pathlib.Path("~/.ssh/config").expanduser())
    config = paramiko.SSHConfig.from_path(config_path)
    host = config.lookup(options.host)

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(hostname=host["hostname"], username=host["user"])

    stdin, stdout, stderr = client.exec_command("cat /etc/os-release")
    out = stdout.read().decode("utf-8")
    print(out)

    err = stderr.read().decode("utf-8")
    if err:
        print("--- STDERR ---")
        print(err)


if __name__ == "__main__":
    main()
