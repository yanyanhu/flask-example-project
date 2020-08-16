import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    # Create the app
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    # Config database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config is None:
        # Load the default config from config.py when not testing
        app.config.from_pyfile('config.py', silent=False)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Override the config options provided as environment variables
    if os.environ['DATABASE_URL']:
        app.config.from_mapping(
            SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
        )
        app.logger.debug('Database url to use: %s',
                         app.config['SQLALCHEMY_DATABASE_URI'])

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


app = create_app()
database = SQLAlchemy(app)


from db.models import Result  # noqa: E401,E402,F401

# Register blueprints
from . import auth  # noqa: E401,E402,F401
app.register_blueprint(auth.bp)


# A simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'


# A simple page that says hello to given name
@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
