#!/usr/bin/env python

# Opens simple1.ini, simple2.ini and get a couple of settings

from configparser import SafeConfigParser


def showSection(config, section):
    print()
    print("[%s]" % section)
    print("host: %s" % config.get(section, "host"))
    print("port: %d" % config.getint(section, "port"))
    print("user: %s" % config.get(section, "user"))
    print("password: %s" % config.get(section, "password"))


# Create a new parser object
config = SafeConfigParser()

# Read from the first configuration file and display
config.read("simple1.ini")
showSection(config, "server1")
showSection(config, "server2")

# Read additional configuration and display
config.read("simple2.ini")
showSection(config, "server3")
