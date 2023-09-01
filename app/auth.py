from flask import render_template, request, Blueprint, redirect
import database as db
from PIL import Image
from UTIL.captcha import generate_shares
import shortuuid
from UTIL.email import send_share

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['POST'])
def signup_post():
    #form = RegistrationForm()
    f_name = request.form.get('f_name')
    s_name = request.form.get('s_name')
    email = request.form.get('email')
    password = request.form.get('password')
    sec_question = request.form.get('sec_question')
    sec_answer = request.form.get('sec_answer')
    server_pass = shortuuid.uuid()[0:6]
    share_1, share_2 = generate_shares(sec_answer + "@" + server_pass)
    send_share(share_1)
    db.add_user(email, f_name, s_name, share_2, password, server_pass,sec_question)

    return redirect('login')

@auth.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')

@auth.route('/submitshare', methods=['POST'])
def submit_share():

    emailField = request.form.get('email')
    share_2 = request.files['image']
    PILimage = Image.open(share_2)
    PILimage.show()

    #if db.does_user_exist()
    """form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        
        if (not db.does_user_exist(email)):
            flash("User does not exist")
            return redirect(url_for(auth.login))

        user = db.get_user(email)
        
        if(user):
            #flask.session['email'] = email
            pass
        
        # send the user share to the user
        # save the server share, salt and hash to the database 

        # Redirect to a success page or user profile page
        return redirect(url_for('auth.loginshare'))"""

    return render_template('login.html')



@auth.route('/profile')
def profile():
    return render_template("profile.html")