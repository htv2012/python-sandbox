#!/usr/bin/env python3
"""
Aggregated Settings tryout
"""

import os

from settings import Settings

APP_DEFAULTS = {"verbose": True}


def main():
    settings = Settings.from_mixed_sources(
        os.environ,
        "per_user.yaml",
        "system_wide.yaml",
        APP_DEFAULTS,
    )

    print(f"User: {settings.user}")
    print(f"Password: {settings.password}")
    print(f"Server: {settings.server}")
    print(f"Port: {settings.port}")
    print(f"Verbose: {settings.verbose}")
    print(f"Home: {settings.HOME}")


if __name__ == "__main__":
    main()
