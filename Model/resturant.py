import googlemaps as gm
from geopy.geocoders import Nominatim


class Resturant:
    # location = '6279 eagles drive'
    name = ''
    price_range = ''
    akey = 'AIzaSyCqpnuB4GgssSCxpbmGrGWYSyzGcOtgleo'
    long =  ''
    lat = ''
    
    
    

    # def test():
    #     result = maps.places_nearby(location = (lat + ", " + long), radius = 40000, open_now = True, type = "Resturant")
    #     print(result)


    def __init__(self, location):
        # Assign the argument to the instance's name attribute
        self.location = location
        maps = gm.Client(key = self.akey)
        # url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(location) +'?format=json'
        # response = requests.get(url).json()
        # lat = response[0]["lat"]
        # long = response[0]["lon"]
        geolocator = Nominatim(user_agent="http")
        location = geolocator.geocode(location)
        # we need address, city, and province
        result = maps.places_nearby(location = (location.latitude + ", " + location.longitude), radius = 40000, open_now = True, type = "Resturant")
        print(result)





