#!/usr/bin/env python
import fileinput
import subprocess


def pb_copy(text):
    process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    process.stdin.write(text)
    process.stdin.close()
    process.wait()


def main():
    """ Entry """
    text = '\n'.join(fileinput.input())
    pb_copy(text)


if __name__ == '__main__':
    main()
