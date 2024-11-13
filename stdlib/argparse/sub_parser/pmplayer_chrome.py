import argparse


def configure_parser(parser):
    parser.add_argument(
        "url",
        help="URL to play using Chrome"
    )


def play(options):
    print(f"Play via chrome with URL: {options.url}")
