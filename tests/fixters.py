

import requests
import pytest
from optparse import OptionParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from src.models.user import *
from src.models.book import *
from api.book_api import *


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrom_driver_path = r'C:\Users\inegr\Desktop\Michael_projects\chromedriver'

# michael@kolet.com
# 123456
# "admin@sela.co.il
# 1234


def get_url():
    parser = OptionParser()
    parser.add_option("-u", action="store", type="string", dest="URL", default="http://localhost/")
    (options, args) = parser.parse_args()
    return options.URL


url = get_url()


@pytest.fixture()
def user():
    data = {'mail': 'admin@sela.co.il',
            'password': '1234',
            'first_name': 'michael',
            'last_name': 'kolet'
            }

    return User(**data)

@pytest.fixture()
def user2():
    data = {'mail': 'michael@sela.co.il',
            'password': '1234',
            'first_name': 'michael',
            'last_name': 'kolet'
            }

    return User(**data)

@pytest.fixture()
def url1():
    return 'http://localhost:7017/api/Books/'

@pytest.fixture()
def books(url1):
    return Book_api(url1)


@pytest.fixture()
def book(books):
    return books.get_book_byId(3)