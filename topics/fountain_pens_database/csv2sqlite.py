import csv
import pathlib
import sqlite3


def text2numeric(text):
    """Convert '$1,000.00' to 1000."""
    text = text.replace("$", "").replace(",", "")
    number = float(text)
    return number


def main():
    """Entry"""
    input_path = pathlib.Path(__file__).with_name("data.csv")
    with open(input_path, mode="r", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        # entries = [row for row in reader if row["Category"] == "Fountain Pen"]
        entries = list(reader)
        for entry in entries:
            entry["Price"] = text2numeric(entry["Price"])

    # Create a new database
    output_path = input_path.with_name("data.sqlite")
    output_path.unlink(missing_ok=True)
    with sqlite3.connect(output_path) as connection:
        connection.execute(
            """
            CREATE TABLE entry (
                Category TEXT,
                Brand TEXT,
                Model TEXT,
                Color TEXT,
                Note TEXT,
                Nib TEXT,
                Date TEXT,
                Price REAL,
                Retailer TEXT
            )
            """
        )
        connection.executemany(
            "INSERT into entry "
            "(Category, Brand, Model, Color, Note, Nib, Date, Price, Retailer) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (tuple(entry.values()) for entry in entries),
        )


if __name__ == "__main__":
    main()
