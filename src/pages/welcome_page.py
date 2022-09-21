from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages import base as base
from src.pages.register_page import Register_page
from src.pages.auters_page import Auters_page
from src.pages.result_page import Result_page
import time

from src.models.user import *
from src.models.book import *
from api.book_api import *
import logging

logging.basicConfig(level=logging.INFO)
my_logger = logging.getLogger()


class Welcome_page(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {
        "welcome": (By.XPATH, '//*[@id="root"]/div/h1'),
        'books_container': (By.CLASS_NAME, 'book-container'),
        'book-container': (By.CLASS_NAME, 'book-container'),
        'btn_buy': (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div[2]/button'),
        'login_btn': (By.LINK_TEXT, 'Log In'),
        'src_box': (By.ID, 'searchtext'),
        'search_btn': (By.CLASS_NAME, 'btn-outline-success'),
        'Authors': (By.LINK_TEXT, 'Authors')
    }


    def chack_page(self):

        flag = False
        try:
            res = self.find_element(*self.locator['welcome'])
            flag = True
        except:
            res = self.find_element(*self.locator['login_btn'])

        logging.info(res.text)
        assert flag



    def buy_book(self, book: Book, books: Book_api):
        logging.info(book.get_name())
        count_of_books_before = books.get_book_byId(book.get_id()).get_amountInStock()
        logging.info(count_of_books_before)

        buy_btn = self.find_element(*self.locator['btn_buy'])
        buy_btn.click()
        time.sleep(3)

        count_of_books_after = books.get_book_byId(book.get_id()).get_amountInStock()
        logging.info(count_of_books_after)

        assert count_of_books_after + 1 == count_of_books_before






    def auters(self):
        authors_btn = self.find_element(*self.locator['Authors'])
        authors_btn.click()
        return Auters_page(self._driver)

    def login(self):
        login_btn = self.find_element(*self.locator['login_btn'])
        login_btn.click()
        return self._driver

    def search(self, test_to_search: str) -> Result_page:
        search_box = self.find_element(*self.locator['src_box'])
        search_box.send_keys(test_to_search)

        search_btn = self.find_element(*self.locator['search_btn'])
        search_btn.click()
        search_btn.click()
        return Result_page(self._driver)