#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import os

PORT = os.getenv('PORT', 5000)
HOST = os.getenv('HOST', '127.0.0.1')
URL_PREFIX = os.getenv('URL_PREFIX', '/soa/v1')
DEBUG_MODE = bool(os.getenv('DEBUG_MODE', 'False'))
BARCELONA_CKAN_TOKEN = os.getenv('BARCELONA_CKAN_TOKEN', '')