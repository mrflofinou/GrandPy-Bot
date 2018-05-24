import requests


def maps(query):
    google_key = "AIzaSyAOcEnqP9jbC1eApGVZ6iYHtD4jNdXrFco"
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    search_params = {"query":' '.join(query), "key":google_key}
    # I make a request at google maps API to search a location
    search_request = requests.get(search_url, params=search_params)
    search_json = search_request.json()
    # I get the id of the first place of the list of the search results
    place_id = search_json["results"][0]["place_id"]
    # The place_id will use in the iframe of google maps to display the location
    return place_id
