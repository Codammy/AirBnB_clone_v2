#!/usr/bin/python3
"""
starts a web Flask application.
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def say_hello():
    """says hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def say_hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_what(text):
    """C is fun!"""
    return f"C {text}".replace("_", " ")


@app.route("/python/", defaults={"text": "is cool"},
           strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is(text):
    """Python is cool"""
    return f"Python {text}".replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def n_type(n):
    """n should be a number"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_type_template(n):
    """n should be a number"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(debug=True)
