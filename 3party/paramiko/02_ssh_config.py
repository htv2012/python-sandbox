#!/usr/bin/env python3
"""
Plays with ssh config file
"""
import pathlib

import paramiko


def main():
    """Entry"""
    config_path = pathlib.Path("~/.ssh/config").expanduser()
    print(f"Config file: {config_path}")
    config = paramiko.SSHConfig.from_path(config_path)

    host_names = ", ".join(sorted(config.get_hostnames()))
    print(f"Host Names: {host_names}")
    for host_name in sorted(config.get_hostnames()):
        print(host_name)
        for k, v in config.lookup(host_name).items():
            print(f"    {k}: {v}")


if __name__ == "__main__":
    main()
