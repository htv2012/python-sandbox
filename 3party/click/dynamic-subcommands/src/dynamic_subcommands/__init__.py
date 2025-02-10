import importlib
import pathlib
import types

import click

__all__ = ["main"]


class Api:
    def get(self):
        click.echo("Get is under construction")

    def put(self):
        click.echo("Put is under construction")


class MyGroup(click.Group):
    def list_commands(self, ctx: click.Context):
        root = pathlib.Path(__file__).parent / "commands"
        commands = [path.stem.removeprefix("cmd_") for path in root.glob("cmd_*.py")]
        return sorted(commands)

    def get_command(self, ctx: click.Context, name):
        try:
            mod = importlib.import_module(f"dynamic_subcommands.commands.cmd_{name}")
            return mod.main
        except ModuleNotFoundError:
            ctx.fail(f"There is no command: {name}")


@click.command(cls=MyGroup)
@click.pass_context
def main(ctx: click.Context):
    ctx.ensure_object(types.SimpleNamespace)
    ctx.obj.api = Api()
