# Use a shared parser among different commands

import argparse
from common_parser import (
    create_common_parser,
    ALL_OPTIONS,
    SERVER_PORT_OPTIONS,
    COMMON_OPTIONS,
)

if __name__ == "__main__":
    print("parser1:", create_common_parser().parse_args(["-uhaiv"]))
    print(
        "parser2:",
        create_common_parser(ALL_OPTIONS).parse_args(
            ["-server=foo.bar", "-uhaiv", "-pforgotten1"]
        ),
    )

    parser = create_common_parser(SERVER_PORT_OPTIONS)
    parser.add_argument("-q", "--quiet", action="store_true", default=False)
    print(
        "parser3:",
        parser.parse_args(
            ["-uhaiv", "-pforgotten1", "-sfoo.bar", "--port=3306", "--quiet"]
        ),
    )

    # A different way to use create_common_parser()
    parser = argparse.ArgumentParser(
        prog="parser4", add_help=False, parents=[create_common_parser()]
    )
    parser.add_argument("-q", "--quiet", action="store_true", default=False)
    print("parser4:", parser.parse_args(["-uhaiv"]))
