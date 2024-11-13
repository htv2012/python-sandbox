#!/usr/bin/env python3
"""
Demo: changes to chain map will be applied to the first dict
"""
from collections import ChainMap


def main():
    """Entry"""
    app_default = {
        "server": "1.2.3.4",
        "port": 1111,
        "username": "app-user",
    }

    global_settings = {
        "username": "global-app-user",
    }

    custom_settings = {
        "username": "custom-user",
    }

    settings = ChainMap(custom_settings, global_settings, app_default)
    settings["servers"] = "9.9.9.9"
    print(f"app_default={app_default}")
    print(f"global_settings={global_settings}")
    print(f"custom_settings={custom_settings}")


if __name__ == "__main__":
    main()
