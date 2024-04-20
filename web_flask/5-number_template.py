#!/usr/bin/python3
"""
Initiates a Flask-based web application.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Shows 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'Hello HBNB!'"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Show "C" along with the value stored in the text variable"""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Show "python" and then the value stored in the text variable"""
    return 'python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Show "n is a number" only if n is an integer"""
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_templates(n):
    """Show an HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
