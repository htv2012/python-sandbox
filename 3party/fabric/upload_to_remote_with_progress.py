"""
Upload file with progress bar
"""

import contextlib
import os

import fabric
import tqdm


@contextlib.contextmanager
def progress_bar(bar):
    sofar = 0

    def update(new_sofar, _):
        nonlocal sofar
        delta = new_sofar - sofar
        bar.update(delta)
        sofar = new_sofar
    
    with bar:
        yield update

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
            progress_bar(tqdm.tqdm(total=os.stat(local_path).st_size, unit="bytes"))
        )
        sftp.put(
            "/tmp/big",
            "/tmp/big",
            callback=progress,
        )

        # Clean up
        conn.local("rm /tmp/big")
        conn.run("rm /tmp/big")


if __name__ == "__main__":
    main()
