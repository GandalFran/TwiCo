
from flask_cors import CORS
from flask import Flask, Blueprint

from example import config
from example.api.v1 import api
from example.core import cache, limiter
from example.api.namespace_example import example_ns

app = Flask(__name__)

VERSION = (1, 0)
AUTHOR = 'Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto) and Francisco Pinto-Santos (@gandalfran)'


def get_version():
    """
    This function returns the API version that is being used.
    """

    return '.'.join(map(str, VERSION))


def get_authors():
    """
    This function returns the API's author name.
    """

    return str(AUTHOR)


__version__ = get_version()
__author__ = get_authors()
    

namespaces = [ example_ns ]


def initialize_app(flask_app):
    """
    This function initializes the Flask Application, adds the namespace and registers the blueprint.
    """

    flask_app.config.from_object(config)

    v1 = Blueprint('api', __name__, url_prefix=config.URL_PREFIX)
    api.init_app(v1)
    cache.init_app(flask_app)
    for ns in namespaces:
        api.add_namespace(ns)
    flask_app.register_blueprint(v1)
    limiter.exempt(v1)


initialize_app(app)
CORS(app)

def main():
    separator_str = ''.join(map(str, ["=" for i in range(136)]))
    print(separator_str)
    print(f'Debug mode: {config.DEBUG_MODE}')
    print(f'Authors: {get_authors()}')
    print(f'Version: {get_version()}')
    print(f'Base URL: http://{config.HOST}:{config.PORT}{config.URL_PREFIX}')
    print(separator_str)
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG_MODE)


if __name__ == '__main__':
    main()