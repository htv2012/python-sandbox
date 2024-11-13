#!/usr/bin/env python3
"""
A simple invoke example
"""
import invoke


def main():
    """Entry"""
    result = invoke.run("ls")
    print("\nresult")
    for name in [
        "stdout",
        "stderr",
        "encoding",
        "command",
        "shell",
        "exited",
        "pty",
        "hide",
    ]:
        print(f"  .{name}={getattr(result, name)!r}")


if __name__ == "__main__":
    main()
