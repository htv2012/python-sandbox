import csv
import pathlib

import pandas as pd
import requests

data_file = pathlib.Path("/tmp/pens.csv")
sheet_id = "1kKDbZYSMm44fhUAwhN5-Myqt2jlNfCK52Hp76ifPtu4"


def download_google_sheet(sheet_id: str, output_filename: str):
    export_url = (
        f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=0"
    )

    # Download content
    response = requests.get(export_url)
    if not response.ok:
        raise SystemExit("Failed to download data file")

    # Save to local CSV file
    with open(output_filename, "wb") as f:
        f.write(response.content)


def normalize_row(row):
    row["Price"] = float(row["Price"].removeprefix("$").replace(",", "") or "0")
    row["Country"] = row["Country"] or "Unknown"
    return row


def normalize_csv(path: pathlib.Path):
    with open(path) as stream:
        reader = csv.DictReader(stream)
        rows = [normalize_row(row) for row in reader]

    with open(path, "w") as stream:
        writer = csv.DictWriter(stream, reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def read(force_download: bool = False) -> pd.DataFrame:
    """Read the data and return a data frame.

    :param force_download: If true, force download, default is false
    :return: A Pandas data frame

    """
    if force_download or not data_file.exists():
        download_google_sheet(sheet_id, data_file)

    normalize_csv(data_file)
    df = pd.read_csv(data_file)
    df = df.sort_values(["Brand", "Model"])
    return df
