#!/usr/bin/env python3
import json
import logging
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

logging.basicConfig(level=os.getenv("LOGLEVEL", "WARN"))
LOGGER = logging.getLogger(__name__)

with open("restconf.json") as stream:
    data = json.load(stream)


def get_data(data, path):
    path = path.replace("/restconf/data", "")
    path = path.strip("/")
    keys = path.split("/")

    from pudb import set_trace

    set_trace()  # xyz
    for key in path.split("/"):
        data = data.get(key, {})

    return data


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global data

        self.send_response(200)
        self.send_header("content-type", "application/yang-data+json")
        self.end_headers()

        result = get_data(data, self.path)
        result = json.dumps(data, indent=4, sort_keys=True)
        result = result.encode("utf-8")

        self.wfile.write(result)


if __name__ == "__main__":
    server_address = ("0.0.0.0", 8008)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
