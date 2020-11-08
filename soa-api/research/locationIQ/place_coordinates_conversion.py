#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

from locationiq.geocoder import LocationIQ
from locationiq_config import *

MAPBOX_KEY = "pk.eyJ1IjoibWlndWVsY2FiZXphc3B1ZXJ0byIsImEiOiJja2g5NG80Nm4wcXVpMnducWZyeDh5Y2xrIn0.X-9lAGXU4ZBiNr_1uj8udQ"


class LocationIQConverter:
    def __init__(self):
    # Create LocationIQ API object to convert places into their coordinates
        self.geocoder = LocationIQ(ACCESS_TOKEN)
    #Geolocate the received place returning  its latitude and longitude among other properties
    def place_to_coordinates(self,place=None):
        if(place == None):
            return None
        results = self.geocoder.geocode(place)
        return results

if __name__ == '__main__':
    l_iq_converter = LocationIQConverter()
    address = "Les Corts Barcelona"
    results = l_iq_converter.place_to_coordinates(address)
    if results == None :
        print("Any address has been introduced")
    else:
    	if results == {} :
    	    print("Address,"+address+ ",not found")
    	else:
            for result in results:
                #print(result)
                lat = result['lat']
                print(lat)
                lng = result['lon']
                print(lng)
                display_name = result['display_name']
                print(display_name)
                type = result['class']
                print(type)

