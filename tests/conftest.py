
import requests
import pytest
import logging
from optparse import OptionParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from src.pages.login_page import *
from src.pages.welcome_page import *
from src.models.user import *
from src.models.book import *
from api.book_api import *
from api.authors_api import Authors_api
from api.account_api import Account_api

logging.basicConfig(level=logging.INFO)
my_logger = logging.getLogger()



chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrom_driver_path = r'C:\Users\inegr\Desktop\Michael_projects\chromedriver'





@pytest.fixture
def get_url():
    parser = OptionParser()
    parser.add_option("--u", action="store", type="string", dest="URL", default="http://localhost/")
    (options, args) = parser.parse_args()
    return options.URL

@pytest.fixture(scope='session')
def get_swagger():
    parser = OptionParser()
    parser.add_option("--s",
                      action="store",
                      type="string",
                      dest="SWAGGER",
                      default="http://localhost:7017/api")

    (options, args) = parser.parse_args()
    return options.SWAGGER





@pytest.fixture
def setup(get_url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    driver.get(get_url)
    return Login_page(driver)


@pytest.fixture(scope='session')
def user():
    data = {'mail': 'admin@sela.co.il',
            'password': '1234',
            'first_name': 'michael',
            'last_name': 'kolet'
            }

    return User(**data)

@pytest.fixture(scope='session')
def user2():
    data = {'mail': 'michael@sela.co.il',
            'password': '1234',
            'first_name': 'michael',
            'last_name': 'kolet'
            }

    return User(**data)


@pytest.fixture(scope='session')
def url1(get_swagger):
    return f'{get_swagger}/Books/'


@pytest.fixture(scope='session')
def url_for_authors(get_swagger):
    return f'{get_swagger}/Authors/'


@pytest.fixture(scope='session')
def url_for_account(get_swagger):
    return f'{get_swagger}/Account/'


@pytest.fixture(scope='session')
def get_session(user, url_for_account):
    session = requests.session()

    d = {'email': 'admin@sela.co.il',
            'password': '1234'
            }

    res = session.post(f'{url_for_account}login', json=d)
    logging.info(res.json())

    h = {'Authorization': 'Bearer ' + res.json()["token"],
         'accept': 'application/json'}

    session.headers.update(h)
    return session


@pytest.fixture(scope='session')
def authors(url_for_authors, get_session):
    return Authors_api(url_for_authors, get_session)


@pytest.fixture(scope='session')
def author():
    d = {"name": "dani Din",
          "id": 3,
         "homeLatitude": 41.76758,
         "homeLongitude": 22.70144
         }
    return Author(**d)


@pytest.fixture(scope='session')
def books(url1, get_session):
    return Book_api(url1, get_session)


@pytest.fixture(scope='session')
def book(books):
    return books.get_book_byId(3)

@pytest.fixture(scope='session')
def account(url_for_account, get_session):
    return Account_api(url_for_account, get_session)

@pytest.fixture(scope='session')
def get_book():
    pass