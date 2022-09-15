import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.login_page import *
from src.pages.welcome_page import *
from tests.fixters import *



# @pytest.fixture
def test_set_up():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    return Login_page(driver)


# @pytest.fixture
def test_login(user):

   # enter to the website
   login_page_ = test_set_up()

   # Enter the user information and click submit
   welcome_page = login_page_.submit(user)


def test_register_btn(user):

    # enter to the website
    login_page_ = test_set_up()

    # click on register btn
    register_page = login_page_.click_register()

    # assert we are in register page
    assert register_page.check_page()

    # add new user
    register_page.add_new_user(user)
    register_page.submit()

    #back to login and enter with user data
    login_page_ = register_page.back()


def test_buying_abook(user, book):

    # enter to the website
    login_page_ = test_set_up()

    # Enter the user information and click submit
    welcome_page = login_page_.submit(user)

    # peek book
    welcome_page.buy_book(book)

    # buy it
    


