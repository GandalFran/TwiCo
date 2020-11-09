#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

# Variables that contains the credentials to access MapBox API
from soa import config
from locationiq.geocoder import LocationIQ

class LocationIQConverter:
    def __init__(self):
    # Create LocationIQ API object to convert places into their coordinates
        self.geocoder = LocationIQ(LOCATIONIQ_TOKEN)
    #Geolocate the received place returning  its latitude and longitude among other properties
    def place_to_coordinates(self,place=None):
        if(place == None):
            return None
        results = self.geocoder.geocode(place)
        return results

