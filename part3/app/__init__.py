from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from config import DevelopmentConfig

bcrypt = Bcrypt()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    bcrypt.init_app(app)

    api = Api(app, prefix='/api/v1')

    from app.api.v1.users import api as users_api
    api.add_namespace(users_api)

    return app
