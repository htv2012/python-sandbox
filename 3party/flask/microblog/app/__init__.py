#!/usr/bin/env python3
import os
import logging

from flask import Flask

from config import Config


logging.basicConfig(level=os.getenv("LOGLEVEL", "WARN"))
LOGGER = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
