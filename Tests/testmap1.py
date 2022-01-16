import googlemaps as gm
from geopy.geocoders import Nominatim

maps = gm.Client(key = 'AIzaSyCqpnuB4GgssSCxpbmGrGWYSyzGcOtgleo')
        # url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(location) +'?format=json'
        # response = requests.get(url).json()
        # lat = response[0]["lat"]
        # long = response[0]["lon"]
geolocator = Nominatim(user_agent="http")
location = geolocator.geocode('6279 Eagles Dr Vancouver BC')
# we need address, city, and province
lat_long = str(location.latitude) + "," + str(location.longitude)
result = maps.places_nearby(location = lat_long, radius = 5000, open_now = False, type = "restaurant")
for place in result['results']:
            my_place_id = place['place_id']
            my_fields = ['name', 'formatted_phone_number', 'type']
            place_details = maps.place(place_id = my_place_id, fields = my_fields)
            print(place_details)