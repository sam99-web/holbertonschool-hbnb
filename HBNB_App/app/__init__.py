from flask import Flask
from flask_restx import Api
from config import config
from app.api.v1.amenities import api as amenities_ns
api.add_namespace(amenities_ns, path='/amenities')

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


