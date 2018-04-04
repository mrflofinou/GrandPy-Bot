import pytest

from .. import app
from .. import views

# Creation of client for the test
# This client will be use in several tests
@pytest.fixture
def client():
    app.config.from_object("gdpyapp.tests.config")
    client = app.test_client()
    return client

def test_app_runs(client):
    res = client.get('/')
    assert res.status_code == 200

def test_index_print_hello_world(client):
    res = client.get('/')
    assert b"Hello world !" in res.data # 'b' transorm 'str' in 'bytes' type

def test_connexion_mediawiki_API():
    assert views.get_from_mediawiki_API("https://en.wikipedia.org/w/api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json&formatversion=2").status_code == 200

def test_results_return_text(client):
    res = client.get('/results/?text=le-louvre-paris')
    assert "Le musée du Louvre, inauguré en 1793 sous l'appellation Muséum central des arts de la République dans le palais du Louvre, ancienne résidence royale située au centre de Paris, est aujourd'hui le plus grand musée d'art et d'antiquités au monde" in str(res.data)
