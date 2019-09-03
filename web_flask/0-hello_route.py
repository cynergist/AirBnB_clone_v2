#!/usr/bin/python3
''' Script starts a Flask web application '''

from flask import Flask
app = Flask(__name__)
# Use the decorator @app.route'/'
@app.route('/', strict_slashes=False)

def hello():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.debug = True
    # Don't run on localhost
    app.run(host='0.0.0.0', port=5000)
