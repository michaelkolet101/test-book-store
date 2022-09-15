from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages import base as base
from src.pages.register_page import Register_page
from src.models.user import *
from src.models.book import *
import logging


class Welcome_page(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {
        "welcome": (By.XPATH, '//*[@id="root"]/div/h1'),
        'books_container':(By.CLASS_NAME, 'book-container')

    }


    def chack_page(self):

        res = self.find_element(*self.locator['welcome'])
        assert res.test == 'Welcome to our store'


    def buy_book(self, book: Book):

        # find the book
        books_container = self.find_elements(*self.locator['books_container'])
        logging.info(f"hello {books_container}")
