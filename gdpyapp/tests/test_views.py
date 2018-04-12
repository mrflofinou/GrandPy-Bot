import pytest
import requests
from flask_testing import LiveServerTestCase
from selenium import webdriver

from .. import app
from .. import views

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
        assert "Grand Py Bot" in res.text

    def test_results_runs(self):
        payload = {'request': 'musée du louvre'}
        res = requests.post(self.get_server_url() + '/results/', data=payload)
        assert res.status_code == 200

    def test_results_return_text(self):
        payload = {'request': 'musée du louvre'}
        res = requests.post(self.get_server_url() + '/results/', data=payload)
        assert "Le <b>musée du Louvre</b>, inauguré en 1793 sous l'appellation <i>Muséum central des arts de la République</i> dans le palais du Louvre, ancienne résidence royale située au centre de Paris, est aujourd'hui le plus grand musée d'art et d'antiquités au monde." in res.text
