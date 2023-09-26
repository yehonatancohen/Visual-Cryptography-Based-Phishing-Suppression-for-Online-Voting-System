from flask import Flask
import sqlite3, os
import database as db
from blueprints.auth.auth import auth
from blueprints.home.home import home
from blueprints.polls.polls import polls

def create_app():
    app = Flask(__name__, static_folder="blueprints/static")
    app.secret_key = 'your_secret_key_here'
    app.config['UPLOAD'] = app.static_folder + '/uploads'

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(polls, url_prefix='/')

    # connect to the database
    try:
        db.init_tables()
    except sqlite3.OperationalError:
        # TABLES ALREADY INITIATED
        pass
    
    app.run(debug=True)

    return app

if __name__ == "__main__":
    create_app().run()