#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import datetime
from flask_restx import Resource

from soa import config
from soa.run import api
from soa.core import cache, limiter
from soa.api.twitter_models import twitter_model
from soa.api.twitter_parsers import twitter_argument_parser
from soa.models.twitter_model import TwitterExtraction
from soa.utils import handle400error, handle404error, handle500error


twitter_ns = api.namespace('twitter', description='Provides tweets about a specific theme or topic')


@twitter_ns.route('/tweets')
class GetTweets(Resource):

    @limiter.limit('1000/hour') 
    @cache.cached(timeout=60, query_string=True)
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

            count = args['count']
            if count is None:
                count = config.DEFAULT_NUM_TWEETS_EXTRACTED
            else:
                count = int(count)

            lang = args['lang']
            if lang is None:
                lang = config.DEFAULT_TWEETS_LANGUAGE

            from_date = args['from_date']
            if from_date is None:
                from_date = datetime.datetime.now().strftime('%Y-%m-%d')

            to_date = args['to_date']
            if to_date is None:
                to_date = datetime.datetime.now().strftime('%Y-%m-%d')

            include_both = args['include_both']
            if include_both is None:
                include_both = False

        except Exception as e:
            print(e)
            return handle400error(twitter_ns, 'The provided arguments are not correct. Please, check the swagger documentation at /v1')

        # Check arguments
        
        try:
            q = query.split(",")
            if type(q) != list:
                return handle400error(twitter_ns, 'The provided query is not a list.')
        except:
            return handle400error(twitter_ns, 'The provided query is not a list.')

        if count <= 0:
            return handle400error(twitter_ns, 'The provided number of tweets is 0.')

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

        include_both_flag = False
        if type(include_both) != bool:
            if include_both.lower() not in ['true', 'false']:
                return handle400error(twitter_ns, "The value indicated for the parameter is not a correct. The value must be 'True' or 'False'.")
            else:
                if include_both.lower() == 'true':
                    include_both_flag = True
                elif include_both.lower() == 'false':
                    include_both_flag = False

        # retrieve covid cases
        try:
            extractor = TwitterExtraction()
            if len(q) > 1:
                tweets = extractor.get_tweets_multiple_query(query=q, 
                                                             count=count,
                                                             lang=lang,
                                                             start_date=from_date_dt,
                                                             end_date=to_date_dt,
                                                             include_both=include_both_flag)
            elif len(q) == 1:
                tweets = extractor.get_tweets_single_query(query=q, 
                                                           count=count,
                                                           lang=lang,
                                                           start_date=from_date_dt,
                                                           end_date=to_date_dt)
        except:
            return handle500error(twitter_ns)

        # if there are no tweets found about the topic given, return 4040 error
        if not tweets:
            return handle404error(twitter_ns, 'No tweets were found for the given parameters.')

        return tweets
            