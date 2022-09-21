import requests
from src.models.book import *
from src.models.Author import Author
from src.models.baseObj import *
from src.models.Author import Author


class Authors_api(baseObj):


    def __init__(self, url: str, session: requests.session()):
        self._url = url
        self.token = ""
        self._headrs = {'accept': 'application/json'}
        self._session = session


    def get_all_auters(self) -> json:
        response = self._session.get(f'{self._url}')
        return response.json()

    def add_new_authors(self, new_author: Author) ->int:
        d = new_author.to_json()
        response = self._session.post(f'{self._url}', json=d, headers=self._headrs)
        return response

    def remove_authors_byid(self, authors_id: int):
        res = self._session.delete(f'{self._url}{authors_id}')
        return res.status_code

    def get_author_byid(self, autore_id) -> Author:
        res = self._session.get(f'{self._url}{autore_id}')
        if res.status_code < 400:
            return Author(**res.json())
        else:
            return res.status_code




#
# a = Authors_api('http://localhost:7017/api', requests.session())
# list_of_authors = a.get_all_auters()
# print(list_of_authors)
# # d = {"name": "dani Din",
# #      "id": 3,
# #      "homeLatitude": 41.76758,
#      "homeLongitude": 22.70144
#      }
# b = Author(**d)
#
# print(a.add_new_authors(b))