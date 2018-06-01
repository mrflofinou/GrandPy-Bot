import pytest
import requests
import requests_mock

from .. import app
from ..helpers import API_helper


app.config.from_object('gdpyapp.tests.config')

def test_google_maps_search_runs():
    params = {"query":"Paris", "key": app.config["GOOGLE_KEY"]}
    req = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json", params=params)
    assert req.status_code == 200

def test_google_maps_return_place_id(monkeypatch):
    results = {
        "results": [
            {
                "place_id": "ChIJD7fiBh9u5kcRYJSMaMOCCwQ"
            }
        ],
        "status": "OK"
    }

    def mockreturn(request, params):
        # I use the library 'requests-mock' to mock a Requests' response.
        session = requests.Session()
        adapter = requests_mock.Adapter()
        session.mount('mock', adapter)
        adapter.register_uri('GET', 'mock://test.com', json=results, status_code=200)
        resp = session.get('mock://test.com')
        return resp

    monkeypatch.setattr(requests, 'get', mockreturn)

    assert API_helper.ApiHelper.get_google_map("Paris", app.config["GOOGLE_KEY"]) == "ChIJD7fiBh9u5kcRYJSMaMOCCwQ"
