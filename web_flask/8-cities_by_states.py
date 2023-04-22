#!/usr/bin/python3
#<<<<<<< HEAD
'''
    Starts a Flask web application.
'''

from flask import Flask
from flask import render_template
from models import storage
#=======
""" Starts a Flask application related to HBNB. """

from os import getenv
from flask import Flask, render_template
from models import storage
from models.state import State
#>>>>>>> 36b56ffa1fd79c4b54a506f4ab42f55fa2dfc3b9

app = Flask(__name__)


#<<<<<<< HEAD
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''
        Returns a list of all cities by state.
    '''
    states = storage.all('State')
    return render_template('8-cities_by_states.html',
                           states=states)


@app.teardown_appcontext
def teardown_db(exception):
    '''
        This is necessary to remove the
        global SQLAlchemy session completely.
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')

#=======
@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
        Flask route at /cities_by_states.
        Displays the list of the Cities in the database with their states.
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
#>>>>>>> 36b56ffa1fd79c4b54a506f4ab42f55fa2dfc3b9
