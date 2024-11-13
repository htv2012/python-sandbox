#!/usr/bin/env python
import os
import platform
import subprocess

command = [os.path.abspath('./notify.py'), '9']
print(command)
subprocess.call(command, shell=platform.system()=='Windows')
