#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.


from flask_restx import fields

from soa.run import api


covid_model = api.model('Covid information', {
	'cases': fields.Integer(example=10, description='Number of confirmed cases.'),
	'city': fields.String(example='Barcelona', description='Affected city.'),
	'date': fields.DateTime(example='2020-11-02T00:00:00', description='Date in ISO 8601 format.'),
	'neighborhood': fields.String(example='la Barceloneta', description='Neighborhood city.'),
	'source': fields.String(example='Agència de Salut Pública de Barcelona', description='Institution that provides the information.')
}, description='Information of number of confirmed COVID cases, in a concrete city neighborhood and date.')