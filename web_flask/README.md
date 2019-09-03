# 0x04. AirBnB clone - Web framework

## Resources
[Python Flask Tutorial: Full-Featured Web App Part 1 - Getting Started](https://duckduckgo.com/?q=flask+tutorial+video+introduction&t=brave&ia=videos&iax=videos&iai=MwZwr5Tvyxo) </br >
[What is a Web Framework? by Jeff Knupp](https://jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/) </br >
[Flask Quickstart page](https://flask.palletsprojects.com/en/1.0.x/quickstart/) </br >
[A Jinja template synopsis: Template Designer Documentation](https://jinja.palletsprojects.com/en/2.9.x/templates/) </br >
[The Pallets Projects - Flask](https://palletsprojects.com/p/flask/) </br >
[Python Tutorials: Flask with static html files](https://pythonspot.com/flask-with-static-html-files/) </br >

## Tasks
0. `0-hello_route.py`, `__init__.py` // a script that starts a Flask web application:

- Web application is listening on `0.0.0.0, port `5000`
- Routes:
-- `/`: display “Hello HBNB!”
- Option `strict_slashes=False` required in route definition

1. `1-hbnb_route.py` // a script that starts a Flask web application:

- All the above requirements.
Routes:
- Add: `/hbnb`: display “HBNB”

2. `2-c_route.py` // a script that starts a Flask web application:

- All the above requirements.
Routes:
- Add: `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space )

3. `3-python_route.py` // a script that starts a Flask web application:

All the above requirements.
Routes:
- Add: `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space )
- The default value of `text` is “is cool”

4. `4-number_route.py` // a script that starts a Flask web application:

- All the above requirements.
Routes:
- Add: `/number/<n>`: display “`n` is a number” only if `n` is an integer

5. `5-number_template.py`, `templates/5-number.html` // a script that starts a Flask web application:

All the above requirements.
- Add: `/number_template/<n>`: display a HTML page only if `n` is an integer:
-- `H1` tag: “Number: `n`” inside the tag `BODY`

6. `6-number_odd_or_even.py`, `templates/6-number_odd_or_even.html` // a script that starts a Flask web application:

All the above requirements.
Routes:
- Add: `/number_odd_or_even/<n>`: display a HTML page only if `n` is an integer:
-- `H1` tag: “Number: `n` is `even|odd`” inside the tag `BODY`

7. File: `models/engine/file_storage.py`, `models/engine/db_storage.py`, `models/state.py` // To display our HBNB data, I'll update some parts of the engine:

Update `FileStorage`: (`models/engine/file_storage.py`)

- Add a public method `def close(self):`: call `reload()` method for deserializing the JSON file to objects

Update `DBStorage`: (`models/engine/db_storage.py`)

- Add a public method `def close(self):`: call `remove()` method on the private session attribute (`self.__session`) [tips](https://docs.sqlalchemy.org/en/13/orm/contextual.html) or `close()` on the class `Session` [tips](https://docs.sqlalchemy.org/en/13/orm/session_api.html)
Update `State`: (`models/state.py`) - If it’s not already present

- If your storage engine is not `DBStorage`, add a public getter method `cities` to return the list of `City` objects from `storage` linked to the current `State`

8. File: `web_flask/7-states_list.py`, `web_flask/templates/7-states_list.html`
a script that starts a Flask web application:

- Web application must be listening on `0.0.0.0`, port `5000`
- Storage used for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
- After each request you must remove the current SQLAlchemy Session:
-- Declare a method to handle `@app.teardown_appcontext`
-- Call in this method `storage.close()`
- Routes:
- `/states_list`: display a HTML page: (inside the tag `BODY`)
-- `H1` tag: “States”
-- `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by `name` (A->Z) [tip](https://jinja.palletsprojects.com/en/2.9.x/templates/)
--- `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
- Import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql) to have some data
- You must use the option `strict_slashes=False` in your route definition

9. Files: `web_flask/8-cities_by_states.py`, `web_flask/templates/8-cities_by_states.html` // a script that starts a Flask web application:

To all of the above, add:
- To load all cities of a State:
-- If storage engine is `DBStorage`, use `cities` relationship
-- Otherwise, use the public getter method `cities`

10. File: `web_flask/9-states.py`, `web_flask/templates/9-states.html` // a script that starts a Flask web application:
To all of the above, add:

- Routes:
-- `/states`: display a HTML page: (inside the tag `BODY`)
-- `H1` tag: “States”
-- `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by `name` (A->Z) [tip](https://jinja.palletsprojects.com/en/2.9.x/templates/)
--- `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
- `/states/<id>`: display a HTML page: (inside the tag `BODY`)
-- If a `State` object is found with this `id`:
--- `H1` tag: “State: ”
--- `H3` tag: “Cities:”
--- `UL` tag: with the list of `City` objects linked to the `State` sorted by `name` (A->Z)
---- `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`
- Otherwise:
-- `H1` tag: “Not found!”

11. Files: `web_flask/10-hbnb_filters.py`, `web_flask/templates/10-hbnb_filters.html`, `web_flask/static/` // a script that starts a Flask web application:

To all of the above, add:
- Routes:
-- `/hbnb_filters`: display a HTML page like `6-index.html`, which was done during the project 0x01. AirBnB clone - Web static
- Copy files `3-footer.css`, `3-header.css`, `4-common.css` and `6-filters.css` from `web_static/styles/` to the folder `web_flask/static/styles`
- Copy files `icon.png` and `logo.png` from `web_static/images/` to the folder `web_flask/static/images`
- Update `.popover` class in `6-filters.css` to allow scrolling in the popover and a max height of 300 pixels.
- Use `6-index.html` content as source code for the template `10-hbnb_filters.html`:
-- Replace the content of the `H4` tag under each filter title (`H3` States and `H3` Amenities) by `&nbsp`;
- `State`, `City` and `Amenity` objects must be loaded from `DBStorage` and sorted by name (A->Z)
- Import this [10-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql) to have some data