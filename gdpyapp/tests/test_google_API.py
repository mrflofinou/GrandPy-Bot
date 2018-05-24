import pytest
import requests


def test_google_maps_url_runs():
    req = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json")
    assert req.status_code == 200

def test_google_maps_search_runs():
    params = {"query":"Paris", "key":"AIzaSyAOcEnqP9jbC1eApGVZ6iYHtD4jNdXrFco"}
    req = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json", params=params)
    assert req.status_code == 200

def test_google_maps_results():
    params = {"query":"Paris", "key":"AIzaSyAOcEnqP9jbC1eApGVZ6iYHtD4jNdXrFco"}
    req = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json", params=params)
    req = req.json()
    assert req["results"][0]["place_id"] == "ChIJD7fiBh9u5kcRYJSMaMOCCwQ"
