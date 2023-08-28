# main.py
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
from forms import RegistrationForm, LoginForm
import database
from helpers import captcha, key
app = Flask(__name__)
csrf = CSRFProtect(app)

# Set up your database and import necessary functions/models

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Get user input
        first_name = form.name.data.split(" ")[0]
        last_name = form.name.data.split(" ")[1]
        email = form.email.data
        password = form.password.data

        (user_share, server_share) = captcha.generate_shares()

        database.add_user(email, first_name, last_name, server_share, password)
        
        # send the user share to the user

        # Redirect to a success page or user profile page
        return redirect(url_for('registration_success'))

    return render_template('registration.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Get user input
        email = form.email.data
        password = form.password.data
        
        (salt, hashed_key, server_key) = key.generate_key()

        (user_share, server_share) = captcha.new_user()
        
        # send the user share to the user
        # save the server share, salt and hash to the database 

        # Redirect to a success page or user profile page
        return redirect(url_for('registration_success'))

    return render_template('registration.html', form=form)

@app.route('/mail_check', methods=['POST', 'GET'])
def mail_check(email):
    pass
    #check if email exits, if so, return server share, hash and salt

@app.route('/registration-success')
def registration_success():
    return "Registration successful! Welcome to our site."

if __name__ == '__main__':
    app.run()
