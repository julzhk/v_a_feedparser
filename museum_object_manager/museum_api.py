import requests
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.conf import settings
import json

def museum_query(rest_qry, extrapath='search'):
    '''
    Abstract base function: pass in the specific 'rest query' to make queries.
    API returns json, converted to a python dict
    '''
    url = '%s/%s' % (settings.MUSEUM_API_URL,extrapath)
    response = requests.get(
        url,
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

def full_record_details(id):
    '''
    Full record details
    append the object_number from the fields section
    eg:
    http://www.vam.ac.uk/api/json/museumobject/O12345
    Yes - that's an 'O' for Oscar.

    With a museum object, you'll see all the associated
    people, places, categories, styles and periods, materials and techniques.
    In short, everything we know about the object usefully split up into separate fields.
    '''

    data = museum_query(rest_qry = {'q':id})
    return [{'pk':17079}]

