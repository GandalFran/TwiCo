#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import datetime
from flask_restx import Resource
import json

from soa import config
from soa.run import api
from soa.core import cache, limiter
from soa.api.twitter_models import twitter_model
from soa.api.twitter_parsers import twitter_argument_parser
from soa.services.news_twitter_extraction import NewsAndTwitterExtraction
from soa.utils import handle400error, handle404error, handle500error


twitter_ns = api.namespace('twitter', description='Provides tweets about a specific theme or topic')


@twitter_ns.route('/tweets')
class GetTweets(Resource):

    @limiter.limit('1000/hour') 
    @cache.cached(timeout=84600, query_string=True)
    @api.expect(twitter_argument_parser)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @api.marshal_with(twitter_model, code=200, description='OK', as_list=True)
    def get(self):
        """
        Returns a JSON array with the information of the tweets retrieved about a specific topic or theme.
        """

        # Retrieve arguments
        try:
            args = twitter_argument_parser.parse_args()

            query = args['q']
            if query is None:
                return handle400error(twitter_ns, "The 'q' argument is required. Please, check the swagger documentation at /v1")

            count_tweets = args['count_tweets']
            if count_tweets is None:
                count_tweets = config.DEFAULT_NUM_TWEETS_EXTRACTED
            else:
                count_tweets = int(count_tweets)

            count_news = args['count_news']
            if count_news is None:
                count_news = config.DEFAULT_NUM_NEWS_EXTRACTED
            else:
                count_news = int(count_news)

            lang = args['lang']
            if lang is None:
                lang = config.DEFAULT_TWEETS_LANGUAGE

            from_date = args['from_date']
            if from_date is None:
                from_date = datetime.datetime.now().strftime('%Y-%m-%d')

            to_date = args['to_date']
            if to_date is None:
                to_date = datetime.datetime.now().strftime('%Y-%m-%d')

        except Exception as e:
            print(e)
            return handle400error(twitter_ns, 'The provided arguments are not correct. Please, check the swagger documentation at /v1')

        # Check arguments
        
        if not query:
            return handle400error(twitter_ns, 'The provided query is empty')

        if count_tweets <= 0:
            return handle400error(twitter_ns, 'The provided number of tweets to extract is 0.')

        if count_news <= 0:
            return handle400error(twitter_ns, 'The provided number of news to extract is 0.')

        if len(lang) > 5: # 5 is the maximum length of a ISO language code
            return handle400error(twitter_ns, 'The provided language is not an ISO code')

        try:
            to_date_dt = datetime.datetime.strptime(to_date, '%Y-%m-%d')
        except:
            return handle400error(twitter_ns, 'The provided date in to_date argument is not properly formatted in ISO (YYYY-mm-dd).')

        try:
            from_date_dt = datetime.datetime.strptime(from_date, '%Y-%m-%d')
        except:
            return handle400error(twitter_ns, 'The provided date in from_date argument is not properly formatted in ISO (YYYY-mm-dd).')

        if from_date_dt > to_date_dt:
            return handle400error(twitter_ns, 'The date interval provided in from_date and to_date arguments is not consistent.')

        # retrieve covid cases
        results = []
        try:
            extractor = NewsAndTwitterExtraction()
            results = extractor.extract(query=query, 
                                       count_tweets=count_tweets,
                                       count_news=count_news,
                                       lang=lang,
                                       from_date=from_date_dt,
                                       to_date=to_date_dt)
        except:
            return handle500error(twitter_ns)

        # if there are no tweets found about the topic given, return 4040 error
        if not results:
            return handle404error(twitter_ns, 'No results were found for the given parameters.')

        with open('data.json', 'w') as outfile:
            json.dump(results, outfile)

        return results
            