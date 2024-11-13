"""
main
"""
import argparse

from . import pmplayer_chrome, pmplayer_safari


def main():
    # This parser is common to all players
    common_parser = argparse.ArgumentParser(add_help=False)
    common_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="Add plenty of logging",
    )
    common_parser.add_argument(
        "-d",
        "--duration",
        type=int,
        default=10,
    )
    common_parser.add_argument(
        "-e",
        "--env",
        choices=["stage", "prod"],
        default="stage",
    )

    parser = argparse.ArgumentParser("driver")
    actions = parser.add_subparsers(dest="player")
    actions.required = True

    # Configure chrome
    chrome_action = actions.add_parser("chrome", parents=[common_parser])
    pmplayer_chrome.configure_parser(chrome_action)

    # Configure Safari
    safari_action = actions.add_parser("safari", parents=[common_parser])
    pmplayer_safari.configure_parser(safari_action)

    # Parse
    options = parser.parse_args()
    print(options)

    if options.player == "chrome":
        pmplayer_chrome.play(options)
    else:
        pmplayer_safari.play(options)


if __name__ == "__main__":
    main()
