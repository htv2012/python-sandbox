import io
from typing import List, Optional


def exception_group(base):
    class ExceptionGroup(base):
        def __init__(self, message, exceptions: Optional[List[Exception]] = None):
            self.message = message
            self.exceptions = exceptions or []

        def __str__(self):
            buf = io.StringIO()
            buf.write(f"{self.message}\n")
            for exc in self.exceptions:
                buf.write(f"- {exc}\n")
            return buf.getvalue()

    return ExceptionGroup


AssertionGroup = exception_group(AssertionError)


def main():
    try:
        raise AssertionGroup(
            "Out of Milk",
            [
                AssertionError("foo"),
                AssertionError("bar"),
            ],
        )
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
