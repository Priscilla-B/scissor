from flask import Flask, render_template
from flask_login import LoginManager

from .auth.views import auth_views
from .auth.models import User

from ._url.views import url_views

from .config import config_chosen
from .utils import db, migrate

 


def create_app(config=config_chosen):
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_views, url_prefix='/auth')
    app.register_blueprint(url_views, path='/')
    
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth_views.login'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    with app.app_context():
        db.create_all()

    @app.errorhandler(404)
    def invalid_route(e):
        return render_template('404-page.html')
    
    
    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'User':User
        }

    return app