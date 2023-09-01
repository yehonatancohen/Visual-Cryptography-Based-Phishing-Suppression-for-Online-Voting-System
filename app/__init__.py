from flask import Flask
import database as db
from flask_login import LoginManager
import sqlite3
from flask_wtf.csrf import CSRFProtect

UPLOAD_FOLDER = './app/uploads'

def create_app():
    app = Flask(__name__)

    # connect to the database
    try:
        db.init_tables()
    except sqlite3.OperationalError:
        # TABLES ALREADY INITIATED
        pass

    #login_manager = LoginManager()
    #login_manager.init_app(app)

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

if __name__ == "__main__":
    create_app().run()