import argparse
import logging
from common_parser import create_logger, credential_parser


if __name__ == "__main__":
    parser = argparse.ArgumentParser(parents=[credential_parser])
    parser.add_argument("-l", "--logfile", default=None, type=create_logger)
    args = parser.parse_args(["-uhaiv"])
    logger = create_logger() if args.logfile is None else args.logfile
    logger.info("User name is %s", args.user)
