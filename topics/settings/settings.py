"""
settings.py
"""

import collections
import os
import sys


def get_settings_location(base_filename):
    filename = os.path.expanduser("~/." + base_filename)
    return filename


def load_file(filename):
    config = {}
    if os.path.exists(filename):
        exec(compile(open(filename).read(), filename, "exec"), config)
        del config["__builtins__"]
    return config


def load(base_filename):
    """
    Load a settings file
    """
    filename = get_settings_location(base_filename)
    return load_file(filename)


class Settings(collections.MutableMapping):
    def __init__(self, base_filename=None, required=None):
        if not base_filename:
            path, filename = os.path.split(sys.argv[0])
            base_filename = os.path.splitext(filename)[0]
        self.__dict__ = load(base_filename)

        # Accounting
        self._base_filename = base_filename
        self._modified = False

        # Check for required settings
        if required is not None:
            for key in required:
                if key not in self.__dict__:
                    raise KeyError("Required key not present: " + key)

    def __delitem__(self, key):
        del self.__dict__[key]
        self._modified = True

    def __getitem__(self, key, default_value=None):
        return self.__dict__.get(key, default_value)

    def __iter__(self):
        return iter({k: v for k, v in self.__dict__.items() if not k.startswith("_")})

    def __len__(self):
        return len([k for k in self.__dict__ if not k.startswith("_")])

    def __setitem__(self, key, value):
        self.__dict__[key] = value
        self._modified = True

    def __contains__(self, key):
        return key in self.__dict__

    def __str__(self):
        result = "\n".join(
            "{} = {}".format(k, repr(v))
            for k, v in list(self.__dict__.items())
            if not k.startswith("_")
        )
        return result

    def __repr__(self):
        return "<Settings {}>".format(self._base_filename)

    def save(self):
        """
        Save the settings to the configuration file if modified.
        """
        print("Saving...")
        # if not self._modified: return
        filename = get_settings_location(self._base_filename)
        print("File:", filename)
        with open(filename, "wb") as f:
            f.write(self.__str__())
