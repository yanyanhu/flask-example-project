from tests.myapp.client import client  # noqa: F401


def test_root_notfound(client):  # noqa: F811
    """Test root url / which is not found."""

    rv = client.get('/')
    assert rv.status_code == 404
    assert '404 Not Found' in str(rv.data)


def test_hello_without_login(client):  # noqa: F811
    """Test /hello without login."""

    rv = client.get('/hello')
    assert rv.status_code == 404
