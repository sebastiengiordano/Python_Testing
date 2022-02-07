import json
from datetime import datetime

import server


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


def saveClubs():
    with open("clubs.json", "w") as file:
        return json.dump({"clubs": server.clubs}, file, indent=4)


def saveCompetitions():
    with open("competitions.json", "w") as file:
        return json.dump({"competitions": server.competitions}, file, indent=4)


def get_club_id_by_email(email):
    club_id = None

    for index, club_data in enumerate(server.clubs):
        if club_data['email'] == email:
            club_id = index
            break

    return club_id


def get_club_id_by_name(name):
    club_id = None

    for index, club_data in enumerate(server.clubs):
        if club_data['name'] == name:
            club_id = index
            break

    return club_id


def get_club_by_id(club_id):
    return server.clubs[club_id]


def get_club_points_by_id(club_id):
    club = get_club_by_id(club_id)
    club_point = int(club['points'])
    # Clubs shouldn't be able to book more than 12 places per competition,
    # and more than it's available points
    max_points = min(12, club_point)

    return str(max_points)


def get_competition_id_by_name(name):
    competition_id = None

    for index, competition_data in enumerate(server.competitions):
        if competition_data['name'] == name:
            competition_id = index
            break

    return competition_id


def str_to_datetime(date_time_str):
    return datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
