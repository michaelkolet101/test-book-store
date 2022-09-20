from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Base_page:
    def __init__(self, driver: webdriver):
        self._driver = driver



    def find_element(self, by_find, token, wait=30):
        elem = WebDriverWait(self._driver, wait).until(EC.presence_of_element_located((by_find, token)))
        return elem

    def find_elements(self, by_find, token):
        elements = self._driver.find_elements(by_find, token)
        return elements


