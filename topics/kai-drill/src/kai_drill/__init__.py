import re


def path_split(path: str):
    pattern = re.compile(
        r"""
        \[\d+\]                     # List index
        |
        \[[a-zA-Z_][a-zA-Z0-9_]*\]  # Dictionary key
        |
        \.[a-zA-Z_]+                # Object attribute
        """,
        re.VERBOSE,
    )

    tokens = pattern.findall(path)
    out = []
    for token in tokens:
        if "[" in token:
            token = token[1:-1]
            try:
                # List Index
                out.append((int(token), "index"))
            except ValueError:
                # Dictionary key
                out.append((token, "key"))
        else:
            token = token[1:]
            out.append((token, "attribute"))

    return out


def kai(obj, path, default=None):
    if isinstance(path, str):
        path = path.split(".")

    # out = obj
    # for name in path:
