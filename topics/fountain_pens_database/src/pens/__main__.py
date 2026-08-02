from .download import download_gsheet_csv
def main():
    download_gsheet_csv(
        "https://docs.google.com/spreadsheets/d/1kKDbZYSMm44fhUAwhN5-Myqt2jlNfCK52Hp76ifPtu4/edit?gid=0",
        "data.csv",
    )


if __name__ == "__main__":
    main()
