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
    get_club_points_by_id,
    get_competition_id_by_name,
    str_to_datetime)


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html', clubs=clubs)


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


@app.route('/book/<competition>/<club>', methods=['POST'])
def book(competition, club):
    # Get club and competition id
    club_id = get_club_id_by_name(club)
    competition_id = get_competition_id_by_name(competition)
    # Check if club and competition have been found
    if club_id is not None and competition_id is not None:
        max_points = get_club_points_by_id(club_id)
        if max_points == '0':
            flash(
                "Warning: You cannot book more place, "
                "since you have no more point.")
        return render_template(
            'booking.html',
            club=clubs[club_id],
            competition=competitions[competition_id],
            max_points=max_points)

    flash("Something went wrong-please try again")
    if club_id is None:
        return render_template('index.html'), HTTPStatus.BAD_REQUEST
    else:
        return render_template(
            'welcome.html',
            club=clubs[club_id],
            competitions=competitions), HTTPStatus.BAD_REQUEST


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
            club=clubs[club_id],
            competitions=competitions), HTTPStatus.BAD_REQUEST

    # Check if no more than 12 places
    # per competition has been booked
    elif placesRequired > 12:
        flash('    Sorry !!!')
        flash('You cannot book more than 12 places.')
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions), HTTPStatus.BAD_REQUEST

    # Else, everything is OK
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
        # Display success messages
        flash('Great-booking complete!')
        flash('')
        competition_name = competitions[competition_id]['name']
        if placesRequired == 1:
            flash(f'You\'ve book one place for {competition_name}.')
        else:
            flash(f'You\'ve book {placesRequired} places '
                    f'for {competition_name}.')
        return render_template(
            'welcome.html',
            club=clubs[club_id],
            competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
