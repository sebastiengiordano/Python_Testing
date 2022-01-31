import pytest
from http import HTTPStatus

import server


@pytest.mark.parametrize(
    'competition, club, club_id, number_of_places, expected_value',
    [
        ('Spring Festival', 'Testuser1 One', 0, 1, '12'),
        ('Spring Festival', 'Testuser2 Two', 1, 4, '0'),
        ('Spring Festival', 'Testuser3 Three', 2, 10, '2')])
def test__status_code__ok(
        client,
        clubs__data_for_test,
        competitions__data_for_test,
        competition, club, club_id, number_of_places, expected_value):
    response = client.post(
        f'/book/{competition}/{club}',
        data={
            'numberOfPlaces': number_of_places
        })

    assert response.status_code == HTTPStatus.OK
    assert server.clubs[club_id]['points'] == expected_value
