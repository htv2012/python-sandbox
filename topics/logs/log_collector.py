#!/usr/bin/env python3
import contextlib

import paramiko


class LinesCollector:
    """
    Collect lines from a file that are added since the creation of this object
    Usage:
        collector = LinesCollector(...)
        # Some time later...
        for line in collector:
            # Do something with those lines
    """

    def __init__(self, host, path, username, password, port=22):
        self.host = host
        self.path = path
        self.username = username
        self.password = password
        self.port = port

        try:
            with self.open_sftp() as sftp:
                stat = sftp.stat(self.path)
                self.start = stat.st_size
        except FileNotFoundError:
            # File does not exist now, it might later
            self.start = 0

    @contextlib.contextmanager
    def open_sftp(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, self.port, self.username, self.password)

        # Using ExitStack to automatically close sftp and ssh in reverse
        # order
        with contextlib.ExitStack() as stack:
            sftp = ssh.open_sftp()
            stack.enter_context(ssh)
            stack.enter_context(sftp)
            yield sftp

    def __iter__(self):
        try:
            with self.open_sftp() as sftp, sftp.open(self.path) as stream:
                stream.seek(self.start)
                yield from stream
                self.start = stream.tell()
        except FileNotFoundError:
            # File does not exist, return an empty iterable
            self.start = 0
            return iter([])


if __name__ == "__main__":
    import time

    lc = LinesCollector("mercury.local", "/tmp/log.txt", "haiv", None)

    # Add lines
    with lc.open_sftp() as sftp, sftp.open(lc.path, "a") as stream:
        stream.write("Roses are red\n")
        stream.write("Violets are blue\n")

    for line in lc:
        print(line, end="")

    # Add more lines
    with lc.open_sftp() as sftp, sftp.open(lc.path, "a") as stream:
        stream.write("Sugar are sweet\n")
        stream.write("Not for the diabetes\n")

    print("Take a rest")
    time.sleep(3)

    for line in lc:
        print(line, end="")
