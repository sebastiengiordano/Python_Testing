import pytest

from server import app


@pytest.fixture(scope='function')
def client():
    '''Create a test client using the
    Flask application configured for testing.'''
    app.config.from_object({"TESTING": True})
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture(scope='function')
def clubs__data_for_test(monkeypatch):
    '''Used to modify the club dictionary for testing purposes.'''
    data_for_test = [
            {
                "name": "Testuser1 One",
                "email": "email@testuser1.com",
                "points": "13"
            },
            {
                "name": "Testuser2 Two",
                "email": "email@testuser2.fr",
                "points": "4"
            },
            {
                "name": "Testuser3 Three",
                "email": "email@testuser3.uk",
                "points": "12"
            }]
    monkeypatch.setattr('server.clubs', data_for_test)


@pytest.fixture(scope='function')
def competitions__data_for_test(monkeypatch):
    '''Used to modify the competitions dictionary for testing purposes.'''
    data_for_test = [
            {
                "name": "Spring Festival",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25"
            },
            {
                "name": "Fall Classic",
                "date": "2020-10-22 13:30:00",
                "numberOfPlaces": "13"
            }]
    monkeypatch.setattr('server.competitions', data_for_test)


@pytest.fixture(scope='function')
def loadClubs_fixture(monkeypatch):
    '''Used to modify the club dictionary for testing purposes.'''
    def clubs__update():
        return [
            {
                "name": "Testuser1 One",
                "email": "email@testuser1.com",
                "points": "13"
            },
            {
                "name": "Testuser2 Two",
                "email": "email@testuser2.fr",
                "points": "4"
            },
            {
                "name": "Testuser3 Three",
                "email": "email@testuser3.uk",
                "points": "12"
            }]
    monkeypatch.setattr('server.loadClubs', clubs__update)


@pytest.fixture(scope='function')
def loadCompetitions_fixture(monkeypatch):
    '''Used to modify the competitions dictionary for testing purposes.'''
    def competitions__update():
        return [
            {
                "name": "Test Festival",
                "date": "2022-03-27 10:00:00",
                "numberOfPlaces": "25"
            },
            {
                "name": "Test Classic",
                "date": "2021-10-22 13:30:00",
                "numberOfPlaces": "13"
            }]
    monkeypatch.setattr('server.loadCompetitions', competitions__update)
