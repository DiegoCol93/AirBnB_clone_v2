#!/usr/bin/python3
# Sets a basic flask server.
""" Module for storing the Flask setup. """
from flask import Flask, render_template
from models.__init__ import storage
from models.amenity import Amenity
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


# Cities by state List route. - - - - - - - - - - - - - - - - - - - - - - - - |
@app.route('/hbnb_filters')
def states_list():
    """ Returns the list of states currently on the HBNB_storage. """

    # Bring dictionaries from storage.
    all_amenities = storage.all(Amenity)
    template = '10-hbnb_filters.html'
    all_states = storage.all(State)

    # Return with the jinja template.
    return render_template(template, states=all_states, amenities=all_amenities)


# Close ORM connection. - - - - - - - - - - - - - - - - - - - - - - - - - - - |
@app.teardown_appcontext
def teardown_db_connection(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
