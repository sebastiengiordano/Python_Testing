from http import HTTPStatus
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for)
from datetime import datetime

from utils import (
    loadClubs,
    loadCompetitions,
    saveClubs,
    saveCompetitions,
    get_club_id_by_email,
    get_club_id_by_name,
    get_competition_id_by_name,
    str_to_datetime)


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    email = request.form['email']
    club_id = get_club_id_by_email(email)
    if club_id is None:
        return render_template(
            'index.html',
            email_not_found=email), \
                HTTPStatus.BAD_REQUEST
    else:
        return render_template(
            'welcome.html',
            club=clubs[club_id],
            competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template(
            'booking.html',
            club=foundClub,
            competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    # Get request hidden data
    competition = request.form['competition']
    club = request.form['club']
    placesRequired = int(request.form['places'])
    # Get club and competition id
    club_id = get_club_id_by_name(club)
    competition_id = get_competition_id_by_name(competition)

    # Check the competition date
    if (
            str_to_datetime(competitions[competition_id]['date'])
            < datetime.today()):
        flash('    Sorry !!!')
        flash('This competition has already been played.')
        flash('You cannot book places.')
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions), HTTPStatus.BAD_REQUEST
    # Everything is OK
    else:
        # Removed points in clubs
        clubs[club_id]["points"] = str(
            int(clubs[club_id]["points"])
            - placesRequired)
        saveClubs()
        # Removed points in competitions
        competitions[competition_id]['numberOfPlaces'] = str(
            int(competitions[competition_id]['numberOfPlaces'])
            - placesRequired)
        saveCompetitions()
        flash('Great-booking complete!')
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
