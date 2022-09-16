import requests
from src.models.book import *




class Book_api:


    def __init__(self, url: str):
        self._url = url
        self._headrs = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers = self._headrs

    def get_book_byId(self, book_id: int) -> Book:
        response = self._session.get(f'{self._url}{book_id}')
        return Book(**response.json())



#
# b = Book_api('http://localhost:7017/api/Books/')
#
# b1 = b.get_book_byId(3)
#
# print(b1.get_amountInStock())

