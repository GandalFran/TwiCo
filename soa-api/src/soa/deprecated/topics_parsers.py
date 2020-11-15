#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

from flask_restx import reqparse

topics_argument_parser = reqparse.RequestParser()

topics_argument_parser.add_argument('text',
									location='args',
									type=str,
									required=True,
									default=None,
									help='The text of the news to extract topics from.')

topics_argument_parser.add_argument('num_categories',
									location='args',
									type=str,
									required=False,
									default=None,
									help='The number of posible categories to extract.')

topics_argument_parser.add_argument('num_topics_per_category',
									location='args',
									type=str,
									required=False,
									default=None,
									help='The number of topics to extract from each posible category.')