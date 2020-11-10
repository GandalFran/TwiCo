#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import datetime
from flask_restx import Resource

from soa.run import api
from soa.core import cache, limiter
from soa.api.covid_models import covid_model
from soa.api.covid_parsers import covid_argument_parser
from soa.models.location_iq_model import LocationIqModel
from soa.models.covid_model import BarcelonaCKANCovidExtractor
from soa.utils import handle400error, handle404error, handle500error


covid_ns = api.namespace('covid', description='Provides covid information')


@covid_ns.route('/barcelona')
class GetCovidCases(Resource):

    @limiter.limit('1000/hour') 
    @cache.cached(timeout=60, query_string=True)
    @api.expect(covid_argument_parser)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @api.marshal_with(covid_model, code=200, description='OK', as_list=True)
    def get(self):
        """
        Returns a JSON array with the information of the covid positive cases per neighbourhood in the Barcelona city.
        """

        # retrieve and chek arguments
        try:
            args = covid_argument_parser.parse_args()

            to_date = args['to_date']
            if to_date is None:
                to_date = datetime.datetime.now().date().isoformat()

            from_date = args['from_date']
            if from_date is None:
                from_date = datetime.datetime.now().date().isoformat()
        except:
            return handle400error(covid_ns, 'The providen arguments are not correct. Please, check the swagger documentation at /v1')

        try:
            to_date_dt = datetime.datetime.strptime(to_date, '%Y-%m-%d')
        except:
            return handle400error(covid_ns, 'The providen date in to_date argument is not properly formatted in ISO (YYYY-mm-dd).')

        try:
            from_date_dt = datetime.datetime.strptime(from_date, '%Y-%m-%d')
        except:
            return handle400error(covid_ns, 'The providen date in from_date argument is not properly formatted in ISO (YYYY-mm-dd).')

        if from_date_dt > to_date_dt:
            return handle400error(covid_ns, 'The date interval providen in from_date and to_date arguments is not consistent.')

        # retrieve covid cases
        try:
            extractor = BarcelonaCKANCovidExtractor()
            covid_cases = extractor.extract(from_date=from_date, to_date=to_date)
        except:
            return handle500error(covid_ns)

        # obtain location for each 
        try:
            location_model = LocationIqModel()
            geocoded_places = { p : location_model.get_coordinates(p) for p in list(set([f"{c['neighborhood']}, {c['city']}" for c in covid_cases])) }
            for c in covid_cases:
                c['location'] = geocoded_places[f"{c['neighborhood']}, {c['city']}"]
        except:
            return handle500error(covid_ns)

        # if there is not covid cases found, return 4040 error
        if not covid_cases:
            return handle404error(covid_ns, 'No COVID data was found for the given parameters.')

        return covid_cases
            