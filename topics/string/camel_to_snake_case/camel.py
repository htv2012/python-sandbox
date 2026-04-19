import string

CAPS = string.ascii_uppercase


def camel2snake(text: str) -> str:
    text_len = len(text)
    out = ""

    for i, ch in enumerate(text):
        if (
            i != 0  # Exclude first char
            and i + 1 != text_len  # Exclude last char
            and ch in CAPS  # Cap that is...
            and not (
                text[i - 1] in CAPS  # not preceded by cap and...
                and text[i + 1] in CAPS  # not followed by cap
            )
        ):
            ch = "_" + ch
        out += ch.lower()
    return out
