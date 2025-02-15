"""
https://stackoverflow.com/q/79437778/459745

Display a progress bar while uploading file to a remote host
"""

import contextlib
import pathlib
import subprocess

import paramiko
import tqdm


def main():
    hostname = "ssh-sandbox"
    local_path = "/tmp/big"

    config = paramiko.config.SSHConfig()
    config_path = pathlib.Path("~/.ssh/config").expanduser()
    config = paramiko.config.SSHConfig.from_path(config_path)

    if hostname not in config.get_hostnames():
        raise SystemExit(f"{hostname} not found in ~/.ssh/config")
    cfg = config.lookup(hostname=hostname)

    subprocess.run(["truncate", "-s", "1GB", local_path])

    with contextlib.ExitStack() as stack:
        conn = stack.enter_context(paramiko.SSHClient())
        conn.load_system_host_keys()
        conn.connect(cfg["hostname"], username=cfg["user"])
        sftp = stack.enter_context(conn.open_sftp())

        inf = stack.enter_context(open(local_path, "rb"))
        outf = stack.enter_context(sftp.file(local_path, "wb"))
        pbar = stack.enter_context(tqdm.tqdm(total=inf.seek(0, 2), unit="bytes"))
        inf.seek(0, 0)

        # Read & write in chunks
        chunk_size = 10 * 1024 * 1024
        while chunk := inf.read(chunk_size):
            outf.write(chunk)
            pbar.update(chunk_size)


if __name__ == "__main__":
    main()
