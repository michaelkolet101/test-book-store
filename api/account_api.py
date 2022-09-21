import requests
from src.models.book import *
from src.models.Author import Author
from src.models.user import User
from src.models.baseObj import baseObj


class Account_api(baseObj):


    def __init__(self, url: str, session):
        self._url = url
        self._headrs = {'accept': 'application/json'}
        self._session = session


    def login(self, user: User) -> int:
        data = {
              "email": user.get_mail(),
              "password": user.get_password()
            }

        res = self._session.post(f'{self._url}login', json=data)
        return res.status_code

# a = Account_api('http://localhost:7017/api')
#
#
# data = {'mail': "admin@sela.co.il",
#             'password': "1234",
#             'first_name': 'michael',
#             'last_name': 'kolet'
#             }
#
# u = User(**data)
#
# print(a.login(u)["token"])