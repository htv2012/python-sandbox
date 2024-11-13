#!/usr/bin/env python3
"""
A Python skeleton script
"""
import contextlib
import pathlib
import shutil

import paramiko


def main():
    """Entry"""
    config_path = pathlib.Path("~/.ssh/config").expanduser()
    config = paramiko.SSHConfig.from_path(config_path)
    host_info = config.lookup("nuc")

    with contextlib.ExitStack() as exit_stack:
        client = exit_stack.enter_context(paramiko.SSHClient())
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client.connect(
            hostname=host_info["hostname"],
            username=host_info.get("user"),
            key_filename=host_info.get("identityfile"),
        )

        sftp = exit_stack.enter_context(client.open_sftp())
        infile = exit_stack.enter_context(sftp.open("/etc/os-release", "rb"))

        local_destination = pathlib.Path("/tmp/os-release-from-nuc")
        with open(local_destination, "wb") as outfile:
            shutil.copyfileobj(infile, outfile)

        # Read, then delete
        print(local_destination.read_text())
        local_destination.unlink()


if __name__ == "__main__":
    main()
