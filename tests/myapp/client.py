import pytest

import myapp


@pytest.fixture
def client():
    myapp.app.config['TESTING'] = True

    with myapp.app.test_client() as client:
        yield client
