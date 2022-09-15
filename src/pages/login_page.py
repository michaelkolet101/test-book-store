from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages import base as base
from src.pages.register_page import Register_page
from src.models.user import *
from src.pages.welcome_page import *



class Login_page(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {
        "register": (By.XPATH, '//*[@id="root"]/div/button'),
        "mail": (By.ID, 'email'),
        "password": (By.ID, 'password'),
        'submit': (By.XPATH, '//*[@id="root"]/div/form/button')
    }


    def click_register(self):
        btn = self.find_element(*self.locator['register'])
        btn.click()
        return Register_page(self._driver)

    def check_page(self):
        btn = self.find_element(*self.locator["register"])
        print(btn.text)
        return btn.text == 'Register!'


    def submit(self, user: User):

        # find and fill mail
        mail = self.find_element(*self.locator["mail"])
        mail.send_keys(user.get_mail())

        # find and fill password
        password = self.find_element(*self.locator["password"])
        password.send_keys(user.get_password())

        # find submit btn and click it
        btn = self.find_element(*self.locator["submit"])
        btn.click()

        return Welcome_page(self._driver)

