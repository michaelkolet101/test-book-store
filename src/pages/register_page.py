from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages import base as base

# from src.pages.login_page import Login_page
from src.models.user import User

import logging




class Register_page(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {
        "Back": (By.XPATH, '//*[@id="root"]/div/button'),
        'mail': (By.ID, 'email'),
        'password': (By.ID, 'password'),
        'firstName': (By.ID, 'firstName'),
        'lastName': (By.ID, 'lastName'),
        'submit': (By.XPATH, '//*[@id="root"]/div/form/button')
    }



    def check_page(self):

        back = self.find_element(*self.locator["Back"])
        print(back.text)
        return back.text == 'Back To Login'


    def add_new_user(self, user: User):

        mail = self.find_element(*self.locator["mail"])
        mail.send_keys(user.get_mail())

        password = self.find_element(*self.locator["password"])
        password.send_keys(user.get_password())

        name = self.find_element(*self.locator["firstName"])
        name.send_keys(user.get_first_name())

        last = self.find_element(*self.locator["lastName"])
        last.send_keys(user.get_last_name())

    def submit(self):
        btn = self.find_element(*self.locator["submit"])
        btn.click()
        return self._driver

# TODO fix that the Loging page will return
    def back(self):
        btn = self.find_element(*self.locator['Back'])
        btn.click()
        # return Login_page(self._driver)
