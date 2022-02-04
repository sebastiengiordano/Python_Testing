import pytest
from datetime import datetime, timedelta

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
    today = datetime.today()
    date_in_past = (today - timedelta(minutes=1))
    date_in_past = date_in_past.strftime("%Y-%m-%d %H:%M:%S")
    date_in_future = (today + timedelta(minutes=1))
    date_in_future = date_in_future.strftime("%Y-%m-%d %H:%M:%S")

    data_for_test = [
            {
                "name": "Test Festival",
                "date": "2022-03-27 10:00:00",
                "numberOfPlaces": "25"
            },
            {
                "name": "Test Classic",
                "date": "2021-10-22 13:30:00",
                "numberOfPlaces": "13"
            },
            {
                "name": "Test Low Number of place",
                "date": "2023-10-22 13:30:00",
                "numberOfPlaces": "1"
            },
            {
                "name": "Competition in past",
                "date": date_in_past,
                "numberOfPlaces": "20"
            },
            {
                "name": "Competition in future",
                "date": date_in_future,
                "numberOfPlaces": "15"
            }]
    monkeypatch.setattr('server.competitions', data_for_test)


@pytest.fixture(scope='function')
def saveClubs__fixture(monkeypatch):
    '''Used to avoid saving test data in "clubs.json".'''

    def saveClubs__mock():
        pass
    monkeypatch.setattr('server.saveClubs', saveClubs__mock)


@pytest.fixture(scope='function')
def saveCompetitions__fixture(monkeypatch):
    '''Used to avoid saving test data in "competitions.json".'''

    def saveCompetitions__mock():
        pass
    monkeypatch.setattr('server.saveCompetitions', saveCompetitions__mock)
