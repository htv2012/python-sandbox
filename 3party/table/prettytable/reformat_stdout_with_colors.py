#!/usr/bin/env python3
"""
Reformat stdout using pretty table
"""

from tablelib import tsv_table


class Colors:
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    RED = "\033[91m"
    YELLOW = "\033[93m"

    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def banner(text: str):
    print()
    print("#")
    print(f"# {text}")
    print("#")
    print()

def colorize(text: str):
    lookup = {
        "Passed": Colors.GREEN,
        "Failed": Colors.RED,
        "Blocked": Colors.MAGENTA,
        "Passed with warnings": Colors.YELLOW,
    }
    color = lookup.get(text, "")
    if color:
        text = f"{color}{text}{Colors.RESET}"
    return text


def show_results(results):
        print("Test\tResult")
        for name, result in results:
            result = colorize(result)
            print(f"{name}\t{result}")
def main():
    """Entry"""
    results = [
        ("Check Connection", "Passed"),
        ("Check Banner", "Passed"),
        ("Check User Login", "Failed"),
        ("Check Cookies", "Blocked"),
        ("Check Endpoints", "Passed with warnings"),
    ]

    banner("Raw Output")
    show_results(results)

    banner("Formatted Output")
    with tsv_table():
        show_results(results)


if __name__ == "__main__":
    main()
