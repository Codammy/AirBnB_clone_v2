#!/usr/bin/python3
"""
starts a Flask web application and handle some routes
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """APP root displays Hello HBNB!"""
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_string(text):
    """displays C followed by the value of text"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
def python_string2(text='is cool'):
    """displays Python followed by the value of text"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/python/<text>', strict_slashes=False)
def python_string(text='is cool'):
    """displays Python followed by the value of text"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """displays n if only n is a number"""
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
