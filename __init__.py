from openedoo.core.libs import Blueprint
from openedoo_project.db import Query

query = Query()
module_books = Blueprint('module_books', __name__)

@module_books.route('/', methods=['POST', 'GET'])
def index():
	return "Hello module module_books"
