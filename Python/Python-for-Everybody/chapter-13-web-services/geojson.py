import urllib.request, urllib.parse, urllib.error
import json

# Google Maps API requires key to get data, 
# so we use the JSON data directly
googleAddressJson = '''
{
    "results": [
        {
            "address_components": [
                {
                    "long_name": "Ann Arbor",
                    "short_name": "Ann Arbor",
                    "types": [ "locality", "political"]
                },
                {
                    "long_name": "Washtenaw County",
                    "short_name": "Washtenaw County",
                    "types": [ "administrative_area_level_2", "political" ]
                },
                {
                    "long_name": "Michigan",
                    "short_name": "MI",
                    "types": [ "administrative_area_level_1", "political" ]
                },
                {
                    "long_name": "United States",
                    "short_name": "US",
                    "types": [ "country", "political" ]
                }
            ],
            "formatted_address": "Ann Arbor, MI, USA",
            "geometry": {
                "bounds": {
                    "southeast": {
                        "lat": 42.3239728,
                        "lng": -83.6785069
                    },
                    "southwest": {
                        "lat": 42.222668,
                        "lng": -83.7999572
                    }
                },
                "location": {
                    "lat": 42.2808256,
                    "lng": -83.7430378
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 42.3239728,
                        "lng": -83.6758069
                    },
                    "southwest": {
                        "lat": 42.222668,
                        "lng": -83.799572
                    }
                }
            },
            "place_id": "ChIJMx9D1....",
            "types": [ "locality", "political" ]
        }
    ],
    "status": "OK"
}
'''

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = input('Enter location: ')
if len(address) < 1: exit()

url = serviceurl + urllib.parse.urlencode(
    {'address': address})

print('Retrieving', url)

# do not request Google Maps API, use JSON data instead
# uh = urllib.request.urlopen(url)
# data = uh.read().decode()
data = googleAddressJson

print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    exit()

print(json.dumps(js, indent=4))

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)


# Code: http://www.py4e.com/code3/geojson.py

# Output:
# $ python geojson.py
# Enter location: Ann Arbor, MI
# Retrieving http://maps.googleapis.com/maps/api/
#   geocode/json?sensor=false&address=Ann+Arbor%2C+MI
# Retrieved 1669 characters