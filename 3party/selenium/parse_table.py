#!/usr/bin/env python
import collections
import time

from selenium import webdriver


User = collections.namedtuple("User", "uid,alias,shell")


def extract_rows(table, cast=tuple):
    """
    Given a table object, returns its contents

    :param table: a WebElement which represents a table
    :param cast: A type cast for each row
    :return: A list of rows, where each row is a tuple or a cast
    """
    rows = iter(table.find_elements_by_tag_name("tr"))
    next(rows)

    rows = [
        cast(cell.text for cell in row.find_elements_by_tag_name("td"))
        for row in rows
    ]
    return rows

driver = webdriver.Safari()
with driver:
    driver.get("file:///Users/hvu/Projects/sandbox/python/3party/selenium/table.html")
    table = driver.find_element_by_id("users")
    rows = extract_rows(table, cast=User._make)
    for row in rows:
        print(row)

    time.sleep(2)
