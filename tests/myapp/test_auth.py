from tests.myapp.client import client_with_db as c  # noqa: F401


def register(client, username, password):
    """Register a user with given name and password"""

    return client.post(
        '/auth/register',
        json={'username': "user1", "password": "pass1"}
    )


def login(client, username, password):
    """Login using given username and password"""

    return client.post(
        '/auth/login',
        data=dict(
            username=username,
            password=password
            ),
        follow_redirects=True
        )


def logout(client):
    """Logout current user"""
    return client.get('/auth/logout', follow_redirects=True)


def test_register(c):  # noqa: F811
    """Test POST /auth/reigster

    This URL is public accessible.
    Expected result: 404 Not Found.
    """

    rv = register(c, 'user1', 'pass1')

    assert rv.status_code == 200
    assert 'registration succeeded!' in str(rv.data)


def test_login_logout(c):  # noqa: F811
    """Test login and logout."""

    # Register a test user before testing login/logout
    rv = register(c, 'user1', 'pass1')

    # Login with correct user
    rv = login(c, 'user1', 'pass1')
    assert 'User user1 log in successfully' in str(rv.data)

    # Logout current user
    rv = logout(c)
    assert 'User log out successfully' in str(rv.data)

    # Login with username doesn't exist
    rv = login(c, 'fake_user', 'pass1')
    assert 'Invalid username' in str(rv.data)

    # Login with invalid password
    rv = login(c, 'user1', 'fake_pass')
    assert 'Invalid password' in str(rv.data)
