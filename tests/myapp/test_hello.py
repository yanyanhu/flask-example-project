from tests.myapp.client import client_without_db as c  # noqa: F401


def test_root_notfound(c):  # noqa: F811
    """Test root url /

    This URL is not defined.
    Expected result: 404 Not Found.
    """

    rv = c.get('/')
    assert rv.status_code == 404
    assert '404 Not Found' in str(rv.data)


def test_hello_world(c):  # noqa: F811
    """Test /hello/world

    This URL is public accessible.
    Expected result: 200.
    """

    rv = c.get('/hello')
    assert rv.status_code == 404


def test_hello_name_without_login(c):  # noqa: F811
    """Test /hello/<name>

    This URL is protected by login.
    Expected result: 404 Not Found.
    """

    rv = c.get('/hello')
    assert rv.status_code == 404
