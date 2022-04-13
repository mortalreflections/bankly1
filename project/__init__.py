from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
import os
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'youcantseeme'
    # base_dir = os.path.abspath(os.path.dirname(__file__))
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, "bankly.sqlite")
    app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://jjkwydocedaxxj:35f616601d2be97b2467fb104989ddde89291e8ff3cb87eff2615ad275d02484@ec2-35-168-194-15.compute-1.amazonaws.com:5432/d9gcscj9c6c6c7'
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate=Migrate(app,db)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)



    from .models import Users, Deposits

    @login_manager.user_loader
    def load_user(user_id):
          return Users.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app