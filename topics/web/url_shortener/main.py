#!/usr/bin/env python
"""
A list of favorite songs for karaoke with search
"""
import csv
import locale
import logging
import os
import pathlib
import re
import unicodedata

from flask import Flask, render_template, request
from flask_restful import Resource, Api

# import qrcode

# import network

from api import Shorties


os.environ["LOGLEVEL"] = "DEBUG"
logging.basicConfig(level=os.getenv("LOGLEVEL", "WARN"))
LOGGER = logging.getLogger("shortie")
STATIC_DIR = pathlib.Path(__file__).parent.resolve() / "static"
PORT = 3001

def generate_url_qrcode(text, filename):
    """
    Generates the QR code for the text
    """
    img = qrcode.make(text)
    img.save(filename)


app = Flask(__name__)
api = Api(app)
api.add_resource(Shorties, '/api', '/api/<string:short>')


@app.route("/")
def index():
    """
    The web entry point
    """
    # title = request.args.get("title", "")
    # author = request.args.get("author", "")

    # rows = [row for row in ROWS if match(title, row[SEARCHABLE_TITLE])]
    # rows = [row for row in rows if match(author, row[SEARCHABLE_AUTHOR])]

    # LOGGER.debug("title=%r, author=%r", title, author)
    # result = render_template(
    #     "index.html",
    #     header=HEADER,
    #     rows=rows,
    # )
    # return result
    return "hello world"


def main():
    """
    The back-end entry point
    """
    # public_ip = network.public_ip()
    # if public_ip is not None:
    #     url = f"http://{public_ip}:{PORT}/"
    # else:
    #     url = "Ask Hai for the URL"

    # generate_url_qrcode(url, "static/site_qrcode.png")
    # LOGGER.debug(f"Serving on {url}")

    # try:
    #     LOGGER.debug("Set locale to vi_VN")
    #     locale.setlocale(locale.LC_COLLATE, "vi_VN")
    # except locale.Error:
    #     LOGGER.debug("Set locale failed")

    # with open("favorites.csv") as stream:
    #     reader = csv.DictReader(stream)
    #     HEADER = reader.fieldnames
    #     ROWS = list(reader)

    # for row in ROWS:
    #     row[SEARCHABLE_TITLE] = strip_accents(row[TITLE])
    #     row[SEARCHABLE_AUTHOR] = strip_accents(row[AUTHOR])

    app.run(
        host="0.0.0.0",
        port=PORT,
        debug=True,
    )


if __name__ == "__main__":
    main()
