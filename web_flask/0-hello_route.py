#!/user/bin/python3
"""
Initiates a Flask-based web application.
"""

from flask import Flask


app = Flask(__name__)
''' The instance of the Flask application. '''


@app.route('/', strict_slashes=False)
def index():
    '''The main page.'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
