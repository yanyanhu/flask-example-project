from flask import (
    Blueprint, request
)

from myapp import app

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        app.logger.debug('Receive auth reg request: %s',
                         str(request.json))
        username = request.json['username']
        password = request.json['password']

    return 'User registration succeeded!'
