import contextlib
import subprocess

import click


class LinuxDateTimeParamType(click.DateTime):
    def convert(self, value, param, ctx):
        with contextlib.suppress(click.BadParameter):
            return super().convert(value, param, ctx)

        # The above failed, try parsing with the Linux date command
        process = subprocess.run(
            ["date", "-d", value, "+%Y-%m-%dT%H:%M:%S"], text=True, capture_output=True
        )
        new_value = process.stdout.strip()
        return super().convert(new_value, param, ctx)
