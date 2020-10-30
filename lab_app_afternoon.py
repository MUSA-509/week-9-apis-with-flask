"""MUSA 509 demo app"""
from flask import Flask, request
import json

app = Flask(__name__, template_folder="templates")

with open("mapbox_token.json") as tokenf:
    MAPBOX_TOKEN = json.load(tokenf)['token']

# index page
@app.route("/")
def index():
    return f"Hello, Welcome to Week 9 Lab in MUSA 509! :)"

# Example
# variable rules
@app.route("/hello/<string:name>/")
def hello_name(name):
    return f"<marquee>Hello {name}!</marquee>"

## 1. Welcome someone and tell them the time

# > "Hello, Andy it's October 29, 2020 at 5pm :D"

## 2. Let's add some HTML bling to the response

## 3. Static Map Generation

def get_static_map_url(lng, lat, zoom):
    url = f"https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/{lng},{lat},{zoom},0/800x800?access_token={MAPBOX_TOKEN}"
    return url


 # `/map?lat=10`

@app.route('/map')
def map_of_area():
    lng = request.args.get("lng", 0)
    lat = request.args.get("lat", 0)
    zoom = request.args.get("zoom", 12)
    if not isinstance(zoom, int):
        zoom = 12
    url = get_static_map_url(lng, lat, zoom)
    return f"""
      <h1>Here is your map of your location ({lng}, {lat}, {zoom})</h1>

      <img src='{url}' />
     """


def helper_function(a, b):

    return a + b

## 4. Turn an address into a static map


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)
