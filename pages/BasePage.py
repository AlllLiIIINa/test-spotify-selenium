from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver=webdriver.Chrome()):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.base_url = 'https://open.spotify.com/search'

    def start_site(self):
        return self.driver.get(self.base_url)

    def find(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    def input(self, locator, text):
        return self.find(locator).send_keys(text)
