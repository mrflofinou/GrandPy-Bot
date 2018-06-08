import pytest
import requests

from .. import app
from ..helpers import api_helper, mock


app.config.from_object('gdpyapp.tests.config')

def test_google_maps_search_runs():
    params = {"query":"Paris", "key": app.config["GOOGLE_KEY_TEST"]}
    req = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json", params=params)
    req = req.json()
    assert req["status"] == "OK"


def test_get_google_maps_return_place_id(monkeypatch):
    results = {
        "results": [
            {
                "place_id": "AbCdEf"
            }
        ],
        "status": "OK"
    }

    def mockreturn(request, params):
        # I use the library 'requests-mock' to mock a Requests' response.
        return mock.mock_requests(results)

    monkeypatch.setattr(requests, 'get', mockreturn)

    assert api_helper.ApiHelper.get_google_map_place_id("Paris", app.config["GOOGLE_KEY_TEST"]) == "AbCdEf"


def test_get_google_maps_return_adress(monkeypatch):
    results = {
        "result": {
            "formatted_address": "3 rue des oubliettes, Perpette les oies"
        },
        "status": "OK"
    }

    def mockreturn(request, params):
        # I use the library 'requests-mock' to mock a Requests' response.
        return mock.mock_requests(results)

    monkeypatch.setattr(requests, 'get', mockreturn)

    assert api_helper.ApiHelper.get_google_map_adress("Paris", app.config["GOOGLE_KEY_TEST"]) == "3 rue des oubliettes, Perpette les oies"
