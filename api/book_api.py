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


    def get_all_books(self):
        response = self._session.get(f'{self._url}')
        return response.json()


    def put_book_to_author(self, book: Book, author_id: int):
        book.set_authorId(author_id)
        d = book.to_json()
        response = self._session.put(f'{self._url}{book.get_id()}', json=d)
        return response.status_code



# b = Book_api('http://localhost:7017/api/Books/', requests.session())
#
# b1 = b.get_book_byId(3)
#
# print(b1.get_amountInStock())
#
