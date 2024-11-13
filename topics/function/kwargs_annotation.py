#!/usr/bin/env python3
"""
Annotate kwargs using TypedDict
"""

import logging
import logging.config
import pathlib
from typing import NotRequired, TypedDict, Unpack

logging.config.fileConfig(pathlib.Path(__file__).with_name("logging.ini"))


class ConnectionParameters(TypedDict):
    port: NotRequired[int]
    username: NotRequired[str]
    password: NotRequired[str]


def connect(host: str, **kwargs: Unpack[ConnectionParameters]):
    kwargs = ConnectionParameters(kwargs)

    logging.debug("host: %r", host)
    logging.debug("port: %r", kwargs.get("port"))
    logging.debug("username: %r", kwargs.get("username"))
    logging.debug("password: %r", kwargs.get("password"))
    logging.debug("---")


connect("myhost")
connect("myhost", port=8888, username="root", password="i4Got")
