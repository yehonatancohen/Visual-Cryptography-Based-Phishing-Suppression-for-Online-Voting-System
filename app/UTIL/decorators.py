from functools import wraps
from flask import redirect, url_for
from flask_login import current_user
from functools import wraps
#from ..database import users, surveys, voters

def guest_required(view_function):
    @wraps(view_function)
    def wrapped_view(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('home.index'))
        return view_function(*args, **kwargs)
    return wrapped_view 

'''def user_can_vote(survey_id):
    def decorator(view_function):
        @wraps(view_function)
        def wrapped_view(*args, **kwargs):
            if not current_user.is_authenticated:
                #flash("Please log in to vote.", "warning")
                return redirect(url_for('login')) 

            current_survey = surveys.get_survey(survey_id)
            if not current_survey:
                #flash("Survey does not exist.", "warning")
                return redirect(url_for('home.index'))
            
            if not users.does_user_exist(current_user.email):
                #flash("User does not exist.", "warning")
                return redirect(url_for('home.index'))
            
            user_surverys = voters.get_participating_surveys(current_user.email)
            if not current_survey in user_surverys:
                #flash("You are not eligible to vote.", "warning")
                return redirect(url_for('home.index'))
        return wrapped_view
    return decorator'''