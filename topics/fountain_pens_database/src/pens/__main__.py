import click

from . import data
from .shell import interactive_shell


@click.command
@click.option("-f", "--force-download", is_flag=True, default=False)
@click.option("-c", "--category")
@click.option("-b", "--brand")
@click.option("-r", "--retailer")
@click.option("-s", "--shell", is_flag=True)
def main(force_download, category, brand, retailer, shell):
    df = data.read(force_download=force_download)
    if shell:
        interactive_shell(df)
        return

    if category:
        df = df[df["Category"] == category]
    if brand:
        df = df[df["Brand"] == brand]
    if retailer:
        df = df[df["Retailer"] == retailer]
    df = df.reset_index(drop=True)

    print(df.to_string())


if __name__ == "__main__":
    main()
