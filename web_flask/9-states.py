#!/usr/bin/python3
# Sets a basic flask server.
""" Module for storing the Flask setup. """
from flask import Flask, render_template
from models.__init__ import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


# Cities by state List route. - - - - - - - - - - - - - - - - - - - - - - - - |
@app.route('/states')
def states_list():
    """ Returns the list of states currently on the HBNB_storage. """

    # Bring dictionary from storage.
    models = storage.all(State)
    template = '7-states_list.html'

    # Return with the jinja template.
    return render_template(template, models=models)


@app.route('/states/<id>')
def states_id_list(id):
    """ Returns the list of cities by states currently on the HBNB_storage. """
    # Bring dictionary from storage.
    models = storage.all(State)
    template = '9-states.html'

    if "State.{}".format(id) in models:
        state = models.pop("State.{}".format(id))
    else:
        return ("<h1>Not found!</h1>")

    # Return with the jinja template.
    return render_template(template, state=state)


# Close ORM connection. - - - - - - - - - - - - - - - - - - - - - - - - - - - |
@app.teardown_appcontext
def teardown_db_connection(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
