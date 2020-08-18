from tests.myapp.client import client_without_db as c  # noqa: F401


def test_root_notfound(c):  # noqa: F811
    """Test root url / which is not found."""

    rv = c.get('/')
    assert rv.status_code == 404
    assert '404 Not Found' in str(rv.data)


def test_hello_without_login(c):  # noqa: F811
    """Test /hello without login."""

    rv = c.get('/hello')
    assert rv.status_code == 404
