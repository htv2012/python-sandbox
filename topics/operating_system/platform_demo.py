#!/usr/bin/env python
# encoding: utf-8
"""
platform_demo.py
Created by Hai Vu on 2012-10-25.
Demo: using the platform module
"""
from __future__ import print_function
import platform


def main():
    print("architecture          =", platform.architecture())
    print("libc_ver              =", platform.libc_ver())
    print("machine               =", platform.machine())
    print("mac_ver               =", platform.mac_ver())
    print("node                  =", platform.node())
    print("platform              =", platform.platform())
    print("processor             =", platform.processor())
    print("python_branch         =", platform.python_branch())
    print("python_build          =", platform.python_build())
    print("python_compiler       =", platform.python_compiler())
    print("python_implementation =", platform.python_implementation())
    print("python_revision       =", platform.python_revision())
    print("python_version        =", platform.python_version())
    print("python_version_tuple  =", platform.python_version_tuple())
    print("release               =", platform.release())
    print("system                =", platform.system())
    print("uname                 =", platform.uname())
    print("version               =", platform.version())
    print("win32_ver             =", platform.win32_ver())


if __name__ == "__main__":
    main()
