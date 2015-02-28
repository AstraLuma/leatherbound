"""
Primary entry point for leatherbound.

Sets up the Flask app.
"""
from __future__ import absolute_import, division
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/new')
def addentry():
    """Display the new entry page to a user"""
    return 'FIXME: New entry form goes here'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
