from collections import Mapping


class ChainMap(Mapping):
    def __init__(self, *maps):
        self._maps = maps
        self._keys = set()
        for mapping in self._maps:
            self._keys.update(list(mapping.keys()))

    def __getitem__(self, key):
        for mapping in self._maps:
            if key in mapping:
                return mapping[key]
        raise KeyError("Key not found: {}".format(key))

    def __iter__(self):
        return iter(self._keys)

    def __len__(self):
        return len(self._keys)

    def __getattr__(self, name):
        return self[name]


if __name__ == "__main__":
    default_options = {
        "dry_run": False,
        "verbose": False,
        "branch": "main",
        "max_len": 5,
    }
    config_file_options = {
        "branch": "core-dev",
    }
    command_line_options = {
        "max_len": 10,
        "verbose": True,
    }

    options = ChainMap(command_line_options, config_file_options, default_options)

    for item in options.items():
        print("{}: {}".format(*item))
