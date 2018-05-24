import requests
from bs4 import BeautifulSoup

def wikipedia(query):
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
