#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import json
import datetime
import requests

from soa import config

class BarcelonaCKANCovidExtractor:
    
    def __init__(self):
        self._token = config.BARCELONA_CKAN_TOKEN
        self._base_url = 'https://opendata-ajuntament.barcelona.cat/data/api/action/datastore_search_sql?sql='
        self._resource_id = '290eb517-e7fa-41fb-aa59-389becb8f55b'
        
    def _build_query(self, from_date: str, to_date: str) -> str:
        """
        Builds a SQL query for the CKAN resource.
        
        Arguments:
            from_date (:obj:`str`): Date in ISO 8601 format (YYYY-mm-dd) where data retrieval time interval will start.
            to_date (:obj:`str`): Date in ISO 8601 format (YYYY-mm-dd) where data retrieval time interval will stop.
        
        Returns:
            :obj:`str` SQL query to retrieve covid data from from_date to to_date.
        """

        query = f'SELECT * \
        FROM "{self._resource_id}" \
        WHERE "Territori"=\'Barcelona\' \
        and "Nom_Indicador"=\'Nombre de casos positius per barri\' \
        and "Frequencia_Indicador"=\'Diari\''
        return query

    def _build_uri(self, from_date: str, to_date: str) -> str:
        """
        Builds the URI to perform a CKAN query over covid data provided by barcelona opendata.
        
        Arguments:
            from_date (:obj:`str`): Date in ISO 8601 format (YYYY-mm-dd) where data retrieval time interval will start.
            to_date (:obj:`str`): Date in ISO 8601 format (YYYY-mm-dd) where data retrieval time interval will stop.
        
        Returns:
            :obj:`str` URI to perform a CKAN query to retrieve covid data from from_date to to_date.
        """

        return f'{self._base_url}{self._build_query(from_date, to_date)}'
    
    def _do_request(self, uri: str) -> list:
        """
        Performs a HTTP GET request, following CKAN protocol to obtain COVID data provided by barcelona opendata.
        
        Arguments:
            uri (:obj:`str`): URI to perform an HTTP GET request.
        
        Returns:
            :obj:`list` of :obj:`dict` result from the request, contianing the COVID information in Barcelona per neighborhood.
        """

        response = requests.get(uri, headers={'Authorization':self._token})
        if response.status_code == 200:
            return response.json()['result']['records']
        else:
            return None
        
    def _format_response(self, response:list) -> list:
        """
        Performs a HTTP GET request, following CKAN protocol to obtain COVID data provided by barcelona opendata.
        
        Arguments:
            response (:obj:`list` of :obj:`dict`): result of the HTTP GET request, containing COVID data.
        
        Returns:
            :obj:`list` of :obj:`dict` formatted COVID data.
        """

        return [{
            'date': r['Data_Indicador'],
            'city': r['Territori'],
            'neighborhood': r['Nom_Variable'],
            'cases': r['Valor'],
            'source': r['Font']
        } for r in response]
    
    def extract(self, from_date=None, to_date=None):
        """
        Performs a HTTP GET request, following CKAN protocol to obtain COVID data provided by barcelona opendata.
        
        Arguments:
            from_date (:obj:`str`, optional): Date in ISO 8601 format (YYYY-mm-dd) where data retrieval time interval will start.
            to_date (:obj:`str`, optional): Date in ISO 8601 format (YYYY-mm-dd) where data retrieval time interval will stop.
        
        Returns:
            :obj:`list` of :obj:`dict` formatted COVID data.

        Examples:
            >>> print(self.extract())
            [{'cases': '44', 'city': 'Barcelona', 'date': '2020-11-02T00:00:00', 'neighborhood': 'Can Baró', 'source': 'Agència de Salut Pública de Barcelona'}, ...]
        """

        if from_date is None:
            from_date = (datetime.datetime.now() - datetime.timedelta(days=1)).date().isoformat()
        if to_date is None:
            to_date = datetime.datetime.now().date().isoformat()

        uri = self._build_uri(from_date, to_date)
        data = self._do_request(uri)
        if data or data is not None:
            data = self._format_response(data)
        else:
            with open('/etc/bcn_data.json','r') as f:
                data = json.loads(f.read())

        return data