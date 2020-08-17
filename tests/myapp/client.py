import os

import pytest
import tempfile

import myapp


def init_db(db_url):
    """Init database using given db_url."""

    cmd = 'export DATABASE_URL=%s && python db/manage.py db upgrade' % db_url
    os.system(cmd)


@pytest.fixture
def client():
    """Create test client without DB initialized"""

    myapp.app.config['TESTING'] = True

    with myapp.app.test_client() as client:
        yield client


@pytest.fixture
def client_withdb():
    """Create test client with DB initialized"""

    # Create tmp file for test db
    db_fd, db_file_path = tempfile.mkstemp()
    # Generate sqlite DB URL
    myapp.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file_path
    myapp.app.config['TESTING'] = True

    # Init DB and return client
    with myapp.app.test_client() as client:
        with myapp.app.app_context():
            init_db(myapp.app.config['SQLALCHEMY_DATABASE_URI'])
        yield client

    # Close and remove tmp file after test is done
    os.close(db_fd)
    os.unlink(db_file_path)
