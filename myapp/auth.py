from flask import (
    Blueprint, flash, request
)

from werkzeug.security import check_password_hash, generate_password_hash

from db.models import User  # noqa: E401,E402,F401
from myapp import app
from myapp import database as db


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        app.logger.debug('Receive auth reg request: %s',
                         str(request.json))
        username = request.json['username']
        password = request.json['password']

        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        user = User.query.filter_by(username=username).first()
        if user is not None:
            # User has been registered
            error = 'User {} is already registered.'.format(username)
            app.logger.debug(error)
        else:
            # Insert new user record
            app.logger.debug('Insert new user record for %s', username)
            try:
                user = User(
                    username=username,
                    password=generate_password_hash(password),
                )
                db.session.add(user)
                db.session.commit()
            except Exception as error:
                detail = str(error.orig) + " for parameters" + \
                    str(error.params)
                error = 'Failed to insert new user record to DB: ' + detail
                app.logger.warning(error)

        flash(error)

    return 'User registration succeeded!'
