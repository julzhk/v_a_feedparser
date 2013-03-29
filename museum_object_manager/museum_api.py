import requests
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.conf import settings
import json

def museum_query(rest_qry):
    '''
    Abstract base function: pass in the specific 'rest query' to make queries.
    API returns json, converted to a python dict
    '''
    response = requests.get(
        settings.MUSEUM_API_URL,
        params = rest_qry,
        headers = {
            'Accept':'application/json'
        })
    assert response.status_code == 200
    response_dict =response.json()
    return response_dict

def keywordsearch(term =''):
    '''
    eg :
    Everything the API knows about is searchable by keyword.
    Simply pass your query string to the search interface in the q GET parameter
    http://www.vam.ac.uk/api/json/museumobject/search?q=wooden+door
    '''
    data = museum_query(rest_qry = {'q':term})
    meta = data['meta']
    records = data['records']
    return records