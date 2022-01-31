import pytest
from http import HTTPStatus

import server


# @pytest.mark.parametrize(
#     'competition, club, club_id, number_of_places, expected_value',
#     [
#         # ('Test Festival', 'Testuser1 One', 0, 1, '12'),
#         # ('Test Festival', 'Testuser2 Two', 1, 4, '0'),
#         # ('Test Festival', 'Iron Temple', 1, 4, '0'),
#         ('Spring Festival', 'Iron Temple', 2, 10, '2')])
#         # ('Test Festival', 'Testuser3 Three', 2, 10, '2')])
# def test__status_code__ok(
#         client,
#         loadClubs_fixture,
#         loadCompetitions_fixture,
#         competition, club, club_id, number_of_places, expected_value):

#     print(clubs, '\n\n', competitions)
#     response = client.post(
#         f'/book/{competition}/{club}',
#         data={
#             'numberOfPlaces': number_of_places
#         })

#     assert response.status_code == HTTPStatus.OK
#     assert clubs[club_id] == {}
#     assert clubs[club_id]['points'] == expected_value


@pytest.mark.parametrize(
    'competition, club, club_id, number_of_places, expected_value',
    [
        # ('Spring Festival', 'Testuser1 One', 0, 1, '12'),
        # ('Spring Festival', 'Testuser2 Two', 1, 4, '0'),
        ('Spring Festival', 'Iron Temple', 2, 10, '2')])
        # ('Spring Festival', 'Testuser3 Three', 2, 10, '2')])
def test__status_code__ok(
        client,
        loadClubs_fixture,
        loadCompetitions_fixture,
        competition, club, club_id, number_of_places, expected_value):

    print(server.clubs, '\n\n', server.competitions)
    response = client.post(
        f'/book/{competition}/{club}',
        data={
            'numberOfPlaces': number_of_places
        })

    assert response.status_code == HTTPStatus.OK
    assert server.clubs[club_id]['points'] == expected_value
