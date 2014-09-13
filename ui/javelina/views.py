'''
views.py
========

javelina views

:copyright: (c) 2014 by Jeff Perry
'''

from javelina import app

from flask import (
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
    jsonify,
    )
import requests

@app.route('/')
def home():
    return render_template('home.html')

# see https://pythonhosted.org/Flask-Uploads/
