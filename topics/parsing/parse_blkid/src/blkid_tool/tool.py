# tool.py
import contextlib
import csv
import subprocess


def parse_block(text: str):
    reader = csv.reader(text.splitlines(), delimiter="=")
    block = {}
    for key, value in reader:
        with contextlib.suppress(ValueError):
            value = int(value)
        block[key] = value
    return block


def get_block_devices():
    completed_process = subprocess.run(
        ["blkid", "--output", "udev"], capture_output=True, text=True
    )
    blocks = completed_process.stdout.split("\n\n")
    block_devices = [parse_block(text) for text in blocks]
    return block_devices
