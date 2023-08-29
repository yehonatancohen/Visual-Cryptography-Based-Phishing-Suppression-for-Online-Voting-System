from flask import Flask
import database as db

def create_app():
    app = Flask(__name__)

    # connect to the database

    db.init_tables()

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app