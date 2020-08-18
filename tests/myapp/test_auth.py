from tests.myapp.client import client_with_db as c  # noqa: F401


def register(client, username, password):
    return client.post(
        '/auth/register',
        json={'username': "user1", "password": "pass1"}
    )


def login(client, username, password):
    return client.post(
        '/auth/login',
        data=dict(
            username=username,
            password=password
            ),
        follow_redirects=True
        )


def logout(client):
    return client.get('/auth/logout', follow_redirects=True)


def test_register(c):  # noqa: F811
    """Test POST /auth/reigster """

    rv = register(c, 'user1', 'pass1')

    assert rv.status_code == 200
    assert 'registration succeeded!' in str(rv.data)


def test_login_logout(c):  # noqa: F811
    """Make sure login and logout works."""

    # Register a test user before testing login/logout
    rv = register(c, 'user1', 'pass1')

    rv = login(c, 'user1', 'pass1')
    assert 'User user1 log in successfully' in str(rv.data)

    rv = logout(c)
    assert 'User log out successfully' in str(rv.data)

    rv = login(c, 'fake_user', 'pass1')
    assert 'Invalid username' in str(rv.data)

    rv = login(c, 'user1', 'fake_pass')
    assert 'Invalid password' in str(rv.data)
