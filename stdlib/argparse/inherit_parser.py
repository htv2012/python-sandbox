# Use a shared parser among different commands

import argparse
from common_parser import credential_parser, mysql_parser, mail_server_parser


if __name__ == "__main__":
    parser1 = argparse.ArgumentParser(parents=[credential_parser])
    parser1.add_argument("-s", "--server")
    print("Server:      ", parser1.parse_args(["-uhaiv", "-sgrumpy.local"]))

    parser2 = argparse.ArgumentParser(parents=[credential_parser, mysql_parser])
    print("MySQL server:", parser2.parse_args(["-uhaiv", "-piForgot", "-sfoo"]))

    parser3 = argparse.ArgumentParser(parents=[mail_server_parser])
    print("Mail server: ", parser3.parse_args(["-uhaiv", "-pforgot", "-sexample.com"]))
