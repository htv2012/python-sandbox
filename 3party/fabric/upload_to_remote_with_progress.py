"""
Upload file with progress bar
"""

import contextlib
import os

import fabric
import tqdm


class Progress:
    def __init__(self, bar):
        self.sofar = 0
        self.bar = bar

    def update(self, sofar, _):
        delta = sofar - self.sofar
        self.sofar = sofar
        self.bar.update(delta)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_instance, exception_traceback):
        self.bar.close()


def main():
    hostname = "ssh-sandbox"
    local_path = "/tmp/big"

    config = fabric.Config()
    if hostname not in config.base_ssh_config.get_hostnames():
        raise SystemExit(f"{hostname} not found in ~/.ssh/config")

    with contextlib.ExitStack() as stack:
        conn = stack.enter_context(fabric.Connection(host=hostname))
        sftp = stack.enter_context(conn.sftp())
        conn.local(f"truncate -s 1GB {local_path}")  # Create large local file
        progress = stack.enter_context(
            Progress(tqdm.tqdm(total=os.stat(local_path).st_size, unit="bytes"))
        )
        sftp.put(
            "/tmp/big",
            "/tmp/big",
            callback=progress.update,
        )

        # Clean up
        conn.local("rm /tmp/big")
        conn.run("rm /tmp/big")


if __name__ == "__main__":
    main()
