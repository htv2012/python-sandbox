import re

import requests


def download_gsheet_csv(url: str, output_filename: str, gid: str = "0"):
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
