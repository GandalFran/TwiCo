#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import json
import datetime
import pandas as pd

from soa import config

class EUCovidExtraction:
    
    def _do_request(self, uri: str) -> pd.DataFrame:
        """
        Retrieves data from COVID worldwide from the EU opendata portal.
        
        Arguments:
            uri (:obj:`str`): dataset's URI.

        Returns:
            :obj:`pd.DataFrame`: result from the request, contianing the COVID information worldwide per country.
        """

        try:
            df = pd.read_csv(uri)
            return df
        except:
            return None

    def _filter_dates(self, df: pd.DataFrame, from_date: str, to_date: str) -> list:
        """
        Filters teh dataset by given dates.
        
        Arguments:
            df (:obj:`pd.DataFrame`): dataFrame to filter.
            from_date (:obj:`str`): Date in ISO 8601 format (YYYY-mm-dd) where data retrieval time interval will start.
            to_date (:obj:`str`): Date in ISO 8601 format (YYYY-mm-dd) where data retrieval time interval will stop.
     
        Returns:
            :obj:`list` of :obj:`dict` result from the request, contianing the COVID information in worldwide per country.
        """

        # create datetimes to comparision
        to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')
        from_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')

        # build datetime objects with df
        df['dateRep'] = pd.to_datetime(df['dateRep'], format='%d/%m/%Y')

        # select data
        selected_data = df.loc[(df['dateRep'] >= from_date ) & ( df['dateRep'] <= to_date )].copy()

        # turn data to JSON format
        json_data = selected_data.to_dict(orient='records')
        return json_data

    def _format_response(self, response:list) -> list:
        """
        Performs a HTTP GET request, following CKAN protocol to obtain COVID data provided by barcelona opendata.
        
        Arguments:
            response (:obj:`list` of :obj:`dict`): result of the HTTP GET request, containing COVID data.
        
        Returns:
            :obj:`list` of :obj:`dict` formatted COVID data.
        """

        transform_country = lambda x: ' '.join(x.split('_')).replace('(',' ').replace(')',' ')

        return [{
            'date': r['dateRep'].isoformat(),
            'country': transform_country(r['countriesAndTerritories']),
            'cases': r['cases_weekly'],
            'cases': r['deaths_weekly']
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

        # format dates
        if from_date is None:
            from_date = (datetime.datetime.now() - datetime.timedelta(days=2)).date().isoformat()
        if to_date is None:
            to_date = datetime.datetime.now().date().isoformat()

        # build uri of opendata
        uri = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv'

        # download and retrieve data and build dataframe
        df = self._do_request(uri)

        # filter dates
        if df is not None:
            df = self._filter_dates(df, from_date, to_date)
            data = self._format_response(df)
        
        if data is None or not data:
            with open('/etc/eu_data.json','r') as f:
                data = json.loads(f.read())

        return data