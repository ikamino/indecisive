import googlemaps as gm
from geopy.geocoders import Nominatim



def rest_info_list(location):
    place_data = []
    maps = gm.Client(key = '!!!PASTE APIKEY HERE!!!')
        # url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(location) +'?format=json'
        # response = requests.get(url).json()
        # lat = response[0]["lat"]
        # long = response[0]["lon"]
    geolocator = Nominatim(user_agent="http")
    location = geolocator.geocode(location)
    # we need address, city, and province
    lat_long = str(location.latitude) + "," + str(location.longitude)
    result = maps.places_nearby(location = lat_long, rank_by = 'distance', open_now = False, type = "restaurant")

    for place in result['results']:
            # spaghetti declarations to create usable dictionary  
            my_fields = ['formatted_phone_number', 'formatted_address']
            my_place_id = place['place_id']
            place_details = maps.place(place_id = my_place_id, fields = my_fields)
            details = place_details['result']
            
            
                
                
            try:
                pl = str((place['price_level']))
            except:
                pl = None
                    
            try: 
                fa = str(details['formatted_phone_number'])
            except:
                fa = None
                
            try:
                ra = str((place['rating']))
            except:
                ra = None
        
        
            
            place_dict = {
                    "name": str((place['name'])),
                    "price_rating": pl,
                    "rating": ra,
                    "address": str(details['formatted_address']),
                    "phone": fa     
            }
            
            place_data.append(place_dict)
   
    return place_data
    

      

        #     my_fields = ['name', 'formatted_phone_number', 'type']
        #     place_details = maps.place(place_id = my_place_id, fields = my_fields)
        #     print(place_details)