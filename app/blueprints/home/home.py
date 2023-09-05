from flask import Blueprint, render_template, redirect, url_for
import database as db

home = Blueprint('home', __name__,
    template_folder='templates',
    static_folder='static/home')

@home.route('/')
def index():
    return render_template('home.html')

@home.route('/profile')
def profile():
    return render_template('profile.html')

@home.route('/about')
def about():
    return render_template('about.html')

@home.route('/contact')
def contact():
    return render_template('contact.html')