import pytest
import requests
from flask_testing import LiveServerTestCase
from selenium import webdriver

from .. import app
from .. import views
from ..helpers import gdpy_sentences

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

    def test_result_runs(self):
        payload = {'request': 'musée du louvre'}
        res = requests.post(self.get_server_url() + "/results/", data=payload)
        assert res.status_code == 200

    def test_results_return_text(self):
        payload = {'request': 'musée du louvre'}
        res = requests.post(self.get_server_url() + "/results/", data=payload)
        res = res.json()
        assert "Le musée du Louvre, inauguré en 1793 sous l'appellation Muséum central des arts de la République dans le palais du Louvre, ancienne résidence royale située au centre de Paris, est aujourd'hui le plus grand musée d'art et d'antiquités au monde." in res["wikipedia"]

    def test_results_return_place_id(self):
        payload = {'request': 'musée du louvre'}
        res = requests.post(self.get_server_url() + "/results/", data=payload)
        res = res.json()
        assert "ChIJD3uTd9hx5kcR1IQvGfr8dbk" in res["place_id"]

    def test_results_return_error_message_when_form_is_void(self):
        payload = {'request': ''}
        res = requests.post(self.get_server_url() + "/results/", data=payload)
        res = res.json()
        assert gdpy_sentences.gdpy_need_informations in res["wikipedia"]

    def test_results_return_place_id_null_when_form_is_void(self):
        payload = {'request': ''}
        res = requests.post(self.get_server_url() + "/results/", data=payload)
        res = res.json()
        assert "null" in res["place_id"]

    def test_results_return_error_message_when_form_is_random_letters(self):
        payload = {'request': 'frsdlkvz'}
        res = requests.post(self.get_server_url() + "/results/", data=payload)
        res = res.json()
        assert gdpy_sentences.gdpy_dont_understand in res["wikipedia"]

    def test_results_return_place_id_null_when_form_is_random_letters(self):
        payload = {'request': 'frsdlkvz'}
        res = requests.post(self.get_server_url() + "/results/", data=payload)
        res = res.json()
        assert "null" in res["place_id"]

    # def test_home_display(self):
    #     # Le navigateur est Firefox
    #     self.driver = webdriver.Firefox()
    #     self.driver.get(self.get_server_url())
    #     assert self.driver.current_url == 'http://localhost:8943/'
    #     self.driver.quit()
