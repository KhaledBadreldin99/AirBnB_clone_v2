#!/usr/bin/python3
"""
Initiates a Flask-based web application.
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """The main page"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """page of HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Show "C" along with the value stored in the text variable"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python' , strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """Show "python" and then the value stored in the text variable"""
    return 'python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """Show "n is a number" only if n is an integer"""
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>' strict_slashes=False)
def numbersandtemplates(n):
    """Show an HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port'5000')
