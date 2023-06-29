from flask import Flask
from flask_jwt_extended import JWTManager

from .auth.views import auth_namespace
from .auth.models import User

from ._url.views import url_namespace

from .config import config_chosen
from .utils import db, migrate

 


def create_app(config=config_chosen):
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    authorizations = {
        "Bearer Auth":{
            "type":"apiKey",
            "in":"header",
            "name":"Authorization",
            "description":"Add a JWT with ** Bearer &lt;JWT&gt; ** to authorize"
        }
    }

    

    api.add_namespace(auth_namespace, path='/api/auth')
    api.add_namespace(url_namespace, path='/api/')

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