from openedoo_project import db
from openedoo_project import config

database_prefix = config.database_prefix

class OD_books(db.Model):
	__tablename__ = '{db_prefix}_books'.format(db_prefix=database_prefix)
	book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	isbn = db.Column(db.String(10), unique=True)
	title = db.Column(db.String(100))
	author = db.Column(db.String(100))
	publisher = db.Column(db.String(100))
	price = db.Column(db.String(50))
	category = db.Column(db.String(50))

	def __init__(self, isbn, title, author, publisher, price, category):
		self.isbn = isbn
		self.title = title
		self.author = author
		self.publisher = publisher
		self.price = price
		self.category = category

class OD_categories(db.Model):
	__tablename__ = '{db_prefix}_categories'.format(db_prefix=database_prefix)
	category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100))

	def __init__(self, name):
		self.name = name


