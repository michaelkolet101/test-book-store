import requests
from src.models.book import *
from src.models.Author import Author
from src.models.baseObj import baseObj


class Book_api(baseObj):


    def __init__(self, url: str, session):
        self._url = url
        self._headrs = {'accept': 'application/json'}
        self._session = session


    def get_book_byId(self, book_id: int) -> Book:
        response = self._session.get(f'{self._url}{book_id}')
        return Book(**response.json())






b = Book_api('http://localhost:7017/api/Books/', requests.session())

b1 = b.get_book_byId(3)

print(b1.get_amountInStock())

