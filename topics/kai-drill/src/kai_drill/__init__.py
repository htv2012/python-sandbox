import enum
import re


class TokenKind(enum.Enum):
    ATTRIBUTE = enum.auto()
    KEY_OR_INDEX = enum.auto()


def split_path(path: str):
    pattern = re.compile(
        r"""
        \[[^\]]+\]       # Dictionary key or list index
        |                # or
        \.[a-zA-Z0-9_]+  # Object attribute
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
                out.append((int(token), TokenKind.KEY_OR_INDEX))
            except ValueError:
                out.append((token, TokenKind.KEY_OR_INDEX))
        else:
            token = token.removeprefix(".")
            out.append((token, TokenKind.ATTRIBUTE))

    return out


def kai(obj, path, default=None):
    out = obj
    try:
        for name, kind in split_path(path):
            if kind == TokenKind.KEY_OR_INDEX:
                out = out[name]
            elif kind == TokenKind.ATTRIBUTE:
                out = getattr(out, name)
        return out
    except (KeyError, IndexError, AttributeError):
        return default
