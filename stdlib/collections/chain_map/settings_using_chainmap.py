#!/usr/bin/env python3
"""Use ChainMap to store settings.

Consider an app's settings, which could come from the following:

- In app. These are settings that are in the app itself
- System defaults. These are the per-system defaults
- User defaults

The user defaults will override the system defaults. Likewise, the
system defaults will override the in-app defaults. New settings,
however are written into the user-defaults space. This is exactly
what ChainMap does.
"""
import collections


def main():
    """Perform script."""
    print("\n# Initial state")
    app_defaults = {"indent": "tab", "tab_width": 8}
    system_defaults = {"indent": "as_is"}
    user_defaults = {}
    settings = collections.ChainMap(user_defaults, system_defaults, app_defaults)
    print(f"{app_defaults=}")
    print(f"{system_defaults=}")
    print(f"{user_defaults=}")

    print("\n# Initial settings")
    print(f"indent: {settings['indent']}")
    print(f"tab_width: {settings['tab_width']}")

    print("\n# The user modifies the indent and tab_width")
    settings["indent"] = "space"
    settings["tab_width"] = 4
    print(f"indent: {settings['indent']}")
    print(f"tab_width: {settings['tab_width']}")

    print("\n# Final state")
    print(f"{app_defaults=}")
    print(f"{system_defaults=}")
    print(f"{user_defaults=}")


if __name__ == "__main__":
    main()
