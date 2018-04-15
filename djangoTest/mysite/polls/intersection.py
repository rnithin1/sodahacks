import requests
import logging
import time
import googlemaps
import json, urllib
from urllib.parse import urlencode
import urllib.request

API_KEY='AIzaSyC3TNP_puUzeF_VVYjbSuR_4tOo-Ad4Urc'
RETURN_FULL_RESULTS = False

def fixedcentroids(address, api_key=API_KEY, return_full_response=False):
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={}".format(address)
    if api_key is not None:
       geocode_url = geocode_url + "&key={}".format(api_key)

    results = requests.get(geocode_url)
    results = results.json()
    if len(results['results']) == 0:
        output = {
            "formatted_address" : None,
            "neighborhood" : None,
            "latitude": None,
            "longitude": None,
            "accuracy": None,
            "google_place_id": None,
            "type": None,
            "postcode": None
        }
    else:
        answer = results['results'][0]
        output = {
            "formatted_address" : answer.get('formatted_address'),
            "neighborhood" : ",".join([x['long_name'] for x in answer.get('address_components')
                                  if 'neighborhood' in x.get('types')]),
            "latitude": answer.get('geometry').get('location').get('lat'),
            "longitude": answer.get('geometry').get('location').get('lng'),
            "accuracy": answer.get('geometry').get('location_type'),
            "google_place_id": answer.get("place_id"),
            "type": ",".join(answer.get('types')),
            "postcode": ",".join([x['long_name'] for x in answer.get('address_components')
                                  if 'postal_code' in x.get('types')])
        }
    output['input_string'] = address
    output['number_of_results'] = len(results['results'])
    output['status'] = results.get('status')
    if return_full_response is True:
        output['response'] = results
    print(geocode_url)
    return str(output["latitude"])+","+str(output["longitude"])

test_result = fixedcentroids("40.752726,-73.977229", API_KEY, RETURN_FULL_RESULTS)
print(test_result)

def get_route(curr, dest):
    url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((('origin', fixedcentroids(curr, API_KEY, RETURN_FULL_RESULTS)),('destination', dest)))
    ur = urllib.request.urlopen(url)
    result = json.load(ur)

    for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
        j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
        print(j)


get_route("40.752726,-73.977229","40.753624,-73.981231")
