from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from flask_login import login_required
from UTIL.captcha import create_combination
from flask import current_app
import io, uuid, os, json
from PIL import Image
import database as db

polls = Blueprint('polls', __name__,
    template_folder='templates',
    static_folder='static/polls')


@polls.route('/createpoll', methods=['GET','POST'])
@login_required
def createpoll():
    if request.method == 'POST':
        poll_name = request.form.get('pollname')
        #options = request.form.getlist('optionList')
        optionList_json = request.form['optionList']
        optionList = json.loads(optionList_json )
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
        if(owner not in email_list):
            email_list.append(owner)
        id = db.add_survey(poll_name, from_day, from_month, from_year, to_day, to_month, to_year, owner)
        for candidate in optionList:
            db.add_candidate(id, candidate, '')
        db.add_voters(emails=email_list,survey_id=id)
        return redirect(url_for('polls.mypolls'))
    elif request.method == 'GET':
        return render_template('createPoll.html')

@polls.route('/mypolls', methods=['GET'])
@login_required
def mypolls():
    polls = db.get_surveys_related_to_user(session.get('email'))
    return render_template('mypolls.html',user_polls=polls)

@polls.route('/vote/<survey_id>')
@login_required
def vote(survey_id):
    session['survey_id'] = survey_id
    survey = db.get_survey(survey_id)
    candidates = db.get_all_candidates(survey_id)
    survey_name = survey.name
    end_date = survey.end_date
    return render_template('vote.html',survey_id=survey_id, survey_name=survey_name, end_date=end_date, candidates=candidates)

@polls.route('/submitvote', methods=['POST'])
@login_required
def submitvote():
    response = {
        'succeed': False,
        'message': ""
    }
    survey_id = session.get('survey_id')
    candidate_id = int(request.form.get('candidate_id').split('-')[1])
    if candidate_id == 0:
        #flash("Please select a candidate.", "warning")
        response['message'] = "Please select a candidate."
        return jsonify(response)
    sec_answer = request.form.get('sec_answer')
    is_valid = True #db.validate_user(email, password, sec_answer).
    if not is_valid:
        #flash("Invalid credentials.", "warning")
        response['message'] = "Invalid credentials"
        return jsonify(response)
    voter_email = session.get('email')
    result = db.voter_vote(voter_email, survey_id, candidate_id)
    response['succeed'] = result
    if not result:
        response['message'] = "An error occured while voting."
    else:
        response['message'] = '/mypolls'
    return jsonify(response)

@polls.route('/results/<survey_id>')
@login_required
def results(survey_id):
    results_votes= db.get_candidates_results_per_servey(survey_id=survey_id, get_in_precentage=False)
    results_precentage= db.get_candidates_results_per_servey(survey_id=survey_id, get_in_precentage=True)
    return render_template('results.html',results_votes=results_votes, results_precentage=results_precentage)

@polls.route('/submitshare_poll', methods=['POST'])
def submit_share():
    email = session.get('email')
    user_share = request.files['image']
    if user_share.filename != '' and user_share.filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            PILimage = Image.open(io.BytesIO(user_share.read()))

    server_share = db.get_share(email)
    
    # This is the combined image that needs to be viewed to the user
    combined_image = create_combination(server_share, PILimage)

    filename = str(uuid.uuid4()) + '.png'
    combined_image.save(os.path.join(current_app.config['UPLOAD'], filename))

    return jsonify(os.path.join('/static/uploads', filename))


