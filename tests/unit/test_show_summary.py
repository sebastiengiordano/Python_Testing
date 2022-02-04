import pytest
from http import HTTPStatus


@pytest.mark.parametrize('user_email', [
    'email@testuser1.com',
    'email@testuser2.fr',
    'email@testuser3.uk'])
def test__status_code__ok(client, user_email, clubs__data_for_test):
    form = {
        'email': user_email
    }
    response = client.post(
        '/showSummary',
        data=form)
    assert response.status_code == HTTPStatus.OK
    assert b'Welcome, ' in response.data
    assert bytes(
        user_email,
        encoding='utf8') in response.data
    assert b'Logout' in response.data


def test__unknow_email_adress(client, clubs__data_for_test):
    form = {
        'email': 'unknow@email.adress'
    }
    response = client.post(
        '/showSummary',
        data=form)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert b'GUDLFT Registration' in response.data
    assert b'Welcome to the GUDLFT Registration Portal!' \
        in response.data
    assert b'Please enter your secretary email to continue:' \
        in response.data
    assert b'Sorry, the email' in response.data
