#!/usr/bin/env python

import configparser


class Configuration(object):
    @classmethod
    def from_ini(cls, config_parser):
        """
        Create a new instance given a RawConfigParser() object or and of
        its subclasses
        """
        configuration = cls()

        for section_name in config_parser.sections():
            section = Configuration()
            for kv in config_parser.items(section_name):
                setattr(section, *kv)
            setattr(configuration, section_name, section)

        return configuration


SERVER_REPORT = """Host: {0.host}
Port: {0.port}
User: {0.user}
Password: {0.password}
"""


if __name__ == "__main__":
    ini = configparser.ConfigParser()
    ini.read("data/ini2nestedobj.ini")
    configuration = Configuration.from_ini(ini)

    print(SERVER_REPORT.format(configuration.test1))
    print(SERVER_REPORT.format(configuration.test2))
