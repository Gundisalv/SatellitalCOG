from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from satcog.config import Config
from satcog.log import load_logger
import os


app = None
_api = None


def create_app():
    global app, _api, jwt

    os.environ['FLASK_ENV'] = Config.flask['env']
    load_logger()

    app = Flask(__name__, instance_relative_config=True)
    app.config['TESTING'] = Config.flask['testing']
    app.config['DEBUG'] = Config.flask['testing']
    app.url_map.strict_slashes = False

    CORS(app)

    authorizations = {
        'apiKey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        },
        'apiKeyQuery': {
            'type': 'apiKey',
            'in': 'query_string',
            'name': 'AuthorizationMobile'
        }
    }

    _api = Api(app, version='1.0',
               title='Optiagro API V2',
               description='Complete REST API', authorizations=authorizations)

    app.config['JWT_SECRET_KEY'] = Config.flask['JWT_SECRET']
    app.config['ERROR_404_HELP'] = False
    app.config['ERROR_INCLUDE_MESSAGE'] = False
    jwt = JWTManager(app)

    from mongoengine import connect
    from elasticsearch_dsl import connections
    import api.rest.utils.auth.auth_decorator
    import api.rest.utils.error.handlers

    connections.create_connection(hosts=[Config.ELASTICSEARCH['URL']], timeout=20)

    # OPEN MONGO CONNECTION
    connect(alias='default', host=Config.MONGO['HOST'])
    _load_namespaces(_api)
    return app


def _load_namespaces(api):
    from api.rest.auth import ns, resources
    api.add_namespace(ns)

    from api.rest.admin import ns, resources
    api.add_namespace(ns)

    from api.rest.account import ns, resources
    api.add_namespace(ns)

    from api.rest.contractor import ns, resources
    api.add_namespace(ns)

    from api.rest.campos import ns
    api.add_namespace(ns)

    from api.rest.campos.gis.chemicals import ns
    api.add_namespace(ns)

    from api.rest.campos.gis.crops import ns
    api.add_namespace(ns)

    from api.rest.campos.gis.downloads import ns
    api.add_namespace(ns)

    from api.rest.engineer import ns
    api.add_namespace(ns)

    from api.rest.campos.gis.history import ns
    api.add_namespace(ns)

    from api.rest.campos.gis.notes import ns
    api.add_namespace(ns)

    from api.rest.campos.gis.satellital import ns
    api.add_namespace(ns)

    from api.rest.campos.gis.tasks import ns
    api.add_namespace(ns)
    
    from api.rest.campos.gis.user_layers import ns
    api.add_namespace(ns)

    from api.rest.machinery import ns
    api.add_namespace(ns)

    from api.rest.media import ns
    api.add_namespace(ns)

    from api.rest.rent.rent_account import ns
    api.add_namespace(ns)

    from api.rest.rent import ns, ns_campos
    api.add_namespace(ns)
    api.add_namespace(ns_campos)

    from api.rest.rent.campos.gis.assessment.ambient import ns
    api.add_namespace(ns)

    from api.rest.rent.campos.gis.assessment import ns
    api.add_namespace(ns)

    from api.rest.rent.campos.gis.assessment.flood import ns
    api.add_namespace(ns)
    
    from api.rest.rent.campos.gis.assessment.route import ns
    api.add_namespace(ns)

    from api.rest.rent.campos.gis.assessment.points import ns
    api.add_namespace(ns)

    from api.rest.rent.campos.gis.assessment.precipitation import ns
    api.add_namespace(ns)
    
    from api.rest.rent.campos.gis.assessment.route import ns
    api.add_namespace(ns)

    from api.rest.rent.campos.gis.assessment.soil import ns
    api.add_namespace(ns)

    from api.rest.rent.campos.gis.assessment.stability import ns
    api.add_namespace(ns)

    from api.rest.rent.campos.gis.assessment.weeds import ns
    api.add_namespace(ns)

    from api.rest.reports import ns
    api.add_namespace(ns)

    from api.rest.notifications import ns
    api.add_namespace(ns)

