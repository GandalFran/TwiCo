#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import datetime
from flask_restx import Resource

from soa import config
from soa.run import api
from soa.core import cache, limiter
from soa.api.sentiment_models import sentiment_model
from soa.api.sentiment_parsers import sentiment_argument_parser
from soa.models.sentiment_model import SentimentAnalyzer
from soa.utils import handle400error, handle404error, handle500error


sentiment_ns = api.namespace('analyze', description='Provides tweets about a specific theme or topic')


@sentiment_ns.route('/sentiment')
class GetSentimentAnalysis(Resource):

    @limiter.limit('1000/hour') 
    @cache.cached(timeout=60, query_string=True)
    @api.expect(sentiment_argument_parser)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @api.marshal_with(sentiment_model, code=200, description='OK', as_list=True)
    def get(self):
        """
        Returns a JSON array with the information of the tweets retrieved about a specific topic or theme.
        """

        # Retrieve arguments
        try:
            args = sentiment_argument_parser.parse_args()

            content = args['content']
            if content is None:
                return handle400error(sentiment_ns, "The 'content' argument is required. Please, check the swagger documentation at /v1")
        except:
            return handle400error(sentiment_ns, 'The provided arguments are not correct. Please, check the swagger documentation at /v1')

        # Check arguments
        if type(content) != str:
            return handle400error(sentiment_ns, 'The type of the provided argument is not correct.')

        # retrieve covid cases
        try:
            analyzer = SentimentAnalyzer()
            sentiment_result = analyzer.analyze(content)
        except:
            return handle500error(sentiment_ns)

        # if there are no tweets found about the topic given, return 4040 error
        if not sentiment_result:
            return handle404error(sentiment_ns, 'No sentiment result was given for the given parameters.')

        return sentiment_result
            