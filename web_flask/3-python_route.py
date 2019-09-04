#!/usr/bin/python3
''' Script starts a Flask web application '''

from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def home():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
def python_is(text='is cool'):
    return 'Python {}'.format(escape(text.replace('_', ' ')))

if __name__ == '__main__':
    app.debug = True
    # Don't run on localhost
    app.run(host='0.0.0.0', port=5000)
