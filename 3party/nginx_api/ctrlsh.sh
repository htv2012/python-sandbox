#!/usr/bin/env python3
"""Ctrl Shell."""
import argparse
import cmd
import contextlib
import json
import logging
import shlex
import shutil
import subprocess
import tempfile
import types
import urllib3

import requests


PATH_ENVIRONMENT = "services/environments"


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()


def show_json(data):
    jq = shutil.which("jq")
    text = json.dumps(data, indent=4, sort_keys=True)
    if jq is None:
        print(text)
        return

    subprocess.run(["jq", "."], input=text, encoding="utf-8")


class NginxApi:
    def __init__(self, symbols):
        self.symbols = symbols
        self.session = requests.Session()
        self.session.verify = False

    def login(self):
        url = self._url("platform/login")
        LOGGER.info(
            "Logging in using email %r and password %r",
            self.symbols.ctrl_admin_email,
            self.symbols.ctrl_admin_pass,
        )
        LOGGER.info("URL=%r", url)
        assert url == "https://52.38.180.93/api/v1/platform/login"
        assert not self.session.verify
        payload = {
            "credentials": {
                "username": self.symbols.ctrl_admin_email,
                "password": self.symbols.ctrl_admin_pass,
                "type": "BASIC",
            }
        }
        response = self.session.post(url, json=payload)
        response.raise_for_status()

    def get(self, path):
        url = self._url(path)
        response = self.session.get(url)
        return response

    def create_environment(self, payload):
        url = self._url(PATH_ENVIRONMENT)
        response = self.session.post(url=url, json=payload)
        return response

    def _url(self, path):
        path = path.strip("/")
        url = f"https://{self.symbols.control_host_ips[0]}/api/v1/{path}"
        return url


class Shell(cmd.Cmd):
    prompt = "ctrlsh> "

    def __init__(self, api, completekey="tab", stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        self.api = api

    def do_env(self, args):
        """Perform actions on environments."""
        tokens = shlex.split(args)
        subcmd = tokens.pop(0)
        method = getattr(self, f"env_{subcmd}", None)
        if method is None:
            print(f"env sub-command not found: {subcmd}")
            return
        method(*tokens)

    def env_list(self, *args):
        """List the environments."""
        response = self.api.get(PATH_ENVIRONMENT)
        output = response.json()
        for entry in output["items"]:
            print(entry["metadata"]["name"])

    def env_get(self, *args):
        """Get a particular environment."""
        response = self.api.get(f"{PATH_ENVIRONMENT}/{args[0]}")
        show_json(response.json())

    def env_create(self, *args):
        """Create an environment."""
        temp_file = tempfile.NamedTemporaryFile(suffix=".json", delete=False)
        temp_file.close()
        payload = {
            "metadata": {
                "name": "env_name",
                "displayName": "My Environment",
                "description": "This is a test environment",
                "tags": ["tag1", "tag2"],
            },
            "desiredState": {},
        }
        with open(temp_file.name, "w", encoding="utf-8") as stream:
            json.dump(payload, stream, indent=4)
        subprocess.run(["vim", temp_file.name])

        with open(temp_file.name, "r", encoding="utf-8") as stream:
            payload = json.load(stream)

        response = self.api.create_environment(payload)
        show_json(response.json())

    def emptyline(self) -> bool:
        pass

    def do_exit(self, args):
        return True

    # Aliases
    do_q = do_exit
    do_quit = do_exit
    do_EOF = do_exit


def main():
    """Entry"""
    urllib3.disable_warnings()

    parser = argparse.ArgumentParser()
    parser.add_argument("symbols_file")
    options = parser.parse_args()

    with open(options.symbols_file, encoding="utf-8") as stream:
        symbols = json.load(stream)
        symbols = types.SimpleNamespace(**symbols)

    api = NginxApi(symbols)
    api.login()
    shell = Shell(api)
    shell.cmdloop()


if __name__ == "__main__":
    main()
