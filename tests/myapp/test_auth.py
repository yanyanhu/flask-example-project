from tests.myapp.client import client_withdb as client  # noqa: F401


def test_register(client):  # noqa: F811
    """Test POST /auth/reigster """

    rv = client.post(
        '/auth/register',
        json={'username': "user1", "password": "pass1"}
    )

    assert rv.status_code == 200
    assert 'registration succeeded!' in str(rv.data)
