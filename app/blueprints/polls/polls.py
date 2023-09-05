from flask import Blueprint, render_template
import database as db

polls = Blueprint('polls', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='/assets')


@polls.route('/CreatePoll')
def createpoll():
    return render_template('createPoll.html')

@polls.route('/mypolls')
def mypolls():
    return render_template('myPolls.html')

@polls.route('/vote')
def vote():
    return render_template('vote.html')