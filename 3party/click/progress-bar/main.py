import time

import click


def main():
    with click.progressbar(range(15), label="Downloading") as bar:
        for _ in bar:
            time.sleep(0.5)


if __name__ == "__main__":
    main()
