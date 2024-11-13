#!/usr/bin/env python3
"""
Upload a file
"""
import pathlib
import stat

import paramiko

if __name__ == "__main__":
    # Track the local file
    local_path = pathlib.Path(__file__).resolve().parent / "dumps" / "mlc"
    if not local_path.exists():
        raise SystemExit("mlc tool is not found")

    # Connect to the remote host
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(
        "34.217.104.203",
        username="ec2-user",
        key_filename="/home/haiv/.ssh/aws-haiv-20190713.pem",
    )

    # Upload file and fix up the permission
    sftp = client.open_sftp()
    remote_path = "/tmp/mlc"
    attributes = sftp.put(local_path, remote_path)
    mode = attributes.st_mode | stat.S_IXUSR
    sftp.chmod(remote_path, mode)
