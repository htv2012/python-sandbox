#!/usr/bin/env python3
"""
1Password tryout
"""

import collections
import json
import logging
import os
import subprocess

CLI = "op"


logging.basicConfig(level=os.getenv("LOGLEVEL", "WARN"))
LOGGER = logging.getLogger(__name__)


class NestedDict(collections.Mapping):
    def __init__(self, dic):
        for key, value in dic.items():
            value = NestedDict.make(value)
            setattr(self, key, value)

    def __iter__(self):
        return iter(x for x in self.__dict__ if not x.startswith("_"))

    def __getitem__(self, key):
        return self.__dict__[key]

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        kv = ", ".join("{}={!r}".format(k, v) for k, v in list(self.items()))
        result = "{}({})".format(self.__class__.__name__, kv)
        return result

    @classmethod
    def make(cls, data):
        LOGGER.debug(f"make {data!r}")
        if isinstance(data, collections.abc.Mapping):
            return cls(data)
        elif isinstance(data, list):
            return [cls.make(element) for element in data]
        else:
            return data


class Item(NestedDict):
    """
    Some of the fields are: overview.title, username, password, url
    """

    def __init__(self, dict_object):
        super(Item, self).__init__(dict_object)
        self._raw = dict_object

        # Setup the fields
        for field_info in self.details.fields:
            setattr(self, field_info["name"], field_info["value"])


def cli_installed():
    try:
        subprocess.run(CLI, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False


if not cli_installed():
    raise RuntimeError(
        "This library requires the command line interface for 1Password installed"
    )


class OnePassword:
    """1Password API"""

    def __init__(self, url: str, email: str, secret_key: str):
        """
        Create a new 1Password API

        :param url: The URL, e.g. 'https://my.1password.com'
        :param email: The email of the account
        :param secret_key: The secret key which, e.g. 'A3-...'
        """
        self.url = url
        self.email = email
        self.secret_key = secret_key
        self._session_id = None

    @property
    def session_id(self) -> str:
        """
        Return the session ID by signing into the 1Password service.
        The session ID will be cached for subsequent reads

        :return: A session ID
        """
        if self._session_id is None:
            command = (
                f"op signin {self.url} {self.email} {self.secret_key} --raw".split()
            )
            self._session_id = subprocess.check_output(
                command, encoding="utf-8"
            ).strip()
        return self._session_id

    def get_item(self, name):
        """
        Get an item from 1Password

        :param name: The title or the UUID of the item
        :return: The item
        """
        command = f"op --session {self.session_id} get item {name}".split()
        output = subprocess.check_output(command, encoding="utf-8")
        output = json.loads(output)
        item = Item.make(output)
        return item


def get_item(url: str, email: str, secret_key: str, name: str) -> Item:
    """
    A function version of OnePassword.get_item

    :param url: The URL, e.g. 'https://my.1password.com'
    :param email: The email of the account
    :param secret_key: The secret key which, e.g. 'A3-...'
    :param name: The title or the UUID of the item
    :return: The item
    """
    one_password = OnePassword(url, email, secret_key)
    item = one_password.get_item(name)
    return item
