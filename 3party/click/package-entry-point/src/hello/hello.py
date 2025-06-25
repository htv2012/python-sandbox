import click

@click.command
@click.option("-s", "--server")
@click.option("-p", "--port", type=int, default=2200)
def main(server, port):
    print(f"{server=}")
    print(f"{port=}")

if __name__ == "__main__":
    main()

