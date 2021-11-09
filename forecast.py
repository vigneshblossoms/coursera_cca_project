import requests
import json

# https://knasmueller.net/using-the-open-weather-map-api-with-python
api_key = "5655eaaef545990b2199a39a4f331343"
lat = "48.208176"
lon = "16.373819"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
response = requests.get(url)
data = json.loads(response.text)
print(data)