#!/usr/bin/env python

import argparse
import configparser

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config", nargs="+")
    args = parser.parse_args("trivial.ini extension.ini more.ini".split())

    cfg = configparser.ConfigParser()
    cfg.read(args.config)

    admin = "admin"
    model_basic = "model basic"

    print("basename:", cfg.get(admin, "basename"))
    print("defaults:", cfg.defaults())
    print("{}: {}".format(admin, cfg.items(admin)))
    print("{}: {}".format(model_basic, cfg.items(model_basic)))
