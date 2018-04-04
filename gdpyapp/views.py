import requests
from flask import Flask, request


app = Flask(__name__)

def get_from_mediawiki_API(url):
    """ Connexion to the wikipedia mediawiki API """
    return requests.get(url)

@app.route('/')
def index():
    return "Hello world !"

# /results?text=livre-truc-a
@app.route('/results/')
def form_result():
    return request.args.get("text")

# https://en.wikipedia.org/w/api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json&formatversion=2
