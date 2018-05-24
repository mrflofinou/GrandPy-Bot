from flask import Flask, request, render_template, jsonify

from .helpers import parser, mediawiki, maps


app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

# @app.route('/',  methods=['GET', 'POST'])
@app.route('/results/', methods=['GET', 'POST'])
def results():
    # To handle the request from the form
    form_result = request.form['request']
    # To use a parser with user request from the form
    form_parsing = parser.parserkiller(str(form_result))
    # Make a search from the parser's words with mediawiki API
    response = mediawiki.wikipedia(form_parsing)
    # google maps search
    place_id = maps.maps(form_parsing)
    # I create a response in JSON. I will use it with the javascript file
    return jsonify({"wikipedia":response, "maps":place_id})
