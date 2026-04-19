#!/usr/bin/env python

from string import Template


def main():
    who = "Tim"
    what = "chicken"
    template = Template("$who likes $what")

    print(template.substitute(locals()))
    print(template.substitute(who="Anne", what="Apple"))


if __name__ == "__main__":
    main()
