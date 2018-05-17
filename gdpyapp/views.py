import requests
from flask import Flask, request, render_template, Markup
from bs4 import BeautifulSoup

from .helpers import parser


app = Flask(__name__)

# @app.route('/')
# @app.route('/index/')
# def index():
#     return render_template('index.html')

@app.route('/',  methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        if len(request.form['request']) == 0:
            response = "Me demander quelque chose tu dois"
        else:
            # To handle the request from the form
            form_result = request.form['request']
            # To use a parser with user request from the form
            form_parsing = parser.parserkiller("{}".format(form_result))
            # Make a search from the parser's words with mediawiki API
            search = requests.get("https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&prop=revisions&rvprop=content&format=json&formatversion=2".format('%20'.join(form_parsing)))
            search_data = search.json()
            search_results = search_data["query"]["search"]
            # With this previous research we have several results
            # We consider the first result of the research is the most relevant
            pageid = search_results[0]["pageid"]
            # Make a request to obtain the page of the previous first result with its page id
            page_request = requests.get("https://fr.wikipedia.org/w/api.php?action=query&pageids={}&prop=extracts&rvprop=content&format=json&formatversion=2".format(pageid))
            page_data = page_request.json()
            # To scrape the result
            html_doc = page_data["query"]["pages"][0]["extract"]
            # BeautifulSoup is a HTML scraper
            soup = BeautifulSoup(html_doc)
            # return the first paragraph of the page
            response = soup.find('p').text
        return response
        # return render_template('results.html', description=description)
    else:
        return render_template('index.html')
