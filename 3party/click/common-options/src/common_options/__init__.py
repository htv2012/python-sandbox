import click


@click.group()
def main() -> None:
    pass


def common_server(fn):
    options = [
        click.option("-s", "--server", help="Host or IP of the server"),
        click.option("-p", "--port", type=int, help="Port number"),
    ]

    for option in reversed(options):
        fn = option(fn)

    return fn


@main.command
@common_server
def up(server, port):
    """Upload to a server"""
    print(f"Upload to {server}:{port}")


@main.command
@common_server
def down(server, port):
    """Download from a server"""
    print(f"Download from {server}:{port}")
