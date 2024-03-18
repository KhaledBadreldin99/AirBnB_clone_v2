#!/usr/bin/python3
"""
Initiates the Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb: HBNB main page.
"""

from flask import render_template
from flask import Flask
from models import storage

app = Flask(__name__)

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Shows the main HBNB filters HTML page."""
    states = storage.all("state")
    amenities = storage.all("Amenity")
    places = storage.all("place")
    return render_template("100-hbnb.html",
                            states=states, amenities=amenities,
places=places)

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLALCHEMY session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
