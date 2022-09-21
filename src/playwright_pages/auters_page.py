import requests
from src.playwright_pages.base import Base_page
from playwright.sync_api import sync_playwright


from api.authors_api import Authors_api
from src.models.Author import Author

from src.playwright_pages.login_page import *
from src.models.user import User

import logging


class Auters_page(Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver

    locator = {
        'authors_list': '.author-container'
    }

    def check_page(self):
        back = self.find_element(self.locator["Back"])
        print(back.text)
        return back.text == 'Back To Login'


    def get_authors_count(self, authors: Authors_api):
        return len(authors.get_all_auters())


    def cheack_authoers(self, authors: Authors_api):

        authors_list = self.find_elements(self.locator['authors_list'])

        count = 0
        for item in authors_list:
            count = count + 1
            logging.info(item.inner_text())

        logging.info(f'my_count {count}')
        logging.info(f'count in db {self.get_authors_count(authors)}')
        count_in_db = self.get_authors_count(authors)

        assert count_in_db == count

    def find_author(self, author: Author):

        authors_list = self.find_elements(self.locator['authors_list'])
        check = False
        for item in authors_list:
            logging.info(author.get_name())
            logging.info(item.inner_text())

            if author.get_name() in item.inner_text():
                check = True
                break
        return check

