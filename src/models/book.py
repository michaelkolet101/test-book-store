from src.models.baseObj import *


class Book(baseObj):
    def __init__(self, name: str,
                 description: str,
                 price: float,
                 amountInStock: int,
                 imageUrl: str,
                 authorId: int,
                 id: int=None):

        self._name = name
        self._description = description
        self._price = price
        self._amountInStock = amountInStock
        self._imageUrl = imageUrl
        self._authorId = authorId
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_description(self):
        return self._description

    def set_description(self, new_description):
        self._description = new_description

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        self._price = new_price

    def get_amountInStock(self):
        return self._amountInStock

    def set_amountInStock(self, new_amountInStock):
        self._amountInStock = new_amountInStock

    def get_imageUrl(self):
        return self._imageUrl

    def set_imageUrl(self, new_imageUrl):
        self._imageUrl = new_imageUrl

    def get_authorId(self):
        return self._authorId

    def set_authorId(self, new_authorId):
        self._authorId = new_authorId

    def get_id(self):
        return self._id

    def set_id(self, new_id):
        self._id = new_id
