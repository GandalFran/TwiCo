#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import datetime
from flask_restx import Resource

from soa import config
from soa.run import api
from soa.core import cache, limiter
from soa.api.news_models import news_model
from soa.api.news_parsers import news_argument_parser
from soa.models.news_model import NewsExtraction
from soa.utils import handle400error, handle404error, handle500error

news_ns = api.namespace('newspaper', description='Provides news about a specific theme or topic')

@news_ns.route('/news')
class GetNews(Resource):

    @limiter.limit('1000/hour')
    @cache.cached(timeout=60, query_string=True)
    @api.expect(news_argument_parser)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @api.marshal_with(news_model, code=200, description='OK', as_list=True)
    def get(self):
        """
        Returns a JSON array with the information of the news retrieved about a specific topic or theme.
        """

        # Retrieve arguments
        try:
            args = news_argument_parser.parse_args()

            query = args['q']
            if query is None:
                return handle400error(news_ns, "The 'qInTitle' argument is required. Please, check the swagger documentation at /v1")

            from_date = args['from']
            if from_date is None:
                from_date = datetime.datetime.now().strftime('%Y-%m-%d')

            to_date = args['to']
            if to_date is None:
                to_date = datetime.datetime.now().strftime('%Y-%m-%d')

            lang = args['lang']
            if lang is None:
                lang = config.DEFAULT_NEWS_LANGUAGE

            count = args['count']
            if count is None:
                count = config.DEFAULT_NUM_NEWS_EXTRACTED
            else:
                count = int(count)

        except Exception as e:
            print(e)
            return handle400error(news_ns, 'The provided arguments are not correct. Please, check the swagger documentation at /v1')

        # Check arguments
        try:
            q = query.strip()
            index = q.find(' ')
            if index != -1:
                return handle400error(news_ns, 'The provided query is not a single word.')
        except:
            return handle400error(news_ns, 'The provided query is not a single word.')

        try:
            from_date_dt = datetime.datetime.strptime(from_date, '%Y-%m-%d')
        except:
            return handle400error(news_ns, 'The provided date in from_date argument is not properly formatted in ISO (YYYY-mm-dd).')

        try:
            to_date_dt = datetime.datetime.strptime(to_date, '%Y-%m-%d')
        except:
            return handle400error(news_ns, 'The provided date in to_date argument is not properly formatted in ISO (YYYY-mm-dd).')

        if from_date_dt > to_date_dt:
            return handle400error(news_ns, 'The date interval provided in from_date and to_date arguments is not consistent.')

        if len(lang) != 2: # 2 is the exact length of a ISO 639-1 country code
            return handle400error(news_ns, 'The provided language is not an ISO 639-1 code')
        elif lang not in config.LIST_OF_LANGUAGE_CODES:
            return handle400error(news_ns, 'The provided language code is not supported.')

        if count <= 0:
            return handle400error(news_ns, 'Minimum number of news retrieved is 1.')
        elif count > 100:
            return handle400error(news_ns, 'Maximum number of news retrieved is 100.')

        # Retrieve news
        try:
            extractor = NewsExtraction()
            news = extractor.get_news_everything(q = query,
                                                    from_date = from_date,
                                                    to_date = to_date,
                                                    lang = lang,
                                                    count = count)
        except:
            return handle500error(news_ns)

        # If there are no news found about the topic given, return 404 error
        if len(news) == 0:
            return handle404error(news_ns, 'No news were found for the given parameters.')

        return news
