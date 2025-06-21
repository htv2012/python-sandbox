from config import get_config

__all__ = [
    "get_config",
    "main",
    "parent",
    "Foo",
]


def main() -> None:
    print("Hello from sample-project!")


def parent():
    def child():
        pass

    return child


class Foo:
    def __init__(self):
        pass

    def do_foo(self):
        pass
