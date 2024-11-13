#!/usr/bin/env python
import pathlib
import shutil

import paramiko


def main():
    global name, value, hk
    # Make a copy and don't touch the original
    original = pathlib.Path("~/.ssh/known_hosts").expanduser()
    copy = pathlib.Path("/tmp/known_hosts")
    shutil.copy(original, copy)

    # Load the known_hosts copy
    hk = paramiko.hostkeys.HostKeys(copy)

    for name, value in hk.items():
        print(f"\n{name}")
        print(f"{value}")

    hk.pop("bitbucket.org", default=None)
    hk.save(copy.with_name("known_hosts2"))


if __name__ == "__main__":
    main()
