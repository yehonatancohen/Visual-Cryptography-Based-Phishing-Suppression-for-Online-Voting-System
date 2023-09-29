from flask import Blueprint, render_template
import database as db

polls = Blueprint('polls', __name__,
    template_folder='templates',
    static_folder='static/polls')


@polls.route('/createpoll')
def createpoll():
    return render_template('createPoll.html')

@polls.route('/mypolls', methods=['GET'])
def mypolls():
    return render_template('mypolls.html')

@polls.route('/vote')
def vote():
    return render_template('vote.html')