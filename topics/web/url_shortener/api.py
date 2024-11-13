#!/usr/bin/env python
"""
A list of favorite songs for karaoke with search
"""
import csv
import locale
import logging
import json
import os
import pathlib
import re
import unicodedata

from flask import (
    Flask,
    render_template,
    request,
)
from flask_restful import Resource, Api


os.environ["LOGLEVEL"] = "DEBUG"
logging.basicConfig(level=os.getenv("LOGLEVEL", "WARN"))
LOGGER = logging.getLogger("shortie")
SHORT_LIST = [
    {'short': 'kfav', 'long': 'http://167.172.199.218:3000/'},
    {'short': 'paramiko', 'long': 'https://docs.paramiko.org/en/stable/'},
    {'short': 'flaskrest', 'long': 'https://flask-restful.readthedocs.io/en/latest/'},
]

class Shorties(Resource):
    def get(self, short=None):
        if short is None:
            return SHORT_LIST

        for d in SHORT_LIST:
            if d['short'] == short:
                return d
        return {'error': 'not found'}


def main():
    """
    The back-end entry point
    """
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Shorties, '/s', '/s/<string:short>')
    app.run(
        host="0.0.0.0",
        port=3001,
        debug=True,
    )


if __name__ == "__main__":
    main()
