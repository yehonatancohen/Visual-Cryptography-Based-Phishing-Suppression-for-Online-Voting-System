from flask import Flask, render_template, request, redirect, url_for, blueprints, flash
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
from forms import RegistrationForm, LoginForm
from models import user
import database as db
from helpers import captcha, key

auth = Blueprint('auth', __name__)

@auth.route('/register')
def signup():
    return render_template('register.html')

@auth.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Get user input
        first_name = form.name.data.split(" ")[0]
        last_name = form.name.data.split(" ")[1]
        security_code = form.security.data # Security question
        email = form.email.data
        password = form.password.data

        (user_share, server_share) = captcha.generate_shares()

        user_msg = db.add_user(email, first_name, last_name, server_share, password)

        if (user_msg):
            flash("error message")
            return redirect(url_for('auth.register'))
        
        # send the user share to the user

        # Redirect to a success page or user profile page
        return redirect(url_for('auth.profile'))

    return render_template('register.html', form=form)


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        
        if (not db.does_user_exist(email)):
            flash("User does not exist")
            return redirect(url_for(auth.login))

        
        
        # send the user share to the user
        # save the server share, salt and hash to the database 

        # Redirect to a success page or user profile page
        return redirect(url_for('auth.profile'))

    return render_template('login.html', form=form)

@auth.route('/profile')
def profile():
    return render_template("profile.html")