from flask import render_template, request, Blueprint, redirect, url_for, jsonify
import database as db
from PIL import Image
from UTIL.captcha import generate_shares, create_combination
import shortuuid
from UTIL.email import send_share

auth = Blueprint('auth', __name__,
    template_folder='templates',
    static_folder='static/auth')


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
def login():
    return render_template('login.html')

@auth.route('/logout', methods=['POST'])
def logout():
    pass

@auth.route('/checkemail', methods=['POST'])
def check_email():
    form = request.form

    response = {
        'succeed': True,
        'message': ""
    }

    email = request.form.get('email')
    
    if (not db.does_user_exist(email)):
        response['succeed'] = False
        response['message'] = 'User does not exist'
        return jsonify(response)
    
    user = db.get_user(email)
    
    if(user):
        response = email
    
    # send the user share to the user
    # save the server share, salt and hash to the database 
    # Redirect to a success page or user profile page
    # return redirect(url_for('auth.loginshare'))
    return jsonify(response)

@auth.route('/submitshare', methods=['POST'])
def submit_share():

    email = request.form.get('email')
    user_share = request.files['image']
    PILimage = Image.open(user_share)
    PILimage.show()

    server_share = db.get_share(email)
    
    # This is the combined image that needs to be viewed to the user
    combined_image = create_combination(server_share, user_share)

    #if db.does_user_exist()
    

    return render_template('login.html')

@auth.route('/verifypassword', methods=['POST'])
def verify_password():
    email = request.form.get('email')
    password = request.form.get('password')
    sec_question = request.form.get('s_question')
    
    is_valid = db.validate_user(email, password, sec_question)

    if(is_valid):
        return redirect(url_for('auth.profile'))

    return render_template('login.html')