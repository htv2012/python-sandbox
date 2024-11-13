#!/usr/bin/env python3
"""
Demo: Redirect stdout
"""
import contextlib
import io


def main():
    """Entry"""
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        print("this text goes to stdout")
    print(f"After redirection, captured text is: {stdout.getvalue()!r}")


if __name__ == "__main__":
    main()
