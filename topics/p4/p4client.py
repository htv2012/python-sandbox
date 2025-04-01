#!/usr/bin/env python
import marshal
import subprocess
from pprint import pprint


class P4Client(object):
    def __init__(self):
        command = "p4 -G client -o".split()
        pipe = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pipe.wait()
        client_info = marshal.load(pipe.stdout)
        client_info["views"] = dict(
            v.replace("/...", "").split() for k, v in client_info.items() if "View" in k
        )
        pprint(client_info)
        self.__dict__ = {
            k.lower(): v for k, v in client_info.items() if "View" not in k
        }

    def __repr__(self):
        return "{0}({1!r})".format(self.__class__.__name__, self.client)


if __name__ == "__main__":
    c = P4Client()
    print(c)
