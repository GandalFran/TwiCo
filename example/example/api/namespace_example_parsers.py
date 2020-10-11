#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

from flask_restx import reqparse

person_information_arguments = reqparse.RequestParser()

person_information_arguments.add_argument('name',
							location='args',
							type=str,
							required=True,
							help='The name of the person to obtain.')