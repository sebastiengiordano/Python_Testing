import json
from http import HTTPStatus
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for)

from utils import (
    loadClubs,
    loadCompetitions,
    saveClubs,
    saveCompetitions,
    get_club_id_by_email,
    get_club_id_by_name,
    get_competition_id_by_name)


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
    competition = [
        c for c in competitions
        if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = (
        int(competition['numberOfPlaces'])
        - placesRequired)
    flash('Great-booking complete!')
    return render_template(
        'welcome.html',
        club=club,
        competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
