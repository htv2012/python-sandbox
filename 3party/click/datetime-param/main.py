import datetime

import click


def datetime_to_time_callback(ctx, param, datetime_obj):
    if datetime_obj is None:
        return None

    time_obj = datetime.time(
        hour=datetime_obj.hour,
        minute=datetime_obj.minute,
        second=datetime_obj.second,
    )
    return time_obj


@click.command
@click.option(
    "--time",
    type=click.DateTime(formats=("%H:%M", "%H:%M:%S")),
    callback=datetime_to_time_callback,
)
def main(time):
    print(f"time = {time}, repr: {time!r}")


if __name__ == "__main__":
    main()
