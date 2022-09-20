from playwright.sync_api import sync_playwright

from src.playwright_pages.base import Base_page

from src.models.user import User

import logging




class Register_page(Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver
        #super()._init_(self._driver)

    locator = {
        "Back": 'button:has-text("Back To Login")',
        'mail': '#email',
        'password': '#password',
        'firstName': '#firstName',
        'lastName': '#lastName',
        'submit': 'button:has-text("submit")'
    }

# TODO until here

    def check_page(self):

        back = self.find_element(self.locator["Back"])
        print(back.text)
        return back.text == 'Back To Login'


    def add_new_user(self, user: User):

        mail = self.find_element(self.locator["mail"])
        mail.fill(user.get_mail())

        password = self.find_element(self.locator["password"])
        password.fill(user.get_password())

        name = self.find_element(self.locator["firstName"])
        name.fill(user.get_first_name())

        last = self.find_element(self.locator["lastName"])
        last.fill(user.get_last_name())

    def submit(self):
        btn = self.find_element(self.locator["submit"])
        btn.click()
        return self._driver

# TODO fix that the Loging page will return
    def back(self):
        btn = self.find_element(self.locator['Back'])
        btn.click()

