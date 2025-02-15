"""
Upload file with progress bar
"""

import contextlib
import os

import fabric
import tqdm


def main():
    hostname = "ssh-sandbox"

    config = fabric.Config()
    if hostname not in config.base_ssh_config.get_hostnames():
        raise SystemExit(f"{hostname} not found in ~/.ssh/config")

    with contextlib.ExitStack() as stack:
        conn = stack.enter_context(fabric.Connection(host=hostname))
        sftp = stack.enter_context(conn.sftp())
        conn.local("truncate -s 1GB /tmp/big")
        pbar = stack.enter_context(tqdm.tqdm(total=os.stat("/tmp/big").st_size))
        sftp.put(
            "/tmp/big",
            "/tmp/big",
            callback=lambda sofar, total: pbar.update(sofar - pbar.n),
        )

        # Clean up
        conn.local("rm /tmp/big")
        conn.run("rm /tmp/big")


if __name__ == "__main__":
    main()
