#!/usr/bin/python3
"""
script that starts a Flask web application:
    web application would be listening on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greet():
    """returns hello"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def greet_hbnb():
    """returns hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """describes c language"""
    return f"C {text}".replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
