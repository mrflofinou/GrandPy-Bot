import random

from flask import Flask, request, render_template, jsonify

from .helpers import api_helper, parser, gdpy_sentences
from .helpers.exceptions import GoogleError, QueryEmptyError, WikipediaResultError


app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/results/', methods=['GET', 'POST'])
def results():
    # I use try / except to handle exceptions raise
    try:
        gdpy_adress = random.choice(gdpy_sentences.gdpy_adress)
        gdpy_story = random.choice(gdpy_sentences.gdpy_story)
        # To handle the request from the form
        form_result = request.form['request']
        # To use a parser with user request from the form
        form_parsing = parser.parserkiller(str(form_result))
        # Make a search from the parser's words with mediawiki API
        response = api_helper.ApiHelper.get_wikipedia_result(form_parsing)
        # google maps search for place_id and adress of the place
        place_id = api_helper.ApiHelper.get_google_map_place_id(form_parsing, app.config["GOOGLE_KEY"])
        adress = api_helper.ApiHelper.get_google_map_adress(place_id, app.config["GOOGLE_KEY"])
    except QueryEmptyError:
        response = gdpy_sentences.gdpy_need_informations
        place_id = "null"
        adress = "null"
    except WikipediaResultError:
        response = gdpy_sentences.gdpy_dont_understand
        place_id = "null"
        adress = "null"
    except GoogleError:
        response = gdpy_sentences.gdpy_dont_find_adress
        place_id = "null"
        adress = "null"

    # I create a response in JSON. I will use it with the javascript file
    return jsonify({"gdpy_adress":gdpy_adress, "gdpy_story": gdpy_story, "gdpy_knowledge":response, "place_id":place_id, "adress":adress, "google_key":app.config["GOOGLE_KEY"]})
