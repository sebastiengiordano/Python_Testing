from http import HTTPStatus

from tests.conftest import client


def test__status_code__ok(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert b'GUDLFT Registration' in response.data
    assert b'Welcome to the GUDLFT Registration Portal!' \
        in response.data
    assert b'Please enter your secretary email to continue:' \
        in response.data
