import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    """Create a flask app"""

    # Create the app
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    # Config database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    testing = os.environ['TESTING'] if 'TESTING' in os.environ else False
    if not testing:
        # Load the default config from config.py when not testing
        app.config.from_pyfile('config.py', silent=False)
    else:
        # Load the test config if in testing mode
        app.config.from_pyfile('config_test.py', silent=False)

    # Override the config options provided as environment variables
    if 'DATABASE_URL' in os.environ:
        app.config.from_mapping(
            SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
        )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


# Creatre the app
app = create_app()

# Create the database
database = SQLAlchemy(app)


# Register blueprints
from . import auth  # noqa: E401,E402,F401
from . import hello  # noqa: E401,E402,F401

# Blueprint for authentication APIs
app.register_blueprint(auth.bp)

# Blueprint for hello test APIs
app.register_blueprint(hello.bp)
