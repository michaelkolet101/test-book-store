from playwright.sync_api import sync_playwright

from src.playwright_pages.welcome_page import Welcome_page
from src.playwright_pages.base import Base_page
from src.playwright_pages.register_page import Register_page
from src.models.user import *

import logging


logging.basicConfig(level=logging.INFO)
my_logger = logging.getLogger()


class Login_page(Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver

    locator = {
        "register": 'xpath=//*[@id="root"]/div/button',
        "mail": '#email',
        "password": '#password',
        'submit': 'xpath=//*[@id="root"]/div/form/button',
        'login_btn': 'xpath=//*[@id="root"]/nav/div/div/a[3]',
        'logout_btn': 'xpath=//*[@id="root"]/nav/div/div/button',
        'bookstore': 'text=Book Store',
        'store': 'text=Store'
    }


    def click_register(self):
        btn = self.find_element(self.locator['register'])
        btn.click()
        return Register_page(self._driver)

    def check_page(self):
        btn = self.find_element(self.locator["register"])
        print(btn.inner_text())
        return btn.inner_text() == 'Register!'


    def submit(self, user: User):

        login_btn = self.find_element(self.locator["login_btn"])
        logging.info(login_btn.inner_text())
        assert 'Log In' == login_btn.inner_text()


        # find and fill mail
        mail = self.find_element(self.locator["mail"])
        mail.fill(user.get_mail())

        # find and fill password
        password = self.find_element(self.locator["password"])
        password.fill(user.get_password())

        # find submit btn and click it
        btn = self.find_element(self.locator["submit"])
        btn.click()
        return Welcome_page(self._driver)

    def bookstore(self):
        bookstore_btn = self.find_element(self.locator["bookstore"])
        bookstore_btn.click()
        return Welcome_page(self._driver)

    def store(self):
        store_btn = self.find_element(self.locator["store"])
        store_btn.click()
        return Welcome_page(self._driver)