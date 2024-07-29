#!/usr/bin/python3

"""Start a Flask application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Flask app route for root URL
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Flask app route for /hbnb URL
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Flask app route for /c/<text> URL
    """
    text_c = text.replace("_", " ")
    return "C {}".format(text_c)


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """Flask app route for /python/<text> URL
    """
    text_python = text.replace("_", " ")
    return "Python {}".format(text_python)


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """Flask app route for /number/<n> URL
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Flask app route for /number_template/<n> URL
    """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
