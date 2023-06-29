from flask import Flask
from flask_jwt_extended import JWTManager

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

    # authorizations = {
    #     "Bearer Auth":{
    #         "type":"apiKey",
    #         "in":"header",
    #         "name":"Authorization",
    #         "description":"Add a JWT with ** Bearer &lt;JWT&gt; ** to authorize"
    #     }
    # }

    

    app.register_blueprint(auth_views, url_prefix='/auth')
    app.register_blueprint(url_views, path='/')

    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'User':User
        }

    return app