#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

from flask_restx import reqparse

sentiment_argument_parser = reqparse.RequestParser()

sentiment_argument_parser.add_argument('content',
										location='args',
										type=str,
										required=True,
										default=None,
										help='The text to pass through sentiment analysis and detect sentiment.')