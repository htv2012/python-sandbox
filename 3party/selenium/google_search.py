import selenium.webdriver

from google import GoogleHome


with selenium.webdriver.Chrome() as driver:
    driver.get("https://www.google.com")
    google = GoogleHome(driver)
    google.search("best toaster oven 2020")
    import time
    time.sleep(5)

