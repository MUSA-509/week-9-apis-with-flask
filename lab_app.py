"""MUSA 509 demo app"""
from flask import Flask, request
import json

app = Flask(__name__, template_folder="templates")

with open("mapbox_token.json") as tokenf:
    MAPBOX_TOKEN = json.load(tokenf)

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

## 2. Let's add some HTML bling to the response

## 3. Static Map Generation
def get_static_map_url(lng, lat):
    url = f"https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/{lng},{lat},10,0/800x800?access_token={MAPBOX_TOKEN}",
    return url

## 4. Turn an address into a static map


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)
