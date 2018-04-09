import requests
from flask import Flask, request

from .helpers import parser


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

# /results?text=livre-truc-a
@app.route('/results/')
def form_result():
    # I use my parser
    client_request = parser.parserkiller("Le musée du louvre de Paris")
    # Make a search from the parser's words with mediawiki API
    primary_search = requests.get("https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&prop=revisions&rvprop=content&format=json&formatversion=2".format('%20'.join(client_request)))
    primary_data = primary_search.json()
    primary_serach_results = primary_data["query"]["search"]
    # We consider the first result of the research is the most relevant
    pageid = primary_serach_results[0]["pageid"]
    # Make a search from the previous first result with its page id
    final_search = requests.get("https://fr.wikipedia.org/w/api.php?action=query&pageids={}&prop=revisions&rvprop=content&format=json&formatversion=2".format(pageid))
    final_data = final_search.json()
    return str(final_data)# ["query"]["pages"][0]["revisions"][0]["content"])

    # return request.args.get("text")
