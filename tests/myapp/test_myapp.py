import pytest

import myapp


@pytest.fixture
def client():
    myapp.app.config['TESTING'] = True

    with myapp.app.test_client() as client:
        yield client


def test_root_notfound(client):
    """Test root url / which is not found."""

    rv = client.get('/')
    assert rv.status_code == 404
    assert '404 Not Found' in str(rv.data)


def test_hello_without_login(client):
    """Test /hello without login."""

    rv = client.get('/hello')
    assert rv.status_code == 404
