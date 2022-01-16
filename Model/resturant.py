import googlemaps as gm
import requests
import urllib.parse


class Resturant:
    location = '6279 eagles drive'
    name = ''
    price_range = ''
    akey = 'AIzaSyCqpnuB4GgssSCxpbmGrGWYSyzGcOtgleo'

    
    
    # result = maps.places_nearby(location = )

    def __init__(self, location):
        # Assign the argument to the instance's name attribute
        self.location = location
        maps = googlemaps.Client(key = akey)
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(location) +'?format=json'
        response = requests.get(url).json()
        print(response[0]["lat"])
        print(response[0]["lon"])




