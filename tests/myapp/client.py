import os

import pytest
import tempfile

import myapp


def init_db(db_url):
    """Init database using given db_url.

    This function calls the cmd to initialize the DB using the
    migration history.
    """

    cmd = 'export DATABASE_URL=%s && python db/manage.py db upgrade' % db_url
    os.system(cmd)


@pytest.fixture
def client_without_db():
    """Create test client without DB initialized

    This client is for test scenarios where database is not required.
    """

    myapp.app.config['TESTING'] = True

    with myapp.app.test_client() as client:
        yield client


@pytest.fixture
def client_with_db():
    """Create test client with DB initialized

    This client is for test scenarios where database is required.
    """

    # Create tmp file for test sqlite db
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
