from .plural_rules import plural

__all__ = ["main", "plural"]


def main():
    data = [
        (5, "monkey"),
        (1, "bucket"),
        (0, "tumbler"),
        (3, "vase"),
        (380, "meter"),
        (1, "meter"),
        (2, "match(es)"),
        (2, "child|children"),
    ]
    for count, word in data:
        print(plural(count, word))
