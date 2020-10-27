"""Geocoder script. Geocodes an address/place name/etc. provided by the user
NOTE: this is a docstring. It describes what's in this file.
"""
import json
import sys
import pprint
import requests

# NOTE: Standard practice says that global variables should be capitalized
with open("mapbox_token.json") as token_json:
    MAPBOX_TOKEN = json.load(token_json)["token"]

def geocode_place(place_name):
    """Geocode by place name (address, POI, city name, etc.)
    using Mapbox Geocoding API

    Note: this is a docstring. It describes what this function does

    Args:
        place_name (str): A place name to geocode. Can be an address, name of a
          city, a point of interest, etc.

    Returns:
        dict: Response from API as a GeoJSON dictionary

    """
    geocoding_call = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json"
    resp = requests.get(
        geocoding_call,
        params={'access_token': MAPBOX_TOKEN}
    )
    return resp.json()

if __name__ == '__main__':
    response = geocode_place(sys.argv[1])
    pprint.pprint(response)
