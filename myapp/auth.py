import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from db.models import User  # noqa: E401,E402,F401
from myapp import app
from myapp import database as db


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        app.logger.debug('Receive auth/reg request')
        username = request.json['username']
        password = request.json['password']

        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        # Check the existence of the user
        if not error:
            user = User.query.filter_by(username=username).first()
            if user is not None:
                # User has been registered
                error = 'User %s has already been registered.' % username
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

        if error:
            app.logger.warning(error)
            # Note: this is not required if the req is not from a browser
            flash(error)

            return error

        return 'User %s registration succeeded!' % username


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        app.logger.debug('Receive auth/login request')
        username = request.form["username"]
        password = request.form["password"]

        error = None
        # Check the existence of the user
        user = User.query.filter_by(username=username).first()
        if user is None:
            # User does not exist
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            # User exists, but password check failed
            error = 'Incorrect password.'

        if error:
            app.logger.warning(error)
            # Note: this is not required if the req is not from a browser
            flash(error)

            return error

        session.clear()
        session['user_id'] = user.id
        return 'User %s log in successfully.' % username

    return render_template("auth/login.html")


@bp.route('/logout')
def logout():
    session.clear()
    return 'User log out successfully.'


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
