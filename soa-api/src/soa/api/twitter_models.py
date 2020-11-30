#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.


from flask_restx import fields

from soa.run import api

tweet_model = api.model("Tweet information", {
    'url': fields.String(example='https://twitter.com/NASA/status/967824267948773377', description='URL to the tweet'),
    'text': fields.String(example='This is a tweet about COVID #covid-19', description='Text of the tweet extracted'),
    'sentiment': fields.String(example='positive', description='Sentiment result of text analysis'),
}, description='Information of Tweet data in the API.')

topics_model_2 = api.model("Topics subinformation", {
    'name': fields.String(example='covid', description='Theme or topic of the tweets extracted'),
    'tweets': fields.Nested(tweet_model, description='Tweets retrieved from the topics given.', as_list=True)
}, description='Information of Topics subdata in the API.')

topics_model_1 = api.model("Topics main information", {
    't1': fields.Nested(topics_model_2, description='Tweets retrieved from the topics given.', as_list=True)
}, description='Information of Topics main data in the API.')

source_model = api.model("Source News information", {
    'id': fields.String(example='covid', description='Id of the newspaper source of the news.'),
    'name': fields.String(example='covid', description='Name of the newspaper source of the news.')
}, description='Information of News Source data in the API.')

news_model = api.model("News information", {
    'source': fields.Nested(source_model, description='Information about the source of the news.', as_list=True),
    'author': fields.String(example='covid', description='Author of the news'),
    'title': fields.String(example='covid', description='Title of the news'),
    'description': fields.String(example='covid', description='Description of the news'),
    'url': fields.String(example='covid', description='Original url of the news'),
    'urlToImage': fields.String(example='covid', description='Image in the header of the news'),
    'publishedAt': fields.String(example='covid', description='Date of the publishing of the news'),
    'content': fields.String(example='covid', description='Content of the news')
}, description='Information of News data in the API.')

twitter_model = api.model('Extraction information', {
	'news': fields.Nested(news_model, description='News extracted from the query given.', as_list=True),
	'topics': fields.Nested(topics_model_1, description='Topics and twitter information extracted from the query given.', as_list=True)
}, description='Result of Twitter and News extraction and topic modelling and sentiment analysis')


