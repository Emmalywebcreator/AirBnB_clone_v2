#!/usr/bin/python3

"""Start a Flask application
"""

from flask import Flask

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
