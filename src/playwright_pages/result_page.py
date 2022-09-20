import requests
from playwright.sync_api import sync_playwright
from src.playwright_pages.base import Base_page
from api.authors_api import Authors_api
from src.models.Author import Author
from src.pages import base as base
from src.pages.login_page import *
from src.models.user import User

import logging


class Result_page(Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {
        'authors_list': '.author-container'
    }

    def check_page(self):
        back = self.find_element(self.locator["Back"])
        print(back.inner_text())
        return back.inner_text() == 'Back To Login'


