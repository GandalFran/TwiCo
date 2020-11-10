#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.


from flask_restx import fields

from soa.run import api


adress_model = api.model('Adress information', {
	'suburb': fields.String(example='Pedralbes'),
	'city_district': fields.String(example='les Corts'),
	'city': fields.String(example='Barcelona'),
	'county': fields.String(example='Barcelonès'),
	'state': fields.String(example='Catalonia'),
	'postcode': fields.String(example='08001'),
	'country': fields.String(example='Spain'),
	'country_code': fields.String(example='es'),
}, description='Information of a concrete adress in the API.')

location_model = api.model('Location information',{
	'lon': fields.Float(example=2.10935592753843, description='Latitude.'),
	'lat': fields.Float(example=41.3916525, description='Longitude.'),
	'address': fields.Nested(adress_model, description='Dictionary with extra adress information.')
}, description='Information of location data in the API.')

covid_model = api.model('Covid information', {
	'cases': fields.Integer(example=10, description='Number of confirmed cases.'),
	'location': fields.Nested(location_model, description='Covid cases location information.'),
	'date': fields.DateTime(example='2020-11-02T00:00:00', description='Date in ISO 8601 format.'),
	'source': fields.String(example='Agència de Salut Pública de Barcelona', description='Institution that provides the information.')
}, description='Information of number of confirmed COVID cases, in a concrete city neighborhood and date.')