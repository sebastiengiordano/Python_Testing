import pytest
from http import HTTPStatus

import server


@pytest.mark.parametrize(
    'competition, club, club_id, competition_id, number_of_places,'
    'club_remaining_points, competition_remaining_points',
    [
        ('Competition in past', 'Testuser1 One', 0, 4, 1, '13', '15'),
        ('Competition in past', 'Testuser2 Two', 1, 4, 4, '4', '15'),
        ('Competition in past', 'Testuser3 Three', 2, 4, 10, '12', '15')])
def test__book_in_past(
        client,
        clubs__data_for_test,
        competitions__data_for_test,
        saveClubs__fixture,
        saveCompetitions__fixture,
        competition, club, club_id, competition_id,
        number_of_places, club_remaining_points,
        competition_remaining_points):
    response = client.post(
        '/purchasePlaces',
        data={
            'competition': competition,
            'club': club,
            'places': number_of_places
        })

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert server.clubs[club_id]['points'] == club_remaining_points
    assert server.competitions[
        competition_id][
            'numberOfPlaces'] == competition_remaining_points
    assert b'Welcome, ' in response.data
    assert b'    Sorry !!!' in response.data
    assert b'This competition has already been played.' in response.data
    assert b'You cannot book places.' in response.data
    assert b'Logout' in response.data
