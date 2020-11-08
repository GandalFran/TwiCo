#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.


from flask_restx import fields

from soa.run import api


twitter_model = api.model('Twitter information', {
	'text': fields.String(example='This is a tweet about COVID #covid-19', description='Text of the retrieved tweet'),
	'date': fields.String(example='2020-11-02, 00:00:00', description='Date and time of the tweet posting'),
	'geolocation': fields.String(example='{"type": "Point","coordinates": [-105.2812196, 40.0160921]}', description='Geolocation of the tweet.'),
	'coordinates': fields.String(example='{"type": "Point","coordinates": [-105.2812196, 40.0160921]}', description='Coordinates of the area where the tweet was posted'),
}, description='Tweets posted talking about COVID and other themes')