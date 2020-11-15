#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

from flask_restx import reqparse

news_argument_parser = reqparse.RequestParser()

news_argument_parser.add_argument('q',
							location='args',
							type=str,
							required=True,
							default=None,
							help='The keyword to search in the title of news.')

news_argument_parser.add_argument('from',
							location='args',
							type=str,
							required=False,
							default=None,
							help='The start date to retrieve news from. The date must be in ISO 8601 format YYYY-mm-dd.')

news_argument_parser.add_argument('to',
							location='args',
							type=str,
							required=False,
							default=None,
							help='The end date to retrieve news from. The date must be in ISO 8601 format YYYY-mm-dd.')

news_argument_parser.add_argument('lang',
							location='args',
							type=str,
							required=False,
							default=None,
							help="Language of the news to retrieve. The language must be ISO coded. For example, English code would be 'en'.")

news_argument_parser.add_argument('count',
							location='args',
							type=str,
							required=False,
							default=None,
							help='Number of news to retrieve.')
