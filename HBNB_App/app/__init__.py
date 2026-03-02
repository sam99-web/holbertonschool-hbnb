from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    api = Api(app, version='1.0', title='HBnB API',
              description='HBnB Application API - Part 2',
              doc='/api/v1/', prefix='/api/v1')

    # ✅ CES LIGNES DOIVENT ÊTRE ICI, DANS LA FONCTION, APRÈS api = Api(...)
    from app.api.v1.amenities import api as amenities_ns
    api.add_namespace(amenities_ns, path='/amenities')

    return app
