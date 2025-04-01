"""
Sandbox for registry stuff
"""

import winreg
from pprint import pprint


def get_values(hive, path):
    top_key = winreg.OpenKey(hive, path)

    ret = dict()
    _, VALUES_COUNT, _ = winreg.QueryInfoKey(top_key)
    for i in range(VALUES_COUNT):
        name, value, _ = winreg.EnumValue(top_key, i)
        ret[name] = value
    return ret


if __name__ == "__main__":
    pprint(
        get_values(winreg.HKEY_CURRENT_USER, "Software\\Tableau\\Tableau near\\Prompts")
    )
