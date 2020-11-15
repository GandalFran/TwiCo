#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.


from flask_restx import fields

from soa.run import api

news_model = api.model('News information', {
	'title': fields.String(example='This is the title of a new', description='Title of the retrieved new'),
	'description': fields.String(example='This is the description of a new', description='Description of the retrieved new'),
	'publishedAt': fields.String(example='2020-11-02, 00:00:00', description='Date and time of the retrieved new'),
	'content': fields.String(example='This is the content of a new', description='Content of the retrieved new'),
	'url': fields.String(example='http://localhost:5000/soa/v1/newspaper/news?q=covid&country_code=gb', description='Url of the retrieved new'),
}, description='News posted talking about COVID and other themes')