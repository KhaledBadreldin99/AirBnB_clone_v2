#!/usr/bin/python3
"""
Starts a Flask-based web application.
"""


from flask import Flask
from werkzeug.utils import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """

    Displays 'Hello HBNB!' when acessing root URL.
    """

    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Displays 'HBNB' when acessing /hbnb URL.
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    Displays 'C' followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return 'C{}'.format(escape(text.replace('_', ' ')))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """
    Displays 'python' followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    Default value of text is 'is cool'.
    """
    return 'python {}'.format(escape(text.replace('_', ' ')))



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
