import requests
import requests_mock

"""
this function help to mock a Requests' response for unit tests
"""

def mock_requests(results):
    session = requests.Session()
    adapter = requests_mock.Adapter()
    session.mount('mock', adapter)
    adapter.register_uri('GET', 'mock://test.com', json=results, status_code=200)
    resp = session.get('mock://test.com')
    return resp
