import re

PLACEHOLDER_PATTERN = re.compile(
    r"""
    {{
        \s*
        (.+?)
        \s*        
    }}
    """,
    re.VERBOSE,
)


class Template:
    def __init__(self, **mappings):
        self.mappings = mappings

    def expand(self, text: str):
        new_text = PLACEHOLDER_PATTERN.sub(self.replace, text)
        return new_text

    def replace(self, match: re.Match) -> str:
        dot_key = match[1]
        new_value = self.lookup(dot_key)
        return new_value

    def lookup(self, dot_key: str) -> str:
        node = self.mappings
        for key in dot_key.split("."):
            try:
                node = node[key]
            except TypeError:
                node = getattr(node, key)
        return node
