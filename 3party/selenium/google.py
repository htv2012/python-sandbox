from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class GoogleHome:
    def __init__(self, driver):
        self.driver = driver

        # Waits for the search box
        wait = WebDriverWait(self.driver, 10)
        self.search_box = wait.until(
            ec.presence_of_element_located((By.NAME, "q"))
        )

    def search(self, text):
        self.search_box.send_keys(text)
        self.search_box.send_keys("\n")
