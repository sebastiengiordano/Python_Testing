import pytest
from http import HTTPStatus

import server


@pytest.mark.parametrize(
    'competition, club, club_id, competition_id, number_of_places,'
    'club_remaining_points, competition_remaining_points',
    [
        ('Competition in future', 'Testuser1 One', 0, 4, 1, '12', '14'),
        ('Competition in future', 'Testuser2 Two', 1, 4, 4, '0', '11'),
        ('Competition in future', 'Testuser3 Three', 2, 4, 10, '2', '5')])
def test__status_code__ok(
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

    assert response.status_code == HTTPStatus.OK
    assert server.clubs[club_id]['points'] == club_remaining_points
    assert server.competitions[
        competition_id][
            'numberOfPlaces'] == competition_remaining_points
