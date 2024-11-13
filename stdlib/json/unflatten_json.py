import itertools
import re

KEYS_PATTERN = re.compile(
    r"""
    (                  # Start group
        \[\d+\]        # Matches numeric indices, such as "[2]", "[10]"
        |              # or
        [a-zA-Z0-9 ]+  # Match words
    )                  # End group
    """,
    flags=re.VERBOSE,
)


def set_value(node, key_path, value):
    key_path = _split_key(key_path)
    keys, next_keys = itertools.tee(key_path)
    next_key = next(next_keys, None)

    for key, next_key in zip(keys, next_keys):
        node = _create_node(node, key, next_key)

    leaf = next_key
    if isinstance(leaf, int):
        while len(node) < leaf + 1:
            node.append(None)
        node[leaf] = value
    else:
        node[leaf] = value


def unflatten(dict_obj: dict) -> dict:
    out = {}
    for key_path, value in dict_obj.items():
        set_value(out, key_path, value)
    return out


def _create_node(node, key, next_key):
    if isinstance(next_key, int):
        next_node = []
    else:
        next_node = {}

    if isinstance(node, dict):
        return node.setdefault(key, next_node)
    else:
        node.append(next_node)
        return next_node


def _split_key(key_path: str) -> list:
    """Split a key path into a list of keys.

    Keys are separated by dots. If a key is in the form "[<number>]",
    then it will be converted to int. For example, "[2]" will be
    convert to 2. Here are a few examples:

    >>> _split_key("metadata.tags[0]")
    ['metadata', 'tags', 0]

    >>> _split_key( "useCases[2].templateGroupRef.ref")
    ['useCases', 2, 'templateGroupRef', 'ref']
    """

    def parse_key(key: str):
        if "[" not in key:
            return key

        key = key.removeprefix("[").removesuffix("]").strip()
        return int(key)

    keys = [parse_key(key) for key in KEYS_PATTERN.findall(key_path)]
    return keys
