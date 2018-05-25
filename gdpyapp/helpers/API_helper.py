import requests
from bs4 import BeautifulSoup

class ApiHelper:
    """
    This class group methods to connect to the APIs:
        - Google Mpas to get informations for a location
        - Wikimedia to get informations from wikipedia
    """

    @classmethod
    def get_google_map(self, query):
        """
        This method allow to communicate with google maps API
        The goal of this method is to get the id of a place (place_id)
        to display it on a map
        """
        google_key = "AIzaSyAOcEnqP9jbC1eApGVZ6iYHtD4jNdXrFco"
        search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        search_params = {"query":' '.join(query), "key":google_key}
        # I make a request at google maps API to search a location
        search_request = requests.get(search_url, params=search_params)
        search_json = search_request.json()
        # I get the id of the first place of the list of the search results
        if len(search_json["results"]) == 0:
            place_id = "null"
        else:
            place_id = search_json["results"][0]["place_id"]
        # The place_id will use in the iframe of google maps to display the location
        return place_id

    @classmethod
    def get_wikipedia_result(self, query):
        """
        This method allow to communicate with wikimedia API
        The goal of this methos is to get the first lines of the dercription
        of a place.
        So, I search a place from the user query
        I use the first result to find the id of its page
        In this page I get the first paragraph
        """
        if len(query) == 0:
            response = "Me demander quelque chose tu dois, jeune padawan"
        else:
            wikipedia_api_url = "https://fr.wikipedia.org/w/api.php"
            search = requests.get(wikipedia_api_url + "?action=query&list=search&srsearch={}&prop=revisions&rvprop=content&format=json&formatversion=2".format('%20'.join(query)))
            search_data = search.json()
            search_results = search_data["query"]["search"]
            # With this previous research we have several results
            # We consider the first result of the research is the most relevant
            pageid = search_results[0]["pageid"]
            # Make a request to obtain the page of the previous first result with its page id
            page_request = requests.get(wikipedia_api_url + "?action=query&pageids={}&prop=extracts&rvprop=content&format=json&formatversion=2".format(pageid))
            page_data = page_request.json()
            # To scrape the result
            html_doc = page_data["query"]["pages"][0]["extract"]
            # BeautifulSoup is a HTML scraper
            soup = BeautifulSoup(html_doc)
            # return the first paragraph of the page
            response = soup.find('p').text

        return response
