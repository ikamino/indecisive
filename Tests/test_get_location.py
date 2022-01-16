from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="http")
location = geolocator.geocode("6319 Tyne Street Vancouver BC")
# we need address, city, and province
print(location.latitude, location.longitude)