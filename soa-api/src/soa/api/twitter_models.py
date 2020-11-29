#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.


from flask_restx import fields

from soa.run import api

tweet_model = api.model("Tweet information", {
    'url':  fields.String(example='https://twitter.com/NASA/status/967824267948773377', description='URL to the tweet'),
    'text':  fields.String(example='This is a tweet about COVID #covid-19', description='Text of the tweet extracted'),
    'sentiment':  fields.String(example='positive', description='Sentiment result of text analysis'),
})

topics_model = api.model("Topics information", {
    'name': fields.String(example='covid', description='Theme or topic of the tweets extracted'),
    'tweets': fields.List(fields.Nested(tweet_model))
})

twitter_model = api.model('Twitter information', {
	'news': fields.List(example='["This is a news about covid-19,...", "...", ...]', description='News extracted about a theme given'),
	'topics': fields.Nested(topics_model)
}, description='Result of Twitter and News extraction and topic modelling and sentiment analysis')

