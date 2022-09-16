from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages import base as base
from src.pages.register_page import Register_page
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
        'btn': (By.TAG_NAME, 'button')
    }


    def chack_page(self):

        res = self.find_element(*self.locator['welcome'])
        assert res.text == 'Welcome to our store'


# TODO see in comments
    def buy_book(self, book: Book):

        book_container = self.find_elements(*self.locator['book-container'])
        btn = ""
        for book_ in book_container:
            if book.get_name() in book_.text:
                logging.info(book_.text)
                btn = book_.find_element(*self.locator['btn'])
                break

        logging.info(btn.text)
        book_amount_befor = book.get_amountInStock()
        assert book_amount_befor > 0
        # TODO the click not work!
        #btn.click()

        # TODO move the url to some fixters
        b = Book_api('http://localhost:7017/api/Books/')
        b1 = b.get_book_byId(3)
        book_amount_after = b1.get_amountInStock()

        logging.info(book_amount_after)
        assert book_amount_befor - book_amount_after == 1

