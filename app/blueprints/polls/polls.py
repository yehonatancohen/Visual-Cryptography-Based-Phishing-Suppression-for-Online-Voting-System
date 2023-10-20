from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_required
import database as db

polls = Blueprint('polls', __name__,
    template_folder='templates',
    static_folder='static/polls')


@polls.route('/createpoll', methods=['GET','POST'])
@login_required
def createpoll():
    if request.method == 'POST':
        poll_name = request.form.get('pollname')
        options = request.form.getlist('choises')
        print(options)
        from_date = request.form.get('fromdate')
        to_date = request.form.get('todate')
        invitees = request.form.get('invitees')
        cleaned_mails = invitees.replace('\r\n', '')
        email_list = cleaned_mails.split(',')
        owner = session.get('email')
        fromdate_parts = from_date.split('-')
        todate_parts = to_date.split('-')
        from_day = int(fromdate_parts[2])
        from_month = int(fromdate_parts[1])
        from_year = int(fromdate_parts[0])
        to_day = int(todate_parts[2])
        to_month = int(todate_parts[1])
        to_year = int(todate_parts[0])
        id = db.add_survey(poll_name, from_day, from_month, from_year, to_day, to_month, to_year, owner)
        db.add_voters(emails=email_list,survey_id=id)
        return redirect(url_for('polls.mypolls'))
    elif request.method == 'GET':
        return render_template('createPoll.html')

@polls.route('/mypolls', methods=['GET'])
@login_required
def mypolls():
    polls = db.get_surveys_related_to_user(session.get('email'))
    return render_template('mypolls.html',user_polls=polls)

@polls.route('/vote')
@login_required
def vote():
    return render_template('vote.html')

@polls.route('/results/<survey_id>')
@login_required
def results(survey_id):
    results= db.get_candidates_results_per_servey(survey_id=survey_id)
    return render_template('results.html',results=results)
