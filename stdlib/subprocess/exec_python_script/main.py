#!/usr/bin/env python3
"""How to properly invoke a Python executable and run another python script."""
import pathlib
import subprocess
import sys


script = pathlib.Path(__file__).with_name("child.py")
command = [sys.executable, str(script)]
print("Running:")
print(" ".join(command))

completed_process = subprocess.run(
    command,
    encoding="utf-8",
    capture_output=True,
)

print("Output:")
print(completed_process.stdout)
