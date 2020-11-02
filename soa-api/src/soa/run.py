#!/flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

from flask_cors import CORS
from flask import Flask, Blueprint

from soa import config
from soa.api.v1 import api
from soa.core import cache, limiter
from soa.api.covid_ns import covid_ns

app = Flask(__name__)

VERSION = (1, 0)
AUTHOR = 'Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)'


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
    

namespaces = [ covid_ns ]


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

@app.route('/')
def register_redirection():
    """
    Redirects to dcoumentation page.
    """

    return redirect(f'{request.url_root}/{config.URL_PREFIX}', code=302)


initialize_app(app)
CORS(app)

def main():
    separator_str = ''.join(map(str, ["=" for i in range(136)]))
    print(separator_str)
    print(f'Debug mode: {config.DEBUG_MODE}')
    print(f'Authors: {get_authors()}')
    print(f'Version: {get_version()}')
    print(f'Base URL: http://localhost:{config.PORT}{config.URL_PREFIX}')
    print(separator_str)
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG_MODE)


if __name__ == '__main__':
    main()