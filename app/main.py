from flask import Blueprint, render_template
import database as db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')