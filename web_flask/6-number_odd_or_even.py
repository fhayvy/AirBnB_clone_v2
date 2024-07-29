#!/usr/bin/python3

""" Write a script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
Route: /: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask
from flask import render_template

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
    (replace underscore symbol _ with a space)
    """

    txt = text.replace('_', ' ')
    return f"C {txt}"


@app.route('/python',  strict_slashes=False)
@app.route('/python/<text>',  strict_slashes=False)
def python_text(text='is cool'):
    """Displays Python followed by the text variable
    (replace underscore symbol _ with a space
    """

    txt = text.replace('_', ' ')
    return f"Python {txt}"


@app.route('/number/<int:n>',  strict_slashes=False)
def number(n):
    """Displays n is a number only if n is an integer
    """

    if isinstance(n, int):
        return f"{n} is a number"


@app.route('/number_template/<int:n>',  strict_slashes=False)
def number_template(n):
    """Displays a HTML page only if n is an integer
    H1 tag: “Number: n” inside the tag BODY
    """

    if isinstance(n, int):
        return render_template("5-number.html", num=n)


@app.route('/number_odd_or_even/<int:n>',  strict_slashes=False)
def number_odd_or_even(n):
    """Displays a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """

    if isinstance(n, int):
        return render_template("6-number_odd_or_even.html", num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
