import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
    )

    # config database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('setup.cfg', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


app = create_app()
database = SQLAlchemy(app)


from db.models import Result


# A simple page that says hello
@app.route('/hello')
def hello():
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    return 'Hello, World!'


# A simple page that says hello to given name
@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)