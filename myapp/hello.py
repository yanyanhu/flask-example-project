from flask import (
    Blueprint
)

from myapp.auth import login_required


bp = Blueprint('hello', __name__, url_prefix='/hello')


# A simple page that says hello
@bp.route('/world', methods=['GET'])
def hello():
    return 'Hello, World!'


# A simple page that says hello to given name
@bp.route('/<name>', methods=['GET'])
@login_required
def hello_name(name):
    return "Hello {}!".format(name)
