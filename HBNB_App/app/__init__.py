from flask import Flask
from flask_restx import Api
from app.config import config
from app.api.v1.api_blueprint import api_v1

def create_app(config_name='default'):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize Flask-RESTx API
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API - Part 2',
        doc='/api/v1/',
        prefix='/api/v1'
    )
    
    # Register API blueprint
    api.add_namespace(api_v1)
    
    return app
