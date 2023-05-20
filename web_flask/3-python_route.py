#!/usr/bin/python3
"""
This module defines a Flask web application.
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function defines the route '/' of the Flask web application.
    It returns the string 'Hello HBNB!'.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function defines the route '/hbnb' of the Flask web application.
    It returns the string 'HBNB'.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    This function defines the route '/c/<text>' of the Flask web application.
    It returns the string 'C ' followed by the value of the text variable
    (replace underscore _ symbols with a space).
    """
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    This function defines the route '/python/<text>' of the Flask web application.
    If no text is provided, it uses the default value 'is cool'.
    It returns the string 'Python ' followed by the value of the text variable
    (replace underscore _ symbols with a space).
    """
    return 'Python {}'.format(escape(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
