#!/usr/bin/env python3
import enum
import shlex
import subprocess


class Status(enum.Enum):
    UNKNOWN = enum.auto()
    PENDING = enum.auto()
    OK = enum.auto()
    FAILED = enum.auto()
    CANCELED = enum.auto()


class Response:
    def __init__(self, proc: subprocess.Popen):
        self.proc = proc
        self.code = None

    def __repr__(self):
        return f"{self.__class__.__name__}(status={self.status!r}, code={self.code!r})"

    @property
    def status(self) -> Status:
        self.code = self.proc.poll()
        if self.code is None:
            return Status.PENDING
        elif self.code < 0:
            return Status.CANCELED
        elif self.code == 0:
            return Status.OK
        else:
            return Status.FAILED

    def wait(self, timeout: int = -1):
        self.proc.communicate(timeout=None if timeout == -1 else timeout)
        return self.status


class Exec:
    def run(self, command):
        if isinstance(command, str):
            args = shlex.split(command)
        else:
            args = list(command)

        proc = subprocess.Popen(
            args=args,
            text=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
        )
        return Response(proc)
