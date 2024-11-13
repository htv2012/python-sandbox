"""Demo values conversion to bool, int, ..."""

import configparser

import box


def main():
    """Entry"""
    config = configparser.ConfigParser()
    config.read("data/config.ini")
    config_box = box.ConfigBox({name: dict(value) for name, value in config.items()})

    print(f"server = {config_box.options.server}")
    print(f"port = {config_box.options.int('port')}")
    print(f"verbose = {config_box.options.bool('verbose')}")
    print(f"max_width = {config_box.options.int('max_width')}")


if __name__ == "__main__":
    main()
