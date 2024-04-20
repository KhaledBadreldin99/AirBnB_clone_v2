#!/usr/bin/python3
"""
Initiates a Flask-based web application.
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Shows "Hello HBNB!" when acessing the main URL.'''

    return 'HelloHBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Displays 'HBNB' when acessing /hbnb URL."""

    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Show "C" along with the value stored in the text variable."""

    return 'C {}' .format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
