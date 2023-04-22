#!/usr/bin/python3
<<<<<<< HEAD

'''
    Starts a Flask web application.
    The application listens on 0.0.0.0, port 5000.
    Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
'''

from models import storage
from flask import Flask
from flask import render_template
=======
""" Starts a Flask application related to HBNB. """

from os import getenv
from flask import Flask, render_template
from models import storage
from models.state import State
>>>>>>> 36b56ffa1fd79c4b54a506f4ab42f55fa2dfc3b9

app = Flask(__name__)


<<<<<<< HEAD
@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")

=======
@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request."""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """
        Flask route at /states.
        Displays the list of the States in the database.

        Flask route at /states/<id>.
        Displays the list of the Cities in the State with id <id>.
    """
    states = storage.all(State).values()
    if id is not None:
        for state in states:
            if state.id == id:
                return render_template('9-states.html', states=state)
        return render_template('9-states.html')
    return render_template('9-states.html', states=states, full=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
>>>>>>> 36b56ffa1fd79c4b54a506f4ab42f55fa2dfc3b9
