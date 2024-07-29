#!/usr/bin/python3

"""Start a Flask application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Flask app route
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Return HBNB
    """
    return "HBNH"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
