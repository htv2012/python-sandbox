#!/usr/bin/env python
"""
Simple exercise of dotenv
"""
import os

import dotenv


if __name__ == "__main__":
    # Load without altering the env var
    vars = dotenv.dotenv_values()
    print("\n# Return value for dotenv_values()")
    print(f"  vars = {vars}")

    print("\n# Before calling load_dotenv()")
    print(f"  user = {os.getenv('user')}")

    print("\n# After calling load_dotenv()")
    dotenv.load_dotenv()
    print(f"  user = {os.getenv('user')}")
