import pytest

import logging
import time


# Test the registration button on the login screen
def test_register(setup, user2, accounts):
    logging.info('test_register')
    register_page = setup.click_register()
    register_page.add_new_user(user2)
    register_page.submit()
    register_page.back()
    # check login with the api login
    assert accounts.login(user2) < 400


def test_login(setup, user):
    logging.info('test_login')
    logging.info(setup)
    welcome_page_ = setup.submit(user)
    welcome_page_.chack_page()
    welcome_page_.close()


# Test for the process of buying a book on the website
def test_buying_abook(setup, user, book, books):
    logging.info('test_buying_abook')
    # Enter the user information and click submit
    welcome_page = setup.submit(user)
    welcome_page.buy_book(book, books)
    welcome_page.close()


# Test Authrs button
def test_authors_button(setup, user, authors):
    logging.info('test_authors_button')
    welcome_page = setup.submit(user)
    welcome_page.chack_page()
    auters_page_ = welcome_page.auters()
    auters_page_.cheack_authoers(authors)
    auters_page_.close()

# Test for adding a new author to the system
def test_add_author(user, account, author, authors, setup):
    logging.info('test_add_author')
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
def test_bookstore_button(setup, user):
    logging.info('test_bookstore_button')
    login_page_ = setup
    welcome_page_ = login_page_.bookstore()
    welcome_page_.chack_page()


# Test the store button in the top menu
def test_store_button(setup):
    logging.info('test_store_button')
    login_page_ = setup
    welcome_page_ = login_page_.store()
    welcome_page_.chack_page()

# Test the login button in the top menu
def test_login_button(setup):
    logging.info('test_login_button')
    login_page_ = setup
    welcome_page_ = login_page_.store()
    welcome_page_.chack_page()
    login_page_ = welcome_page_.login()

# Test adding a book to the author
def test_add_book(user, account, author, authors, setup, books, book):

    logging.info('test_add_book')
    # Log in through the swagger and log in as an admin user
    # add a new author
    res = authors.add_new_authors(author)
    logging.info(res.status_code)
    author_id = res.json()["id"]

    # We will add a book to the author of the book
    ans = books.put_book_to_author(book, author_id)
    logging.info(ans)

    # We will make sure that the book has been added to the author in the database
    our_author = authors.get_author_byid(author_id)
    assert our_author.get_books()[0]['id'] == book.get_id()


def test_cleanup(authors):
    list_of_authores = authors.get_all_auters()
    logging.info(list_of_authores)

    for item in list_of_authores:
        if int(item['id']) > 3:
            authors.remove_authors_byid(int(item['id']))

