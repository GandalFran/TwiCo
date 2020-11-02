#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.


from flask_restx import fields

from example.run import api


person_information_model = api.model('Person information', {
	'name': fields.String,
	'fullName': fields.String,
	'age': fields.Integer,
	'weight': fields.Float
}, 
example={
	'name': 'perico',
	'fullName': 'perico de los palotes',
	'age': 19,
	'weight': 97.45
})
