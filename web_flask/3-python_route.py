#!/usr/bin/python3

""" Write a script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
Route: /: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route('/',  strict_slashes=False)
def hello():
    """Displays Hello Flask!"""
    return "Hello HBNB!"


@app.route('/hbnb',  strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<text>',  strict_slashes=False)
def c_text(text):
    """Displays C followed by the text variable
    (replace underscore symbol _ with a space
    """

    txt = text.replace('_', ' ')
    return f"C {txt}"


@app.route('/python/<text>',  strict_slashes=False)
def python_text(text):
    """Displays Python followed by the text variable
    (replace underscore symbol _ with a space
    """

    txt = text.replace('_', ' ')
    return f"Python {txt}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
