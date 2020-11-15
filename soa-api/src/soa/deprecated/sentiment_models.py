#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.


from flask_restx import fields

from soa.run import api


sentiment_model = api.model('Twitter information', {
	'sentiment': fields.String(example='positive', description='Sentiment result of sentiment analysis with VaderSentiment')
}, description='The result of sentiment analysis of a text given talking about COVID')