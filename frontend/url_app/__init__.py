import os

from flask import Flask
# from flask_login import LoginManager

# from .url import views
from .auth.views import auth_views
# from .url.views import mail

from dotenv import load_dotenv
load_dotenv('.env') 


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'somerandomletters'


    # app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth_views, url_prefix='/')

    # login_manager = LoginManager(app)
    # login_manager.login_view = 'auth_views.login'

    # @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))

    return app
