#!/usr/bin/env python
from collections import Counter
from subprocess import PIPE, Popen


def count_git_status():
    command = ["git", "status", "--porcelain"]
    pipe = Popen(command, stdout=PIPE, encoding="utf-8")
    status = Counter(line.split()[0] for line in pipe.stdout)
    return status


def git_branch():
    command = ["git", "branch", "--list"]
    pipe = Popen(command, stdout=PIPE, encoding="utf-8")
    return next(
        (x.split()[1] for x in pipe.stdout if x.startswith("* ")), "unknown branch"
    )


def main():
    status = count_git_status()
    print("Untracked: {}".format(status["??"]))
    print("Modified:  {}".format(status["M"]))
    print("Deleted:   {}".format(status["D"]))
    print("Branch:    {}".format(git_branch()))


if __name__ == "__main__":
    main()
