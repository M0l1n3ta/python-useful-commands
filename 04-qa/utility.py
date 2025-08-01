import requests

def make_request( query_parameters):
    base_url = "https://api.nasa.gov/neo/rest/v1/feed"
    api_key = "sEIdCnfQnbOxATp8IEQFjG6WJDWtzqhHRU9NVg3I"
    p = {"api_key": api_key }
    p.update(query_parameters)
    response = requests.get(base_url, params=p)
    return response
