import csv
import pathlib
import re

import pandas as pd
import requests

data_file = pathlib.Path("/tmp/pens.csv")
data_url = "https://docs.google.com/spreadsheets/d/1kKDbZYSMm44fhUAwhN5-Myqt2jlNfCK52Hp76ifPtu4/edit?gid=0"


def download_google_sheet(url: str, output_filename: str, gid: str = "0"):
    # Extract the Document ID using regex
    match = re.search(r"/d/([a-zA-Z0-9-_]+)", url)
    if not match:
        raise ValueError("Invalid Google Sheet URL format.")

    sheet_id = match.group(1)

    # Check if a specific sheet tab (gid) is included in the URL
    gid_match = re.search(r"gid=([0-9]+)", url)
    if gid_match:
        gid = gid_match.group(1)

    # Construct direct download URL
    export_url = (
        f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    )

    # Download content
    response = requests.get(export_url)
    response.raise_for_status()  # Check for errors (e.g., 404 or 403)

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


def read(force: bool = False):
    """Read the data and return a data frame"""
    if force or not data_file.exists():
        download_google_sheet(data_url, data_file)

    normalize_csv(data_file)
    df = pd.read_csv(data_file)
    df = df.sort_values(["Brand", "Model"])
    return df
