#!/usr/bin/env python
import selenium.webdriver
from selenium.webdriver.common.keys import Keys


browser = selenium.webdriver.Chrome()
# browser.get("https://www.yahoo.com/")
browser.get("https://www.google.com/")

search_box = browser.find_element_by_name("q")
search_box.send_keys("seleniumhq" + Keys.RETURN)
