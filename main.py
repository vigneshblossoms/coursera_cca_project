from flask import Flask
from flask import jsonify
import flask
import requests
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

@app.route("/echo/<index>")
def echo(index):
    response = "Hello" + index
    return response

# Extra web route to multiply the change by 100
@app.route('/forecasts/', methods=["POST"])
def extrawebroute():
    json_data = flask.request.json
    lat = json_data["lat"] # "48.208176"
    lon = json_data["lon"] # "16.373819"
    api_key = "5655eaaef545990b2199a39a4f331343"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)