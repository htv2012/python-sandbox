"""
https://stackoverflow.com/q/79437778/459745

Display a progress bar while uploading file to a remote host
"""

import contextlib

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

        inf = stack.enter_context(open("/tmp/big", "rb"))
        outf = stack.enter_context(sftp.file("/tmp/big", "wb"))
        pbar = stack.enter_context(tqdm.tqdm(total=inf.seek(0, 2)))
        inf.seek(0, 0)

        # Read & write in chunks
        chunk_size = 10 * 1024 * 1024
        while chunk := inf.read(chunk_size):
            outf.write(chunk)
            pbar.update(chunk_size)

        # Clean up
        conn.run("rm /tmp/big")


if __name__ == "__main__":
    main()
