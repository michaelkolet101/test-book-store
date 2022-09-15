from src.models.baseObj import *


class User(baseObj):

	def __init__(self, mail, password, first_name, last_name):
		self._mail = mail
		self._password = password
		self._first_name = first_name
		self._last_name = last_name
		
	def get_mail(self):
		return self._mail

	def set_mail(self, new_mail):
		self._mail = new_mail

	def get_password(self):
		return self._password

	def set_password(self, new_password):
		self._password = new_password

	def get_first_name(self):
		return self._first_name

	def set_first_name(self, new_first_name):
		self._first_name = new_first_name

	def get_last_name(self):
		return self._last_name

	def set_last_name(self, new_last_name):
		self._last_name = new_last_name
