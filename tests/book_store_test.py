import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.login_page import *
from src.pages.welcome_page import *
from tests.fixters import *
import logging

logging.basicConfig(level=logging.INFO)
my_logger = logging.getLogger()


@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    return Login_page(driver)


# @pytest.fixture
def test_login(setup, user):
    logging.info(setup)
    welcome_page = setup.submit(user)
    welcome_page.chack_page()


def test_register_btn(setup, user):
    register_page = setup.click_register()
    register_page.add_new_user(user2)
    register_page.submit()
    login_page_ = register_page.back()


def test_buying_abook(setup, user, book):
    # Enter the user information and click submit
    welcome_page = setup.submit(user)
    welcome_page.buy_book(book)


    


