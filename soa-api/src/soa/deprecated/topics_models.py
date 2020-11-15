#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.


from flask_restx import fields

from soa.run import api


topics_model = api.model('Topic Extraction information', {
	'topics': fields.List(example=['politics', 'health', 'care', 'analysis'], description='Topics or themes predicted from a news text about COVID.')
}, description='The result of extracting the topics or main themes from a text about COVID')