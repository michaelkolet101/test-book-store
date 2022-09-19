from src.models.baseObj import baseObj
from src.models.book import Book


class Author(baseObj):

	def __init__(self, name: str, id: int, homeLatitude: int, homeLongitude: int, books: [Book]=[] ):
		self._name = name
		self._id = id
		self._homeLatitude = homeLatitude
		self._homeLongitude = homeLongitude
		self._books = books
		
	def get_name(self):
		return self._name

	def set_name(self, new_name):
		self._name = new_name

	def get_id(self):
		return self._id

	def set_id(self, new_id):
		self._id = new_id

	def get_homeLatitude(self):
		return self._homeLatitude

	def set_homeLatitude(self, new_homeLatitude):
		self._homeLatitude = new_homeLatitude

	def get_homeLongitude(self):
		return self._homeLongitude

	def set_homeLongitude(self, new_homeLongitude):
		self._homeLongitude = new_homeLongitude

	def get_books(self):
		return self._books

	def set_books(self, new_books):
		self._books = new_books
