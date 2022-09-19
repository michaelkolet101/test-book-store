import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages import base as base
from api.authors_api import Authors_api
from src.models.Author import Author
from src.pages import base as base
from src.pages.login_page import *
from src.models.user import User

import logging


class Result_page(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {
        'authors_list': (By.CLASS_NAME, 'author-container')
    }

    def check_page(self):
        back = self.find_element(*self.locator["Back"])
        print(back.text)
        return back.text == 'Back To Login'


