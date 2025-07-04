import click
import time


def main():
    steps = [f"step {i}" for i in range(15)]
    with click.progressbar(steps) as bar:
        for step in bar:
            time.sleep(0.5)


if __name__ == "__main__":
    main()
