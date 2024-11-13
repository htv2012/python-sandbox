import argparse
import logging


config_parser = argparse.ArgumentParser(add_help=False)
config_parser.add_argument('-c', '-config_file',
    help='location of the configuration file')

credential_parser = argparse.ArgumentParser(add_help=False)
credential_parser.add_argument("-u", "--user")
credential_parser.add_argument("-p", "--password")

mysql_parser = argparse.ArgumentParser(add_help=False)
mysql_parser.add_argument("-s", "--server", required=True)
mysql_parser.add_argument("-P", "--port", type=int, default=3306)

mail_server_parser = argparse.ArgumentParser(add_help=False, parents=[credential_parser])
mail_server_parser.add_argument("-s", "--server", required=True)
mail_server_parser.add_argument("--tls", action="store_true", default=False)


def common_ports_to_number(port_name):
    common_ports = {"ftp":21, "ssh":22}
    return common_ports.get(port_name, port_name)

#
# Create test parser
#

arguments = {
    "user":     {"flags": ("-u", "--user"),     "kw": {}},
    "password": {"flags": ("-p", "--password"), "kw": {}},
    "server":   {"flags": ("-s", "--server"),   "kw": {}},
    "port":     {"flags": ("-P", "--port"),     "kw": {"type": int}}
}
COMMON_OPTIONS = ["user", "password"]
SERVER_PORT_OPTIONS = COMMON_OPTIONS + ["server", "port"]
ALL_OPTIONS = COMMON_OPTIONS + ["server", "port"]


def create_common_parser(option_list=None, **kws):
    global ALL_OPTIONS, COMMON_OPTIONS
    global arguments

    if option_list is None:
        option_list = COMMON_OPTIONS

    parser = argparse.ArgumentParser(**kws)
    for option_name in option_list:
        argument = arguments.get(option_name)
        if argument is None: continue
        parser.add_argument(*argument["flags"], **argument["kw"])

    return parser


def create_logger(filename=None):
    '''
    Create a logger that log to the console, if a filename is supplied, log to that file
    as well.
    '''
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create console handler and set appropriate level
    ch = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)-8s %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Create a file handler and set appropriate level
    if filename is not None:
        fh = logging.FileHandler(filename=filename, mode='w')
        fformatter = logging.Formatter(
            '%(asctime)s;%(filename)s;%(lineno)d;%(levelname)s;%(message)s',
            "%Y-%m-%d %H:%M:%S")
        fh.setFormatter(fformatter)
        logger.addHandler(fh)

    return logger
