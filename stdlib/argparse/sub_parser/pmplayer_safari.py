import argparse


def configure_parser(parser):
    parser.add_argument(
        "url",
        help="URL to play using Safari"
    )
    parser.add_argument(
        "-u", "--user",
        required=True,
        help="login user"
    )
    parser.add_argument(
        "-p", "--password",
        required=True,
        help="login password"
    )


def play(options):
    print(f"Play via Safari with URL: {options.url}")
    print(f"  User: {options.user}")
