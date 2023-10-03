from functools import wraps
from flask import redirect, url_for
from flask_login import current_user

def guest_required(view_function):
    @wraps(view_function)
    def wrapped_view(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('home.index'))  # Replace 'dashboard' with your desired redirect route
        return view_function(*args, **kwargs)
    return wrapped_view 