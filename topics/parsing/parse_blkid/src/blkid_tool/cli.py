# cli.py

import rich

from . import get_block_devices


def main():
    blocks = get_block_devices()
    rich.print_json(data=blocks, indent=4)
