"""MUSA 509 demo app"""
from flask import Flask, request
import json
from datetime import datetime


app = Flask(__name__, template_folder="templates")

with open("mapbox_token.json") as tokenf:
    MAPBOX_TOKEN = json.load(tokenf)["token"]

# index page
@app.route("/")
def index():
    return f"Hello, Welcome to Week 9 Lab in MUSA 509!"

# Example
# variable rules
@app.route("/hello/<string:name>/")
def hello_name(name):
    return f"Hello, {name}!"

## 1. Welcome someone and tell them the time
@app.route("/hello_time/<string:name>/")
def hello_time(name):
    curr_time = datetime.now().strftime("%B %d, %Y %I:%M %p")

    return f"""
      <h1 style="background-color:powderblue;">Welcome</h1>
      <p>
        Hello, <b>{name_long}</b><br />
        The time is <span style='color: #990000;'>{curr_time}</span>!
      </p>
     """


## 2. Let's add some HTML bling to the response

## 3. Static Map Generation
def get_static_map_url(lng, lat, zoom=10):
    url = f"https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/{lng},{lat},{zoom},0/800x800?access_token={MAPBOX_TOKEN}"
    return url

@app.route("/map/")
def static_map():
    lng = request.args.get("lng")
    lat = request.args.get("lat")
    zoom = request.args.get("zoom")
    map_url = get_static_map_url(lng, lat, zoom)
    return f"""
    <p>Map for ({lng}, {lat})</p>
    <img src='{map_url}' />
    """

## 4. Turn an address into a static map


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)
