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
                return handle400error(news_ns, "The 'q' argument is required. Please, check the swagger documentation at /v1")

            country_code = args['country_code']
            if country_code is None:
                country_code = config.DEFAULT_NEWS_COUNTRY

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

        if len(country_code) != 2: # 2 is the exact length of a ISO 3166-1 country code
            return handle400error(news_ns, 'The provided country is not an ISO 3166-1 code')
        elif country_code not in config.LIST_OF_COUNTRY_CODES:
            return handle400error(news_ns, 'The provided country code is not supported.')

        # Retrieve news
        try:
            extractor = NewsExtraction()
            news = extractor.get_news_top_headlines(query = query,
                                                        country_code = country_code)
        except:
            return handle500error(news_ns)

        # If there are no news found about the topic given, return 404 error
        if len(news) == 0:
            return handle404error(news_ns, 'No news were found for the given parameters.')

        return news
