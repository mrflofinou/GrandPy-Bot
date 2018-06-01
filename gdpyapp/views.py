from flask import Flask, request, render_template, jsonify

from .helpers import API_helper, parser


app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/results/', methods=['GET', 'POST'])
def results():
    # To handle the request from the form
    form_result = request.form['request']
    # To use a parser with user request from the form
    form_parsing = parser.parserkiller(str(form_result))
    # Make a search from the parser's words with mediawiki API
    response = API_helper.ApiHelper.get_wikipedia_result(form_parsing)
    # google maps search
    place_id = API_helper.ApiHelper.get_google_map(form_parsing, app.config["GOOGLE_KEY"])
    # I create a response in JSON. I will use it with the javascript file
    return jsonify({"wikipedia":response, "place_id":place_id, "google_key":app.config["GOOGLE_KEY"]})
