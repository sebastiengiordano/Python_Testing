import pytest
from http import HTTPStatus


@pytest.mark.parametrize(
    'competition, club',
    [
        ('Competition in future', 'Testuser1 One'),
        ('Competition in future', 'Testuser2 Two'),
        ('Competition in future', 'Testuser3 Three')])
def test__status_code__ok(
        client,
        clubs__data_for_test,
        competitions__data_for_test,
        competition, club):
    response = client.get(
        f'/book/{competition}/{club}')

    assert response.status_code == HTTPStatus.OK
    assert bytes(
        competition,
        encoding='utf8') in response.data
    assert b'Places available:' in response.data
    assert b'How many places?' in response.data


@pytest.mark.parametrize(
    'competition, club', [
        ('Test Classic', 'TestUserUnknow'),
        ('Unknow competition', 'TestUserUnknow')])
def test__status_code__bad_request__unknow_club(
        client,
        clubs__data_for_test,
        competitions__data_for_test,
        competition, club):
    response = client.get(
        f'/book/{competition}/{club}')

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert b'Something went wrong-please try again' in response.data
    assert b'GUDLFT Registration' in response.data
    assert b'Welcome to the GUDLFT Registration Portal!' \
        in response.data
    assert b'Please enter your secretary email to continue:' \
        in response.data


@pytest.mark.parametrize(
    'competition, club, user_email', [
        ('Unknow competition', 'Testuser1 One', 'email@testuser1.com'),
        ('Unknow competition', 'Testuser2 Two', 'email@testuser2.fr'),
        ('Unknow competition', 'Testuser3 Three', 'email@testuser3.uk')])
def test__status_code__bad_request__unknow_competition(
        client,
        clubs__data_for_test,
        competitions__data_for_test,
        competition, club, user_email):
    response = client.get(
        f'/book/{competition}/{club}')

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert b'Something went wrong-please try again' in response.data
    assert b'Welcome, ' in response.data
    assert bytes(
        user_email,
        encoding='utf8') in response.data
    assert b'Logout' in response.data
