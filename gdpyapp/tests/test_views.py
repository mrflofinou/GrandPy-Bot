import pytest
import requests
from flask_testing import LiveServerTestCase
from selenium import webdriver

from .. import app
from .. import views

# Creation of client for the test
# This client will be use in several tests
# @pytest.fixture
# def client():
#     app.config.from_object("gdpyapp.tests.config")
#     client = app.test_client()
#     return client
#
# @pytest.fixture
# def selenium():
#     driver = webdriver.Firefox()
#     yield driver
#     driver.quit()
#
# def test_app_runs(client):
#     res = client.get('/')
#     assert res.status_code == 200
#
# def test_index_print_hello_world(client):
#     res = client.get('/')
#     assert b"Hello world !" in res.data # 'b' transorm 'str' in 'bytes' type
#
# def test_connexion_mediawiki_API():
#     assert client.get('/results/) == 200

# def test_results_return_text(client):
#     res = client.get('/results/?text=le-louvre-paris')
#     assert "le-louvre-paris" in str(res.data)



class gdpyapp_test(LiveServerTestCase):
    def create_app(self):
        app.config.from_object('gdpyapp.tests.config')
        return app

    # def setUp(self):
    #     """Setup the test driver and create test users"""
    #     # Le navigateur est Firefox
    #     self.driver = webdriver.Firefox()
    #
    # def tearDown(self):
    #     self.driver.quit()

    def test_app_runs(self):
        res = requests.get(self.get_server_url())
        assert res.status_code == 200

    def test_index_print_hello_world(self):
        res = requests.get(self.get_server_url())
        assert "Hello world !" in res.text

    def test_connexion_mediawiki_API(self):
        res = requests.get(self.get_server_url() + '/results/')
        assert res.status_code == 200

    def test_results_return_text(self):
        res = requests.get(self.get_server_url() + '/results/')
        assert "Le musée du Louvre, inauguré en 1793 sous l'appellation Muséum central des arts de la République dans le palais du Louvre, ancienne résidence royale située au centre de Paris, est aujourd'hui le plus grand musée d'art et d'antiquités au monde" in res.text
