

import requests
import pytest
from optparse import OptionParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from src.models.user import *
from src.models.book import *

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrom_driver_path = r'C:\Users\inegr\Desktop\Michael_projects\chromedriver'

# michael@kolet.com
# 123456


def get_url():
    parser = OptionParser()
    parser.add_option("-u", action="store", type="string", dest="URL", default="http://localhost/")
    (options, args) = parser.parse_args()
    return options.URL


url = get_url()


@pytest.fixture()
def user():
    data = {'mail': 'michael@kolet.com',
            'password': '123456',
            'first_name': 'michael',
            'last_name': 'kolet'
            }

    return User(**data)

@pytest.fixture()
def book():
    data = {
    "id": 3,
    "name": "The Hunger Games",
    "description": "The Hunger Games is a 2008 dystopian novel by the American writer Suzanne Collins",
    "price": 50,
    "amountInStock": 8,
    "imageUrl": "https://images-na.ssl-images-amazon.com/images/I/61i8nC90deL.jpg",
    "authorId": 2
    }
    return Book(**data)