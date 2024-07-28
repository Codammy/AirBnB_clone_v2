#!/usr/bin/python3
"""
starts a web Flask application.
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def say_hello():
    """says hello"""
    return "Hello HBNB!"


@app.route("hbnb", strict_slashes=False)
def say_hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run()
