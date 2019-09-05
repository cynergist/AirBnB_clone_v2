#!/usr/bin/python3
''' Script starts a Flask web application '''
from models import storage
from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' renders template for jinja states list '''
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session(self):
    ''' app.teardown tells the host computer to close the session '''
    storage.close()


if __name__ == '__main__':
    app.debug = True
    # Don't run on localhost
    app.run(host='0.0.0.0', port=5000)
