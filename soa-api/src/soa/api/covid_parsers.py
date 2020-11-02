#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

from flask_restx import reqparse

covid_argument_parser = reqparse.RequestParser()

covid_argument_parser.add_argument('from_date',
							location='args',
							type=str,
							required=False,
							default=None,
							help='The start date to retrieve covid information from. The date must be in ISO 8601 format YYYY-mm-dd.')

covid_argument_parser.add_argument('to_date',
							location='args',
							type=str,
							required=False,
							default=None,
							help='The start date to retrieve covid information from. The date must be in ISO 8601 format YYYY-mm-dd.')