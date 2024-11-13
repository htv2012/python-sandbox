#!/usr/bin/env python3
import sshtools


def main():
    config = sshtools.parse_config()
    host_info = config.lookup("nuc")
    with sshtools.open_sftp(
        path="/tmp/foo.txt",
        mode="r",
        hostname=host_info["hostname"],
        username=host_info["user"],
        look_for_keys=True,
    ) as handle:
        buffer = handle.read()
        buffer = buffer.decode("utf-8")
        print(buffer)


if __name__ == "__main__":
    main()
