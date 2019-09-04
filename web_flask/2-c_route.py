#!/usr/bin/python3
''' Script starts a Flask web application '''

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c_is(text):
    return 'C {}'.format(text.replace('_', ' '), strict_slashes=False)


if __name__ == '__main__':
    app.debug = True
    # Don't run on localhost
    app.run(host='0.0.0.0', port=5000)
