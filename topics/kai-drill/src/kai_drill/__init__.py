import re


def path_split(path: str):
    pattern = re.compile(
        r"""
        \[\d+\]                     # List index
        |
        \[[^\]]+\]  # Dictionary key
        |
        \.[a-zA-Z0-9_]+             # Object attribute
        """,
        re.VERBOSE,
    )

    # Clean up the path, add leading dot if needed
    if path[0] != "[" and path[0] != ".":
        path = "." + path

    tokens = pattern.findall(path)
    out = []
    for token in tokens:
        if "[" in token:
            token = token[1:-1]
            try:
                out.append((int(token), "index"))
            except ValueError:
                out.append((token, "key"))
        else:
            token = token.removeprefix(".")
            out.append((token, "attribute"))

    return out


def kai(obj, path, default=None):
    if isinstance(path, str):
        path = path.split(".")

    # out = obj
    # for name in path:
