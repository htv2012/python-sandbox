#!/usr/bin/env python
"""
Cleans up the ~/.ssh/known_hosts by deleting those entries that are not in
- A pre-defined set
- ~/.ssh/config
"""
import fileinput
import pathlib
import shutil

import paramiko


def backup_known_hosts():
    original = pathlib.Path("~/.ssh/known_hosts").expanduser()
    backup = original.with_name("known_hosts.bak")
    shutil.copyfile(original, backup)


def get_hosts_from_config():
    config_filename = pathlib.Path("~/.ssh/config").expanduser()
    ssh_config = paramiko.config.SSHConfig.from_path(config_filename)
    for name in ssh_config.get_hostnames():
        info = ssh_config.lookup(name)
        hostname = info.get("hostname", "*")
        if hostname != "*":
            yield hostname


def main():
    backup_known_hosts()
    to_keep = {"bitbucket.org", "github.com"}
    to_keep.update(get_hosts_from_config())

    known_hosts_filename = pathlib.Path("~/.ssh/known_hosts").expanduser()
    with fileinput.input(known_hosts_filename, inplace=True) as known_hosts:
        for line in known_hosts:
            try:
                hosts = set(line.split()[0].split(","))
                if hosts.intersection(to_keep):
                    print(line, end="")
            except IndexError:
                pass
        print()


if __name__ == "__main__":
    main()
