#!/usr/bin/python3
<<<<<<< HEAD
'''
    Flask route that returns a list of states.
'''
from flask import Flask, render_template
from models import storage
=======
""" Starts a Flask application related to HBNB. """

from flask import Flask, render_template
from models import storage
from models.state import State
>>>>>>> 36b56ffa1fd79c4b54a506f4ab42f55fa2dfc3b9

app = Flask(__name__)


<<<<<<< HEAD
@app.route('/states_list', strict_slashes=False)
def states_list():
    '''
        Returns a list of states.
    '''
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    '''
        Remove the current SQLAlchemy Session.
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
=======
@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
        Flask route at /states_list.
        Displays the list of the States in the database.
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 36b56ffa1fd79c4b54a506f4ab42f55fa2dfc3b9
