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


def test_hello(client):
    """Test /hello."""

    rv = client.get('/hello')
    assert rv.status_code == 200
    assert 'Hello, World!' in str(rv.data)
