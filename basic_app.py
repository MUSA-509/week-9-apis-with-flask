"""basic_app.py"""
from flask import Flask

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return "Hi MUSA 509, this is the Flask index."

if __name__ == "__main__":
    app.run(debug=True)
