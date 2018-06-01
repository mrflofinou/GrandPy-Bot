import requests
from bs4 import BeautifulSoup

from .gdpy_sentences import gdpy_need_informations, gdpy_dont_understand


class ApiHelper:
    """
    This class group methods to connect to the APIs:
        - Google Mpas to get informations for a location
        - Wikimedia to get informations from wikipedia
    """

    WIKIMEDIA_API_URL = "https://fr.wikipedia.org/w/api.php?action=query&rvprop=content&format=json&formatversion=2"

    @classmethod
    def get_google_map(cls, query, google_key):
        """
        This method allow to communicate with google maps API
        The goal of this method is to get the id of a place (place_id)
        to display it on a map
        """
        search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        search_params = {"query":query, "key":google_key}
        # I make a request at google maps API to search a location
        search_request = requests.get(search_url, params=search_params)
        search_json = search_request.json()
        # If Google Maps don't find results
        if search_json["status"] != "OK":
            place_id = "null"
        else:
            # I get the id of the first place of the list of the search results
            place_id = search_json["results"][0]["place_id"]
        # The place_id will use in the iframe of google maps to display the location
        return place_id


    @classmethod
    def _get_wikipedia_page_id(cls, query):
        """
        This method communicate with the wikimedia API to get the wikipedia page id of the query.
        This id will be use to find the page for the query.
        """
        search_params = {"list": "search", "prop": "revisions","srsearch":query}
        search = requests.get(cls.WIKIMEDIA_API_URL, params=search_params)
        search_data = search.json()
        search_results = search_data["query"]["search"]
        if len(search_results) == 0:
            page_id = ""
        else:
            # We consider the first result of the search is the most relevant
            page_id = search_results[0]["pageid"]

        return page_id

    @classmethod
    def get_wikipedia_result(cls, query):
        """
        This method allow to communicate with wikimedia API
        The goal of this methos is to get the first lines of the dercription
        of a place.
        We use the id of a page to find it and get the first paragraph
        """
        if len(query) == 0:
            response = gdpy_need_informations
        else:
            page_id = cls._get_wikipedia_page_id(query)
            # If wikipedia don't find results
            if page_id == "":
                response = gdpy_dont_understand
            else:
                search_params = {"prop": "extracts" , "pageids": page_id}
                # Make a request to obtain the page of the previous first result with its page id
                page_request = requests.get(cls.WIKIMEDIA_API_URL, params=search_params)
                page_data = page_request.json()
                # To scrap the result
                wikipedia_html_doc = page_data["query"]["pages"][0]["extract"]
                # BeautifulSoup is a HTML scraper
                soup = BeautifulSoup(wikipedia_html_doc, "html.parser")
                # return the first paragraph of the page
                response = soup.find('p').text

        return response
