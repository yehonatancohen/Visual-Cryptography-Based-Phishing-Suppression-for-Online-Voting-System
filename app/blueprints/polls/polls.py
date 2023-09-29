from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import database as db

polls = Blueprint('polls', __name__,
    template_folder='templates',
    static_folder='static/polls')


@polls.route('/createpoll', methods=['GET','POST'])
def createpoll():
    if request.method == 'POST':
        poll_name = request.form.get('pollname')
        from_date = request.form.get('fromdate')
        to_date = request.form.get('todate')
        invitees = request.form.get('invitees')
        owner = session.get('email')
        fromdate_parts = from_date.split('-')
        todate_parts = to_date.split('-')
        from_day = int(fromdate_parts[2])
        from_month = int(fromdate_parts[1])
        from_year = int(fromdate_parts[0])
        to_day = int(todate_parts[2])
        to_month = int(todate_parts[1])
        to_year = int(todate_parts[0])
        db.add_survey(poll_name, from_day, from_month, from_year, to_day, to_month, to_year, owner)
        return redirect(url_for('polls.mypolls'))
    elif request.method == 'GET':
        return render_template('createPoll.html')

@polls.route('/mypolls', methods=['GET'])
def mypolls():
    user_polls = db.get_user_surveys(session.get('email'))
    return render_template('mypolls.html',user_polls=user_polls)

@polls.route('/vote')
def vote():
    return render_template('vote.html')