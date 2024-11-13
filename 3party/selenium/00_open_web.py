#!/usr/bin/env python
import time

from selenium import webdriver


browser = webdriver.Chrome()
with browser:
    browser.get("https://www.selenium.dev/selenium/docs/api/py/index.html")
    time.sleep(10)
