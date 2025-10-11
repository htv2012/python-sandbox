from .plural import format_count

__all__ = ["format_count", "main"]


def main():
    data = [
        (5, "monkey"),
        (1, "bucket"),
        (0, "tumbler"),
        (3, "vase"),
        (380, "meter"),
        (1, "meter"),
    ]
    for count, word in data:
        print(format_count(count, word))
