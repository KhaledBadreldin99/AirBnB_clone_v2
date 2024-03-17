#!/usr/bin/python3
"""
Initiates a Flask-based web application.
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    '''The main page'''
    return 'HelloHBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Show "C" along with the value stored in the text variable."""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
