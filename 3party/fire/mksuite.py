#!/usr/bin/env python
import fire


def main(*suites, name=None):
    print(f"suites: {suites}")
    print(f"name: {name}")


if __name__ == '__main__':
    fire.Fire(main)
