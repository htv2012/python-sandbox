#!/usr/bin/env python3
import tabulate


def main():
    """Entry"""
    data = dict(
        uid=(501, 502, 503),
        alias=("peter", "paul", "mary"),
        shell=("zsh", "bash", "dash"),
    )
    print(tabulate.tabulate(data, headers="keys"))


if __name__ == "__main__":
    main()
