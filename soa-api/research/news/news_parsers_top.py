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
							help='The keyword to search news from.')

news_argument_parser.add_argument('country_code',
							location='args',
							type=str,
							required=False,
							default=None,
							help='Country to search news from.')