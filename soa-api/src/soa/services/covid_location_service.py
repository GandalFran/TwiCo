#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

from soa.models.covid_model_eu import EUCovidExtraction
from soa.models.location_iq_model import LocationIqModel
from soa.models.covid_model_bcn import BarcelonaCKANCovidExtractor

class CovidLocationService:

    def extract(self, from_date:str=None, to_date:str=None, world=False) -> list:
        """
        Extracts covid cases and deaths in world or Barcelona city, and transforms the given location into the WGS84
        standar (lat, lon).
        
        Arguments:
            from_date (:obj:`str`, optional): Date in ISO 8601 format (YYYY-mm-dd) where data retrieval time interval will start.
            to_date (:obj:`str`, optional): Date in ISO 8601 format (YYYY-mm-dd) where data retrieval time interval will stop.
            world (bool, optional): If set to true returns COVID world data, else returns barcelona data.
        
        Returns:
            :obj:`list` of :obj:`dict` formatted COVID data.

        Examples:
            >>> print(self.extract())
            [{'cases': '44', 'city': 'Barcelona', 'date': '2020-11-02T00:00:00', 'neighborhood': 'Can Baró', 'source': 'Agència de Salut Pública de Barcelona'}, ...]
        """

        if world:
            # retrieve covid cases
            extractor = EUCovidExtraction()
            covid_cases = extractor.extract(from_date=from_date, to_date=to_date)
            
            # obtain location for each
            location_model = LocationIqModel() 
            geocoded_places = { p : location_model.get_coordinates(p) for p in list(set([c['country'] for c in covid_cases])) }
            for c in covid_cases:
                c['location'] = geocoded_places[c['country']]
        else:
            # retrieve covid cases
            extractor = BarcelonaCKANCovidExtractor()
            covid_cases = extractor.extract(from_date=from_date, to_date=to_date)
            
            # obtain location for each
            location_model = LocationIqModel() 
            geocoded_places = { p : location_model.get_coordinates(p) for p in list(set([f"{c['neighborhood']}, {c['city']}" for c in covid_cases])) }
            for c in covid_cases:
                c['location'] = geocoded_places[f"{c['neighborhood']}, {c['city']}"]


        return covid_cases
