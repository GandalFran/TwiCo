#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import time
from soa import config
from locationiq.geocoder import LocationIQ, LocationIqRequestLimitExeceeded

class LocationIqModel:
	
	def __init__(self):
		"""
		Create LocationIQ API object to convert places into their coordinates
		"""

		self.geocoder = LocationIQ(config.LOCATIONIQ_TOKEN)

	def get_coordinates(self, place:str, max_tries:int=10, time_between_tries:int=1) -> dict:
		"""
		Geolocate the received place returning  its latitude and longitude among other properties.

        Arguments:
            place (:obj:`str`): Plate to convert to coordinates.
            max_tries (:int, optional): Number of tries to obtain location info.
            time_between_tries (:int, optional): Time between tries to obtain location info.
        
        Returns:
            :obj:`dict`: contanining the information in matter of geocoding of the given place.
		"""

		for i in range(max_tries+1):
			try:	
				geocoding_data = self.geocoder.geocode(place)
				if geocoding_data:
					geocoding_data = geocoding_data[0]
					result = {
						'lat': float(geocoding_data['lat']),
						'lon': float(geocoding_data['lon']),
						'address': geocoding_data['address']
					}
				else:
					result = { 'lat': None, 'lon': None, 'address': None }
				return result
			except LocationIqRequestLimitExeceeded:
				time.sleep(time_between_tries)
			except:
				pass

		return None

