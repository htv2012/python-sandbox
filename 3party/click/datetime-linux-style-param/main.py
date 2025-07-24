import datetime

import click

from clicklib import LinuxDateTimeParamType


def test_end_time_callback(ctx, param, test_end_time):
    if test_end_time is None:
        return None

    if test_end_time < datetime.datetime.now():
        test_end_time += datetime.timedelta(days=1)
    return test_end_time


@click.command
@click.option(
    "--test-end-time", type=LinuxDateTimeParamType(), callback=test_end_time_callback
)
def main(test_end_time):
    print(f"{test_end_time = }")


if __name__ == "__main__":
    main()
