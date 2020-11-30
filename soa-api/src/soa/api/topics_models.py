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
    'name': fields.String(example='covid AND christmas AND famous', description='Theme or topic of the tweets extracted'),
    'tweets': fields.Nested(tweet_model, description='Tweets retrieved from the topics given.', as_list=True)
}, description='Information of Topics subdata in the API.')

topics_model_1 = api.model("Topics main information", {
    't1': fields.Nested(topics_model_2, description='Tweets retrieved from the topics given.', as_list=True)
}, description='Information of Topics main data in the API.')

source_model = api.model("Source News information", {
    'id': fields.String(example='usa-today', description='Id of the newspaper source of the news.'),
    'name': fields.String(example='USA Today', description='Name of the newspaper source of the news.')
}, description='Information of News Source data in the API.')

news_model = api.model("News information", {
    'source': fields.Nested(source_model, description='Information about the source of the news.', as_list=True),
    'author': fields.String(example='Irene S. Levine, Contributor', description='Author of the news'),
    'title': fields.String(example='How To Watch The Andrea Bocelli Christmas Concert At Home', description='Title of the news'),
    'description': fields.String(example='"Beloved tenor Andrea Bocelli made an honor to make his own concert at home.', description='Description of the news'),
    'url': fields.String(example='https://www.forbes.com/sites/irenelevine/2020/11/30/how-to-watch-the-andrea-bocelli-christmas-concert-at-home/', description='Original url of the news'),
    'urlToImage': fields.String(example='https://thumbor.forbes.com/thumbor/fit-in/1200x0/filters%3Aformat%28jpg%29/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F5fc46b8b969cdd6acb06ddb5%2F0x0.jpg', description='Image in the header of the news'),
    'publishedAt': fields.String(example='2020-11-30, 12:00:00', description='Date of the publishing of the news'),
    'content': fields.String(example='italian tenor andrea bocelli at home in forte dei marmi, italy, ...', description='Content of the news')
}, description='Information of News data in the API.')

topics_model = api.model('Extraction information', {
	'news': fields.Nested(news_model, description='News extracted from the query given.', as_list=True),
	'topics': fields.Raw(description='Topics and twitter information extracted from the query given.', as_list=True)
}, description='Result of Twitter and News extraction and topic modelling and sentiment analysis')


