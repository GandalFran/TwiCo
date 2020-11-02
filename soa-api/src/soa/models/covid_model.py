#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import datetime
import requests

from soa import config

class BarcelonaCKANCovidExtractor:
    
    def __init__(self):
        self._token = config.BARCELONA_CKAN_TOKEN
        self._base_url = 'https://opendata-ajuntament.barcelona.cat/data/api/action/datastore_search_sql?sql='
        self._resource_id = '290eb517-e7fa-41fb-aa59-389becb8f55b'
        
    def _build_query(self, from_date, to_date):    
        query = f'SELECT * \
        FROM "{self._resource_id}" \
        WHERE "Territori"=\'Barcelona\' \
        and "Nom_Indicador"=\'Nombre de casos positius per barri\' \
        and "Data_Indicador">=\'{from_date}\' \
        and "Data_Indicador"<=\'{to_date}\' \
        and "Frequencia_Indicador"=\'Diari\''
        return query

    def _build_uri(self, from_date, to_date):
        return f'{self._base_url}{self._build_query(from_date, to_date)}'
    
    def _do_request(self, uri):
        response = requests.get(uri, headers={'Authorization':self._token})
        if response.status_code == 200:
            return response.json()['result']['records']
        else:
            return None
        
    def _format_response(self, response):
        return [{
            'date': r['Data_Indicador'],
            'city': r['Territori'],
            'neighborhood': r['Nom_Variable'],
            'cases': r['Valor'],
            'source': r['Font']
        } for r in response]
    
    def extract(self, from_date=None, to_date=None):
        if from_date is None:
            from_date = (datetime.datetime.now() - datetime.timedelta(days=1)).date().isoformat()
        if to_date is None:
            to_date = datetime.datetime.now().date().isoformat()
        uri = self._build_uri(from_date, to_date)
        data = self._do_request(uri)
        if data is not None:
            data = self._format_response(data)
        return data