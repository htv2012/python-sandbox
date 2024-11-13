#!/usr/bin/env python3
"""
Update the .htpasswd file

Due to the restriction from the remote host, the remote user must
use sudo to read from and write to a file. There is no password for
sudo.

This script performs the following:

1. Read the contents of the htpasswd file (via sudo cat)
2. Remove the specified user's entry
3. Call openssl from the remote host to create a new password entry
4. Update the content
5. Upload that content to the remote host (via sudo cat)
"""
import contextlib
import pathlib
import shlex

import paramiko

HTPASSWD_PATH = "/tmp/htpasswd"


def main():
    config_path = pathlib.Path("~/.ssh/config").expanduser()
    config = paramiko.SSHConfig.from_path(config_path)
    # TODO: Do not hard code, use argparse for host name
    host_info = config.lookup("primary")

    with contextlib.ExitStack() as exit_stack:
        client = exit_stack.enter_context(paramiko.SSHClient())
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client.connect(
            hostname=host_info["hostname"],
            username=host_info.get("user"),
            key_filename=host_info.get("identityfile"),
        )

        _, stdout, _ = client.exec_command(f"sudo cat {HTPASSWD_PATH}")
        # 2. Remove the specified user's entry
        username = "user2"
        lines = [line for line in stdout if not line.startswith(username)]

        # 3. Call openssl from the remote host to create a new password entry
        password = "Testenv12$"
        command = shlex.join(["sudo", "openssl", "passwd", "-6", password])
        _, stdout, _ = client.exec_command(command)
        # hashed included the trailing newline, which is OK
        hashed = stdout.read().decode()

        # 4. Update the content
        lines.append(f"{username}:{hashed}")

        # 5. Upload that content to the remote host
        remote_temp_path = "/tmp/temp-htpasswd"
        with client.open_sftp() as sftp, sftp.file(remote_temp_path, "wb") as stream:
            stream.writelines(lines)
        client.exec_command(f"sudo cp {remote_temp_path} {HTPASSWD_PATH}")
        client.exec_command(f"rm -f {remote_temp_path}")


if __name__ == "__main__":
    main()
