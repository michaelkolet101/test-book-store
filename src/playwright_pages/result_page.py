import requests
from playwright.sync_api import sync_playwright

from api.authors_api import Authors_api
from src.models.Author import Author
from src.playwright_pages.base import Base_page
from src.playwright_pages.login_page import *
from src.models.user import User
from src.playwright_pages.authore_info_page import Authore_info_page
import logging


class Result_page(Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver

    locator = {
        'authors_list': '.author-container',
        'info': 'button:has-text("To Author Page")'
    }

    def check_page(self):
        back = self.find_element(self.locator["Back"])
        print(back.inner_text())
        return back.inner_text() == 'Back To Login'

    def author_info(self):
        info = self.find_element(self.locator["info"])
        info.click()
        return Authore_info_page(self._driver)



