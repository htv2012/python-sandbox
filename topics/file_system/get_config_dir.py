#!/usr/bin/env python
import os
import platform

_local_config_dir = None


def get_config_dir():
    global _local_config_dir

    if _local_config_dir is None:
        system = platform.system()
        if system == "Windows":
            _local_config_dir = os.getenv("LOCALAPPDATA")
        elif system == "Linux" or system == "Darwin":
            _local_config_dir = os.path.expanduser("~/.config")
        else:
            raise NotImplementedError("Not yet implemented for %s" % system)

    return _local_config_dir


if __name__ == "__main__":
    print((get_config_dir()))
