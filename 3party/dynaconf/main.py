#!/usr/bin/env python3
"""
A Python skeleton script
"""
from config import settings


def main():
    """ Entry """
    # From the main config, settings.toml
    print(f"server: {settings.server!r}")
    print(f"port: {settings.port}")
    print(f"ex_factor: {settings.ex_factor!r}")

    # From .env file
    print(f"from_dotenv: {settings.from_dotenv!r}")

    # From a secret file, .secrets.toml
    print(f"password: {settings.password!r}")

    # Settings are callable
    assert settings.password == settings("password")

    # Settings are like a dict
    assert settings.password == settings["password"]


if __name__ == "__main__":
    main()

