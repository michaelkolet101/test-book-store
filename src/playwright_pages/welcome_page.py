import time

from playwright.sync_api import sync_playwright

from src.playwright_pages.base import Base_page
from src.pages.register_page import Register_page
from src.playwright_pages.auters_page import Auters_page
from src.playwright_pages.result_page import Result_page


from src.models.user import *
from src.models.book import *
from api.book_api import *
import logging

logging.basicConfig(level=logging.INFO)
my_logger = logging.getLogger()


class Welcome_page(Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver

    locator = {
        "welcome": 'h1',
        'logout': 'button:has-text("Log Out")',
        'books_container': '.book-container',
        'book-container': '.book-container',
        'btn': 'button',
        'login_btn': 'text=Log In',
        'src_box': '#searchtext',
        'search_btn': '.btn-outline-success',
        'Authors': 'text=Authors',
        'btn_buy': 'xpath=//*[@id="root"]/div/div/div/div[3]/div/div[2]/button'
    }


    def chack_page(self):


        flag = False
        try:
            res = self.find_element(self.locator['welcome'])
            flag = True
        except:
            res = self.find_element(self.locator['login_btn'])

        logging.info(res.inner_text())
        assert flag



    def buy_book(self, book: Book, books: Book_api):

        logging.info(book.get_name())
        count_of_books_before = books.get_book_byId(book.get_id()).get_amountInStock()
        logging.info(count_of_books_before)

        buy_btn = self.find_element('btn_buy')
        buy_btn.click()
        time.sleep(3)

        count_of_books_after = books.get_book_byId(book.get_id()).get_amountInStock()
        logging.info(count_of_books_after)

        assert count_of_books_after + 1 == count_of_books_before


    def auters(self):
        auters_btn = self.find_element(self.locator['Authors'])
        auters_btn.click()
        return Auters_page(self._driver)

    def login(self):
        login_btn = self.find_element(self.locator['login_btn'])
        login_btn.click()
        return self._driver

    def search(self, test_to_search: str) -> Result_page:
        search_box = self.find_element(self.locator['src_box'])
        search_box.fill(test_to_search)

        search_btn = self.find_element(self.locator['search_btn'])
        search_btn.click()
        search_btn.click()
        return Result_page(self._driver)