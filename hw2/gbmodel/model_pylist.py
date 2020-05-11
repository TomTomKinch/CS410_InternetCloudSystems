from datetime import date
from .Model import Model

class model(Model):
	def __init__(movie):
		movie.entries = []
	def select(movie):
		return movie.entries
	def insert(movie, title, year, genre, rating, name, review):
		params = [title, year, genre, rating, name, date.today(), review]
		movie.entries.append(params)
		return True
