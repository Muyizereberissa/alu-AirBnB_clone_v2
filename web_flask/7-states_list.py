#!/usr/bin/python3

"""Starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """Comment"""
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)

