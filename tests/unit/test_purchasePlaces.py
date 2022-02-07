import pytest
from http import HTTPStatus

import server


@pytest.mark.parametrize(
    'competition, club, club_id, competition_id, number_of_places,'
    'club_remaining_points, competition_remaining_points',
    [
        ('Competition in future', 'Testuser1 One', 0, 4, 13, '13', '15'),
        ('Competition in future', 'Testuser3 Three', 2, 4, 13, '12', '15')])
def test__cannot_book_more_than_12(
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
    assert b'You cannot book more than 12 places.' in response.data
    assert b'Logout' in response.data
