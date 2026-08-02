import pathlib

import click
import pandas as pd

from .download import download_gsheet_csv
from .shell import interactive_shell


@click.command
@click.option("-c", "--category")
@click.option("-b", "--brand")
@click.option("-r", "--retailer")
@click.option("-s", "--shell", is_flag=True)
def main(category, brand, retailer, shell):
    data_file = pathlib.Path("/tmp/pens.csv")
    if not data_file.exists():
        download_gsheet_csv(
            "https://docs.google.com/spreadsheets/d/1kKDbZYSMm44fhUAwhN5-Myqt2jlNfCK52Hp76ifPtu4/edit?gid=0",
            data_file,
        )

    df = pd.read_csv(data_file)
    df = df.sort_values(["Brand", "Model"])
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
