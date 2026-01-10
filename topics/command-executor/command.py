#!/usr/bin/env python3
import shlex
import subprocess


class Response:
    def __init__(self, proc: subprocess.Popen):
        self.proc = proc
        self._state = None


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
