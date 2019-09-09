#!/usr/bin/python3
''' Script starts a Flask web application '''
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def states_list(id=None):
    ''' Renders template for jinja states list '''
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    ''' Renders template for jinja cities_by_states list '''
    states = storage.all('State')
    cities = storage.all('City')
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    ''' Renders template for jinja states_id list '''
    states = storage.all('State')
    cities = storage.all('City')
    state_list = list()
    cities_list = list()
    for state in states.values():
        state_list.append(state)
    for city in cities.values():
        cities_list.append(city)

    state_id = "State.{}".format(id)
    if id is not None and state_id not in states:
        states = None
    return render_template('9-states.html', states=states,
                           cities=cities, id=id)


@app.teardown_appcontext
def close_session(self):
    ''' Tells the host computer to close & remove current
    SQLAlchemy Session '''
    storage.close()


if __name__ == '__main__':
    app.debug = True
    # Don't run on localhost
    app.run(host='0.0.0.0', port=5000)
