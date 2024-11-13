#!/usr/bin/env python3
import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "you-will-never-guess-this")
