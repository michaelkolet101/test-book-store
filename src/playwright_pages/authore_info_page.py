import requests
from playwright.sync_api import sync_playwright

from api.authors_api import Authors_api
from src.models.Author import Author
from src.playwright_pages.base import Base_page
from src.playwright_pages.login_page import *
from src.models.user import User

import logging


class Authore_info_page(Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver

    locator = {
        'book_container': '.book-container'
    }

    def check_page(self):
        back = self.find_element(self.locator["Back"])
        print(back.inner_text())
        return back.inner_text() == 'Back To Login'

    def has_abook(self, book_name :str) -> bool:
        flag = False

        container = self.find_element(self.locator['book_container'])
        logging.info(container.inner_text())
        return True

    def refresh(self):
        self._driver.reload()



