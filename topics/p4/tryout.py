import os

from p4 import Perforce


def main():
    os.chdir("/Users/haiv/projects/p4/sandbox")
    p4 = Perforce()
    result = p4.edit(["hello.py", "basetest.py", "foobar"], preview_only=True)
    # result = p4.edit(['foobar'])
    print(result)


if __name__ == "__main__":
    main()
