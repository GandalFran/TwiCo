#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import datetime
from flask_restx import Resource

from soa import config
from soa.run import api
from soa.core import cache, limiter
from soa.api.topics_models import topics_model
from soa.api.topics_parsers import topics_argument_parser
from soa.models.topic_modelling_model import TopicModellingExtraction
from soa.utils import handle400error, handle404error, handle500error


topics_ns = api.namespace('classification', description='Provides tweets about a specific theme or topic')


@topics_ns.route('/topics')
class GetTopics(Resource):

    @limiter.limit('1000/hour') 
    @cache.cached(timeout=60, query_string=True)
    @api.expect(topics_argument_parser)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @api.marshal_with(topics_model, code=200, description='OK', as_list=True)
    def get(self):
        """
        Returns a JSON array with the information of the tweets retrieved about a specific topic or theme.
        """

        # Retrieve arguments
        try:
            args = topics_argument_parser.parse_args()

            content = args['text']
            if content is None:
                return handle400error(topics_ns, "The 'text' argument is required. Please, check the swagger documentation at /v1")

            num_categories = args['num_categories']
            num_topics_per_category = args['num_topics_per_category']

        except:
            return handle400error(topics_ns, 'The provided arguments are not correct. Please, check the swagger documentation at /v1')

        # Check arguments
        if type(content) != str:
            return handle400error(topics_ns, 'The type of the provided argument is not correct.')

        # retrieve covid cases
        try:
            extractor = None
            topics = []

            if num_categories is None:
                extractor = TopicModellingExtraction()
            else:
                extractor = TopicModellingExtraction(num_topics=num_categories)


            if num_topics_per_category is None:
                topics = extractor.get_topics(text=content)
            else:
                topics = extractor.get_topics(text=content, words_per_topic=num_topics_per_category)
            
        except:
            return handle500error(topics_ns)

        # if there are no tweets found about the topic given, return 4040 error
        if not topics:
            return handle404error(topics_ns, 'No topics result was retrieved for the given parameters.')

        return topics
            