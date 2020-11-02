#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.


from flask_restx import Resource

from example.run import api
from example.core import cache, limiter
from example.utils import handle400error, handle404error, handle500error
from example.api.namespace_example_models import person_information_model
from example.api.namespace_example_parsers import person_information_arguments


example_ns = api.namespace('person', description='example of namespace, used to retrive information from person')


@example_ns.route('/get/person')
class GetPerson(Resource):

    @api.expect(person_information_arguments)
    @api.response(400, 'Invalid parameters')
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @limiter.limit('1000/hour')	
    @cache.cached(timeout=60, query_string=True)
    @api.marshal_with(person_information_model, code=200, description='OK')
    def get(self):
        """
        Returns a JSON object with the information of a person.
        """

        try:

            name = None
            try:
                args = person_information_arguments.parse_args()
                name = args['name']
            except:
                handle400error(example_ns, 'The providen arguments are not correct. Please, check the swagger documentation at /v1')

            person = {
                'name': name,
            	'fullName': 'perico de los palotes',
            	'age': 19,
            	'weight': 97.45
            }
            
            return person

        except:
            return handle500error(example_ns)