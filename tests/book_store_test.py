import pytest

from src.pages.login_page import *
from src.pages.auters_page import *

import logging


# Test the registration button on the login screen
def test_register_btn(setup, user2):
    register_page = setup.click_register()
    register_page.add_new_user(user2)
    register_page.submit()
    login_page_ = register_page.back()
    # TODO understand way not recohnise logging_page!


def test_login(setup, user):
    logging.info(setup)
    welcome_page = setup.submit(user)
    welcome_page.chack_page()


# Test for the process of buying a book on the website
def test_buying_abook(setup, user, book):
    # Enter the user information and click submit
    welcome_page = setup.submit(user)
    welcome_page.buy_book(book)


# Test Authrs button
def test_authrs_button(setup, user):
    welcome_page = setup.submit(user)
    welcome_page.chack_page()
    auters_page_ = welcome_page.auters()
    auters_page_.get_auters()

# Test for adding a new author to the system
def test_add_author(user, account, author, authors, setup):

    # add a new author
    res = authors.add_new_authors(author)
    logging.info(res.status_code)
    logging.info(res.json())
    author_id = res.json()["id"]

    # Check if the author of the book is on the list of authors on the website
    welcome_page = setup.submit(user)
    welcome_page.chack_page()
    auters_page_ = welcome_page.auters()
    assert auters_page_.find_author(author)

    # remove the new author
    status = authors.remove_authors_byid(author_id)
    logging.info(status)
    assert status == 204


# Test of the bookstore button in the top menu
def test_bookstore_button(setup):
    login_page_ = setup
    welcome_page_ = login_page_.bokstore()
    welcome_page_.chack_page()






