import enum
import re


class TokenKind(enum.Enum):
    ATTRIBUTE = enum.auto()
    KEY_OR_INDEX = enum.auto()


def to_slice(token: str):
    if ":" not in token:
        raise ValueError()

    slice_elements = []
    for sub_token in token.split(":"):
        if sub_token == "":
            sub_token = None
        else:
            sub_token = int(sub_token)
        slice_elements.append(sub_token)
    if not any(slice_elements):
        # There is no number in the list
        raise ValueError()
    return slice(*slice_elements)


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
                # Index
                out.append((int(token), TokenKind.KEY_OR_INDEX))
            except ValueError:
                try:
                    out.append((to_slice(token), TokenKind.KEY_OR_INDEX))
                except (ValueError, TypeError):
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
    except (KeyError, IndexError, AttributeError, TypeError):
        return default
