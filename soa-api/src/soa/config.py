#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import os

# api config
PORT = 5000
HOST = '0.0.0.0'
URL_PREFIX = '/soa/v1'
DEBUG_MODE = True

# barcelona ckan token
BARCELONA_CKAN_TOKEN = "12552198a8992ac3b2129ebc803e29ac50515f383dfdc147abf39dd127050db1"

# twitter api config
ACCESS_TOKEN = '1252180895643111426-yOMCKE190xT3UljlDpmGAoTw3vmRyV'
ACCESS_SECRET = 'DbXFYeUlPYAgWSfgnPGyzieRmfFSHk2M3WRm4EpSfAkXm'
CONSUMER_KEY = 'jL9ufYzLGl6ezNygFGhts4uif'
CONSUMER_SECRET = 'eqsQuOxClzrTjmEQcxtXbPkBVD4XrjM3EkYNqgsEcr53mzB3Xl'

# twitter bearer api config
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHwMDwEAAAAAj5283nyjyrK%2BXzu5F01p%2Fx0b104%3DjCVTTywiqnH8C7XMqe60fEeXvaJbnpyoUOs140fLhIUutEgLsa"
SEARCH_TWEETS_URI = 'https://api.twitter.com/1.1/search/tweets.json'

DEFAULT_NUM_TWEETS_EXTRACTED = 300
DEFAULT_TWEETS_LANGUAGE = 'en'

# location api config
LOCATIONIQ_TOKEN = "pk.3086d0188b2fa4e26bcec2436d145356"
MAPBOX_TOKEN = "pk.eyJ1IjoibWlndWVsY2FiZXphc3B1ZXJ0byIsImEiOiJja2g5NG80Nm4wcXVpMnducWZyeDh5Y2xrIn0.X-9lAGXU4ZBiNr_1uj8udQ"