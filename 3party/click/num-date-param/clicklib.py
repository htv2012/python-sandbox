import contextlib
import datetime

import click


class EndConditionParamType(click.DateTime):
    """
    Click parameter type for end condition.

    This parameter type accepts ether an int, which represents the number
    of runs; or a date/time, which represents the end time. If the end
    time occurs in the past, then we move it forward to the next day.
    """

    name = "end_condition"

    def __init__(self):
        # Init with a list of acceptable format strings
        super().__init__(
            (
                "%H:%M",
                "%H:%M:%S",
                "%Y-%m-%d %H:%M",
                "%Y-%m-%d %H:%M-%S",
            )
        )

    def convert(self, value, param, ctx):
        # Parse as int
        with contextlib.suppress(ValueError):
            return int(value)

        # Parse as date/time
        date_time = super().convert(value, param, ctx)

        # Date not specified, assume today's
        if (date_time.year, date_time.month, date_time.day) == (1900, 1, 1):
            now = datetime.datetime.now()
            date_time = date_time.replace(year=now.year, month=now.month, day=now.day)

            # time in the past? Move forward 1 day
            if date_time < now:
                date_time += datetime.timedelta(days=1)

        return date_time
