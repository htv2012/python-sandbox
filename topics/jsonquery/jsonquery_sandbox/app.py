#!/usr/bin/env python3
import config
from flask import Flask

app = Flask(__name__)
app.config.from_object(config)
