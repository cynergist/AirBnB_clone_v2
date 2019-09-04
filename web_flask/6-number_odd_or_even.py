#!/usr/bin/python3
''' Script starts a Flask web application '''

from flask import Flask, escape, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text='is cool'):
    return 'Python {}'.format(escape(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template', strict_slashes=False)
@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n=None):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even', strict_slashes=False)
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n=None):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.debug = True
    # Don't run on localhost
    app.run(host='0.0.0.0', port=5000)
