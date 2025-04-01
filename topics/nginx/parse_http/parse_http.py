#!/usr/bin/env python3
"""Parse http file."""

import base64
import json
import pathlib
import re
import sys

import requests


def lookup(dotkey, vars_dict):
    """Given a dot key such as 'env1.metadata.uid', return its value."""
    dotkey = dotkey.replace("{", "").replace("}", "").strip()
    node = vars_dict
    for key in dotkey.split("."):
        if key not in node:
            raise KeyError(f"{dotkey}: {key} not found")
        node = node[key]
    return node


def sub(text, vars_dict):
    """Subtitude text in a template using variables."""
    pattern = re.compile(r"{{.+?}}")
    placeholders = pattern.findall(text)

    for placeholder in placeholders:
        new_value = lookup(placeholder, vars_dict)
        text = text.replace(placeholder, new_value)

    return text


def parse_var(text, vars_dict):
    """Parse variable declaration."""
    matched = re.match(r"^\s*@(\w+?)\s*=\s*(.+)\s*$", text)
    if matched:
        name, value = matched.groups()
        return {name: sub(value.strip(), vars_dict)}
    return False


def parse_name(text, vars_dict):
    """Parse the name of a request object."""
    matched = re.match(r"^\s*#\s*@name\s*(.+?)\s*$", text)
    if matched:
        name = sub(matched[1].strip(), vars_dict=vars_dict)
        return name
    return False


def parse_request(first_line, subsequent_lines, vars_dict):
    """
    Attempt to parse the request.

    If the first line does not start with GET, POST, PUT, DELETE;
    return False. Otherwise, this function will parse and return a
    dictionary with 4 keys: method, url, headers, and json (payload).
    """
    tokens = [token.strip() for token in first_line.strip().split(" ", 1)]
    if len(tokens) != 2:
        return False

    method, url = tokens
    method = method.upper()
    url = sub(url, vars_dict)

    if method not in {"GET", "POST", "PUT", "DELETE"}:
        return False

    headers = {}
    payload_text = ""
    payload = None
    in_header = True
    for line in subsequent_lines:
        if line.strip().startswith("###"):
            # Encounter the marker which ends the request
            break
        if in_header and (matched := re.match(r"^([^:]+):\s*(.+)$", line)):
            name, value = matched.groups()
            value = sub(value, vars_dict)
            if name.casefold() == "authorization":
                auth_scheme, auth = value.split(" ", 1)
                auth = auth.replace(" ", ".").encode("utf-8")
                auth = base64.b64encode(auth).decode("utf-8")
                value = f"{auth_scheme} {auth}"
            headers[name] = value
        elif in_header and line.strip() == "":
            in_header = False
        else:
            payload_text += line
            try:
                json.loads(payload_text)
            except json.JSONDecodeError:
                pass
            else:
                payload_text = sub(payload_text, vars_dict)
                payload = json.loads(payload_text)
                break

    return dict(method=method, url=url, headers=headers, json=payload)


def rest_parse(stream, vars_dict):
    """
    Given a stream in .http or .rest file format, parse the request.

    This is a generator which yield requests information.

    :stream: A text file, or any iterable of text lines such as a
        list of text, io.StringIO, ...
    :vars_dict: A dictionary which contains the variables and values
    :return: Yield a request information and a name. Each request
        information is a dictionary with the following keys: method,
        url, headers, json.
    """
    name = None
    for text in stream:
        if new_var := parse_var(text, vars_dict):
            vars_dict.update(new_var)
        elif found := parse_name(text, vars_dict):
            name = found
        elif request_info := parse_request(text, stream, vars_dict):
            yield request_info, name


def rest_exec(stream, vars_dict):
    """
    Given a stream, execute the Restful commands and yield each result.

    :stream: A text file, or any iterable of text lines such as a list
        of text, io.StringIO, ...
    :vars_dict: A dictionary which contains the variables and values
    :return: A dictionary with this format
        {
            "request": {"headers": _, "body": _, "method": _, "url": _},
            "response": {"headers": _, "body": _, "_raw": _, "status_code": _}
        }

        Note that the "_raw" value is the requests.Response object,
        which contains many useful information.
    """
    for request_info, name in rest_parse(stream, vars_dict):
        response = requests.request(**request_info, verify=False)
        setattr(response, "body", response.json())
        result = {
            "request": {
                "headers": response.request.headers,
                "body": response.request.body,
                "method": response.request.method,
                "url": response.request.url,
            },
            "response": {
                "headers": response.headers,
                "body": response.json(),
                "_raw": response,
                "status_code": response.status_code,
            },
        }
        if name is not None:
            vars_dict[name] = result
        yield result


def main():
    """Entry"""
    # data_path = pathlib.Path(__file__).with_name("reques.in.http")
    data_path = pathlib.Path("~/sandbox/rest/sample.http").expanduser()
    assert data_path.exists()

    vars_dict = {}
    with open(data_path, "r", encoding="utf-8") as stream:
        for result in rest_exec(stream, vars_dict):
            print()
            print(f"{result['request']['method']} {result['request']['url']}")
            print()
            json.dump(result["response"]["body"], sys.stdout, indent=4)


if __name__ == "__main__":
    main()
