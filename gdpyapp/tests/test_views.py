import pytest

from .. import app
from .. import views
from .. import stopwords


# Creation of client for the test
# This client will be use in several tests
@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    return client

def test_app_runs(client):
    res = client.get('/')
    assert res.status_code == 200

def test_index_print_Hello_World(client):
    res = client.get('/')
    assert b"Hello world !" in res.data # 'b' transorm 'str' in 'bytes' type

def test_parser():
    assert views.parserkiller("") == ""
