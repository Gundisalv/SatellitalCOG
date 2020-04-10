from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from satcog.config import Config
from satcog.log import load_logger
import os

app = None
_api = None

def create_app():
    global app, api

    os.environ['FLASK_ENV'] = Config['flask']['env']
    load_logger()

    app = Flask(__name__, instance_relative_config=True)
    app.config['TESTING'] = Config.getboolean('flask', 'testing')
    app.config['DEBUG'] = Config.getboolean('flask', 'testing')
    app.url_map.strict_slashes = False

    CORS(app)

    api = Api(app, version='1.0',
              title='Satellital COG',
              description='Complete REST API')

    app.config['ERROR_404_HELP'] = False
    app.config['ERROR_INCLUDE_MESSAGE'] = False

    import satcog.rest.utils.error.handlers

    _load_namespaces(api)
    
    return app


def _load_namespaces(api):

    from satcog.rest.landsat.landsat_8 import resources

    from satcog.rest.landsat import ns
    api.add_namespace(ns)
