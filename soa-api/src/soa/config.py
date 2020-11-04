#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import os

##### General variables
PORT = 5000
HOST = '0.0.0.0'
URL_PREFIX = '/soa/v1'
DEBUG_MODE = True

##### Covid variables
BARCELONA_CKAN_TOKEN = "12552198a8992ac3b2129ebc803e29ac50515f383dfdc147abf39dd127050db1"

##### Twitter variables
# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = '1252180895643111426-yOMCKE190xT3UljlDpmGAoTw3vmRyV'
ACCESS_SECRET = 'DbXFYeUlPYAgWSfgnPGyzieRmfFSHk2M3WRm4EpSfAkXm'
CONSUMER_KEY = 'jL9ufYzLGl6ezNygFGhts4uif'
CONSUMER_SECRET = 'eqsQuOxClzrTjmEQcxtXbPkBVD4XrjM3EkYNqgsEcr53mzB3Xl'

# Variables to use bearer token
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHwMDwEAAAAAj5283nyjyrK%2BXzu5F01p%2Fx0b104%3DjCVTTywiqnH8C7XMqe60fEeXvaJbnpyoUOs140fLhIUutEgLsa"
SEARCH_TWEETS_URI = 'https://api.twitter.com/1.1/search/tweets.json'

DEFAULT_NUM_TWEETS_EXTRACTED = 300
DEFAULT_TWEETS_LANGUAGE = 'en'