#!/usr/bin/env python3
"""
Demo: implement the "in" operator for a class
"""


class LogEntry:
    def __init__(self, level, message):
        self.level = level
        self.message = message

    def __contains__(self, term):
        return term in self.message

    def __str__(self):
        return f"{self.level}: {self.message}"


def main():
    log_entry = LogEntry("DEBUG", "x = 35")
    print(log_entry)
    print("Is 35 in the log entry?", "35" in log_entry)


if __name__ == "__main__":
    main()
