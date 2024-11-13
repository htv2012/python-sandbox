#!/usr/bin/env python3
"""
Demo: capture_output vs stdout/stderr
"""
import pathlib
import subprocess

def main():
    """ Entry """
    script = str(pathlib.Path(__file__).with_name("out_err_write.py"))

    print("\n# Omit capture_output, or capture_output=False")
    subprocess.run([script])

    print("\n# capture_output=True")
    completed_process = subprocess.run([script], capture_output=True, encoding="utf-8")
    # Explicitly prints stdout, stderr
    print(f"stdout: {completed_process.stdout!r}")
    print(f"stderr: {completed_process.stderr!r}")

    print("\n# Hide stderr")
    subprocess.run([script], stderr=subprocess.PIPE)

    print("\n# Hide stdout")
    subprocess.run([script], stdout=subprocess.PIPE)


if __name__ == '__main__':
    main()
